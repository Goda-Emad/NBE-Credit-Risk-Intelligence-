"""
Model Monitoring Module
Tracks model performance over time and generates alerts
"""

import numpy as np
import pandas as pd
import pickle
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

logger = logging.getLogger(__name__)

# Performance thresholds
THRESHOLDS = {
    "min_accuracy":        0.70,
    "min_precision":       0.60,
    "min_recall":          0.55,
    "min_f1":              0.57,
    "max_false_neg_rate":  0.40,
    "min_daily_volume":    10,
}


class ModelMonitor:
    """
    Monitors model performance in production.

    Tracks:
    - Prediction accuracy over time
    - False negative rate (critical for credit risk)
    - Prediction volume and distribution
    - Performance degradation alerts
    """

    def __init__(self, log_dir: str = "logs/monitoring"):
        self.log_dir     = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.metrics_log = self.log_dir / "metrics_log.json"
        self.alerts_log  = self.log_dir / "alerts_log.json"
        self.history     = self._load_history()

    # ------------------------------------------------------------------ #
    # Core Methods
    # ------------------------------------------------------------------ #

    def log_prediction(self,
                       prediction:   int,
                       probability:  float,
                       actual_label: int = None,
                       metadata:     dict = None) -> dict:
        """
        Log a single prediction

        Args:
            prediction:   Model prediction (0=Bad, 1=Good)
            probability:  Probability of Good (0-1)
            actual_label: True label if available
            metadata:     Additional info (age, amount, etc.)

        Returns:
            Log entry dictionary
        """
        entry = {
            "timestamp":   datetime.now().isoformat(),
            "prediction":  int(prediction),
            "probability": round(float(probability), 4),
            "actual":      int(actual_label) if actual_label is not None else None,
            "metadata":    metadata or {}
        }

        self.history["predictions"].append(entry)
        self._save_history()

        logger.debug(f"Prediction logged: {prediction} ({probability:.2%})")
        return entry

    def calculate_metrics(self,
                          days: int = 30) -> dict:
        """
        Calculate performance metrics for recent period

        Args:
            days: Number of days to look back

        Returns:
            Dictionary with performance metrics
        """
        cutoff = datetime.now() - timedelta(days=days)

        # Filter recent predictions with actual labels
        recent = [
            p for p in self.history["predictions"]
            if (datetime.fromisoformat(p["timestamp"]) > cutoff
                and p["actual"] is not None)
        ]

        if len(recent) < 10:
            logger.warning(f"Insufficient data for metrics: {len(recent)} samples")
            return {"error": "Insufficient data", "count": len(recent)}

        y_true = [p["actual"]     for p in recent]
        y_pred = [p["prediction"] for p in recent]

        metrics = {
            "period_days":     days,
            "sample_count":    len(recent),
            "accuracy":        round(accuracy_score(y_true, y_pred),    4),
            "precision":       round(precision_score(y_true, y_pred,
                                     zero_division=0),                   4),
            "recall":          round(recall_score(y_true, y_pred,
                                     zero_division=0),                   4),
            "f1_score":        round(f1_score(y_true, y_pred,
                                     zero_division=0),                   4),
            "false_neg_rate":  round(
                sum(1 for t, p in zip(y_true, y_pred)
                    if t == 1 and p == 0) / max(sum(y_true), 1),
                4
            ),
            "approval_rate":   round(sum(y_pred) / len(y_pred), 4),
            "calculated_at":   datetime.now().isoformat()
        }

        logger.info(f"Metrics calculated: accuracy={metrics['accuracy']:.2%}")
        return metrics

    def check_alerts(self) -> list:
        """
        Check for performance alerts

        Returns:
            List of active alerts
        """
        alerts  = []
        metrics = self.calculate_metrics(days=7)

        if "error" in metrics:
            return []

        # Check each threshold
        checks = [
            ("accuracy",        metrics["accuracy"],
             THRESHOLDS["min_accuracy"],
             "Model accuracy dropped below threshold",
             "high"),

            ("precision",       metrics["precision"],
             THRESHOLDS["min_precision"],
             "Precision below threshold",
             "medium"),

            ("recall",          metrics["recall"],
             THRESHOLDS["min_recall"],
             "Recall below threshold",
             "medium"),

            ("false_neg_rate",  metrics["false_neg_rate"],
             THRESHOLDS["max_false_neg_rate"],
             "False negative rate too high! Bad customers being approved!",
             "critical"),
        ]

        for metric_name, value, threshold, message, severity in checks:
            # For false_neg_rate: alert if ABOVE threshold
            if metric_name == "false_neg_rate":
                triggered = value > threshold
            else:
                triggered = value < threshold

            if triggered:
                alert = {
                    "timestamp": datetime.now().isoformat(),
                    "severity":  severity,
                    "metric":    metric_name,
                    "value":     value,
                    "threshold": threshold,
                    "message":   message,
                    "action":    self._get_recommended_action(severity)
                }
                alerts.append(alert)
                logger.warning(f"ALERT [{severity.upper()}]: {message}")

        # Save alerts
        if alerts:
            self._save_alerts(alerts)

        return alerts

    def get_dashboard_data(self) -> dict:
        """Get data for monitoring dashboard"""
        metrics_7d  = self.calculate_metrics(days=7)
        metrics_30d = self.calculate_metrics(days=30)
        alerts      = self.check_alerts()

        # Prediction volume by day
        daily_counts = self._get_daily_counts(days=30)

        return {
            "metrics_7d":    metrics_7d,
            "metrics_30d":   metrics_30d,
            "alerts":        alerts,
            "daily_counts":  daily_counts,
            "total_predictions": len(self.history["predictions"]),
            "last_updated":  datetime.now().isoformat()
        }

    def generate_report(self) -> str:
        """Generate text monitoring report"""
        metrics = self.calculate_metrics(days=30)
        alerts  = self.check_alerts()

        status = "🟢 HEALTHY" if not alerts else (
            "🔴 CRITICAL" if any(a["severity"] == "critical" for a in alerts)
            else "🟡 WARNING"
        )

        report = f"""
# NBE Credit Risk - Model Monitoring Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Status: {status}

## Performance Metrics (Last 30 Days)
- Accuracy:         {metrics.get("accuracy", "N/A")}
- Precision:        {metrics.get("precision", "N/A")}
- Recall:           {metrics.get("recall", "N/A")}
- F1-Score:         {metrics.get("f1_score", "N/A")}
- False Neg Rate:   {metrics.get("false_neg_rate", "N/A")}
- Approval Rate:    {metrics.get("approval_rate", "N/A")}
- Sample Count:     {metrics.get("sample_count", "N/A")}

## Active Alerts ({len(alerts)})
"""
        for alert in alerts:
            report += f"""
### [{alert["severity"].upper()}] {alert["metric"]}
- Value:     {alert["value"]}
- Threshold: {alert["threshold"]}
- Message:   {alert["message"]}
- Action:    {alert["action"]}
"""

        if not alerts:
            report += "No active alerts. Model performing within thresholds.
"

        return report

    # ------------------------------------------------------------------ #
    # Private Methods
    # ------------------------------------------------------------------ #

    def _get_recommended_action(self, severity: str) -> str:
        """Get recommended action for alert severity"""
        actions = {
            "critical": "IMMEDIATE: Trigger retraining pipeline & notify team",
            "high":     "URGENT: Review model performance & consider retraining",
            "medium":   "MONITOR: Track metric trend & schedule review",
            "low":      "INFO: Log for monthly review"
        }
        return actions.get(severity, "Review and investigate")

    def _get_daily_counts(self, days: int = 30) -> dict:
        """Get prediction counts by day"""
        cutoff = datetime.now() - timedelta(days=days)
        daily  = {}

        for pred in self.history["predictions"]:
            ts  = datetime.fromisoformat(pred["timestamp"])
            if ts > cutoff:
                day = ts.strftime("%Y-%m-%d")
                daily[day] = daily.get(day, 0) + 1

        return daily

    def _load_history(self) -> dict:
        """Load prediction history from file"""
        if self.metrics_log.exists():
            with open(self.metrics_log, "r") as f:
                return json.load(f)
        return {"predictions": [], "created_at": datetime.now().isoformat()}

    def _save_history(self) -> None:
        """Save prediction history to file"""
        with open(self.metrics_log, "w") as f:
            json.dump(self.history, f, indent=2)

    def _save_alerts(self, alerts: list) -> None:
        """Save alerts to file"""
        existing = []
        if self.alerts_log.exists():
            with open(self.alerts_log, "r") as f:
                existing = json.load(f)

        existing.extend(alerts)

        with open(self.alerts_log, "w") as f:
            json.dump(existing[-100:], f, indent=2)  # Keep last 100


# ============================================================================
# Standalone demo
# ============================================================================

if __name__ == "__main__":
    print("🔍 NBE Model Monitor Demo")
    print("=" * 50)

    monitor = ModelMonitor()

    # Simulate predictions
    np.random.seed(42)
    for i in range(50):
        pred  = np.random.randint(0, 2)
        prob  = np.random.uniform(0.3, 0.9)
        actual = pred if np.random.random() > 0.25 else 1 - pred
        monitor.log_prediction(pred, prob, actual, {"sample_id": i})

    metrics = monitor.calculate_metrics(days=30)
    print(f"\n📊 Metrics (30 days):")
    for k, v in metrics.items():
        print(f"   {k}: {v}")

    alerts = monitor.check_alerts()
    print(f"\n🚨 Alerts: {len(alerts)}")

    print("\n✅ Monitoring demo complete!")

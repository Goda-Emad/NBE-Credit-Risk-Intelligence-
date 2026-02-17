"""
Data Drift Detection Module
Detects changes in input data distribution over time
"""

import numpy as np
import pandas as pd
import json
import logging
from pathlib import Path
from datetime import datetime
from scipy import stats

logger = logging.getLogger(__name__)

# Drift thresholds
DRIFT_THRESHOLDS = {
    "ks_pvalue":          0.05,   # KS test p-value threshold
    "psi_warning":        0.10,   # PSI warning threshold
    "psi_critical":       0.25,   # PSI critical threshold
    "mean_shift_pct":     0.15,   # 15% mean shift threshold
    "std_shift_pct":      0.20,   # 20% std shift threshold
}

# Key features to monitor for drift
KEY_FEATURES = [
    "Age", "Credit_Amount", "Duration",
    "Installment_Rate", "Existing_Credits"
]


class DriftDetector:
    """
    Detects data drift between training and production data.

    Methods:
    - KS Test:  Statistical test for distribution change
    - PSI:      Population Stability Index
    - Mean/Std: Simple statistical comparison
    """

    def __init__(self,
                 reference_data: pd.DataFrame = None,
                 log_dir: str = "logs/drift"):
        self.log_dir        = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.reference_data = reference_data
        self.drift_log      = self.log_dir / "drift_log.json"
        self.drift_history  = []

    # ------------------------------------------------------------------ #
    # Core Methods
    # ------------------------------------------------------------------ #

    def set_reference(self, data: pd.DataFrame) -> None:
        """Set reference (training) dataset"""
        self.reference_data = data
        logger.info(f"Reference data set: {data.shape}")

    def calculate_psi(self,
                      reference: pd.Series,
                      production: pd.Series,
                      buckets: int = 10) -> float:
        """
        Calculate Population Stability Index (PSI)

        PSI < 0.10:  No significant change
        PSI 0.10-0.25: Moderate change
        PSI > 0.25:  Significant drift

        Args:
            reference:  Reference distribution
            production: Production distribution
            buckets:    Number of buckets

        Returns:
            PSI score
        """
        # Create bins from reference
        breakpoints = np.linspace(
            min(reference.min(), production.min()),
            max(reference.max(), production.max()),
            buckets + 1
        )

        # Calculate distributions
        ref_counts  = pd.cut(reference,  bins=breakpoints).value_counts(normalize=True).sort_index()
        prod_counts = pd.cut(production, bins=breakpoints).value_counts(normalize=True).sort_index()

        # Align indices
        ref_counts, prod_counts = ref_counts.align(prod_counts, fill_value=0.0001)

        # Replace zeros to avoid log(0)
        ref_counts  = ref_counts.replace(0,  0.0001)
        prod_counts = prod_counts.replace(0, 0.0001)

        # PSI formula
        psi = np.sum(
            (prod_counts - ref_counts) *
            np.log(prod_counts / ref_counts)
        )

        return round(float(psi), 6)

    def run_ks_test(self,
                    reference:  pd.Series,
                    production: pd.Series) -> dict:
        """
        Run Kolmogorov-Smirnov test for distribution change

        Returns:
            Dictionary with statistic and p-value
        """
        statistic, p_value = stats.ks_2samp(
            reference.dropna(),
            production.dropna()
        )

        return {
            "statistic": round(float(statistic), 6),
            "p_value":   round(float(p_value),   6),
            "drifted":   p_value < DRIFT_THRESHOLDS["ks_pvalue"]
        }

    def detect_feature_drift(self,
                              production_data: pd.DataFrame,
                              features: list = None) -> dict:
        """
        Detect drift for each feature

        Args:
            production_data: New production data
            features:        Features to check (default: KEY_FEATURES)

        Returns:
            Dictionary with drift results per feature
        """
        if self.reference_data is None:
            raise ValueError("Reference data not set. Call set_reference() first.")

        features = features or KEY_FEATURES
        features = [f for f in features
                    if f in self.reference_data.columns
                    and f in production_data.columns]

        results = {}

        for feature in features:
            ref_col  = self.reference_data[feature].dropna()
            prod_col = production_data[feature].dropna()

            if len(prod_col) < 10:
                logger.warning(f"Insufficient production data for {feature}")
                continue

            # PSI
            psi = self.calculate_psi(ref_col, prod_col)

            # KS Test
            ks  = self.run_ks_test(ref_col, prod_col)

            # Statistics comparison
            ref_mean  = ref_col.mean()
            prod_mean = prod_col.mean()
            mean_shift_pct = abs(prod_mean - ref_mean) / (ref_mean + 1e-10)

            ref_std  = ref_col.std()
            prod_std = prod_col.std()
            std_shift_pct = abs(prod_std - ref_std) / (ref_std + 1e-10)

            # Determine drift level
            if (psi > DRIFT_THRESHOLDS["psi_critical"] or
                    mean_shift_pct > DRIFT_THRESHOLDS["mean_shift_pct"] * 2):
                drift_level = "critical"
            elif (psi > DRIFT_THRESHOLDS["psi_warning"] or
                      ks["drifted"] or
                      mean_shift_pct > DRIFT_THRESHOLDS["mean_shift_pct"]):
                drift_level = "warning"
            else:
                drift_level = "ok"

            results[feature] = {
                "psi":            psi,
                "ks_statistic":   ks["statistic"],
                "ks_p_value":     ks["p_value"],
                "ks_drifted":     ks["drifted"],
                "ref_mean":       round(float(ref_mean),       4),
                "prod_mean":      round(float(prod_mean),      4),
                "mean_shift_pct": round(float(mean_shift_pct), 4),
                "ref_std":        round(float(ref_std),        4),
                "prod_std":       round(float(prod_std),       4),
                "std_shift_pct":  round(float(std_shift_pct),  4),
                "drift_level":    drift_level
            }

            if drift_level != "ok":
                logger.warning(
                    f"DRIFT [{drift_level.upper()}] {feature}: "
                    f"PSI={psi:.4f}, p-value={ks['p_value']:.4f}"
                )

        return results

    def detect_target_drift(self,
                             production_labels: pd.Series) -> dict:
        """
        Detect drift in target variable distribution

        Args:
            production_labels: Production target values

        Returns:
            Dictionary with target drift analysis
        """
        if self.reference_data is None or "Risk" not in self.reference_data.columns:
            return {"error": "Reference data or Risk column not available"}

        ref_rate  = self.reference_data["Risk"].mean()
        prod_rate = production_labels.mean()
        shift_pct = abs(prod_rate - ref_rate) / (ref_rate + 1e-10)

        # Chi-square test
        ref_counts  = pd.Series([
            (self.reference_data["Risk"] == 0).sum(),
            (self.reference_data["Risk"] == 1).sum()
        ])
        prod_counts = pd.Series([
            (production_labels == 0).sum(),
            (production_labels == 1).sum()
        ])

        chi2, p_value = stats.chisquare(
            prod_counts / prod_counts.sum(),
            ref_counts  / ref_counts.sum()
        )

        return {
            "ref_approval_rate":    round(float(ref_rate),   4),
            "prod_approval_rate":   round(float(prod_rate),  4),
            "shift_pct":            round(float(shift_pct),  4),
            "chi2_statistic":       round(float(chi2),        6),
            "chi2_p_value":         round(float(p_value),     6),
            "target_drifted":       p_value < 0.05,
            "drift_level":          (
                "critical" if shift_pct > 0.30
                else "warning" if shift_pct > 0.15
                else "ok"
            )
        }

    def run_full_check(self,
                       production_data: pd.DataFrame) -> dict:
        """
        Run complete drift check

        Args:
            production_data: New production data

        Returns:
            Complete drift report
        """
        logger.info("Running full drift detection check...")

        feature_drift = self.detect_feature_drift(production_data)

        # Target drift if labels available
        target_drift = {}
        if "Risk" in production_data.columns:
            target_drift = self.detect_target_drift(production_data["Risk"])

        # Summary
        critical_features = [
            f for f, r in feature_drift.items()
            if r["drift_level"] == "critical"
        ]
        warning_features = [
            f for f, r in feature_drift.items()
            if r["drift_level"] == "warning"
        ]

        overall_status = (
            "critical" if critical_features or
                          target_drift.get("drift_level") == "critical"
            else "warning" if warning_features or
                              target_drift.get("drift_level") == "warning"
            else "ok"
        )

        report = {
            "timestamp":          datetime.now().isoformat(),
            "overall_status":     overall_status,
            "feature_drift":      feature_drift,
            "target_drift":       target_drift,
            "critical_features":  critical_features,
            "warning_features":   warning_features,
            "production_samples": len(production_data),
            "recommendation":     self._get_recommendation(overall_status)
        }

        self._save_drift_log(report)
        logger.info(f"Drift check complete: {overall_status.upper()}")

        return report

    def generate_report(self,
                        drift_results: dict) -> str:
        """Generate text drift report"""
        status_emoji = {
            "ok":       "🟢",
            "warning":  "🟡",
            "critical": "🔴"
        }

        emoji  = status_emoji.get(drift_results["overall_status"], "⚪")
        report = f"""
# NBE Credit Risk - Data Drift Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Status: {emoji} {drift_results["overall_status"].upper()}

## Summary
- Production Samples: {drift_results["production_samples"]}
- Critical Features:  {drift_results["critical_features"]}
- Warning Features:   {drift_results["warning_features"]}
- Recommendation:     {drift_results["recommendation"]}

## Feature Drift Details
"""
        for feature, results in drift_results["feature_drift"].items():
            level_emoji = status_emoji.get(results["drift_level"], "⚪")
            report += f"""
### {level_emoji} {feature}
- PSI:         {results["psi"]} (threshold: {DRIFT_THRESHOLDS["psi_warning"]})
- KS p-value:  {results["ks_p_value"]} (threshold: {DRIFT_THRESHOLDS["ks_pvalue"]})
- Mean shift:  {results["mean_shift_pct"]:.1%}
  (ref: {results["ref_mean"]} → prod: {results["prod_mean"]})
"""

        if drift_results["target_drift"]:
            td = drift_results["target_drift"]
            report += f"""
## Target Distribution Drift
- Reference Approval Rate:   {td.get("ref_approval_rate", "N/A")}
- Production Approval Rate:  {td.get("prod_approval_rate", "N/A")}
- Shift:                     {td.get("shift_pct", 0):.1%}
- Status:                    {td.get("drift_level", "N/A")}
"""

        return report

    # ------------------------------------------------------------------ #
    # Private Methods
    # ------------------------------------------------------------------ #

    def _get_recommendation(self, status: str) -> str:
        """Get recommendation based on drift status"""
        recommendations = {
            "ok":       "No action needed. Continue monitoring.",
            "warning":  "Monitor closely. Consider retraining within 30 days.",
            "critical": "URGENT: Trigger retraining pipeline immediately."
        }
        return recommendations.get(status, "Investigate further.")

    def _save_drift_log(self, report: dict) -> None:
        """Save drift report to log file"""
        history = []
        if self.drift_log.exists():
            with open(self.drift_log, "r") as f:
                history = json.load(f)

        history.append({
            "timestamp":      report["timestamp"],
            "overall_status": report["overall_status"],
            "critical_count": len(report["critical_features"]),
            "warning_count":  len(report["warning_features"])
        })

        with open(self.drift_log, "w") as f:
            json.dump(history[-90:], f, indent=2)  # Keep last 90 days


# ============================================================================
# Standalone demo
# ============================================================================

if __name__ == "__main__":
    print("🔍 NBE Drift Detection Demo")
    print("=" * 50)

    np.random.seed(42)

    # Reference data
    reference = pd.DataFrame({
        "Age":              np.random.normal(35, 11, 800),
        "Credit_Amount":    np.random.normal(3271, 2822, 800),
        "Duration":         np.random.normal(21, 12, 800),
        "Installment_Rate": np.random.randint(1, 5, 800).astype(float),
        "Existing_Credits": np.random.randint(1, 5, 800).astype(float),
        "Risk":             np.random.choice([0, 1], 800, p=[0.7, 0.3])
    })

    # Production data (with some drift)
    production = pd.DataFrame({
        "Age":              np.random.normal(40, 13, 200),  # Shifted mean
        "Credit_Amount":    np.random.normal(4000, 3000, 200),
        "Duration":         np.random.normal(25, 14, 200),
        "Installment_Rate": np.random.randint(1, 5, 200).astype(float),
        "Existing_Credits": np.random.randint(1, 5, 200).astype(float),
        "Risk":             np.random.choice([0, 1], 200, p=[0.65, 0.35])
    })

    detector = DriftDetector(reference_data=reference)
    results  = detector.run_full_check(production)

    print(f"\n📊 Overall Status: {results['overall_status'].upper()}")
    print(f"⚠️  Critical: {results['critical_features']}")
    print(f"🟡 Warning:  {results['warning_features']}")
    print(f"💡 Action:   {results['recommendation']}")
    print("\n✅ Drift detection demo complete!")

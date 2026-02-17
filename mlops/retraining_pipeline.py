"""
Automated Retraining Pipeline
Handles model retraining when performance degrades
"""

import pickle
import numpy as np
import pandas as pd
import logging
import json
import shutil
from pathlib import Path
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

logger = logging.getLogger(__name__)


class RetrainingPipeline:
    """
    Automated model retraining pipeline.

    Triggers:
    - Performance drops below threshold
    - Significant data drift detected
    - Scheduled periodic retraining
    - Manual trigger

    Steps:
    1. Load new/updated data
    2. Validate data quality
    3. Run feature engineering
    4. Train new model
    5. Compare with current model
    6. Deploy if improved
    7. Log results
    """

    def __init__(self,
                 models_dir: str = "models",
                 data_dir:   str = "data",
                 log_dir:    str = "logs/retraining"):
        self.models_dir = Path(models_dir)
        self.data_dir   = Path(data_dir)
        self.log_dir    = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.run_log    = self.log_dir / "retraining_log.json"

    # ------------------------------------------------------------------ #
    # Core Methods
    # ------------------------------------------------------------------ #

    def check_trigger(self,
                      current_accuracy: float,
                      drift_status: str = "ok",
                      force: bool = False) -> dict:
        """
        Check if retraining should be triggered

        Args:
            current_accuracy: Current model accuracy
            drift_status:     Drift detection result
            force:            Force retraining regardless of conditions

        Returns:
            Dictionary with trigger decision
        """
        triggers = []

        if force:
            triggers.append("Manual trigger")

        if current_accuracy < 0.70:
            triggers.append(
                f"Accuracy below threshold: {current_accuracy:.2%} < 70%"
            )

        if drift_status == "critical":
            triggers.append("Critical data drift detected")

        if drift_status == "warning":
            triggers.append("Warning: data drift detected")

        should_retrain = bool(triggers) or force

        result = {
            "should_retrain": should_retrain,
            "triggers":       triggers,
            "timestamp":      datetime.now().isoformat(),
            "priority":       (
                "critical" if force or current_accuracy < 0.65
                else "high" if current_accuracy < 0.70
                else "medium"
            )
        }

        if should_retrain:
            logger.warning(
                f"Retraining triggered: {triggers}"
            )
        else:
            logger.info("No retraining needed at this time")

        return result

    def load_training_data(self,
                           filename: str = "german_credit_fe_v3.csv"
                           ) -> pd.DataFrame:
        """Load training data"""
        filepath = self.data_dir / "processed" / filename

        if not filepath.exists():
            raise FileNotFoundError(f"Training data not found: {filepath}")

        df = pd.read_csv(filepath)
        logger.info(f"Training data loaded: {df.shape}")
        return df

    def validate_data(self, df: pd.DataFrame) -> dict:
        """
        Validate data quality before training

        Returns:
            Validation results dictionary
        """
        issues = []

        if len(df) < 100:
            issues.append(f"Too few samples: {len(df)} < 100")

        if df.isnull().sum().sum() > 0:
            issues.append(f"Missing values: {df.isnull().sum().sum()}")

        if "Risk" not in df.columns:
            issues.append("Missing target column: Risk")

        if "Risk" in df.columns:
            class_balance = df["Risk"].value_counts(normalize=True)
            if class_balance.min() < 0.05:
                issues.append(
                    f"Severe class imbalance: {class_balance.to_dict()}"
                )

        result = {
            "is_valid":    len(issues) == 0,
            "issues":      issues,
            "n_samples":   len(df),
            "n_features":  len(df.columns) - 1,
            "class_dist":  df["Risk"].value_counts().to_dict()
                           if "Risk" in df.columns else {}
        }

        if issues:
            logger.warning(f"Data validation issues: {issues}")
        else:
            logger.info("Data validation passed")

        return result

    def train_new_model(self,
                        df: pd.DataFrame,
                        model_params: dict = None) -> dict:
        """
        Train a new model

        Args:
            df:           Training DataFrame
            model_params: Optional model hyperparameters

        Returns:
            Dictionary with model, scaler, metrics, features
        """
        logger.info("Starting model training...")
        start_time = datetime.now()

        # Prepare data
        X = df.drop("Risk", axis=1)
        y = df["Risk"]
        feature_names = list(X.columns)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Scale
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled  = scaler.transform(X_test)

        # Train
        params = model_params or {
            "n_estimators":    100,
            "max_depth":       15,
            "min_samples_split": 5,
            "min_samples_leaf":  2,
            "random_state":    42,
            "class_weight":    "balanced",
            "n_jobs":          -1
        }

        model = RandomForestClassifier(**params)
        model.fit(X_train_scaled, y_train)

        # Evaluate
        train_pred = model.predict(X_train_scaled)
        test_pred  = model.predict(X_test_scaled)
        train_acc  = accuracy_score(y_train, train_pred)
        test_acc   = accuracy_score(y_test,  test_pred)
        cm         = confusion_matrix(y_test, test_pred)

        duration = (datetime.now() - start_time).seconds

        result = {
            "model":          model,
            "scaler":         scaler,
            "feature_names":  feature_names,
            "metrics": {
                "train_accuracy":  round(train_acc, 4),
                "test_accuracy":   round(test_acc,  4),
                "false_negatives": int(cm[1, 0]),
                "false_positives": int(cm[0, 1]),
                "true_positives":  int(cm[1, 1]),
                "true_negatives":  int(cm[0, 0])
            },
            "training_samples": len(X_train),
            "test_samples":     len(X_test),
            "n_features":       len(feature_names),
            "training_time_s":  duration,
            "trained_at":       datetime.now().isoformat()
        }

        logger.info(
            f"Training complete: accuracy={test_acc:.2%}, time={duration}s"
        )
        return result

    def compare_models(self,
                       current_metrics: dict,
                       new_metrics: dict) -> dict:
        """
        Compare current vs new model performance

        Returns:
            Comparison results with deployment recommendation
        """
        curr_acc = current_metrics.get("test_accuracy", 0)
        new_acc  = new_metrics.get("test_accuracy",     0)
        curr_fn  = current_metrics.get("false_negatives", 999)
        new_fn   = new_metrics.get("false_negatives",     999)

        acc_improvement = new_acc  - curr_acc
        fn_improvement  = curr_fn  - new_fn   # Positive = fewer FN

        # Deploy if:
        # - Accuracy improved by > 1%, OR
        # - False negatives reduced by > 2 cases with no accuracy loss
        should_deploy = (
            acc_improvement > 0.01 or
            (fn_improvement > 2 and acc_improvement >= -0.005)
        )

        return {
            "current_accuracy":  curr_acc,
            "new_accuracy":      new_acc,
            "accuracy_change":   round(acc_improvement, 4),
            "current_fn":        curr_fn,
            "new_fn":            new_fn,
            "fn_reduction":      fn_improvement,
            "should_deploy":     should_deploy,
            "reason":            (
                f"Accuracy improved by {acc_improvement:.2%}" if acc_improvement > 0.01
                else f"FN reduced by {fn_improvement} cases" if fn_improvement > 2
                else "No significant improvement - keeping current model"
            )
        }

    def deploy_model(self,
                     training_result: dict,
                     version: str = None) -> dict:
        """
        Deploy new model to production

        Args:
            training_result: Output from train_new_model()
            version:         Version string (e.g., "v4.0")

        Returns:
            Deployment result dictionary
        """
        version = version or f"v{datetime.now().strftime('%Y%m%d_%H%M')}"

        logger.info(f"Deploying model version: {version}")

        # Backup current model
        backup_dir = self.models_dir / "checkpoints" / f"backup_{version}"
        backup_dir.mkdir(parents=True, exist_ok=True)

        for filename in ["final_model.pkl",
                         "scaler_final.pkl",
                         "feature_names_final.pkl"]:
            src = self.models_dir / filename
            if src.exists():
                shutil.copy(src, backup_dir / filename)
                logger.info(f"Backed up: {filename}")

        # Deploy new model
        with open(self.models_dir / "final_model.pkl", "wb") as f:
            pickle.dump(training_result["model"], f)

        with open(self.models_dir / "scaler_final.pkl", "wb") as f:
            pickle.dump(training_result["scaler"], f)

        with open(self.models_dir / "feature_names_final.pkl", "wb") as f:
            pickle.dump(training_result["feature_names"], f)

        # Save version info
        version_info = {
            "version":    version,
            "deployed_at": datetime.now().isoformat(),
            "metrics":    training_result["metrics"],
            "n_features": training_result["n_features"],
            "backup_dir": str(backup_dir)
        }

        version_file = self.models_dir / "version_info.json"
        with open(version_file, "w") as f:
            json.dump(version_info, f, indent=2)

        logger.info(f"✅ Model {version} deployed successfully!")
        return version_info

    def run_full_pipeline(self,
                          trigger_reason: str = "Manual",
                          force_deploy:   bool = False) -> dict:
        """
        Run the complete retraining pipeline

        Args:
            trigger_reason: Why retraining was triggered
            force_deploy:   Deploy even if metrics don't improve

        Returns:
            Complete pipeline results
        """
        logger.info(f"Starting retraining pipeline: {trigger_reason}")
        pipeline_start = datetime.now()
        results = {"trigger": trigger_reason, "steps": {}}

        try:
            # Step 1: Load data
            logger.info("Step 1/5: Loading data...")
            df = self.load_training_data()
            results["steps"]["load_data"] = {"status": "success",
                                              "shape":  str(df.shape)}

            # Step 2: Validate
            logger.info("Step 2/5: Validating data...")
            validation = self.validate_data(df)
            results["steps"]["validate"] = validation

            if not validation["is_valid"]:
                raise ValueError(f"Data validation failed: {validation['issues']}")

            # Step 3: Train new model
            logger.info("Step 3/5: Training new model...")
            training = self.train_new_model(df)
            results["steps"]["training"] = {
                "status":  "success",
                "metrics": training["metrics"],
                "time_s":  training["training_time_s"]
            }

            # Step 4: Compare models
            logger.info("Step 4/5: Comparing models...")
            current_metrics = self._load_current_metrics()
            comparison = self.compare_models(current_metrics,
                                              training["metrics"])
            results["steps"]["comparison"] = comparison

            # Step 5: Deploy if better
            logger.info("Step 5/5: Deploying model...")
            if comparison["should_deploy"] or force_deploy:
                version     = f"v{datetime.now().strftime('%Y%m%d')}"
                deploy_info = self.deploy_model(training, version)
                results["steps"]["deployment"] = {
                    "status":  "deployed",
                    "version": version,
                    "reason":  comparison["reason"]
                }
                logger.info(f"✅ New model deployed: {version}")
            else:
                results["steps"]["deployment"] = {
                    "status": "skipped",
                    "reason": comparison["reason"]
                }
                logger.info("ℹ️ Deployment skipped - no improvement")

            results["status"] = "success"

        except Exception as e:
            results["status"] = "failed"
            results["error"]  = str(e)
            logger.error(f"Pipeline failed: {e}")

        # Log pipeline run
        duration = (datetime.now() - pipeline_start).seconds
        results["duration_s"]  = duration
        results["completed_at"] = datetime.now().isoformat()

        self._log_pipeline_run(results)
        logger.info(f"Pipeline complete in {duration}s: {results['status']}")

        return results

    # ------------------------------------------------------------------ #
    # Private Methods
    # ------------------------------------------------------------------ #

    def _load_current_metrics(self) -> dict:
        """Load current model metrics from version info"""
        version_file = self.models_dir / "version_info.json"

        if version_file.exists():
            with open(version_file, "r") as f:
                info = json.load(f)
            return info.get("metrics", {"test_accuracy": 0.765,
                                         "false_negatives": 31})

        # Default current metrics (V3)
        return {"test_accuracy": 0.765, "false_negatives": 31}

    def _log_pipeline_run(self, results: dict) -> None:
        """Log pipeline run to history file"""
        history = []
        if self.run_log.exists():
            with open(self.run_log, "r") as f:
                history = json.load(f)

        history.append({
            "timestamp":  results.get("completed_at"),
            "trigger":    results.get("trigger"),
            "status":     results.get("status"),
            "duration_s": results.get("duration_s")
        })

        with open(self.run_log, "w") as f:
            json.dump(history[-50:], f, indent=2)  # Keep last 50 runs


# ============================================================================
# Standalone demo
# ============================================================================

if __name__ == "__main__":
    print("🔄 NBE Retraining Pipeline Demo")
    print("=" * 50)

    pipeline = RetrainingPipeline()

    # Check trigger
    trigger = pipeline.check_trigger(
        current_accuracy=0.68,
        drift_status="warning"
    )

    print(f"\n🎯 Trigger Check:")
    print(f"   Should retrain: {trigger['should_retrain']}")
    print(f"   Reasons: {trigger['triggers']}")

    if trigger["should_retrain"]:
        print("\n🚀 Running retraining pipeline...")
        try:
            results = pipeline.run_full_pipeline(
                trigger_reason="Demo",
                force_deploy=False
            )
            print(f"\n✅ Pipeline Status: {results['status']}")
            if "training" in results.get("steps", {}):
                metrics = results["steps"]["training"]["metrics"]
                print(f"   New Accuracy: {metrics['test_accuracy']:.2%}")
                print(f"   False Negatives: {metrics['false_negatives']}")
        except Exception as e:
            print(f"\n⚠️ Pipeline error: {e}")
            print("   (This is expected in demo mode without data files)")

    print("\n✅ Retraining pipeline demo complete!")

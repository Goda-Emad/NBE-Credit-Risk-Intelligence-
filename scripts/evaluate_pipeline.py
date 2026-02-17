"""
Model Evaluation Pipeline Script
Runs comprehensive model evaluation and generates reports
Usage: python scripts/evaluate_pipeline.py
"""

import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
from pathlib import Path
from datetime import datetime
from sklearn.metrics import (
    accuracy_score, roc_curve, auc,
    classification_report, confusion_matrix
)
from sklearn.model_selection import train_test_split

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.models.evaluate_model    import ModelEvaluator
from src.visualization.visualize  import CreditRiskVisualizer
from src.utils.logging_config     import setup_logging

logger = setup_logging(log_level="INFO", log_dir="logs")


def load_artifacts() -> tuple:
    """Load all model artifacts"""
    print("\n📦 Loading model artifacts...")

    with open("models/final_model.pkl",          "rb") as f:
        model = pickle.load(f)
    with open("models/scaler_final.pkl",         "rb") as f:
        scaler = pickle.load(f)
    with open("models/feature_names_final.pkl",  "rb") as f:
        feature_names = pickle.load(f)

    print(f"  ✅ Model:    {type(model).__name__}")
    print(f"  ✅ Features: {len(feature_names)}")
    return model, scaler, feature_names


def load_test_data(feature_names: list) -> tuple:
    """Load and prepare test data"""
    print("\n📊 Loading test data...")

    df = pd.read_csv("data/processed/german_credit_fe_v3.csv")

    X = df[feature_names]
    y = df["Risk"]

    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    _, X_train, _, y_train = train_test_split(
        X, y, test_size=0.8, random_state=42, stratify=y
    )

    print(f"  ✅ Test set: {X_test.shape}")
    return X_train, X_test, y_train, y_test


def run_evaluation() -> dict:
    """Run complete evaluation pipeline"""
    print("="*70)
    print("📈 NBE CREDIT RISK - EVALUATION PIPELINE")
    print("="*70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    results = {}
    Path("reports/figures").mkdir(parents=True, exist_ok=True)

    try:
        # ================================================================
        # Load artifacts & data
        # ================================================================
        model, scaler, feature_names = load_artifacts()
        X_train, X_test, y_train, y_test = load_test_data(feature_names)

        X_train_s = scaler.transform(X_train)
        X_test_s  = scaler.transform(X_test)

        # ================================================================
        # Core Metrics
        # ================================================================
        print("\n📊 STEP 1/5: Core Metrics...")
        evaluator = ModelEvaluator()
        metrics   = evaluator.evaluate(
            model, X_train_s, X_test_s, y_train, y_test
        )
        evaluator.print_report()
        results["metrics"] = metrics

        # ================================================================
        # Classification Report
        # ================================================================
        print("\n📋 STEP 2/5: Classification Report...")
        y_pred = model.predict(X_test_s)
        report = classification_report(
            y_test, y_pred,
            target_names=["Bad Risk", "Good Risk"]
        )
        print(report)

        report_path = "reports/classification_report.txt"
        with open(report_path, "w") as f:
            f.write(f"NBE Credit Risk - Classification Report\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write("="*50 + "\n")
            f.write(report)
        print(f"  ✅ Saved: {report_path}")

        # ================================================================
        # ROC Curve
        # ================================================================
        print("\n📈 STEP 3/5: ROC Curve...")
        y_proba  = model.predict_proba(X_test_s)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc  = auc(fpr, tpr)

        viz = CreditRiskVisualizer(output_dir="reports/figures")
        viz.plot_roc_curve(fpr, tpr, roc_auc)
        results["roc_auc"] = round(roc_auc, 4)
        print(f"  ✅ ROC-AUC: {roc_auc:.4f}")

        # ================================================================
        # Feature Importance
        # ================================================================
        print("\n🎯 STEP 4/5: Feature Importance...")
        if hasattr(model, "feature_importances_"):
            fi = model.feature_importances_
            viz.plot_feature_importance(feature_names, fi, top_n=20)

            # Save to CSV
            fi_df = pd.DataFrame({
                "feature":    feature_names,
                "importance": fi,
                "rank":       range(1, len(feature_names) + 1)
            }).sort_values("importance", ascending=False)
            fi_df.to_csv("reports/feature_importance.csv", index=False)
            print(f"  ✅ Top feature: {fi_df.iloc[0]['feature']}")
            print(f"  ✅ Saved: reports/feature_importance.csv")

        # ================================================================
        # False Negatives Analysis
        # ================================================================
        print("\n⚠️  STEP 5/5: False Negatives Analysis...")
        fn_cases = evaluator.get_false_negatives(
            X_test.reset_index(drop=True),
            y_test.reset_index(drop=True),
            y_pred
        )

        fn_path = "reports/false_negatives_analysis.csv"
        fn_cases.to_csv(fn_path, index=False)

        print(f"  ✅ Total False Negatives: {len(fn_cases)}")
        print(f"  ✅ Saved: {fn_path}")

        if len(fn_cases) > 0 and "Age" in fn_cases.columns:
            print(f"  📊 FN Age range:    {fn_cases['Age'].min():.0f} - "
                  f"{fn_cases['Age'].max():.0f} years")
        if len(fn_cases) > 0 and "Credit_Amount" in fn_cases.columns:
            print(f"  📊 FN Credit range: {fn_cases['Credit_Amount'].min():.0f} - "
                  f"{fn_cases['Credit_Amount'].max():.0f}")

        # ================================================================
        # Summary Report
        # ================================================================
        summary = f"""
# NBE Credit Risk - Evaluation Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Model Performance
- Train Accuracy:  {metrics["train_accuracy"]*100:.2f}%
- Test Accuracy:   {metrics["test_accuracy"]*100:.2f}%
- Precision:       {metrics["precision"]*100:.2f}%
- Recall:          {metrics["recall"]*100:.2f}%
- F1-Score:        {metrics["f1_score"]*100:.2f}%
- ROC-AUC:         {roc_auc:.4f}

## Confusion Matrix
- True Negatives:  {metrics["true_negatives"]}
- False Positives: {metrics["false_positives"]}
- False Negatives: {metrics["false_negatives"]}
- True Positives:  {metrics["true_positives"]}

## Business Impact
- False Negative Rate: {metrics["false_negatives"] / 60 * 100:.1f}%
- False Positive Rate: {metrics["false_positives"] / 140 * 100:.1f}%

## Files Generated
- reports/figures/roc_curve.png
- reports/figures/feature_importance_chart.png
- reports/classification_report.txt
- reports/false_negatives_analysis.csv
"""
        with open("reports/evaluation_summary.md", "w") as f:
            f.write(summary)

        results["status"] = "success"
        print("\n" + "="*70)
        print("🎉 EVALUATION COMPLETE!")
        print("="*70)
        print("\n📂 Reports generated:")
        print("   reports/evaluation_summary.md")
        print("   reports/classification_report.txt")
        print("   reports/false_negatives_analysis.csv")
        print("   reports/figures/roc_curve.png")
        print("   reports/figures/feature_importance_chart.png")

    except Exception as e:
        results["status"] = "failed"
        results["error"]  = str(e)
        logger.error(f"Evaluation failed: {e}")
        print(f"\n❌ Evaluation failed: {e}")
        raise

    return results


if __name__ == "__main__":
    run_evaluation()

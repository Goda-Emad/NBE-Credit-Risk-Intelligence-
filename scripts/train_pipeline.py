"""
Full Training Pipeline Script
Runs complete model training from raw data to saved model
Usage: python scripts/train_pipeline.py
"""

import sys
import pickle
import numpy as np
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.data.data_loader          import DataLoader
from src.data.preprocessing        import DataPreprocessor
from src.features.feature_engineering import FeatureEngineer
from src.features.feature_selection  import FeatureSelector
from src.models.train_model        import ModelTrainer
from src.models.evaluate_model     import ModelEvaluator
from src.utils.logging_config      import setup_logging

# Setup logging
logger = setup_logging(log_level="INFO", log_dir="logs")


def run_pipeline(
    data_file:    str  = "german_credit_original.csv",
    save_model:   bool = True,
    model_type:   str  = "random_forest",
    run_cv:       bool = True
) -> dict:
    """
    Run complete training pipeline

    Args:
        data_file:  Raw data filename
        save_model: Whether to save trained model
        model_type: Model type to train
        run_cv:     Whether to run cross-validation

    Returns:
        Pipeline results dictionary
    """
    print("="*70)
    print("🚀 NBE CREDIT RISK - TRAINING PIPELINE")
    print("="*70)
    print(f"Started:    {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Model type: {model_type}")
    print(f"Data file:  {data_file}")
    print("="*70)

    results = {}
    pipeline_start = datetime.now()

    try:
        # ================================================================
        # STEP 1: Load Data
        # ================================================================
        print("\n📥 STEP 1/6: Loading Data...")
        loader = DataLoader(data_dir="data")
        df_raw = loader.load_raw(data_file)
        loader.get_info(df_raw)

        # Validate
        validation = loader.validate(df_raw)
        if not validation["is_valid"]:
            raise ValueError(f"Data validation failed: {validation['issues']}")

        results["load"] = {
            "status": "success",
            "shape":  df_raw.shape
        }
        print(f"  ✅ Loaded: {df_raw.shape}")

        # ================================================================
        # STEP 2: Preprocessing
        # ================================================================
        print("\n🔧 STEP 2/6: Preprocessing...")
        preprocessor = DataPreprocessor()
        df_clean     = preprocessor.run_pipeline(df_raw)
        summary      = preprocessor.get_summary(df_clean)

        results["preprocess"] = {
            "status":  "success",
            "shape":   df_clean.shape,
            "missing": summary["missing"]
        }
        print(f"  ✅ Preprocessed: {df_clean.shape}")
        print(f"  ✅ Missing values: {summary['missing']}")

        # ================================================================
        # STEP 3: Feature Engineering
        # ================================================================
        print("\n⚙️  STEP 3/6: Feature Engineering...")
        engineer = FeatureEngineer()
        df_fe    = engineer.run_pipeline(df_clean)

        results["features"] = {
            "status":   "success",
            "original": df_clean.shape[1],
            "engineered": df_fe.shape[1]
        }
        print(f"  ✅ Features: {df_clean.shape[1]} → {df_fe.shape[1]}")

        # ================================================================
        # STEP 4: Prepare Train/Test Split
        # ================================================================
        print("\n📊 STEP 4/6: Preparing Train/Test Split...")
        from sklearn.model_selection import train_test_split

        X = df_fe.drop("Risk", axis=1)
        y = df_fe["Risk"]
        feature_names = list(X.columns)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        print(f"  ✅ Train: {len(X_train)} | Test: {len(X_test)}")
        print(f"  ✅ Features: {len(feature_names)}")
        print(f"  ✅ Good Risk (train): {y_train.sum()} ({y_train.mean():.1%})")

        # ================================================================
        # STEP 5: Train Model
        # ================================================================
        print(f"\n🤖 STEP 5/6: Training {model_type}...")
        trainer = ModelTrainer(models_dir="models")

        # Scale features
        X_train_s, X_test_s = trainer.scale_features(X_train, X_test)

        # Train
        model = trainer.train(X_train_s, y_train, model_type)
        print(f"  ✅ Model trained!")

        # Cross-validation
        if run_cv:
            print("  🔄 Running cross-validation (5-fold)...")
            cv_results = trainer.cross_validate(X_train_s, y_train, cv=5)
            print(f"  ✅ CV Score: {cv_results['mean']:.4f} "
                  f"(±{cv_results['std']:.4f})")
            results["cross_validation"] = {
                "mean": round(cv_results["mean"], 4),
                "std":  round(cv_results["std"],  4)
            }

        # ================================================================
        # STEP 6: Evaluate & Save
        # ================================================================
        print("\n📈 STEP 6/6: Evaluating & Saving...")
        evaluator = ModelEvaluator()
        metrics   = evaluator.evaluate(
            model, X_train_s, X_test_s, y_train, y_test
        )
        evaluator.print_report()

        results["evaluation"] = metrics

        # Save artifacts
        if save_model:
            trainer.save("final_model")

            # Save feature names
            with open("models/feature_names_final.pkl", "wb") as f:
                pickle.dump(feature_names, f)
            print("  ✅ Feature names saved!")

            # Save processed data
            df_fe.to_csv(
                "data/processed/german_credit_fe_v3.csv",
                index=False
            )
            print("  ✅ Processed data saved!")

        # ================================================================
        # Summary
        # ================================================================
        duration = (datetime.now() - pipeline_start).seconds
        results["status"]     = "success"
        results["duration_s"] = duration
        results["completed"]  = datetime.now().isoformat()

        print("\n" + "="*70)
        print("🎉 TRAINING PIPELINE COMPLETE!")
        print("="*70)
        print(f"  ✅ Train Accuracy:  {metrics['train_accuracy']*100:.2f}%")
        print(f"  ✅ Test Accuracy:   {metrics['test_accuracy']*100:.2f}%")
        print(f"  ✅ Precision:       {metrics['precision']*100:.2f}%")
        print(f"  ✅ Recall:          {metrics['recall']*100:.2f}%")
        print(f"  ✅ F1-Score:        {metrics['f1_score']*100:.2f}%")
        print(f"  ✅ False Negatives: {metrics['false_negatives']}")
        print(f"  ⏱️  Duration:       {duration}s")
        print("="*70)

        if save_model:
            print("\n💾 Saved artifacts:")
            print("   models/final_model.pkl")
            print("   models/scaler_final.pkl")
            print("   models/feature_names_final.pkl")
            print("   data/processed/german_credit_fe_v3.csv")

        print("\n🚀 Next step: python scripts/evaluate_pipeline.py")

    except Exception as e:
        results["status"] = "failed"
        results["error"]  = str(e)
        logger.error(f"Pipeline failed: {e}")
        print(f"\n❌ Pipeline failed: {e}")
        raise

    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="NBE Credit Risk Training Pipeline"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="random_forest",
        choices=["random_forest", "logistic_regression"],
        help="Model type to train"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save model artifacts"
    )
    parser.add_argument(
        "--no-cv",
        action="store_true",
        help="Skip cross-validation"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="german_credit_original.csv",
        help="Raw data filename"
    )

    args = parser.parse_args()

    run_pipeline(
        data_file=args.data,
        save_model=not args.no_save,
        model_type=args.model,
        run_cv=not args.no_cv
    )

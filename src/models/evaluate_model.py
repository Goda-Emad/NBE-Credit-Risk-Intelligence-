"""
Model Evaluation Module
Handles model performance assessment
"""

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix,
    classification_report
)
import logging

logger = logging.getLogger(__name__)


class ModelEvaluator:
    """Handles model evaluation and reporting"""

    def __init__(self):
        self.results = {}

    def evaluate(self,
                 model,
                 X_train: np.ndarray,
                 X_test: np.ndarray,
                 y_train: pd.Series,
                 y_test: pd.Series) -> dict:
        """
        Complete model evaluation

        Returns:
            Dictionary with all metrics
        """
        # Predictions
        train_pred = model.predict(X_train)
        test_pred  = model.predict(X_test)
        test_proba = model.predict_proba(X_test)[:, 1]

        # Confusion matrix
        cm = confusion_matrix(y_test, test_pred)
        tn, fp, fn, tp = cm.ravel()

        self.results = {
            "train_accuracy":  accuracy_score(y_train, train_pred),
            "test_accuracy":   accuracy_score(y_test,  test_pred),
            "precision":       precision_score(y_test, test_pred),
            "recall":          recall_score(y_test,    test_pred),
            "f1_score":        f1_score(y_test,        test_pred),
            "roc_auc":         roc_auc_score(y_test,   test_proba),
            "true_negatives":  int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives":  int(tp),
            "overfitting_gap": accuracy_score(y_train, train_pred) -
                               accuracy_score(y_test, test_pred)
        }

        logger.info(f"Test Accuracy: {self.results['test_accuracy']:.4f}")
        return self.results

    def get_false_negatives(self,
                            X_test: pd.DataFrame,
                            y_test: pd.Series,
                            y_pred: np.ndarray) -> pd.DataFrame:
        """Get false negative cases for analysis"""
        fn_mask  = (y_test.values == 1) & (y_pred == 0)
        fn_cases = X_test[fn_mask].copy()
        fn_cases["true_label"]      = "Good"
        fn_cases["predicted_label"] = "Bad"
        return fn_cases

    def print_report(self) -> None:
        """Print formatted evaluation report"""
        if not self.results:
            raise ValueError("Run evaluate() first")

        print("=" * 60)
        print("📊 MODEL EVALUATION REPORT")
        print("=" * 60)
        print(f"  Train Accuracy:  {self.results['train_accuracy']*100:.2f}%")
        print(f"  Test Accuracy:   {self.results['test_accuracy']*100:.2f}%")
        print(f"  Overfitting Gap: {self.results['overfitting_gap']*100:.2f}%")
        print("-" * 60)
        print(f"  Precision:       {self.results['precision']*100:.2f}%")
        print(f"  Recall:          {self.results['recall']*100:.2f}%")
        print(f"  F1-Score:        {self.results['f1_score']*100:.2f}%")
        print(f"  ROC-AUC:         {self.results['roc_auc']:.4f}")
        print("-" * 60)
        print(f"  True Negatives:  {self.results['true_negatives']}")
        print(f"  False Positives: {self.results['false_positives']}")
        print(f"  False Negatives: {self.results['false_negatives']} ⚠️")
        print(f"  True Positives:  {self.results['true_positives']}")
        print("=" * 60)

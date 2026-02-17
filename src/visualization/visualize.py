"""
Visualization Module
Generates charts and plots for credit risk analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# NBE Brand Colors
NBE_GREEN = "#006341"
NBE_GOLD  = "#D4AF37"
RED       = "#e74c3c"
BLUE      = "#3498db"


class CreditRiskVisualizer:
    """Generates all visualization charts"""

    def __init__(self, output_dir: str = "reports/figures"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        plt.style.use("seaborn-v0_8-whitegrid")

    def plot_confusion_matrix(self,
                              cm: np.ndarray,
                              title: str = "Confusion Matrix",
                              save: bool = True) -> None:
        """Plot confusion matrix heatmap"""
        fig, ax = plt.subplots(figsize=(8, 6))

        labels = [["TN
" + str(cm[0,0]), "FP
" + str(cm[0,1])],
                  ["FN
" + str(cm[1,0]), "TP
" + str(cm[1,1])]]

        sns.heatmap(cm, annot=labels, fmt="", ax=ax,
                    cmap="Greens", linewidths=2,
                    xticklabels=["Predicted Bad", "Predicted Good"],
                    yticklabels=["Actual Bad",    "Actual Good"],
                    annot_kws={"size": 14, "weight": "bold"})

        ax.set_title(title, fontsize=14, fontweight="bold", color=NBE_GREEN)
        ax.set_xlabel("Predicted Label", fontsize=12)
        ax.set_ylabel("Actual Label",    fontsize=12)

        plt.tight_layout()

        if save:
            path = self.output_dir / "confusion_matrix.png"
            plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
            logger.info(f"Saved: {path}")

        plt.show()

    def plot_feature_importance(self,
                                feature_names: list,
                                importances: np.ndarray,
                                top_n: int = 20,
                                save: bool = True) -> None:
        """Plot top N feature importances"""
        fi_df = pd.DataFrame({
            "feature":    feature_names,
            "importance": importances
        }).sort_values("importance", ascending=False).head(top_n)

        colors = [NBE_GREEN if i < 5 else NBE_GOLD if i < 10 else "#95a5a6"
                  for i in range(len(fi_df))]

        fig, ax = plt.subplots(figsize=(10, 8))
        ax.barh(fi_df["feature"], fi_df["importance"],
                color=colors, edgecolor="white")
        ax.set_title(f"Top {top_n} Feature Importances",
                     fontsize=14, fontweight="bold", color=NBE_GREEN)
        ax.set_xlabel("Importance Score")
        ax.invert_yaxis()

        plt.tight_layout()

        if save:
            path = self.output_dir / "feature_importance_chart.png"
            plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
            logger.info(f"Saved: {path}")

        plt.show()

    def plot_roc_curve(self,
                       fpr: np.ndarray,
                       tpr: np.ndarray,
                       auc_score: float,
                       save: bool = True) -> None:
        """Plot ROC curve"""
        fig, ax = plt.subplots(figsize=(8, 6))

        ax.plot(fpr, tpr, color=NBE_GREEN, lw=2.5,
                label=f"ROC Curve (AUC = {auc_score:.3f})")
        ax.plot([0, 1], [0, 1], "k--", lw=1.5, label="Random Classifier")

        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel("False Positive Rate", fontsize=12)
        ax.set_ylabel("True Positive Rate",  fontsize=12)
        ax.set_title("ROC Curve", fontsize=14, fontweight="bold", color=NBE_GREEN)
        ax.legend(loc="lower right")
        ax.grid(True, alpha=0.3)

        plt.tight_layout()

        if save:
            path = self.output_dir / "roc_curve.png"
            plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
            logger.info(f"Saved: {path}")

        plt.show()

    def plot_risk_distribution(self,
                               df: pd.DataFrame,
                               save: bool = True) -> None:
        """Plot risk distribution pie chart"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        risk_counts = df["Risk"].value_counts()

        axes[0].pie(risk_counts.values,
                    labels=["Bad Risk", "Good Risk"],
                    colors=[RED, NBE_GREEN],
                    autopct="%1.1f%%",
                    startangle=90)
        axes[0].set_title("Risk Distribution",
                          fontsize=13, fontweight="bold")

        risk_counts.plot(kind="bar", ax=axes[1],
                         color=[RED, NBE_GREEN], alpha=0.85)
        axes[1].set_title("Risk Counts", fontsize=13, fontweight="bold")
        axes[1].set_xticklabels(["Bad", "Good"], rotation=0)
        axes[1].set_ylabel("Count")

        plt.tight_layout()

        if save:
            path = self.output_dir / "risk_distribution.png"
            plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
            logger.info(f"Saved: {path}")

        plt.show()

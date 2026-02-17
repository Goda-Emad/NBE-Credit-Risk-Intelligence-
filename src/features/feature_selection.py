"""
Feature Selection Module
Selects most important features for the model
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, RFE
import logging

logger = logging.getLogger(__name__)


class FeatureSelector:
    """Selects most important features"""

    def __init__(self, n_features: int = 30):
        self.n_features      = n_features
        self.selected_features = None
        self.importance_df   = None

    def select_by_importance(self,
                             X: pd.DataFrame,
                             y: pd.Series,
                             model=None) -> list:
        """
        Select features by Random Forest importance

        Args:
            X: Feature DataFrame
            y: Target Series
            model: Trained model (optional)

        Returns:
            List of selected feature names
        """
        if model is None:
            model = RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                class_weight="balanced"
            )
            model.fit(X, y)

        self.importance_df = pd.DataFrame({
            "feature":    X.columns,
            "importance": model.feature_importances_
        }).sort_values("importance", ascending=False)

        self.selected_features = (
            self.importance_df
            .head(self.n_features)["feature"]
            .tolist()
        )

        logger.info(f"Selected {len(self.selected_features)} features")
        return self.selected_features

    def select_by_kbest(self,
                        X: pd.DataFrame,
                        y: pd.Series) -> list:
        """Select features using statistical tests"""
        selector = SelectKBest(f_classif, k=self.n_features)
        selector.fit(X, y)

        mask = selector.get_support()
        selected = X.columns[mask].tolist()

        logger.info(f"KBest selected {len(selected)} features")
        return selected

    def get_importance_report(self) -> pd.DataFrame:
        """Get feature importance report"""
        if self.importance_df is None:
            raise ValueError("Run select_by_importance() first")

        self.importance_df["cumulative"] = (
            self.importance_df["importance"].cumsum()
        )
        self.importance_df["rank"] = range(1, len(self.importance_df) + 1)

        return self.importance_df

    def get_features_for_threshold(self, threshold: float = 0.80) -> list:
        """Get minimum features needed to reach importance threshold"""
        if self.importance_df is None:
            raise ValueError("Run select_by_importance() first")

        cumsum = self.importance_df["importance"].cumsum()
        n = (cumsum >= threshold).idxmax() + 1

        features = self.importance_df.head(n)["feature"].tolist()
        logger.info(f"{len(features)} features cover {threshold*100:.0f}% importance")
        return features

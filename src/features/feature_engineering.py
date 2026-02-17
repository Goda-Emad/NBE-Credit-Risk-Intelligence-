"""
Feature Engineering Module
Creates 73 engineered features from 20 original features
"""

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


class FeatureEngineer:
    """Creates engineered features for credit risk modeling"""

    def __init__(self):
        self.categorical_cols = [
            "Status_Account", "Credit_History", "Purpose", "Savings",
            "Employment", "Personal_Status", "Other_Debtors", "Property",
            "Other_Plans", "Housing", "Job", "Telephone", "Foreign_Worker"
        ]

    def create_age_groups(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create age group binary features"""
        df["age_young"]  = (df["Age"] < 25).astype(int)
        df["age_middle"] = ((df["Age"] >= 25) & (df["Age"] < 60)).astype(int)
        df["age_senior"] = (df["Age"] >= 60).astype(int)
        return df

    def create_credit_bins(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create credit amount bin features"""
        df["credit_low"]    = (df["Credit_Amount"] < 2500).astype(int)
        df["credit_medium"] = ((df["Credit_Amount"] >= 2500) &
                               (df["Credit_Amount"] < 5000)).astype(int)
        df["credit_high"]   = (df["Credit_Amount"] >= 5000).astype(int)
        return df

    def create_duration_bins(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create duration bin features"""
        df["duration_short"]  = (df["Duration"] <= 12).astype(int)
        df["duration_medium"] = ((df["Duration"] > 12) &
                                 (df["Duration"] <= 24)).astype(int)
        df["duration_long"]   = (df["Duration"] > 24).astype(int)
        return df

    def create_financial_ratios(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create financial ratio features"""
        df["credit_duration_ratio"]  = df["Credit_Amount"] / (df["Duration"] + 1)
        df["credit_age_ratio"]       = df["Credit_Amount"] / (df["Age"] + 1)
        df["age_credit_interaction"] = df["Age"] * df["Credit_Amount"] / 1000
        return df

    def encode_categoricals(self, df: pd.DataFrame) -> pd.DataFrame:
        """One-hot encode categorical variables"""
        cols_to_encode = [c for c in self.categorical_cols if c in df.columns]
        df = pd.get_dummies(df, columns=cols_to_encode,
                            drop_first=False, dtype=int)
        return df

    def run_pipeline(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run complete feature engineering pipeline"""
        logger.info("Starting feature engineering...")
        original_features = df.shape[1]

        df = df.copy()
        df = self.create_age_groups(df)
        df = self.create_credit_bins(df)
        df = self.create_duration_bins(df)
        df = self.create_financial_ratios(df)
        df = self.encode_categoricals(df)

        new_features = df.shape[1]
        logger.info(f"Features: {original_features} → {new_features}")
        return df

    def get_feature_groups(self) -> dict:
        """Return feature groups for analysis"""
        return {
            "age_features":      ["age_young", "age_middle", "age_senior"],
            "credit_features":   ["credit_low", "credit_medium", "credit_high"],
            "duration_features": ["duration_short", "duration_medium", "duration_long"],
            "ratio_features":    ["credit_duration_ratio",
                                  "credit_age_ratio",
                                  "age_credit_interaction"],
        }

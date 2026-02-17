"""
Data Preprocessing Module
Handles data cleaning and preparation
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DataPreprocessor:
    """Handles all data preprocessing operations"""

    def __init__(self):
        self.categorical_cols = [
            "Status_Account", "Credit_History", "Purpose", "Savings",
            "Employment", "Personal_Status", "Other_Debtors", "Property",
            "Other_Plans", "Housing", "Job", "Telephone", "Foreign_Worker"
        ]
        self.numerical_cols = [
            "Duration", "Credit_Amount", "Installment_Rate",
            "Residence_Since", "Age", "Existing_Credits", "Num_Dependents"
        ]

    def map_target(self, df: pd.DataFrame) -> pd.DataFrame:
        """Map Risk: 1=Bad → 0, 2=Good → 1"""
        df = df.copy()
        if df["Risk"].max() == 2:
            df["Risk"] = df["Risk"].map({1: 0, 2: 1})
            logger.info("Target mapped: 1=Bad→0, 2=Good→1")
        return df

    def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values"""
        df = df.copy()
        missing = df.isnull().sum()

        if missing.sum() == 0:
            logger.info("No missing values found")
            return df

        # Fill numerical with median
        for col in self.numerical_cols:
            if col in df.columns and df[col].isnull().any():
                df[col].fillna(df[col].median(), inplace=True)
                logger.info(f"Filled {col} with median")

        # Fill categorical with mode
        for col in self.categorical_cols:
            if col in df.columns and df[col].isnull().any():
                df[col].fillna(df[col].mode()[0], inplace=True)
                logger.info(f"Filled {col} with mode")

        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicate rows"""
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)

        if before != after:
            logger.info(f"Removed {before - after} duplicates")

        return df

    def validate_ranges(self, df: pd.DataFrame) -> pd.DataFrame:
        """Validate and clip numerical ranges"""
        df = df.copy()
        ranges = {
            "Age":           (18, 100),
            "Duration":      (1,  120),
            "Credit_Amount": (1,  100000),
        }
        for col, (min_val, max_val) in ranges.items():
            if col in df.columns:
                df[col] = df[col].clip(min_val, max_val)
        return df

    def run_pipeline(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run complete preprocessing pipeline"""
        logger.info("Starting preprocessing pipeline...")

        df = self.map_target(df)
        df = self.handle_missing(df)
        df = self.remove_duplicates(df)
        df = self.validate_ranges(df)

        logger.info(f"Preprocessing complete: {df.shape}")
        return df

    def get_summary(self, df: pd.DataFrame) -> dict:
        """Get preprocessing summary"""
        return {
            "shape":          df.shape,
            "missing":        df.isnull().sum().sum(),
            "duplicates":     df.duplicated().sum(),
            "target_balance": df["Risk"].value_counts().to_dict()
                              if "Risk" in df.columns else None
        }

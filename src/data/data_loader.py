"""
Data Loader Module
Handles loading raw data from various sources
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Column names for German Credit Dataset
COLUMN_NAMES = [
    "Status_Account", "Duration", "Credit_History", "Purpose",
    "Credit_Amount", "Savings", "Employment", "Installment_Rate",
    "Personal_Status", "Other_Debtors", "Residence_Since", "Property",
    "Age", "Other_Plans", "Housing", "Existing_Credits", "Job",
    "Num_Dependents", "Telephone", "Foreign_Worker", "Risk"
]


class DataLoader:
    """Handles all data loading operations"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

    def load_raw(self, filename: str = "german_credit_original.csv") -> pd.DataFrame:
        """
        Load raw German Credit Dataset

        Args:
            filename: Name of the raw data file

        Returns:
            DataFrame with raw data
        """
        filepath = self.data_dir / "raw" / filename

        # Try CSV first
        if filepath.exists():
            df = pd.read_csv(filepath)
            logger.info(f"Loaded CSV: {df.shape}")
            return df

        # Try .data format
        data_filepath = self.data_dir / "raw" / "german.data"
        if data_filepath.exists():
            df = pd.read_csv(
                data_filepath,
                sep=r"\s+",
                header=None,
                names=COLUMN_NAMES
            )
            logger.info(f"Loaded .data file: {df.shape}")
            return df

        raise FileNotFoundError(f"No data file found in {self.data_dir}/raw/")

    def load_processed(self, filename: str = "german_credit_fe_v3.csv") -> pd.DataFrame:
        """Load processed/engineered dataset"""
        filepath = self.data_dir / "processed" / filename

        if not filepath.exists():
            raise FileNotFoundError(f"Processed data not found: {filepath}")

        df = pd.read_csv(filepath)
        logger.info(f"Loaded processed data: {df.shape}")
        return df

    def validate(self, df: pd.DataFrame) -> dict:
        """
        Validate loaded dataset

        Returns:
            Dictionary with validation results
        """
        results = {
            "rows":           len(df),
            "columns":        len(df.columns),
            "missing_values": df.isnull().sum().sum(),
            "duplicates":     df.duplicated().sum(),
            "is_valid":       True,
            "issues":         []
        }

        if results["missing_values"] > 0:
            results["issues"].append(f"Missing values: {results['missing_values']}")
            results["is_valid"] = False

        if results["duplicates"] > 0:
            results["issues"].append(f"Duplicates: {results['duplicates']}")

        if "Risk" not in df.columns:
            results["issues"].append("Missing target column: Risk")
            results["is_valid"] = False

        logger.info(f"Validation: {results}")
        return results

    def get_info(self, df: pd.DataFrame) -> None:
        """Print dataset information"""
        print("=" * 60)
        print("📊 DATASET INFO")
        print("=" * 60)
        print(f"  Rows:           {len(df):,}")
        print(f"  Columns:        {len(df.columns)}")
        print(f"  Missing Values: {df.isnull().sum().sum()}")
        print(f"  Memory Usage:   {df.memory_usage(deep=True).sum() / 1024:.1f} KB")

        if "Risk" in df.columns:
            print(f"  Good Risk (1):  {(df['Risk']==1).sum()} ({(df['Risk']==1).mean()*100:.1f}%)")
            print(f"  Bad Risk  (0):  {(df['Risk']==0).sum()} ({(df['Risk']==0).mean()*100:.1f}%)")
        print("=" * 60)

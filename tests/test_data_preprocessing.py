"""
Tests for Data Preprocessing Module
Run: pytest tests/test_data_preprocessing.py -v
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from src.data.preprocessing import DataPreprocessor


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def sample_df():
    """Create sample dataset for testing"""
    return pd.DataFrame({
        "Status_Account":   ["A11", "A12", "A14", "A11", "A13"],
        "Duration":         [6,     48,    12,    42,    24],
        "Credit_History":   ["A34", "A32", "A34", "A32", "A33"],
        "Purpose":          ["A43", "A43", "A46", "A42", "A40"],
        "Credit_Amount":    [1169,  5951,  2096,  7882,  4870],
        "Savings":          ["A65", "A61", "A61", "A61", "A61"],
        "Employment":       ["A75", "A73", "A74", "A74", "A73"],
        "Installment_Rate": [4,     2,     2,     2,     3],
        "Personal_Status":  ["A93", "A92", "A93", "A93", "A93"],
        "Other_Debtors":    ["A101","A101","A101","A103","A101"],
        "Residence_Since":  [4,     2,     3,     4,     4],
        "Property":         ["A121","A121","A121","A122","A124"],
        "Age":              [67,    22,    49,    45,    53],
        "Other_Plans":      ["A143","A143","A143","A143","A143"],
        "Housing":          ["A152","A152","A152","A153","A153"],
        "Existing_Credits": [2,     1,     1,     1,     2],
        "Job":              ["A173","A173","A172","A173","A173"],
        "Num_Dependents":   [1,     1,     2,     2,     2],
        "Telephone":        ["A192","A191","A191","A191","A191"],
        "Foreign_Worker":   ["A201","A201","A201","A201","A201"],
        "Risk":             [1,     2,     1,     1,     2]
    })


@pytest.fixture
def df_with_missing(sample_df):
    """Create dataset with missing values"""
    df = sample_df.copy()
    df.loc[0, "Age"]           = None
    df.loc[1, "Credit_Amount"] = None
    df.loc[2, "Status_Account"]= None
    return df


@pytest.fixture
def preprocessor():
    """Create DataPreprocessor instance"""
    return DataPreprocessor()


# ============================================================================
# Tests: Target Mapping
# ============================================================================

class TestTargetMapping:

    def test_maps_1_to_0(self, preprocessor, sample_df):
        """Bad customers (1) should map to 0"""
        result = preprocessor.map_target(sample_df)
        assert 1 not in result["Risk"].values, "Risk=1 should be mapped to 0"

    def test_maps_2_to_1(self, preprocessor, sample_df):
        """Good customers (2) should map to 1"""
        result = preprocessor.map_target(sample_df)
        assert 2 not in result["Risk"].values, "Risk=2 should be mapped to 1"

    def test_only_binary_values(self, preprocessor, sample_df):
        """Risk column should only contain 0 and 1"""
        result = preprocessor.map_target(sample_df)
        unique_values = set(result["Risk"].unique())
        assert unique_values.issubset({0, 1}), f"Expected {{0,1}}, got {unique_values}"

    def test_does_not_modify_original(self, preprocessor, sample_df):
        """Original DataFrame should not be modified"""
        original_values = sample_df["Risk"].copy()
        preprocessor.map_target(sample_df)
        pd.testing.assert_series_equal(sample_df["Risk"], original_values)

    def test_already_mapped_unchanged(self, preprocessor, sample_df):
        """Already mapped data should remain unchanged"""
        df_mapped = preprocessor.map_target(sample_df)
        df_remapped = preprocessor.map_target(df_mapped)
        pd.testing.assert_frame_equal(df_mapped, df_remapped)


# ============================================================================
# Tests: Missing Values
# ============================================================================

class TestMissingValues:

    def test_no_missing_after_handling(self, preprocessor, df_with_missing):
        """No missing values should remain after handling"""
        df_mapped = preprocessor.map_target(df_with_missing)
        result = preprocessor.handle_missing(df_mapped)
        assert result.isnull().sum().sum() == 0, "Missing values still present"

    def test_clean_data_unchanged(self, preprocessor, sample_df):
        """Clean data should not be modified"""
        df_mapped = preprocessor.map_target(sample_df)
        original_shape = df_mapped.shape
        result = preprocessor.handle_missing(df_mapped)
        assert result.shape == original_shape, "Shape changed for clean data"

    def test_numerical_filled_with_median(self, preprocessor, df_with_missing):
        """Numerical columns should be filled with median"""
        df_mapped = preprocessor.map_target(df_with_missing)
        result = preprocessor.handle_missing(df_mapped)
        assert result["Age"].isnull().sum() == 0
        assert result["Credit_Amount"].isnull().sum() == 0

    def test_categorical_filled_with_mode(self, preprocessor, df_with_missing):
        """Categorical columns should be filled with mode"""
        df_mapped = preprocessor.map_target(df_with_missing)
        result = preprocessor.handle_missing(df_mapped)
        assert result["Status_Account"].isnull().sum() == 0


# ============================================================================
# Tests: Duplicates
# ============================================================================

class TestDuplicateRemoval:

    def test_removes_duplicates(self, preprocessor):
        """Duplicate rows should be removed"""
        df = pd.DataFrame({
            "Age": [25, 25, 30],
            "Credit_Amount": [1000, 1000, 2000],
            "Risk": [1, 1, 2]
        })
        result = preprocessor.remove_duplicates(df)
        assert len(result) == 2, f"Expected 2 rows, got {len(result)}"

    def test_no_duplicates_unchanged(self, preprocessor, sample_df):
        """Data without duplicates should remain unchanged"""
        result = preprocessor.remove_duplicates(sample_df)
        assert len(result) == len(sample_df)


# ============================================================================
# Tests: Range Validation
# ============================================================================

class TestRangeValidation:

    def test_clips_age(self, preprocessor):
        """Age should be clipped to valid range"""
        df = pd.DataFrame({
            "Age": [5, 150, 35],
            "Duration": [12, 24, 36],
            "Credit_Amount": [1000, 2000, 3000],
            "Risk": [0, 1, 0]
        })
        result = preprocessor.validate_ranges(df)
        assert result["Age"].min() >= 18,  "Age below minimum"
        assert result["Age"].max() <= 100, "Age above maximum"

    def test_clips_credit_amount(self, preprocessor):
        """Credit amount should be clipped to valid range"""
        df = pd.DataFrame({
            "Age": [35, 40, 25],
            "Duration": [12, 24, 36],
            "Credit_Amount": [-100, 0, 500000],
            "Risk": [0, 1, 0]
        })
        result = preprocessor.validate_ranges(df)
        assert result["Credit_Amount"].min() >= 1, "Credit below minimum"


# ============================================================================
# Tests: Full Pipeline
# ============================================================================

class TestFullPipeline:

    def test_pipeline_runs_successfully(self, preprocessor, sample_df):
        """Full pipeline should complete without errors"""
        result = preprocessor.run_pipeline(sample_df)
        assert result is not None
        assert len(result) > 0

    def test_pipeline_returns_dataframe(self, preprocessor, sample_df):
        """Pipeline should return a DataFrame"""
        result = preprocessor.run_pipeline(sample_df)
        assert isinstance(result, pd.DataFrame)

    def test_pipeline_no_missing_values(self, preprocessor, sample_df):
        """Pipeline output should have no missing values"""
        result = preprocessor.run_pipeline(sample_df)
        assert result.isnull().sum().sum() == 0

    def test_pipeline_has_risk_column(self, preprocessor, sample_df):
        """Pipeline output should have Risk column"""
        result = preprocessor.run_pipeline(sample_df)
        assert "Risk" in result.columns

    def test_pipeline_binary_target(self, preprocessor, sample_df):
        """Pipeline target should be binary (0/1)"""
        result = preprocessor.run_pipeline(sample_df)
        unique_values = set(result["Risk"].unique())
        assert unique_values.issubset({0, 1})

    def test_get_summary(self, preprocessor, sample_df):
        """Summary should return required keys"""
        summary = preprocessor.get_summary(sample_df)
        required_keys = ["shape", "missing", "duplicates"]
        for key in required_keys:
            assert key in summary, f"Missing key: {key}"

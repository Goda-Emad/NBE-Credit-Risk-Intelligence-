"""
Tests for Feature Engineering Module
Run: pytest tests/test_feature_engineering.py -v
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.features.feature_engineering import FeatureEngineer


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
        "Risk":             [0,     1,     0,     0,     1]
    })


@pytest.fixture
def engineer():
    """Create FeatureEngineer instance"""
    return FeatureEngineer()


# ============================================================================
# Tests: Age Groups
# ============================================================================

class TestAgeGroups:

    def test_creates_age_young(self, engineer, sample_df):
        """Should create age_young column"""
        result = engineer.create_age_groups(sample_df)
        assert "age_young" in result.columns

    def test_creates_age_middle(self, engineer, sample_df):
        """Should create age_middle column"""
        result = engineer.create_age_groups(sample_df)
        assert "age_middle" in result.columns

    def test_creates_age_senior(self, engineer, sample_df):
        """Should create age_senior column"""
        result = engineer.create_age_groups(sample_df)
        assert "age_senior" in result.columns

    def test_young_age_threshold(self, engineer):
        """Age < 25 should be young"""
        df = pd.DataFrame({"Age": [20, 24, 25, 30]})
        result = engineer.create_age_groups(df)
        assert result.loc[0, "age_young"] == 1
        assert result.loc[2, "age_young"] == 0

    def test_senior_age_threshold(self, engineer):
        """Age >= 60 should be senior"""
        df = pd.DataFrame({"Age": [59, 60, 65, 75]})
        result = engineer.create_age_groups(df)
        assert result.loc[0, "age_senior"] == 0
        assert result.loc[1, "age_senior"] == 1

    def test_binary_values_only(self, engineer, sample_df):
        """Age group columns should only contain 0 and 1"""
        result = engineer.create_age_groups(sample_df)
        for col in ["age_young", "age_middle", "age_senior"]:
            assert set(result[col].unique()).issubset({0, 1})

    def test_mutually_exclusive(self, engineer, sample_df):
        """Each customer should belong to exactly one age group"""
        result = engineer.create_age_groups(sample_df)
        group_sum = (result["age_young"] +
                     result["age_middle"] +
                     result["age_senior"])
        assert (group_sum == 1).all(), "Age groups not mutually exclusive"


# ============================================================================
# Tests: Credit Bins
# ============================================================================

class TestCreditBins:

    def test_creates_all_bins(self, engineer, sample_df):
        """Should create all three credit bin columns"""
        result = engineer.create_credit_bins(sample_df)
        for col in ["credit_low", "credit_medium", "credit_high"]:
            assert col in result.columns

    def test_low_credit_threshold(self, engineer):
        """Credit < 2500 should be low"""
        df = pd.DataFrame({"Credit_Amount": [1000, 2499, 2500, 5000]})
        result = engineer.create_credit_bins(df)
        assert result.loc[0, "credit_low"] == 1
        assert result.loc[2, "credit_low"] == 0

    def test_high_credit_threshold(self, engineer):
        """Credit >= 5000 should be high"""
        df = pd.DataFrame({"Credit_Amount": [4999, 5000, 10000]})
        result = engineer.create_credit_bins(df)
        assert result.loc[0, "credit_high"] == 0
        assert result.loc[1, "credit_high"] == 1

    def test_mutually_exclusive(self, engineer, sample_df):
        """Each customer should belong to exactly one credit bin"""
        result = engineer.create_credit_bins(sample_df)
        bin_sum = (result["credit_low"] +
                   result["credit_medium"] +
                   result["credit_high"])
        assert (bin_sum == 1).all()


# ============================================================================
# Tests: Duration Bins
# ============================================================================

class TestDurationBins:

    def test_creates_all_bins(self, engineer, sample_df):
        """Should create all three duration bin columns"""
        result = engineer.create_duration_bins(sample_df)
        for col in ["duration_short", "duration_medium", "duration_long"]:
            assert col in result.columns

    def test_short_duration_threshold(self, engineer):
        """Duration <= 12 should be short"""
        df = pd.DataFrame({"Duration": [6, 12, 13, 24]})
        result = engineer.create_duration_bins(df)
        assert result.loc[0, "duration_short"] == 1
        assert result.loc[1, "duration_short"] == 1
        assert result.loc[2, "duration_short"] == 0

    def test_long_duration_threshold(self, engineer):
        """Duration > 24 should be long"""
        df = pd.DataFrame({"Duration": [24, 25, 36, 72]})
        result = engineer.create_duration_bins(df)
        assert result.loc[0, "duration_long"] == 0
        assert result.loc[1, "duration_long"] == 1

    def test_mutually_exclusive(self, engineer, sample_df):
        """Each customer should belong to exactly one duration bin"""
        result = engineer.create_duration_bins(sample_df)
        bin_sum = (result["duration_short"] +
                   result["duration_medium"] +
                   result["duration_long"])
        assert (bin_sum == 1).all()


# ============================================================================
# Tests: Financial Ratios
# ============================================================================

class TestFinancialRatios:

    def test_creates_all_ratios(self, engineer, sample_df):
        """Should create all ratio columns"""
        result = engineer.create_financial_ratios(sample_df)
        for col in ["credit_duration_ratio",
                    "credit_age_ratio",
                    "age_credit_interaction"]:
            assert col in result.columns

    def test_no_division_by_zero(self, engineer):
        """Should handle zero values without error"""
        df = pd.DataFrame({
            "Credit_Amount": [1000, 2000],
            "Duration":      [0,    12],
            "Age":           [0,    35]
        })
        result = engineer.create_financial_ratios(df)
        assert not result["credit_duration_ratio"].isnull().any()
        assert not result["credit_age_ratio"].isnull().any()

    def test_ratio_values_positive(self, engineer, sample_df):
        """All ratio values should be positive"""
        result = engineer.create_financial_ratios(sample_df)
        assert (result["credit_duration_ratio"] > 0).all()
        assert (result["credit_age_ratio"] > 0).all()
        assert (result["age_credit_interaction"] > 0).all()


# ============================================================================
# Tests: Categorical Encoding
# ============================================================================

class TestCategoricalEncoding:

    def test_removes_original_columns(self, engineer, sample_df):
        """Original categorical columns should be removed after encoding"""
        result = engineer.encode_categoricals(sample_df)
        for col in engineer.categorical_cols:
            assert col not in result.columns, f"{col} still present"

    def test_creates_encoded_columns(self, engineer, sample_df):
        """Encoded columns should be created"""
        result = engineer.encode_categoricals(sample_df)
        assert "Status_Account_A11" in result.columns or                any("Status_Account" in c for c in result.columns)

    def test_encoded_values_binary(self, engineer, sample_df):
        """Encoded columns should only contain 0 and 1"""
        result = engineer.encode_categoricals(sample_df)
        encoded_cols = [c for c in result.columns
                       if any(cat in c for cat in ["Status_Account",
                                                    "Housing", "Job"])]
        for col in encoded_cols:
            assert set(result[col].unique()).issubset({0, 1})


# ============================================================================
# Tests: Full Pipeline
# ============================================================================

class TestFullPipeline:

    def test_pipeline_runs(self, engineer, sample_df):
        """Pipeline should complete without errors"""
        result = engineer.run_pipeline(sample_df)
        assert result is not None

    def test_pipeline_increases_features(self, engineer, sample_df):
        """Pipeline should increase number of features"""
        original_cols = sample_df.shape[1]
        result = engineer.run_pipeline(sample_df)
        assert result.shape[1] > original_cols

    def test_pipeline_preserves_rows(self, engineer, sample_df):
        """Pipeline should not change number of rows"""
        result = engineer.run_pipeline(sample_df)
        assert result.shape[0] == sample_df.shape[0]

    def test_pipeline_no_missing(self, engineer, sample_df):
        """Pipeline output should have no missing values"""
        result = engineer.run_pipeline(sample_df)
        assert result.isnull().sum().sum() == 0

    def test_get_feature_groups(self, engineer):
        """Feature groups should return correct structure"""
        groups = engineer.get_feature_groups()
        assert "age_features"      in groups
        assert "credit_features"   in groups
        assert "duration_features" in groups
        assert "ratio_features"    in groups
        assert len(groups["age_features"]) == 3

"""Feature Transformation for Streamlit App"""
import pandas as pd
import numpy as np


CATEGORICAL_COLS = [
    "Status_Account", "Credit_History", "Purpose", "Savings",
    "Employment", "Personal_Status", "Other_Debtors", "Property",
    "Other_Plans", "Housing", "Job", "Telephone", "Foreign_Worker"
]


def transform_input(
    input_data: dict,
    feature_names: list,
    scaler
) -> np.ndarray:
    """
    Transform raw input into model-ready features

    Args:
        input_data:    Raw input dictionary
        feature_names: Expected feature names from model
        scaler:        Fitted StandardScaler

    Returns:
        Scaled numpy array ready for prediction
    """
    df = pd.DataFrame([input_data])

    # Feature Engineering
    df = _create_age_groups(df)
    df = _create_credit_bins(df)
    df = _create_duration_bins(df)
    df = _create_financial_ratios(df)
    df = _encode_categoricals(df)

    # Align with training features
    for feature in feature_names:
        if feature not in df.columns:
            df[feature] = 0

    df = df[feature_names]

    # Scale
    return scaler.transform(df)


def _create_age_groups(df: pd.DataFrame) -> pd.DataFrame:
    df["age_young"]  = (df["Age"] < 25).astype(int)
    df["age_middle"] = ((df["Age"] >= 25) & (df["Age"] < 60)).astype(int)
    df["age_senior"] = (df["Age"] >= 60).astype(int)
    return df


def _create_credit_bins(df: pd.DataFrame) -> pd.DataFrame:
    df["credit_low"]    = (df["Credit_Amount"] < 2500).astype(int)
    df["credit_medium"] = ((df["Credit_Amount"] >= 2500) &
                           (df["Credit_Amount"] < 5000)).astype(int)
    df["credit_high"]   = (df["Credit_Amount"] >= 5000).astype(int)
    return df


def _create_duration_bins(df: pd.DataFrame) -> pd.DataFrame:
    df["duration_short"]  = (df["Duration"] <= 12).astype(int)
    df["duration_medium"] = ((df["Duration"] > 12) &
                              (df["Duration"] <= 24)).astype(int)
    df["duration_long"]   = (df["Duration"] > 24).astype(int)
    return df


def _create_financial_ratios(df: pd.DataFrame) -> pd.DataFrame:
    df["credit_duration_ratio"]  = df["Credit_Amount"] / (df["Duration"] + 1)
    df["credit_age_ratio"]       = df["Credit_Amount"] / (df["Age"] + 1)
    df["age_credit_interaction"] = df["Age"] * df["Credit_Amount"] / 1000
    return df


def _encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in CATEGORICAL_COLS if c in df.columns]
    return pd.get_dummies(df, columns=cols,
                          drop_first=False, dtype=int)


def get_input_options() -> dict:
    """Get dropdown options for input form"""
    return {
        "Status_Account": {
            "A11": "< 0 DM (Overdrawn)",
            "A12": "0 ≤ x < 200 DM",
            "A13": "≥ 200 DM",
            "A14": "No checking account"
        },
        "Savings": {
            "A61": "< 100 DM",
            "A62": "100 - 500 DM",
            "A63": "500 - 1000 DM",
            "A64": "≥ 1000 DM",
            "A65": "Unknown / No savings"
        },
        "Employment": {
            "A71": "Unemployed",
            "A72": "< 1 year",
            "A73": "1 - 4 years",
            "A74": "4 - 7 years",
            "A75": "≥ 7 years"
        },
        "Housing": {
            "A151": "Rent",
            "A152": "Own",
            "A153": "For free"
        },
        "Job": {
            "A171": "Unskilled (non-resident)",
            "A172": "Unskilled (resident)",
            "A173": "Skilled employee",
            "A174": "Management / Self-employed"
        },
        "Purpose": {
            "A40":  "New Car",
            "A41":  "Used Car",
            "A42":  "Furniture / Equipment",
            "A43":  "Radio / Television",
            "A44":  "Domestic Appliances",
            "A45":  "Repairs",
            "A46":  "Education",
            "A48":  "Retraining",
            "A49":  "Business",
            "A410": "Other"
        },
        "Credit_History": {
            "A30": "No credits / all paid back",
            "A31": "All credits paid back",
            "A32": "Existing credits paid",
            "A33": "Delay in paying",
            "A34": "Critical account"
        },
        "Personal_Status": {
            "A91": "Male: divorced/separated",
            "A92": "Female: divorced/married",
            "A93": "Male: single",
            "A94": "Male: married/widowed"
        },
        "Other_Debtors": {
            "A101": "None",
            "A102": "Co-applicant",
            "A103": "Guarantor"
        },
        "Property": {
            "A121": "Real estate",
            "A122": "Life insurance",
            "A123": "Car or other",
            "A124": "Unknown / No property"
        },
        "Other_Plans": {
            "A141": "Bank",
            "A142": "Stores",
            "A143": "None"
        },
        "Telephone": {
            "A191": "None",
            "A192": "Yes (registered)"
        },
        "Foreign_Worker": {
            "A201": "Yes",
            "A202": "No"
        }
    }

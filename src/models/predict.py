"""
Prediction Pipeline Module
Handles real-time credit risk predictions
"""

import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Risk thresholds
THRESHOLDS = {
    "low_risk":    0.70,
    "medium_risk": 0.50,
    "high_risk":   0.00
}


class CreditRiskPredictor:
    """
    Complete prediction pipeline for credit risk assessment
    """

    def __init__(self, models_dir: str = "models"):
        self.models_dir   = Path(models_dir)
        self.model        = None
        self.scaler       = None
        self.feature_names = None
        self._load_artifacts()

    def _load_artifacts(self) -> None:
        """Load model, scaler, and feature names"""
        try:
            with open(self.models_dir / "final_model.pkl", "rb") as f:
                self.model = pickle.load(f)

            with open(self.models_dir / "scaler_final.pkl", "rb") as f:
                self.scaler = pickle.load(f)

            with open(self.models_dir / "feature_names_final.pkl", "rb") as f:
                self.feature_names = pickle.load(f)

            logger.info("✅ All artifacts loaded successfully")

        except FileNotFoundError as e:
            logger.error(f"Model file not found: {e}")
            raise

    def _engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply feature engineering"""
        # Age groups
        df["age_young"]  = (df["Age"] < 25).astype(int)
        df["age_middle"] = ((df["Age"] >= 25) & (df["Age"] < 60)).astype(int)
        df["age_senior"] = (df["Age"] >= 60).astype(int)

        # Credit bins
        df["credit_low"]    = (df["Credit_Amount"] < 2500).astype(int)
        df["credit_medium"] = ((df["Credit_Amount"] >= 2500) &
                               (df["Credit_Amount"] < 5000)).astype(int)
        df["credit_high"]   = (df["Credit_Amount"] >= 5000).astype(int)

        # Duration bins
        df["duration_short"]  = (df["Duration"] <= 12).astype(int)
        df["duration_medium"] = ((df["Duration"] > 12) &
                                  (df["Duration"] <= 24)).astype(int)
        df["duration_long"]   = (df["Duration"] > 24).astype(int)

        # Financial ratios
        df["credit_duration_ratio"]  = df["Credit_Amount"] / (df["Duration"] + 1)
        df["credit_age_ratio"]       = df["Credit_Amount"] / (df["Age"] + 1)
        df["age_credit_interaction"] = df["Age"] * df["Credit_Amount"] / 1000

        # One-hot encoding
        categorical_cols = [
            "Status_Account", "Credit_History", "Purpose", "Savings",
            "Employment", "Personal_Status", "Other_Debtors", "Property",
            "Other_Plans", "Housing", "Job", "Telephone", "Foreign_Worker"
        ]
        cols_present = [c for c in categorical_cols if c in df.columns]
        df = pd.get_dummies(df, columns=cols_present,
                            drop_first=False, dtype=int)

        # Ensure all expected features exist
        for feature in self.feature_names:
            if feature not in df.columns:
                df[feature] = 0

        return df[self.feature_names]

    def get_risk_category(self, score: float) -> str:
        """Convert score to risk category"""
        if score >= THRESHOLDS["low_risk"]:
            return "Low Risk"
        elif score >= THRESHOLDS["medium_risk"]:
            return "Medium Risk"
        else:
            return "High Risk"

    def get_recommendation(self, score: float) -> dict:
        """Get lending recommendation"""
        category = self.get_risk_category(score)

        recommendations = {
            "Low Risk": {
                "decision":    "APPROVED",
                "action":      "Proceed with standard loan terms",
                "conditions":  []
            },
            "Medium Risk": {
                "decision":    "REVIEW REQUIRED",
                "action":      "Requires manual review by senior officer",
                "conditions":  [
                    "Request additional income verification",
                    "Consider reducing loan amount by 20%",
                    "Require guarantor"
                ]
            },
            "High Risk": {
                "decision":    "REJECTED",
                "action":      "Decline application",
                "conditions":  [
                    "Collateral required (150% of loan value)",
                    "Personal guarantee mandatory",
                    "Maximum 12-month term only"
                ]
            }
        }
        rec = recommendations[category].copy()
        rec["category"] = category
        rec["score"]    = score
        return rec

    def predict(self, input_data: dict) -> dict:
        """
        Make credit risk prediction

        Args:
            input_data: Dictionary with customer information

        Returns:
            Dictionary with prediction results
        """
        # Prepare features
        df = pd.DataFrame([input_data])
        df = self._engineer_features(df)

        # Scale
        X_scaled = self.scaler.transform(df)

        # Predict
        prediction   = self.model.predict(X_scaled)[0]
        probabilities = self.model.predict_proba(X_scaled)[0]
        risk_score   = float(probabilities[1])

        # Build result
        result = {
            "prediction":        int(prediction),
            "risk_score":        round(risk_score * 100, 2),
            "probability_good":  round(float(probabilities[1]), 4),
            "probability_bad":   round(float(probabilities[0]), 4),
            "risk_category":     self.get_risk_category(risk_score),
            "recommendation":    self.get_recommendation(risk_score),
            "model_version":     "v3.0",
            "timestamp":         datetime.now().isoformat()
        }

        logger.info(f"Prediction: {result['risk_category']} ({result['risk_score']}%)")
        return result

    def predict_batch(self, df: pd.DataFrame) -> pd.DataFrame:
        """Make predictions for multiple applications"""
        results = []
        for _, row in df.iterrows():
            result = self.predict(row.to_dict())
            results.append({
                "risk_score":    result["risk_score"],
                "risk_category": result["risk_category"],
                "decision":      result["recommendation"]["decision"]
            })
        return pd.DataFrame(results)

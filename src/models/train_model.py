"""
Model Training Module
Handles training and saving ML models
"""

import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)


class ModelTrainer:
    """Handles model training and persistence"""

    def __init__(self, models_dir: str = "models"):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(exist_ok=True)
        self.model   = None
        self.scaler  = None

    def get_model(self, model_type: str = "random_forest") -> object:
        """
        Get model instance by type

        Args:
            model_type: 'random_forest' or 'logistic_regression'
        """
        models = {
            "random_forest": RandomForestClassifier(
                n_estimators=100,
                max_depth=15,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42,
                class_weight="balanced",
                n_jobs=-1
            ),
            "logistic_regression": LogisticRegression(
                max_iter=1000,
                random_state=42,
                class_weight="balanced"
            )
        }

        if model_type not in models:
            raise ValueError(f"Unknown model: {model_type}. Choose from {list(models.keys())}")

        return models[model_type]

    def scale_features(self,
                       X_train: np.ndarray,
                       X_test: np.ndarray):
        """Scale features using StandardScaler"""
        self.scaler  = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled  = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled

    def train(self,
              X_train: np.ndarray,
              y_train: pd.Series,
              model_type: str = "random_forest") -> object:
        """
        Train model

        Args:
            X_train: Training features
            y_train: Training target
            model_type: Type of model to train

        Returns:
            Trained model
        """
        self.model = self.get_model(model_type)

        logger.info(f"Training {model_type}...")
        start = datetime.now()

        self.model.fit(X_train, y_train)

        duration = (datetime.now() - start).seconds
        logger.info(f"Training complete in {duration}s")

        return self.model

    def cross_validate(self,
                       X: np.ndarray,
                       y: pd.Series,
                       cv: int = 5) -> dict:
        """Run cross-validation"""
        if self.model is None:
            raise ValueError("Train model first")

        scores = cross_val_score(self.model, X, y, cv=cv)

        results = {
            "cv_scores": scores,
            "mean":      scores.mean(),
            "std":       scores.std()
        }

        logger.info(f"CV Score: {results['mean']:.4f} (+/- {results['std']:.4f})")
        return results

    def save(self, name: str = "final_model") -> None:
        """Save model, scaler, and feature names"""
        if self.model is None:
            raise ValueError("No model to save. Train first.")

        # Save model
        model_path = self.models_dir / f"{name}.pkl"
        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)
        logger.info(f"Model saved: {model_path}")

        # Save scaler
        if self.scaler is not None:
            scaler_path = self.models_dir / "scaler_final.pkl"
            with open(scaler_path, "wb") as f:
                pickle.dump(self.scaler, f)
            logger.info(f"Scaler saved: {scaler_path}")

    def load(self, name: str = "final_model") -> object:
        """Load saved model"""
        model_path = self.models_dir / f"{name}.pkl"
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        logger.info(f"Model loaded: {model_path}")
        return self.model

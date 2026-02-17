"""
Tests for Model Training, Evaluation & Prediction
Run: pytest tests/test_model.py -v
"""

import pytest
import pickle
import numpy as np
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.models.train_model    import ModelTrainer
from src.models.evaluate_model import ModelEvaluator


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
def sample_data():
    """Create sample scaled dataset"""
    np.random.seed(42)
    n = 200

    X_train = np.random.randn(n, 73)
    X_test  = np.random.randn(50, 73)
    y_train = pd.Series(np.random.randint(0, 2, n))
    y_test  = pd.Series(np.random.randint(0, 2, 50))

    return X_train, X_test, y_train, y_test


@pytest.fixture
def trained_model(sample_data):
    """Create and train a model"""
    X_train, X_test, y_train, y_test = sample_data
    trainer = ModelTrainer()
    model = trainer.train(X_train, y_train, "random_forest")
    return model, X_train, X_test, y_train, y_test


@pytest.fixture
def production_model():
    """Load production model if available"""
    try:
        with open("models/final_model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("models/scaler_final.pkl", "rb") as f:
            scaler = pickle.load(f)
        with open("models/feature_names_final.pkl", "rb") as f:
            features = pickle.load(f)
        return model, scaler, features
    except FileNotFoundError:
        pytest.skip("Production model not found")


# ============================================================================
# Tests: Model Training
# ============================================================================

class TestModelTrainer:

    def test_creates_random_forest(self):
        """Should create Random Forest model"""
        from sklearn.ensemble import RandomForestClassifier
        trainer = ModelTrainer()
        model = trainer.get_model("random_forest")
        assert isinstance(model, RandomForestClassifier)

    def test_creates_logistic_regression(self):
        """Should create Logistic Regression model"""
        from sklearn.linear_model import LogisticRegression
        trainer = ModelTrainer()
        model = trainer.get_model("logistic_regression")
        assert isinstance(model, LogisticRegression)

    def test_invalid_model_raises_error(self):
        """Invalid model type should raise ValueError"""
        trainer = ModelTrainer()
        with pytest.raises(ValueError):
            trainer.get_model("invalid_model")

    def test_train_returns_model(self, sample_data):
        """Training should return a model"""
        X_train, _, y_train, _ = sample_data
        trainer = ModelTrainer()
        model = trainer.train(X_train, y_train)
        assert model is not None

    def test_trained_model_has_predict(self, sample_data):
        """Trained model should have predict method"""
        X_train, _, y_train, _ = sample_data
        trainer = ModelTrainer()
        model = trainer.train(X_train, y_train)
        assert hasattr(model, "predict")

    def test_trained_model_has_predict_proba(self, sample_data):
        """Trained model should have predict_proba method"""
        X_train, _, y_train, _ = sample_data
        trainer = ModelTrainer()
        model = trainer.train(X_train, y_train)
        assert hasattr(model, "predict_proba")

    def test_scale_features(self, sample_data):
        """Feature scaling should work correctly"""
        X_train, X_test, _, _ = sample_data
        trainer = ModelTrainer()
        X_train_s, X_test_s = trainer.scale_features(X_train, X_test)

        # Check scaled data shape
        assert X_train_s.shape == X_train.shape
        assert X_test_s.shape  == X_test.shape

        # Check scaler is set
        assert trainer.scaler is not None


# ============================================================================
# Tests: Model Evaluation
# ============================================================================

class TestModelEvaluator:

    def test_evaluate_returns_dict(self, trained_model):
        """Evaluate should return dictionary"""
        model, X_train, X_test, y_train, y_test = trained_model
        evaluator = ModelEvaluator()
        results = evaluator.evaluate(model, X_train, X_test, y_train, y_test)
        assert isinstance(results, dict)

    def test_evaluate_has_required_keys(self, trained_model):
        """Results should have all required keys"""
        model, X_train, X_test, y_train, y_test = trained_model
        evaluator = ModelEvaluator()
        results = evaluator.evaluate(model, X_train, X_test, y_train, y_test)

        required_keys = [
            "train_accuracy", "test_accuracy", "precision",
            "recall", "f1_score", "roc_auc",
            "true_negatives", "false_positives",
            "false_negatives", "true_positives"
        ]
        for key in required_keys:
            assert key in results, f"Missing key: {key}"

    def test_accuracy_between_0_and_1(self, trained_model):
        """Accuracy should be between 0 and 1"""
        model, X_train, X_test, y_train, y_test = trained_model
        evaluator = ModelEvaluator()
        results = evaluator.evaluate(model, X_train, X_test, y_train, y_test)
        assert 0 <= results["train_accuracy"] <= 1
        assert 0 <= results["test_accuracy"]  <= 1

    def test_confusion_matrix_values_positive(self, trained_model):
        """Confusion matrix values should be non-negative"""
        model, X_train, X_test, y_train, y_test = trained_model
        evaluator = ModelEvaluator()
        results = evaluator.evaluate(model, X_train, X_test, y_train, y_test)
        assert results["true_negatives"]  >= 0
        assert results["false_positives"] >= 0
        assert results["false_negatives"] >= 0
        assert results["true_positives"]  >= 0

    def test_cm_sum_equals_test_size(self, trained_model):
        """Confusion matrix values should sum to test set size"""
        model, X_train, X_test, y_train, y_test = trained_model
        evaluator = ModelEvaluator()
        results = evaluator.evaluate(model, X_train, X_test, y_train, y_test)
        cm_sum = (results["true_negatives"]  +
                  results["false_positives"] +
                  results["false_negatives"] +
                  results["true_positives"])
        assert cm_sum == len(y_test)


# ============================================================================
# Tests: Production Model
# ============================================================================

class TestProductionModel:

    def test_model_loads_successfully(self, production_model):
        """Production model should load without errors"""
        model, scaler, features = production_model
        assert model   is not None
        assert scaler  is not None
        assert features is not None

    def test_model_has_73_features(self, production_model):
        """Production model should have 73 features"""
        model, scaler, features = production_model
        assert len(features) == 73,             f"Expected 73 features, got {len(features)}"

    def test_model_accuracy_above_threshold(self, production_model):
        """Production model accuracy should be above 70%"""
        model, scaler, features = production_model

        # Load test data
        try:
            df = pd.read_csv("data/processed/german_credit_fe_v3.csv")
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import accuracy_score

            X = df[features]
            y = df["Risk"]
            _, X_test, _, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )

            X_test_scaled = scaler.transform(X_test)
            y_pred = model.predict(X_test_scaled)
            accuracy = accuracy_score(y_test, y_pred)

            assert accuracy >= 0.70,                 f"Model accuracy {accuracy:.2%} below threshold 70%"

        except FileNotFoundError:
            pytest.skip("Test data not available")

    def test_model_prediction_format(self, production_model):
        """Model predictions should be binary (0/1)"""
        model, scaler, features = production_model

        X_sample = np.zeros((5, len(features)))
        X_scaled  = scaler.transform(X_sample)
        predictions = model.predict(X_scaled)

        assert set(predictions).issubset({0, 1}),             f"Unexpected prediction values: {set(predictions)}"

    def test_model_probabilities_sum_to_1(self, production_model):
        """Prediction probabilities should sum to 1"""
        model, scaler, features = production_model

        X_sample  = np.random.randn(10, len(features))
        X_scaled  = scaler.transform(X_sample)
        probas    = model.predict_proba(X_scaled)
        row_sums  = probas.sum(axis=1)

        np.testing.assert_array_almost_equal(
            row_sums,
            np.ones(10),
            decimal=5,
            err_msg="Probabilities don't sum to 1"
        )

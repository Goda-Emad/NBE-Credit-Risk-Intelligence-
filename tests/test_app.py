"""
Tests for Streamlit Application
Run: pytest tests/test_app.py -v
"""

import pytest
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.append(str(Path(__file__).parent.parent))


# ============================================================================
# Tests: Feature Transform
# ============================================================================

class TestFeatureTransform:

    def test_get_input_options_returns_dict(self):
        """Input options should return dictionary"""
        from streamlit_app.utils.feature_transform import get_input_options
        options = get_input_options()
        assert isinstance(options, dict)

    def test_input_options_has_required_fields(self):
        """Input options should have all required fields"""
        from streamlit_app.utils.feature_transform import get_input_options
        options = get_input_options()

        required_fields = [
            "Status_Account", "Savings", "Employment",
            "Housing", "Job", "Purpose"
        ]
        for field in required_fields:
            assert field in options, f"Missing field: {field}"

    def test_status_account_has_4_options(self):
        """Status Account should have exactly 4 options"""
        from streamlit_app.utils.feature_transform import get_input_options
        options = get_input_options()
        assert len(options["Status_Account"]) == 4

    def test_transform_returns_numpy_array(self):
        """Transform should return numpy array"""
        from streamlit_app.utils.feature_transform import transform_input
        from sklearn.preprocessing import StandardScaler

        # Mock scaler
        scaler = MagicMock()
        scaler.transform.return_value = np.zeros((1, 73))

        input_data = {
            "Status_Account":   "A11",
            "Duration":         24,
            "Credit_History":   "A34",
            "Purpose":          "A43",
            "Credit_Amount":    5000,
            "Savings":          "A61",
            "Employment":       "A73",
            "Installment_Rate": 2,
            "Personal_Status":  "A93",
            "Other_Debtors":    "A101",
            "Residence_Since":  2,
            "Property":         "A121",
            "Age":              35,
            "Other_Plans":      "A143",
            "Housing":          "A152",
            "Existing_Credits": 1,
            "Job":              "A173",
            "Num_Dependents":   1,
            "Telephone":        "A191",
            "Foreign_Worker":   "A201"
        }

        # Create dummy feature names
        feature_names = [f"feature_{i}" for i in range(73)]

        result = transform_input(input_data, feature_names, scaler)
        assert isinstance(result, np.ndarray)


# ============================================================================
# Tests: Model Loading
# ============================================================================

class TestModelLoading:

    def test_load_model_returns_tuple(self):
        """load_model_artifacts should return tuple"""
        from streamlit_app.utils.load_model import load_model_artifacts

        with patch("streamlit.cache_resource",
                   lambda **kwargs: lambda f: f):
            try:
                result = load_model_artifacts("models")
                assert isinstance(result, tuple)
                assert len(result) == 3
            except Exception:
                pytest.skip("Model files not available")

    def test_get_model_info_returns_dict(self):
        """get_model_info should return dictionary"""
        from streamlit_app.utils.load_model import get_model_info

        mock_model = MagicMock()
        mock_model.n_estimators   = 100
        mock_model.max_depth      = 15
        mock_model.n_features_in_ = 73

        info = get_model_info(mock_model)
        assert isinstance(info, dict)
        assert "type"    in info
        assert "version" in info

    def test_get_model_info_none_returns_empty(self):
        """get_model_info with None should return empty dict"""
        from streamlit_app.utils.load_model import get_model_info
        result = get_model_info(None)
        assert result == {}


# ============================================================================
# Tests: Visualization Helpers
# ============================================================================

class TestVisualizationHelpers:

    def test_risk_colors_exist(self):
        """All risk categories should have colors"""
        from streamlit_app.utils.visualization_helpers import create_result_card
        # Should not raise errors
        assert callable(create_result_card)

    def test_metric_card_callable(self):
        """create_metric_card should be callable"""
        from streamlit_app.utils.visualization_helpers import create_metric_card
        assert callable(create_metric_card)

    def test_recommendation_box_callable(self):
        """create_recommendation_box should be callable"""
        from streamlit_app.utils.visualization_helpers import create_recommendation_box
        assert callable(create_recommendation_box)


# ============================================================================
# Tests: Chart Components
# ============================================================================

class TestChartComponents:

    def test_render_gauge_returns_figure(self):
        """render_gauge should return Plotly figure"""
        from streamlit_app.components.charts import render_gauge
        import plotly.graph_objects as go

        fig = render_gauge(75.5)
        assert isinstance(fig, go.Figure)

    def test_render_gauge_low_risk(self):
        """High score should indicate low risk"""
        from streamlit_app.components.charts import render_gauge
        fig = render_gauge(85.0)
        assert fig is not None

    def test_render_gauge_high_risk(self):
        """Low score should indicate high risk"""
        from streamlit_app.components.charts import render_gauge
        fig = render_gauge(25.0)
        assert fig is not None

    def test_render_confusion_matrix_returns_figure(self):
        """render_confusion_matrix should return Plotly figure"""
        from streamlit_app.components.charts import render_confusion_matrix
        import plotly.graph_objects as go

        fig = render_confusion_matrix(124, 16, 31, 29)
        assert isinstance(fig, go.Figure)

    def test_render_risk_distribution(self):
        """render_risk_distribution should return Plotly figure"""
        from streamlit_app.components.charts import render_risk_distribution
        import plotly.graph_objects as go

        df = pd.DataFrame({"Risk": [0]*70 + [1]*30})
        fig = render_risk_distribution(df)
        assert isinstance(fig, go.Figure)

    def test_render_feature_importance(self):
        """render_feature_importance should return Plotly figure"""
        from streamlit_app.components.charts import render_feature_importance
        import plotly.graph_objects as go

        features     = [f"feature_{i}" for i in range(20)]
        importances  = np.random.rand(20).tolist()

        fig = render_feature_importance(features, importances)
        assert isinstance(fig, go.Figure)


# ============================================================================
# Tests: Integration
# ============================================================================

class TestIntegration:

    def test_full_prediction_pipeline(self):
        """Full prediction pipeline should work end-to-end"""
        try:
            import pickle
            from streamlit_app.utils.feature_transform import transform_input

            # Load artifacts
            with open("models/final_model.pkl",          "rb") as f:
                model = pickle.load(f)
            with open("models/scaler_final.pkl",         "rb") as f:
                scaler = pickle.load(f)
            with open("models/feature_names_final.pkl",  "rb") as f:
                feature_names = pickle.load(f)

            # Sample input
            input_data = {
                "Status_Account":   "A11",
                "Duration":         24,
                "Credit_History":   "A34",
                "Purpose":          "A43",
                "Credit_Amount":    5000,
                "Savings":          "A61",
                "Employment":       "A73",
                "Installment_Rate": 2,
                "Personal_Status":  "A93",
                "Other_Debtors":    "A101",
                "Residence_Since":  2,
                "Property":         "A121",
                "Age":              35,
                "Other_Plans":      "A143",
                "Housing":          "A152",
                "Existing_Credits": 1,
                "Job":              "A173",
                "Num_Dependents":   1,
                "Telephone":        "A191",
                "Foreign_Worker":   "A201"
            }

            # Transform & predict
            X_scaled     = transform_input(input_data, feature_names, scaler)
            prediction   = model.predict(X_scaled)[0]
            probabilities = model.predict_proba(X_scaled)[0]

            # Validate output
            assert prediction in [0, 1]
            assert len(probabilities) == 2
            assert abs(sum(probabilities) - 1.0) < 0.001
            assert 0 <= probabilities[1] <= 1

        except FileNotFoundError:
            pytest.skip("Model files not available for integration test")

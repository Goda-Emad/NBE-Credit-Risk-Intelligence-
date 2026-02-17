"""Model Loading Utilities"""
import pickle
import streamlit as st
from pathlib import Path


@st.cache_resource(show_spinner="Loading AI Model...")
def load_model_artifacts(models_dir: str = None):
    """
    Load and cache model artifacts

    Args:
        models_dir: Path to models directory

    Returns:
        Tuple of (model, scaler, feature_names)
    """
    if models_dir is None:
        # Auto-detect models directory
        possible_paths = [
            Path(__file__).parent.parent.parent / "models",
            Path("models"),
            Path("../models"),
        ]
        models_dir = next(
            (p for p in possible_paths if p.exists()),
            Path("models")
        )
    else:
        models_dir = Path(models_dir)

    try:
        # Load model
        with open(models_dir / "final_model.pkl", "rb") as f:
            model = pickle.load(f)

        # Load scaler
        with open(models_dir / "scaler_final.pkl", "rb") as f:
            scaler = pickle.load(f)

        # Load feature names
        with open(models_dir / "feature_names_final.pkl", "rb") as f:
            feature_names = pickle.load(f)

        return model, scaler, feature_names

    except FileNotFoundError as e:
        st.error(f"""
        ⚠️ **Model files not found!**

        Please ensure these files exist:
        - `models/final_model.pkl`
        - `models/scaler_final.pkl`
        - `models/feature_names_final.pkl`

        Error: {str(e)}
        """)
        return None, None, None

    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None, None, None


def get_model_info(model) -> dict:
    """Get model information dictionary"""
    if model is None:
        return {}

    info = {
        "type":    type(model).__name__,
        "version": "3.0"
    }

    if hasattr(model, "n_estimators"):
        info["n_estimators"] = model.n_estimators
    if hasattr(model, "max_depth"):
        info["max_depth"] = model.max_depth
    if hasattr(model, "n_features_in_"):
        info["n_features"] = model.n_features_in_

    return info

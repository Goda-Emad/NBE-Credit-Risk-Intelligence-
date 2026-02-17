"""
Helper Functions
Common utility functions used across the project
"""

import time
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Timer:
    """Context manager for timing code blocks"""

    def __init__(self, name: str = ""):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        logger.info(f"{self.name}: {self.elapsed:.2f}s")

    def __str__(self):
        return f"{self.elapsed:.2f}s"


def format_currency(amount: float,
                    currency: str = "EGP") -> str:
    """Format number as currency string"""
    return f"{amount:,.0f} {currency}"


def get_risk_color(risk_category: str) -> str:
    """Get color code for risk category"""
    colors = {
        "Low Risk":    "#28a745",
        "Medium Risk": "#ffc107",
        "High Risk":   "#dc3545"
    }
    return colors.get(risk_category, "#6c757d")


def get_risk_emoji(risk_category: str) -> str:
    """Get emoji for risk category"""
    emojis = {
        "Low Risk":    "✅",
        "Medium Risk": "⚠️",
        "High Risk":   "❌"
    }
    return emojis.get(risk_category, "❓")


def save_pickle(obj, filepath: str) -> None:
    """Save object to pickle file"""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "wb") as f:
        pickle.dump(obj, f)
    logger.info(f"Saved: {filepath}")


def load_pickle(filepath: str):
    """Load object from pickle file"""
    with open(filepath, "rb") as f:
        obj = pickle.load(f)
    logger.info(f"Loaded: {filepath}")
    return obj


def get_model_size(filepath: str) -> str:
    """Get human-readable model file size"""
    size = Path(filepath).stat().st_size
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{size/1024:.1f} KB"
    else:
        return f"{size/1024**2:.1f} MB"


def validate_input(input_data: dict) -> tuple:
    """
    Validate input data for prediction

    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []

    required = ["Age", "Duration", "Credit_Amount",
                "Status_Account", "Savings", "Employment",
                "Housing", "Job", "Purpose"]

    for field in required:
        if field not in input_data or input_data[field] is None:
            errors.append(f"Missing required field: {field}")

    if "Age" in input_data and input_data["Age"] is not None:
        if not (18 <= input_data["Age"] <= 100):
            errors.append("Age must be between 18 and 100")

    if "Credit_Amount" in input_data and input_data["Credit_Amount"] is not None:
        if input_data["Credit_Amount"] <= 0:
            errors.append("Credit Amount must be positive")

    if "Duration" in input_data and input_data["Duration"] is not None:
        if not (1 <= input_data["Duration"] <= 120):
            errors.append("Duration must be between 1 and 120 months")

    return len(errors) == 0, errors


def generate_application_id() -> str:
    """Generate unique application ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_part = np.random.randint(1000, 9999)
    return f"NBE-{timestamp}-{random_part}"

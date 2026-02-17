"""Visualization Helper Functions"""
import streamlit as st


def create_result_card(
    risk_score: float,
    risk_category: str,
    decision: str
) -> None:
    """
    Render styled result card

    Args:
        risk_score:    Score percentage (0-100)
        risk_category: Low/Medium/High Risk
        decision:      APPROVED/REVIEW/REJECTED
    """
    colors = {
        "Low Risk":    ("#d4edda", "#28a745", "#155724"),
        "Medium Risk": ("#fff3cd", "#ffc107", "#856404"),
        "High Risk":   ("#f8d7da", "#dc3545", "#721c24")
    }

    icons = {
        "Low Risk":    "✅",
        "Medium Risk": "⚠️",
        "High Risk":   "❌"
    }

    bg, border, text = colors.get(
        risk_category,
        ("#f8f9fa", "#6c757d", "#333")
    )
    icon = icons.get(risk_category, "❓")

    st.markdown(f"""
    <div style='
        background: {bg};
        border: 3px solid {border};
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin: 15px 0;
    '>
        <h2 style='color:{text}; margin:0; font-size:28px;'>
            {icon} {risk_category.upper()}
        </h2>
        <h3 style='color:{text}; margin:8px 0;'>
            Decision: {decision}
        </h3>
        <p style='color:{text}; font-size:18px; margin:0;'>
            Risk Score: <strong>{risk_score:.1f}%</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)


def create_metric_card(
    title: str,
    value: str,
    delta: str = "",
    color: str = "#006341"
) -> None:
    """Render a styled metric card"""
    st.markdown(f"""
    <div style='
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {color};
        margin: 5px 0;
    '>
        <p style='color:#666; margin:0; font-size:13px;'>{title}</p>
        <h2 style='color:{color}; margin:5px 0;'>{value}</h2>
        {"<p style='color:#28a745; margin:0; font-size:12px;'>" + delta + "</p>" if delta else ""}
    </div>
    """, unsafe_allow_html=True)


def create_recommendation_box(conditions: list) -> None:
    """Render conditions/recommendations box"""
    if not conditions:
        return

    items = "".join([f"<li>{c}</li>" for c in conditions])

    st.markdown(f"""
    <div style='
        background: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    '>
        <strong>📋 Conditions Required:</strong>
        <ul style='margin:8px 0 0;'>{items}</ul>
    </div>
    """, unsafe_allow_html=True)


def create_nbe_css() -> None:
    """Apply global NBE CSS styling"""
    st.markdown("""
    <style>
    /* NBE Brand Colors */
    h1, h2, h3 { color: #006341; }

    /* Buttons */
    .stButton>button {
        background-color: #006341;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #004d32;
        box-shadow: 0 4px 8px rgba(0,99,65,0.3);
        transform: translateY(-1px);
    }

    /* Sidebar */
    .css-1d391kg { background-color: #f8f9fa; }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #006341;
        font-weight: bold;
    }

    /* Dataframe */
    .dataframe { border-radius: 8px; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f8f9fa;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #006341;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

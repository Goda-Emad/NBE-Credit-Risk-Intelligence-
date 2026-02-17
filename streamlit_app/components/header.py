"""Header Component"""
import streamlit as st
from pathlib import Path


def render_header(
    title: str,
    subtitle: str = "",
    icon: str = "🏦"
):
    """
    Render page header with NBE branding

    Args:
        title:    Main page title
        subtitle: Optional subtitle
        icon:     Page icon emoji
    """
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #006341, #004d32);
        padding: 25px 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='
            color: white;
            margin: 0;
            font-size: 32px;
        '>{icon} {title}</h1>
        {"<p style='color:#D4AF37; margin:8px 0 0; font-size:16px;'>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


def render_page_header(page_name: str) -> None:
    """Render standard page headers"""
    headers = {
        "risk_assessment": (
            "Credit Risk Assessment",
            "Evaluate credit applications using AI",
            "🎯"
        ),
        "analytics": (
            "Portfolio Analytics",
            "Comprehensive credit portfolio insights",
            "📊"
        ),
        "performance": (
            "Model Performance",
            "Detailed model evaluation metrics",
            "📈"
        ),
        "about": (
            "About the Platform",
            "Documentation and project information",
            "ℹ️"
        ),
    }

    if page_name in headers:
        title, subtitle, icon = headers[page_name]
        render_header(title, subtitle, icon)

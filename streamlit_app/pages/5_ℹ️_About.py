import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# ------------------------
# Load Background Image
# ------------------------
def get_base64_image(image_path):
    if not Path(image_path).exists():
        return None
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

bg_path = "assets/nbe_branding/nbe_bg.jpg"
bg_base64 = get_base64_image(bg_path)

# ------------------------
# CSS Styling
# ------------------------
if bg_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{bg_base64}") no-repeat center center fixed;
            background-size: cover;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.75));
            z-index: -1;
        }}
        .glass-card {{
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(14px);
            border-radius: 18px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.25);
            color: white;
        }}
        h1, h2, h3 {{ color: #ffffff !important; }}
        p, li {{ color: #f1f1f1 !important; font-size: 16px; }}
        a button {{
            width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 8px;
            border: none; font-weight: bold; cursor: pointer;
        }}
        a button:hover {{ opacity: 0.85; transform: scale(1.02); transition: 0.2s; }}
        .github-btn {{ background-color: #24292e; color: white; }}
        .linkedin-btn {{ background-color: #0077b5; color: white; }}
        .logo {{
            display: block; margin-left: auto; margin-right: auto;
            width: 120px; margin-bottom: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------------
# Page Header & Glass Card
# ------------------------
st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Logo
logo_path = "assets/nbe_branding/nbe_logo_white.png"
st.markdown(f'<img src="{logo_path}" class="logo">', unsafe_allow_html=True)

# Project Overview
st.markdown(
    """
    ### 🎯 Project Overview
    The **NBE Credit Risk Intelligence Platform** is an AI-driven system designed to modernize 
    credit evaluation processes for the banking sector.

    ### 🔧 Technical Specifications
    - **Model:** Random Forest Classifier  
    - **Model Version:** v3.0  
    - **Accuracy:** 76.5%  
    - **Engineered Features:** 73  
    - **Dataset:** German Credit Risk (1,000 records)

    ### 📊 Capabilities
    1️⃣ Automated Risk Assessment: Real-time scoring, confidence-based recommendations  
    2️⃣ Portfolio Intelligence: Trend analysis, risk distribution  
    3️⃣ Model Governance: False negative monitoring, feature importance tracking

    ### 🏗️ Decision Architecture
    ```
    Data Input → Feature Engineering → Random Forest → Risk Score → Decision
    ```
    """,
    unsafe_allow_html=True
)

# Professional Links
st.markdown("### 🔗 Connect with Me")

st.markdown(
    """
    <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
        <button class="github-btn">📁 GitHub Repository</button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
        <button class="linkedin-btn">🔵 LinkedIn Profile</button>
    </a>
    """,
    unsafe_allow_html=True
)

# Footer Info
st.markdown(
    """
    ### 👥 Lead Developer
    **Eng. Goda Emad**  
    *Credit Risk Analytics Specialist*

    **Version:** 3.0  
    **Last Updated:** February 2026  
    **Location:** Cairo, Egypt 🇪🇬
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

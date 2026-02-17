"""About Page - Full Professional Version with Icons, Logo & Background"""

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# Paths
bg_image_path = Path("assets/nbe_branding/nbe_bg.jpg")
logo_path = Path("assets/nbe_branding/nbe_logo_white.png")
# Icons for Capabilities / Tech Stack
icons = {
    "Automated Risk Assessment": "⚡",
    "Portfolio Analytics": "📈",
    "Model Monitoring": "🛡️",
    "Python": "🐍",
    "Streamlit": "🌐",
    "Pandas": "🐼",
    "NumPy": "🔢",
    "Scikit-learn": "📚",
    "Random Forest": "🌲",
    "Git": "🔧",
    "GitHub": "🐱"
}

# CSS for background, glass, buttons, and text
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{bg_image_path.as_posix()}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
.glass-card {{
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    color: #ffffff;
}}
a button:hover {{
    opacity: 0.85;
    transform: scale(1.02);
    transition: 0.2s;
}}
h1, h2, h3, h4, h5, h6 {{
    color: #ffffff;
}}
.logo {{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 120px;
    margin-bottom: 15px;
}}
.icon-text {{
    font-size: 16px;
    margin-bottom: 8px;
}}
</style>
""", unsafe_allow_html=True)

# Glass wrapper
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Logo
st.markdown(f'<img src="{logo_path.as_posix()}" class="logo">', unsafe_allow_html=True)

# Title
st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

# Columns layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 🎯 Project Overview")
    st.markdown("""
    This AI-powered Credit Risk Intelligence Platform is designed for the **National Bank of Egypt (NBE)** 
    to automate and enhance credit application assessment processes using advanced Machine Learning techniques.
    """)

    st.markdown("## 🔧 Technical Details")
    st.markdown("""
    - **Model:** Random Forest Classifier  
    - **Accuracy:** 76.5%  
    - **Features:** 73 engineered features  
    - **Dataset:** German Credit Risk (1,000 applications)
    """)

    st.markdown("## 🏗️ Decision Pipeline")
    st.markdown("""
    **Visual Flow:**  
    Data Input ➡️ Feature Engineering (73 Features) ➡️ Random Forest Model (v3.0) ➡️ Risk Score ➡️ Final Decision
    """)

    st.markdown("## 📊 Capabilities")
    st.markdown(f"""
    <div class="icon-text">{icons['Automated Risk Assessment']} Automated Risk Assessment: Real-time credit scoring, probability-based recommendations, confidence intervals.</div>
    <div class="icon-text">{icons['Portfolio Analytics']} Portfolio Analytics: Application trends, risk distribution, performance metrics.</div>
    <div class="icon-text">{icons['Model Monitoring']} Model Monitoring: Accuracy tracking, false negative analysis, feature importance.</div>
    """, unsafe_allow_html=True)

    st.markdown("## 🛠️ Tech Stack")
    st.markdown(f"""
    <div class="icon-text">{icons['Python']} Python</div>
    <div class="icon-text">{icons['Streamlit']} Streamlit</div>
    <div class="icon-text">{icons['Pandas']} Pandas</div>
    <div class="icon-text">{icons['NumPy']} NumPy</div>
    <div class="icon-text">{icons['Scikit-learn']} Scikit-learn</div>
    <div class="icon-text">{icons['Random Forest']} Random Forest Classifier</div>
    <div class="icon-text">{icons['Git']} Git & {icons['GitHub']} GitHub Version Control</div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("## 🔗 Professional Links")

    st.markdown(f"""
    <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
        <button style="width:100%; padding:10px; background-color:#24292e; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold; margin-bottom:10px;">
            📁 View GitHub Repository
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
        <button style="width:100%; padding:10px; background-color:#0077b5; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold;">
            🔵 Connect on LinkedIn
        </button>
    </a>
    """, unsafe_allow_html=True)

    st.success("""
    **Lead Developer:** **Eng. Goda Emad**  
    *Credit Risk Analytics Specialist*
    """)

    st.info("""
    **Version:** 3.0  
    **Last Updated:** February 2026  
    **Location:** Cairo, Egypt 🇪🇬
    """)

    st.markdown("## 📚 Documentation")
    st.markdown("""
    - Model Card: `docs/model_card.md`  
    - Performance Report: `reports/model_performance_report.md`  
    - GitHub Repository: [View Here](https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-)
    """)

    st.markdown("## 📄 License")
    st.markdown("MIT License © 2026 National Bank of Egypt")

# Close Glass wrapper
st.markdown('</div>', unsafe_allow_html=True)

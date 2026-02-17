import streamlit as st
from pathlib import Path

# --- إعداد الصفحة ---
st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# --- CSS لتنسيق الصفحة ---
st.markdown("""
<style>
/* خلفية عامة Dark Green */
body, .stApp {
    background-color: #004d1a !important;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* صندوق الشعار الأبيض */
.logo-card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    width: fit-content;
    margin-left:auto;
    margin-right:auto;
    margin-bottom:20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* العنوان الرئيسي */
h1 {
    font-size: 36px;
    font-weight: bold;
    color: #b3ff99;
    margin-bottom: 25px;
    text-align: center;
}

/* العناوين الفرعية */
h2 { font-size:28px; font-weight:bold; margin-top:20px; margin-bottom:10px; color:#b3ff99; }
h3 { font-size:22px; font-weight:bold; margin-top:15px; color:#b3ff99; }

/* نصوص الفقرة */
p, li { font-size:18px; line-height:1.6; color:#f1f1f1; }

/* أزرار */
.button-link {
    width:100%; padding:12px; font-weight:bold; border:none; border-radius:8px; cursor:pointer; margin-bottom:10px;
}
.github-btn { background-color:#24292e; color:white; }
.linkedin-btn { background-color:#0077b5; color:white; }

/* Glass card محتوى */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- شعار البنك (مسار مصحح) ---
logo_path = Path(__file__).parents[2] / "assets" / "nbe_branding" / "NBE_logo.png"

if logo_path.is_file():
    st.markdown('<div class="logo-card">', unsafe_allow_html=True)
    st.image(str(logo_path), width=180)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.error(f"Logo file not found! Check the path:\n{logo_path}")

# --- العنوان الرئيسي ---
st.markdown("<h1>ℹ️ About NBE Credit Risk Intelligence</h1>", unsafe_allow_html=True)

# --- محتوى الصفحة ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Project Overview
st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-driven system that modernizes 
credit application assessment for the **National Bank of Egypt (NBE)**.  
It automates decision-making with **high accuracy** and provides **real-time risk insights**.
""", unsafe_allow_html=True)

# KPIs Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="kpi"><h3>Accuracy</h3><p>76.5%</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="kpi"><h3>Engineered Features</h3><p>73</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="kpi"><h3>Version</h3><p>3.0</p></div>', unsafe_allow_html=True)

# Technical Specs
st.markdown("""
### 🔧 Technical Specifications
- **Model:** Random Forest Classifier (v3.0)  
- **Dataset:** German Credit Risk (1,000 applications)
""", unsafe_allow_html=True)

# Capabilities
st.markdown("""
### 📊 Capabilities
1. **Automated Risk Assessment:** Real-time scoring & probability-based recommendations.  
2. **Portfolio Analytics:** Insights into risk distribution, application trends, and performance metrics.  
3. **Model Monitoring:** Feature importance tracking & false negatives analysis.
""", unsafe_allow_html=True)

# Architecture
st.markdown("""
### 🏗️ Decision Architecture
""", unsafe_allow_html=True)

# Team & Contact
st.markdown("""
### 👥 Team
**Credit Risk Analytics Team**  
**National Bank of Egypt**

### 📞 Contact
- **Email:** creditrisk@nbe.com.eg  
- **Last Updated:** Feb 2026  
- **Location:** Cairo, Egypt 🇪🇬
""", unsafe_allow_html=True)

# Professional Links
st.markdown("""
### 🔗 Professional Links
<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
    <button class="button-link github-btn">📁 View GitHub Repository</button>
</a>
<a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
    <button class="button-link linkedin-btn">🔵 Connect on LinkedIn</button>
</a>
""", unsafe_allow_html=True)

# Documentation & License
st.markdown("""
### 📚 Documentation
- Model Card: `docs/model_card.md`  
- Performance Report: `reports/model_performance_report.md`  

### 📄 License
MIT License © 2026 National Bank of Egypt
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

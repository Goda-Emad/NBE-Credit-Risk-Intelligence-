import streamlit as st

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# =============================
# NBE Logo (Base64)
# =============================
nbe_logo_base64 = """
iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAYAAABxo6ZPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAC
... (هنا ضع كامل Base64 لشعار البنك الأهلي PNG)
"""
# =============================
# CSS Styling
# =============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #004d1a, #006622);
    background-attachment: fixed;
}
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    color: white;
}
h1 { font-size: 36px !important; font-weight: bold; color: #ffffff !important; }
h2 { font-size: 28px !important; font-weight: bold; color: #ffffff !important; }
h3 { font-size: 22px !important; font-weight: bold; color: #ffffff !important; }
p, li { font-size: 16px; color: #f1f1f1 !important; }
a button { width: 100%; padding: 12px; margin-bottom: 10px; border-radius: 8px; border: none; font-weight: bold; cursor: pointer; }
a button:hover { opacity: 0.85; transform: scale(1.02); }
.github-btn { background-color: #24292e; color: white; }
.linkedin-btn { background-color: #0077b5; color: white; }
.logo { display: block; margin-left: auto; margin-right: auto; width: 150px; margin-bottom: 25px; }
.kpi-card { background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); border-radius: 15px; padding: 20px; text-align: center; color: white; transition: transform 0.2s; box-shadow: 0 6px 20px rgba(0,0,0,0.3);}
.kpi-card:hover { transform: scale(1.05); }
.kpi-number { font-size: 28px; font-weight: bold; }
.kpi-label { font-size: 16px; margin-top: 5px; color: #dcdcdc; }
.capability { display: flex; align-items: center; margin-bottom: 12px; }
.capability img { width: 30px; height: 30px; margin-right: 10px; }
</style>
""", unsafe_allow_html=True)

# =============================
# Glass Card Container
# =============================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Display Logo
st.markdown(f'<img src="data:image/png;base64,{nbe_logo_base64}" class="logo">', unsafe_allow_html=True)

# Title
st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

# Project Overview
st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-driven system designed to modernize 
credit evaluation processes for the banking sector.
""", unsafe_allow_html=True)

# Technical Specs
st.markdown("""
### 🔧 Technical Specifications
- **Model:** Random Forest Classifier  
- **Model Version:** v3.0  
- **Accuracy:** 76.5%  
- **Engineered Features:** 73  
- **Dataset:** German Credit Risk (1,000 records)
""", unsafe_allow_html=True)

# KPI Mini Dashboard
st.markdown("### 📈 Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="kpi-card"><div class="kpi-number">1,000</div><div class="kpi-label">Total Applications</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="kpi-card"><div class="kpi-number">18%</div><div class="kpi-label">Average Risk Score</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="kpi-card"><div class="kpi-number">76.5%</div><div class="kpi-label">Model Accuracy</div></div>', unsafe_allow_html=True)

# Core Capabilities
st.markdown("### 📊 Core Capabilities")
capabilities = [
    {"icon": "https://img.icons8.com/ios-filled/50/ffffff/automatic.png", "text": "Automated Risk Assessment: Real-time scoring"},
    {"icon": "https://img.icons8.com/ios-filled/50/ffffff/combo-chart.png", "text": "Portfolio Intelligence: Risk trends & distribution"},
    {"icon": "https://img.icons8.com/ios-filled/50/ffffff/analytics.png", "text": "Model Governance: Feature importance & False Negatives"}
]
for cap in capabilities:
    st.markdown(f'<div class="capability"><img src="{cap["icon"]}"><p>{cap["text"]}</p></div>', unsafe_allow_html=True)

# Decision Architecture
st.markdown("### 🏗️ Decision Architecture")
st.code("Data Input → Feature Engineering → Random Forest → Risk Score → Decision", language="text")

# Professional Links
st.markdown("### 🔗 Connect with Me")
st.markdown("""
<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
    <button class="github-btn">📁 GitHub Repository</button>
</a>
<a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
    <button class="linkedin-btn">🔵 LinkedIn Profile</button>
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
### 👥 Lead Developer
**Eng. Goda Emad**  
*Credit Risk Analytics Specialist*

**Version:** 3.0  
**Last Updated:** February 2026  
**Location:** Cairo, Egypt 🇪🇬
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

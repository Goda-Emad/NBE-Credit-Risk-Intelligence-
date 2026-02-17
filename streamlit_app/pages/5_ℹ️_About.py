"""
Professional About Page - NBE Credit Risk Intelligence
With Online Background & Logo
"""

import streamlit as st

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# =============================
# CSS Styling with Online Background & Logo
# =============================
st.markdown("""
<style>
/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    background-attachment: fixed;
}

/* Glass Card */
.glass-card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    color: white;
}

/* Titles */
h1, h2, h3 { color: #ffffff !important; }
p, li { color: #f1f1f1 !important; font-size: 16px; }

/* Buttons */
a button {
    width: 100%;
    padding: 12px;
    margin-bottom: 10px;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    cursor: pointer;
}
a button:hover { opacity: 0.85; transform: scale(1.02); transition: 0.2s; }

.github-btn { background-color: #24292e; color: white; }
.linkedin-btn { background-color: #0077b5; color: white; }

/* Logo */
.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 120px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Page Header
# =============================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Logo from Online Source (Free Placeholder Logo)
st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Bank_icon.png" class="logo">', unsafe_allow_html=True)

st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

# Project Overview
st.markdown("""
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
""", unsafe_allow_html=True)

# =============================
# Professional Links
# =============================
st.markdown("### 🔗 Connect with Me")

st.markdown("""
<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
    <button class="github-btn">📁 GitHub Repository</button>
</a>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
    <button class="linkedin-btn">🔵 LinkedIn Profile</button>
</a>
""", unsafe_allow_html=True)

# Footer Info
st.markdown("""
### 👥 Lead Developer
**Eng. Goda Emad**  
*Credit Risk Analytics Specialist*

**Version:** 3.0  
**Last Updated:** February 2026  
**Location:** Cairo, Egypt 🇪🇬
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

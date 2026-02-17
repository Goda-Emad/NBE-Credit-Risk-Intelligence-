import streamlit as st

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# --- CSS Glassmorphism + Dark Green Background ---
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #004d1a, #006622);
    color: white;
}
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    color: white;
}
h1 { font-size:36px; font-weight:bold; color:white; }
h2 { font-size:28px; font-weight:bold; color:white; }
h3 { font-size:22px; font-weight:bold; color:white; }
p, li { font-size:16px; color:#f1f1f1; }
.button-link {
    width:100%; padding:10px; font-weight:bold; border:none; border-radius:8px; cursor:pointer; margin-bottom:10px;
}
.github-btn { background-color:#24292e; color:white; }
.linkedin-btn { background-color:#0077b5; color:white; }
.logo { display:block; margin-left:auto; margin-right:auto; width:200px; margin-bottom:25px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# --- Logo from GitHub (guaranteed to work on Streamlit Cloud) ---
st.image(
    "https://raw.githubusercontent.com/Goda-Emad/NBE-Credit-Risk-Intelligence-/main/assets/nbe_branding/NBE_logo.png",
    width=200
)

# --- Title ---
st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

# --- Project Overview ---
st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-driven system designed to automate 
credit application assessment processes for the **National Bank of Egypt (NBE)**, 
enhancing accuracy and efficiency using advanced Machine Learning techniques.
""", unsafe_allow_html=True)

# --- Technical Specs ---
st.markdown("""
### 🔧 Technical Specifications
- **Model:** Random Forest Classifier (v3.0)  
- **Accuracy:** 76.5%  
- **Engineered Features:** 73  
- **Dataset:** German Credit Risk (1,000 applications)
""", unsafe_allow_html=True)

# --- Capabilities ---
st.markdown("""
### 📊 Capabilities
1. **Automated Risk Assessment:** Real-time scoring & probability-based recommendations.  
2. **Portfolio Analytics:** Insights into risk distribution, application trends, and performance metrics.  
3. **Model Monitoring:** Feature importance tracking & false negatives analysis.
""", unsafe_allow_html=True)

# --- Architecture ---
st.markdown("""
### 🏗️ Decision Architecture
""", unsafe_allow_html=True)

# --- Team & Contact ---
st.markdown("""
### 👥 Team
**Credit Risk Analytics Team**  
**National Bank of Egypt**

### 📞 Contact
- **Email:** creditrisk@nbe.com.eg  
- **Version:** 3.0  
- **Last Updated:** Feb 2026  
- **Location:** Cairo, Egypt 🇪🇬
""", unsafe_allow_html=True)

# --- Professional Links ---
st.markdown("""
### 🔗 Professional Links
<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank">
    <button class="button-link github-btn">📁 View GitHub Repository</button>
</a>
<a href="https://www.linkedin.com/in/goda-emad/" target="_blank">
    <button class="button-link linkedin-btn">🔵 Connect on LinkedIn</button>
</a>
""", unsafe_allow_html=True)

# --- Documentation & License ---
st.markdown("""
### 📚 Documentation
- Model Card: `docs/model_card.md`  
- Performance Report: `reports/model_performance_report.md`  

### 📄 License
MIT License © 2026 National Bank of Egypt
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

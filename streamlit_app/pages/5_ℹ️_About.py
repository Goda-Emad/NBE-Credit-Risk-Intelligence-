import streamlit as st

st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# Glass Card CSS
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #004d1a, #006622); }
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
.logo { display:block; margin-left:auto; margin-right:auto; width:200px; margin-bottom:25px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Logo
logo_path = "../../assets/nbe_branding/NBE_logo.png"  # المسار النسبي من About Page
st.image(logo_path, width=200)

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

st.markdown('</div>', unsafe_allow_html=True)

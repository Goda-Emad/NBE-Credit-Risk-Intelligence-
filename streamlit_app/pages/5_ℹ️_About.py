import streamlit as st
from pathlib import Path

# --- إعداد الصفحة ---
st.set_page_config(page_title="NBE Credit Risk - About", page_icon="ℹ️", layout="wide")

# --- CSS لتنسيق الصفحة (محسن للـ responsiveness) ---
st.markdown("""
<style>
/* خلفية عامة Dark Green */
body, .stApp {
    background-color: #004d1a !important;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
/* صندوق الشعار الأبيض كبير وواسع (responsive) */
.logo-card {
    background: white;
    border-radius: 20px;
    padding: 30px 40px;
    max-width: 400px; /* responsive: max-width بدل width ثابت */
    margin: 0 auto 20px auto;
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
/* أزرار مع hover effect */
.button-link {
    width:100%; padding:12px; font-weight:bold; border:none; border-radius:8px; cursor:pointer; margin-bottom:10px;
    transition: background-color 0.3s;
}
.github-btn { background-color:#24292e; color:white; }
.github-btn:hover { background-color:#333; }
.linkedin-btn { background-color:#0077b5; color:white; }
.linkedin-btn:hover { background-color:#005f91; }
/* Glass card محتوى (محسن للـ mobile) */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    color: white;
    max-width: 100%; /* responsive */
}
@media (max-width: 768px) {
    .glass-card { padding: 20px; }
}
</style>
""", unsafe_allow_html=True)

# --- دالة لتحميل الشعار مع error handling ---
def load_logo():
    logo_path = Path(__file__).parent / "assets" / "nbe_branding" / "NBE_logo.png"  # عدلت الـ path ليكون أقرب (افترض في streamlit_app)
    if not logo_path.exists():
        logo_path = Path.cwd() / "assets" / "nbe_branding" / "NBE_logo.png"  # fallback to cwd
    if logo_path.is_file():
        st.markdown('<div class="logo-card">', unsafe_allow_html=True)
        st.image(str(logo_path), width=200)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning(f"Logo file not found! Check the path: {logo_path}. Using placeholder.")
        # يمكن إضافة placeholder image هنا إذا لزم

# --- دالة لعرض KPIs (محسنة مع metrics إضافية) ---
def render_kpis():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<h3>Accuracy</h3><p>76.5%</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<h3>Features</h3><p>73</p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<h3>False Negatives</h3><p>31</p>', unsafe_allow_html=True)
    with col4:
        st.markdown('<h3>Version</h3><p>3.0</p>', unsafe_allow_html=True)

# --- دالة لعرض القدرات ---
def render_capabilities():
    st.markdown("""
    ### 📊 Capabilities
    1. **Automated Risk Assessment:** Real-time scoring & probability-based recommendations.
    2. **Portfolio Analytics:** Insights into risk distribution, application trends, and performance metrics.
    3. **Model Monitoring:** Feature importance tracking & false negatives analysis.
    """, unsafe_allow_html=True)

# --- دالة لعرض الـ Explainability (جديد) ---
def render_explainability():
    st.markdown("""
    ### 🔍 Explainability & Compliance
    - Uses SHAP values for local and global feature importance to ensure transparent decisions.
    - Compliant with CBE (Central Bank of Egypt) regulations for AI in credit risk, including audit trails and bias mitigation.
    """, unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.markdown("<h1>ℹ️ About NBE Credit Risk Intelligence</h1>", unsafe_allow_html=True)

# --- محتوى الصفحة الرئيسي ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

load_logo()  # تحميل الشعار

st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-driven system that modernizes
credit application assessment for the **National Bank of Egypt (NBE)**.
It automates decision-making with **high accuracy** and provides **real-time risk insights**.
""", unsafe_allow_html=True)

render_kpis()  # عرض KPIs

st.markdown("""
### 🔧 Technical Specifications
- **Model:** Random Forest Classifier (v3.0)
- **Dataset:** German Credit Risk (1,000 applications)
""", unsafe_allow_html=True)

render_capabilities()  # عرض Capabilities

render_explainability()  # عرض Explainability (جديد)

st.markdown("""
### 🏗️ Decision Architecture
- [System Architecture](docs/architecture.md) (View in repo)
""", unsafe_allow_html=True)

st.markdown("""
### 👥 Team
**Credit Risk Analytics Team** (Independent Project)
""", unsafe_allow_html=True)

st.markdown("""
### 📞 Contact
- **LinkedIn:** [Goda Emad](https://www.linkedin.com/in/goda-emad/)
- **Last Updated:** February 17, 2026
- **Location:** Cairo, Egypt 🇪🇬
""", unsafe_allow_html=True)

# Professional Links
st.markdown("""
### 🔗 Professional Links
<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank" rel="noopener noreferrer">
    <button class="button-link github-btn">📁 View GitHub Repository</button>
</a>
<a href="https://www.linkedin.com/in/goda-emad/" target="_blank" rel="noopener noreferrer">
    <button class="button-link linkedin-btn">🔵 Connect on LinkedIn</button>
</a>
""", unsafe_allow_html=True)

st.markdown("""
### 📚 Documentation
- [Model Card](docs/model_card.md)
- [Performance Report](reports/model_performance_report.md)
- [Data Dictionary](docs/data_dictionary.md)
""", unsafe_allow_html=True)

st.markdown("""
### 📄 License
MIT License © 2026 Goda Emad (Independent Developer)
""", unsafe_allow_html=True)

# Disclaimer (جديد)
st.markdown("""
### ⚠️ Disclaimer
This is an independent academic/prototype project inspired by credit risk practices at NBE and not officially affiliated with the National Bank of Egypt.
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

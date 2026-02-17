import streamlit as st
from pathlib import Path

# --- إعداد الصفحة ---
st.set_page_config(
    page_title="NBE Credit Risk - About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"  # افتراضي مفتوح للـ sidebar
)

# --- CSS احترافي محسن (dark banking theme) ---
st.markdown("""
<style>
    /* خلفية الصفحة الرئيسية */
    .stApp {
        background-color: #003d14;  /* أخضر داكن بنكي أكثر احترافية */
    }

    /* إخفاء أي عناصر غير مرغوبة في الهيدر الافتراضي إذا لزم */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        border-bottom: none !important;
    }

    /* عنوان الصفحة الرئيسي - يسار الهيدر */
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #b3ff99;
        margin: 1.5rem 0 0.5rem 0;
        padding-left: 1.5rem;
        text-align: left;
    }

    /* حاوية الهيدر الكاملة */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        background: linear-gradient(to right, #004d1a, #003d14);
        padding: 1rem 2rem;
        border-bottom: 2px solid #b3ff99;
        margin-bottom: 1.5rem;
    }

    /* اللوجو - خلفية بيضاء، بدون مربع إضافي */
    .logo-wrapper {
        background: white;
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-right: 1.5rem;
        flex-shrink: 0;
    }

    /* نصوص عامة */
    h2, h3 {
        color: #b3ff99 !important;
        font-weight: 600;
    }
    p, li {
        color: #e6ffe6;
        font-size: 1.1rem;
        line-height: 1.7;
    }

    /* KPIs في صفوف متجاوبة */
    .kpi-container {
        display: flex;
        flex-wrap: wrap;
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    .kpi-box {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(179,255,153,0.2);
        border-radius: 12px;
        padding: 1.2rem 1.8rem;
        min-width: 160px;
        text-align: center;
        flex: 1;
    }
    .kpi-label {
        font-size: 1rem;
        color: #b3ff99;
        margin-bottom: 0.5rem;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: bold;
        color: white;
    }

    /* Glass card للمحتوى الرئيسي */
    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(179,255,153,0.15);
        border-radius: 16px;
        padding: 2.5rem;
        margin-bottom: 2rem;
    }

    /* أزرار احترافية */
    .button-link {
        width: 100%;
        padding: 14px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
    }
    .github-btn { background: #24292e; color: white; }
    .github-btn:hover { background: #1f6feb; transform: translateY(-2px); }
    .linkedin-btn { background: #0077b5; color: white; }
    .linkedin-btn:hover { background: #005f8d; transform: translateY(-2px); }

    /* متجاوب للموبايل */
    @media (max-width: 768px) {
        .header-container { flex-direction: column; align-items: flex-start; padding: 1rem; }
        .logo-wrapper { margin: 0 auto 1rem auto; }
        .main-title { text-align: center; padding-left: 0; }
        .kpi-container { flex-direction: column; }
    }
</style>
""", unsafe_allow_html=True)

# --- تحميل اللوجو ---
def display_header():
    logo_path = Path(__file__).parent / "assets" / "nbe_branding" / "NBE_logo.png"
    if not logo_path.exists():
        logo_path = Path.cwd() / "assets" / "nbe_branding" / "NBE_logo.png"

    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    if logo_path.is_file():
        st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
        st.image(str(logo_path), width=140)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Logo not found – using placeholder")
        st.markdown('<div class="logo-wrapper">[NBE Logo Placeholder]</div>', unsafe_allow_html=True)

    st.markdown('<h1 class="main-title">About NBE Credit Risk Intelligence</h1>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- عرض الهيدر ---
display_header()

# --- المحتوى الرئيسي داخل glass card ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-driven system designed to modernize credit application assessment for the **National Bank of Egypt (NBE)**.  
It delivers automated, high-accuracy decision-making and real-time risk insights to support faster, more reliable credit operations.
""")

# KPIs احترافية
st.markdown('<div class="kpi-container">', unsafe_allow_html=True)

cols = st.columns(4)
with cols[0]:
    st.markdown('<div class="kpi-box"><div class="kpi-label">Accuracy</div><div class="kpi-value">76.5%</div></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="kpi-box"><div class="kpi-label">Engineered Features</div><div class="kpi-value">73</div></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="kpi-box"><div class="kpi-label">False Negatives</div><div class="kpi-value">31</div></div>', unsafe_allow_html=True)
with cols[3]:
    st.markdown('<div class="kpi-box"><div class="kpi-label">Version</div><div class="kpi-value">3.0</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
### 🔧 Technical Specifications
- **Model**: Random Forest Classifier (v3.0)  
- **Dataset**: German Credit Risk Dataset (1,000 samples) with advanced feature engineering  

### 📊 Key Capabilities
- Real-time automated risk scoring and probability-based recommendations  
- Portfolio-level analytics and trend monitoring  
- Model performance tracking with focus on explainability and false negatives reduction  

### 🔍 Explainability & Regulatory Alignment
- SHAP-based feature importance for transparent, auditable decisions  
- Designed with alignment to Central Bank of Egypt (CBE) AI governance expectations  
""")

st.markdown("""
### 👥 Project Team
Independent Credit Risk Analytics Initiative  

### 📞 Contact & Links
- **LinkedIn**: [Goda Emad](https://www.linkedin.com/in/goda-emad/)  
- **GitHub**: [Repository](https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-)  
- **Last Updated**: February 2026 | Cairo, Egypt 🇪🇬
""")

st.markdown("""
### 📚 Documentation
- [Model Card](docs/model_card.md)  
- [Performance Report](reports/model_performance_report.md)
""")

st.markdown("""
### ⚠️ Disclaimer
This is an independent prototype / academic project inspired by credit risk practices. Not officially affiliated with or endorsed by the National Bank of Egypt.
""")

st.markdown('</div>', unsafe_allow_html=True)

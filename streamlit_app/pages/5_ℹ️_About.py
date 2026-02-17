import streamlit as st
from pathlib import Path

# ─── إعداد الصفحة ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NBE Credit Risk - About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS احترافي (مع التركيز على عرض اللوجو بخلفية بيضاء صلبة) ────────────────
st.markdown("""
<style>
    .stApp {
        background-color: #003d14;
    }

    header[data-testid="stHeader"] {
        background-color: transparent !important;
        border-bottom: none !important;
    }

    .header-container {
        display: flex;
        align-items: center;
        background: linear-gradient(to right, #004d1a, #003d14);
        padding: 1.2rem 2rem;
        border-bottom: 2px solid #66cc66;
        margin-bottom: 1.8rem;
    }

    .logo-wrapper {
        background: white;                  /* خلفية بيضاء صلبة ← هنا الحل */
        border-radius: 12px;
        padding: 14px 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        margin-right: 1.8rem;
        flex-shrink: 0;
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 700;
        color: #ccffcc;
        margin: 0;
        text-align: left;
    }

    h2, h3 {
        color: #b3ff99;
        font-weight: 600;
        margin-top: 1.6rem;
        margin-bottom: 0.8rem;
    }

    p, li {
        color: #e6ffe6;
        font-size: 1.08rem;
        line-height: 1.65;
    }

    .kpi-container {
        display: flex;
        flex-wrap: wrap;
        gap: 1.2rem;
        margin: 1.8rem 0;
    }

    .kpi-box {
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(179,255,153,0.18);
        border-radius: 12px;
        padding: 1.2rem 1.8rem;
        min-width: 150px;
        text-align: center;
        flex: 1 1 160px;
    }

    .kpi-label {
        font-size: 0.95rem;
        color: #b3ff99;
        margin-bottom: 0.4rem;
    }

    .kpi-value {
        font-size: 1.9rem;
        font-weight: bold;
        color: white;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.055);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(179,255,153,0.14);
        border-radius: 16px;
        padding: 2.4rem;
        margin-bottom: 2rem;
    }

    .button-link {
        width: 100%;
        padding: 14px;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin: 0.7rem 0;
        transition: all 0.25s ease;
    }

    .github-btn   { background: #24292e; color: white; }
    .github-btn:hover   { background: #1f6feb; transform: translateY(-1px); }
    .linkedin-btn { background: #0077b5; color: white; }
    .linkedin-btn:hover { background: #005f8d; transform: translateY(-1px); }

    @media (max-width: 768px) {
        .header-container {
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 1.2rem;
        }
        .logo-wrapper {
            margin: 0 auto 1.2rem auto;
        }
        .main-title {
            text-align: center;
        }
        .kpi-container {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)

# ─── عرض الهيدر مع اللوجو بخلفية بيضاء ────────────────────────────────────────
def display_header():
    # محاولة تحديد مسار اللوجو (مرن لـ local و cloud)
    possible_paths = [
        Path(__file__).parent / "assets" / "nbe_branding" / "NBE_logo.png",
        Path.cwd() / "assets" / "nbe_branding" / "NBE_logo.png",
        Path(__file__).parents[1] / "assets" / "nbe_branding" / "NBE_logo.png",
    ]

    logo_path = None
    for p in possible_paths:
        if p.is_file():
            logo_path = p
            break

    st.markdown('<div class="header-container">', unsafe_allow_html=True)

    if logo_path:
        st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
        st.image(str(logo_path), width=180)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("تعذر العثور على ملف اللوجو. تأكد من وجوده في المسار assets/nbe_branding/NBE_logo.png")

    st.markdown(
        '<h1 class="main-title">About NBE Credit Risk Intelligence</h1>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ─── عرض الهيدر ────────────────────────────────────────────────────────────────
display_header()

# ─── المحتوى الرئيسي ────────────────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown("""
### 🎯 Project Overview
The **NBE Credit Risk Intelligence Platform** is an AI-powered prototype  
that aims to modernize credit application evaluation processes.  
It provides automated risk scoring, real-time insights, and transparent decision support.
""")

# KPIs
st.markdown('<div class="kpi-container">', unsafe_allow_html=True)

cols = st.columns([1,1,1,1])
with cols[0]:
    st.markdown(
        '<div class="kpi-box"><div class="kpi-label">Accuracy</div>'
        '<div class="kpi-value">76.5%</div></div>',
        unsafe_allow_html=True
    )
with cols[1]:
    st.markdown(
        '<div class="kpi-box"><div class="kpi-label">Engineered Features</div>'
        '<div class="kpi-value">73</div></div>',
        unsafe_allow_html=True
    )
with cols[2]:
    st.markdown(
        '<div class="kpi-box"><div class="kpi-label">False Negatives</div>'
        '<div class="kpi-value">31</div></div>',
        unsafe_allow_html=True
    )
with cols[3]:
    st.markdown(
        '<div class="kpi-box"><div class="kpi-label">Version</div>'
        '<div class="kpi-value">3.0</div></div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
### 🔧 Technical Stack
- **Model** — Random Forest Classifier  
- **Dataset** — German Credit Risk (1,000 samples) + heavy feature engineering  
- **Explainability** — SHAP values (local & global)  
- **Frontend** — Streamlit with custom dark banking theme  

### 📊 Core Capabilities
- Instant credit risk scoring  
- Probability of default estimation  
- Portfolio monitoring & trend visualization  
- Model performance & drift tracking  

### 🔍 Regulatory & Ethical Notes
- Designed with transparency and auditability in mind  
- SHAP explanations help meet explainability expectations  
- Independent academic/prototype project  

### 📞 Contact
**Goda Emad**  
LinkedIn → [linkedin.com/in/goda-emad](https://www.linkedin.com/in/goda-emad/)  
GitHub  → [github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-](https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-)  

**Location** : Cairo, Egypt  
**Last update** : February 2026
""")

st.markdown("""
### ⚠️ Important Disclaimer
This is an **independent educational / prototype project**.  
It is **not** officially developed by, affiliated with, or endorsed by  
the National Bank of Egypt (NBE).
""")

st.markdown('</div>', unsafe_allow_html=True)

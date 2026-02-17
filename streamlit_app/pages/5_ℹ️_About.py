import streamlit as st
from pathlib import Path

# ─── إعداد الصفحة ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NBE Credit Risk - About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS احترافي (تم تعديل تنسيق اللوجو لضمان الخلفية البيضاء) ────────────────
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

    /* تعديل حاوية اللوجو لضمان عدم وجود فراغات شفافة */
    .logo-wrapper {
        background-color: white !important;
        border-radius: 12px;
        padding: 10px; /* مسافة داخلية بسيطة حول اللوجو */
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        margin-right: 1.8rem;
        flex-shrink: 0;
        width: fit-content;
    }

    /* التأكد من أن الصورة داخل Streamlit لا تأخذ خلفية شفافة */
    div[data-component-instance-block="true"] img {
        background-color: white !important;
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
    }
</style>
""", unsafe_allow_html=True)

# ─── عرض الهيدر مع اللوجو ───────────────────────────────────────────────────
def display_header():
    # مسارات اللوجو
    possible_paths = [
        Path(__file__).parent / "assets" / "nbe_branding" / "NBE_logo.png",
        Path.cwd() / "assets" / "nbe_branding" / "NBE_logo.png",
    ]

    logo_path = next((p for p in possible_paths if p.is_file()), None)

    # بداية الهيدر
    st.markdown('<div class="header-container">', unsafe_allow_html=True)

    if logo_path:
        # وضع الصورة داخل الـ Wrapper الأبيض
        st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
        st.image(str(logo_path), width=180)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Logo not found.")

    st.markdown('<h1 class="main-title">About NBE Credit Risk Intelligence</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

display_header()

# ─── المحتوى (كما هو في كودك الأصلي) ──────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 🎯 Project Overview")
st.write("The **NBE Credit Risk Intelligence Platform** is an AI-powered prototype...")
# ... باقي المحتوى الخاص بك ...
st.markdown('</div>', unsafe_allow_html=True)

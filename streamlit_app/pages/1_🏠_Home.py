"""
NBE Credit Risk Intelligence - Home Page
Professional UI with NBE Dark Green Branding
"""
import streamlit as st

st.set_page_config(
    page_title="NBE Credit Risk Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS - Professional NBE Dark Green Theme
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Cairo:wght@400;600;700&display=swap');

/* Root Variables */
:root {
    --nbe-dark:    #003d28;
    --nbe-green:   #006341;
    --nbe-light:   #008a57;
    --nbe-gold:    #D4AF37;
    --nbe-cream:   #f9f6f0;
    --nbe-white:   #ffffff;
    --shadow:      0 8px 32px rgba(0,61,40,0.18);
}

/* Global */
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    background-color: var(--nbe-dark) !important;
    color: var(--nbe-white) !important;
}

/* Hide Streamlit defaults */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 2rem 2rem !important; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #002a1c 0%, #003d28 100%) !important;
    border-right: 1px solid var(--nbe-gold);
}
[data-testid="stSidebar"] * { color: var(--nbe-white) !important; }
[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 8px 12px;
    margin: 4px 0;
    transition: all 0.3s;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(212,175,55,0.2);
    border-left: 3px solid var(--nbe-gold);
}

/* Metrics */
[data-testid="stMetricValue"] {
    color: var(--nbe-gold) !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}
[data-testid="stMetricLabel"] { color: #aaa !important; }
[data-testid="stMetricDelta"] { color: #4ade80 !important; }

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--nbe-gold), #b8962e) !important;
    color: var(--nbe-dark) !important;
    font-weight: 700 !important;
    font-family: 'Cairo', sans-serif !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 28px !important;
    font-size: 16px !important;
    transition: all 0.3s !important;
    box-shadow: 0 4px 15px rgba(212,175,55,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(212,175,55,0.5) !important;
}

/* Divider */
hr { border-color: rgba(212,175,55,0.3) !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div style="
    background: linear-gradient(135deg, #002a1c 0%, #003d28 50%, #004d35 100%);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 20px;
    padding: 50px 40px;
    margin: 20px 0 30px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
">
    <!-- Decorative circles -->
    <div style="
        position: absolute; top: -60px; right: -60px;
        width: 250px; height: 250px;
        border-radius: 50%;
        border: 2px solid rgba(212,175,55,0.15);
    "></div>
    <div style="
        position: absolute; top: -30px; right: -30px;
        width: 150px; height: 150px;
        border-radius: 50%;
        border: 2px solid rgba(212,175,55,0.25);
    "></div>
    <div style="
        position: absolute; bottom: -40px; left: -40px;
        width: 180px; height: 180px;
        border-radius: 50%;
        border: 2px solid rgba(212,175,55,0.1);
    "></div>

    <!-- NBE Logo Area -->
    <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
        <div style="
            width: 80px; height: 80px;
            background: linear-gradient(135deg, #D4AF37, #b8962e);
            border-radius: 16px;
            display: flex; align-items: center; justify-content: center;
            font-size: 36px;
            box-shadow: 0 8px 20px rgba(212,175,55,0.4);
            flex-shrink: 0;
        ">🏦</div>
        <div>
            <div style="
                font-family: 'Cairo', sans-serif;
                font-size: 13px;
                color: #D4AF37;
                letter-spacing: 4px;
                text-transform: uppercase;
                margin-bottom: 4px;
            ">NATIONAL BANK OF EGYPT</div>
            <div style="
                font-family: 'Playfair Display', serif;
                font-size: 36px;
                font-weight: 700;
                color: #ffffff;
                line-height: 1.1;
            ">Credit Risk Intelligence</div>
        </div>
    </div>

    <!-- Subtitle -->
    <p style="
        color: rgba(255,255,255,0.75);
        font-size: 18px;
        max-width: 600px;
        line-height: 1.7;
        margin: 0 0 30px;
    ">
        منصة ذكاء اصطناعي متكاملة لتقييم مخاطر الائتمان في الوقت الفعلي،
        مبنية على نموذج Random Forest بدقة <strong style="color:#D4AF37;">76.5%</strong>
    </p>

    <!-- Badge row -->
    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        <span style="background:rgba(212,175,55,0.15); border:1px solid rgba(212,175,55,0.4);
              color:#D4AF37; padding:6px 14px; border-radius:20px; font-size:13px;">
            ✅ CBE Compliant
        </span>
        <span style="background:rgba(74,222,128,0.1); border:1px solid rgba(74,222,128,0.3);
              color:#4ade80; padding:6px 14px; border-radius:20px; font-size:13px;">
            🤖 AI Powered
        </span>
        <span style="background:rgba(96,165,250,0.1); border:1px solid rgba(96,165,250,0.3);
              color:#60a5fa; padding:6px 14px; border-radius:20px; font-size:13px;">
            ⚡ Real-time
        </span>
        <span style="background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.3);
              color:#a78bfa; padding:6px 14px; border-radius:20px; font-size:13px;">
            🔒 Secure
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# METRICS ROW
# ============================================================
col1, col2, col3, col4 = st.columns(4)
metrics = [
    ("🎯 Model Accuracy", "76.5%",  "+2.3%"),
    ("⚡ Features",        "73",     "Engineered"),
    ("📊 Training Data",  "800",    "Samples"),
    ("🌲 Decision Trees", "100",    "Random Forest"),
]
for col, (label, value, delta) in zip([col1,col2,col3,col4], metrics):
    with col:
        st.metric(label, value, delta)

st.markdown("---")

# ============================================================
# FEATURE CARDS
# ============================================================
st.markdown("""
<h2 style="color:#D4AF37; font-family:'Playfair Display',serif;
    font-size:28px; margin-bottom:20px;">
    🎯 Platform Capabilities
</h2>
""", unsafe_allow_html=True)

cards = [
    ("🎯", "Smart Assessment",
     "Real-time credit risk evaluation using Random Forest with 73 engineered features. Results in under 2 seconds.",
     "#D4AF37"),
    ("📊", "Portfolio Analytics",
     "Comprehensive portfolio insights, trend analysis, and performance metrics in interactive dashboards.",
     "#4ade80"),
    ("🔒", "CBE Compliant",
     "Full audit trail, explainable AI decisions, and regulatory compliance with Central Bank of Egypt standards.",
     "#60a5fa"),
    ("📈", "Model Monitoring",
     "Real-time model performance tracking, drift detection, and automated retraining pipeline.",
     "#a78bfa"),
    ("⚡", "Instant Decisions",
     "Sub-second predictions with probability scores and detailed recommendations for loan officers.",
     "#fb923c"),
    ("🔄", "Auto Retraining",
     "MLOps pipeline with automated model retraining when performance degrades below threshold.",
     "#f472b6"),
]

c1, c2, c3 = st.columns(3)
cols = [c1, c2, c3]
for i, (icon, title, desc, color) in enumerate(cards):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #002a1c, #003d28);
            border: 1px solid rgba(255,255,255,0.08);
            border-top: 3px solid {color};
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 16px;
            transition: all 0.3s;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        ">
            <div style="font-size:32px; margin-bottom:12px;">{icon}</div>
            <h3 style="color:{color}; font-size:18px; margin:0 0 10px;
                font-family:'Cairo',sans-serif; font-weight:700;">{title}</h3>
            <p style="color:rgba(255,255,255,0.65); font-size:14px;
                line-height:1.7; margin:0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# QUICK START
# ============================================================
st.markdown("""
<h2 style="color:#D4AF37; font-family:'Playfair Display',serif;
    font-size:28px; margin-bottom:20px;">
    🚀 Quick Start Guide
</h2>
""", unsafe_allow_html=True)

steps = [
    ("01", "🎯 Risk Assessment", "Go to Risk Assessment page from the sidebar"),
    ("02", "📋 Fill Details",    "Enter customer information in the form"),
    ("03", "🔍 Get Decision",    "Click Assess Risk for instant AI prediction"),
    ("04", "📊 View Analytics",  "Explore portfolio insights in Analytics page"),
]
s1, s2, s3, s4 = st.columns(4)
for col, (num, title, desc) in zip([s1,s2,s3,s4], steps):
    with col:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 16px;
            padding: 24px 16px;
            text-align: center;
        ">
            <div style="
                width:50px; height:50px;
                background: linear-gradient(135deg, #D4AF37, #b8962e);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 18px; font-weight: 700;
                color: #002a1c;
                margin: 0 auto 16px;
                font-family: 'Cairo', sans-serif;
            ">{num}</div>
            <h4 style="color:#ffffff; font-size:15px; margin:0 0 8px;
                font-family:'Cairo',sans-serif;">{title}</h4>
            <p style="color:rgba(255,255,255,0.5); font-size:13px;
                margin:0; line-height:1.5;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="
    background: linear-gradient(135deg, #002a1c, #003d28);
    border: 1px solid rgba(212,175,55,0.2);
    border-radius: 16px;
    padding: 30px 40px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
">
    <div>
        <div style="color:#D4AF37; font-weight:700; font-size:16px;
            font-family:'Cairo',sans-serif; margin-bottom:6px;">
            🏦 NBE Credit Risk Intelligence
        </div>
        <div style="color:rgba(255,255,255,0.5); font-size:13px;">
            © 2026 National Bank of Egypt | Version 3.0
        </div>
    </div>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
        <a href="https://www.linkedin.com/in/goda-emad/"
           target="_blank" style="
            background: rgba(10,102,194,0.2);
            border: 1px solid rgba(10,102,194,0.5);
            color: #60a5fa;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
        ">🔗 LinkedIn - ENG.Goda Emad</a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
           target="_blank" style="
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.15);
            color: #ffffff;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-family: 'Cairo', sans-serif;
        ">⭐ GitHub Project</a>
    </div>
</div>
""", unsafe_allow_html=True)

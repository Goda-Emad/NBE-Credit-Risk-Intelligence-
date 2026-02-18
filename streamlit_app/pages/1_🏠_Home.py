"""
NBE Credit Risk Intelligence - Home Page
Professional UI with Real NBE Banner & Logo
"""

import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="NBE Credit Risk Intelligence",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# Helper: Load Image as Base64
# ============================================================
def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# ============================================================
# FIXED: Direct path (works local + cloud)
# ============================================================
base_path = Path("assets/nbe_branding")

banner_file = base_path / "banner.png"
logo_file = base_path / "nbe_logo.jpg"

banner_b64 = get_image_base64(banner_file) if banner_file.exists() else None
logo_b64 = get_image_base64(logo_file) if logo_file.exists() else None
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

/* Banner Image */
.banner-img {
    width: 100%;
    height: auto;
    border-radius: 20px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

/* Logo styles */
.nbe-logo {
    width: 100px;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(212,175,55,0.3);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# BANNER IMAGE (Full Width)
# ============================================================
if banner_b64:
    st.markdown(f"""
    <div style="margin: 20px 0 30px;">
        <img src="data:image/png;base64,{banner_b64}" class="banner-img" alt="NBE Banner">
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HERO SECTION WITH REAL NBE LOGO
# ============================================================
hero_html = """
<div style="
    background: linear-gradient(135deg, #002a1c 0%, #003d28 50%, #004d35 100%);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 20px;
    padding: 50px 40px;
    margin: 0 0 30px;
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

    <!-- Logo & Title Section -->
    <div style="display: flex; align-items: center; gap: 25px; margin-bottom: 25px; flex-wrap: wrap;">
"""

if logo_b64:
    hero_html += f"""
        <img src="data:image/jpeg;base64,{logo_b64}" class="nbe-logo" alt="NBE Logo">
    """
else:
    hero_html += """
        <div style="
            width: 100px; height: 100px;
            background: linear-gradient(135deg, #D4AF37, #b8962e);
            border-radius: 16px;
            display: flex; align-items: center; justify-content: center;
            font-size: 48px;
            box-shadow: 0 8px 20px rgba(212,175,55,0.4);
            flex-shrink: 0;
        ">🏦</div>
    """

hero_html += """
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
                font-size: 42px;
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
        max-width: 700px;
        line-height: 1.7;
        margin: 0 0 30px;
    ">
        منصة ذكاء اصطناعي متكاملة لتقييم مخاطر الائتمان في الوقت الفعلي،
        مبنية على نموذج Random Forest بدقة <strong style="color:#D4AF37;">76.5%</strong>
        ومتوافقة بالكامل مع معايير البنك المركزي المصري
    </p>

    <!-- Badge row -->
    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        <span style="background:rgba(212,175,55,0.15); border:1px solid rgba(212,175,55,0.4);
              color:#D4AF37; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            ✅ CBE Compliant
        </span>
        <span style="background:rgba(74,222,128,0.1); border:1px solid rgba(74,222,128,0.3);
              color:#4ade80; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            🤖 AI Powered
        </span>
        <span style="background:rgba(96,165,250,0.1); border:1px solid rgba(96,165,250,0.3);
              color:#60a5fa; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            ⚡ Real-time
        </span>
        <span style="background:rgba(167,139,250,0.1); border:1px solid rgba(167,139,250,0.3);
              color:#a78bfa; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            🔒 Secure
        </span>
        <span style="background:rgba(251,146,60,0.1); border:1px solid rgba(251,146,60,0.3);
              color:#fb923c; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            📊 73 Features
        </span>
        <span style="background:rgba(244,114,182,0.1); border:1px solid rgba(244,114,182,0.3);
              color:#f472b6; padding:6px 14px; border-radius:20px; font-size:13px; font-weight:600;">
            🌲 100 Trees
        </span>
    </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

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
     "تقييم فوري لمخاطر الائتمان باستخدام Random Forest مع 73 ميزة هندسية. النتائج في أقل من ثانيتين.",
     "#D4AF37"),
    ("📊", "Portfolio Analytics",
     "رؤى شاملة للمحفظة، تحليل الاتجاهات، ومقاييس الأداء في لوحات تحكم تفاعلية.",
     "#4ade80"),
    ("🔒", "CBE Compliant",
     "مسار تدقيق كامل، قرارات ذكاء اصطناعي قابلة للتفسير، والامتثال التنظيمي الكامل للبنك المركزي المصري.",
     "#60a5fa"),
    ("📈", "Model Monitoring",
     "تتبع أداء النموذج في الوقت الفعلي، كشف الانحراف، وخط إعادة تدريب تلقائي.",
     "#a78bfa"),
    ("⚡", "Instant Decisions",
     "تنبؤات بأقل من ثانية مع درجات احتمالية وتوصيات تفصيلية لموظفي القروض.",
     "#fb923c"),
    ("🔄", "Auto Retraining",
     "خط MLOps مع إعادة تدريب تلقائية للنموذج عند انخفاض الأداء تحت العتبة المحددة.",
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
            height: 100%;
        ">
            <div style="font-size:40px; margin-bottom:14px;">{icon}</div>
            <h3 style="color:{color}; font-size:19px; margin:0 0 12px;
                font-family:'Cairo',sans-serif; font-weight:700;">{title}</h3>
            <p style="color:rgba(255,255,255,0.7); font-size:14px;
                line-height:1.8; margin:0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# QUICK START GUIDE
# ============================================================
st.markdown("""
<h2 style="color:#D4AF37; font-family:'Playfair Display',serif;
    font-size:28px; margin-bottom:20px;">
    🚀 Quick Start Guide
</h2>
""", unsafe_allow_html=True)

steps = [
    ("01", "🎯 Risk Assessment", "انتقل إلى صفحة تقييم المخاطر من القائمة الجانبية"),
    ("02", "📋 Fill Details",    "أدخل معلومات العميل في النموذج"),
    ("03", "🔍 Get Decision",    "اضغط على تقييم المخاطر للحصول على تنبؤ فوري بالذكاء الاصطناعي"),
    ("04", "📊 View Analytics",  "استكشف رؤى المحفظة في صفحة التحليلات"),
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
            height: 100%;
            transition: all 0.3s;
        " onmouseover="this.style.transform='translateY(-5px)';this.style.boxShadow='0 12px 30px rgba(212,175,55,0.2)';"
           onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
            <div style="
                width:60px; height:60px;
                background: linear-gradient(135deg, #D4AF37, #b8962e);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 20px; font-weight: 700;
                color: #002a1c;
                margin: 0 auto 18px;
                font-family: 'Cairo', sans-serif;
                box-shadow: 0 6px 20px rgba(212,175,55,0.4);
            ">{num}</div>
            <h4 style="color:#ffffff; font-size:16px; margin:0 0 10px;
                font-family:'Cairo',sans-serif; font-weight:700;">{title}</h4>
            <p style="color:rgba(255,255,255,0.55); font-size:13px;
                margin:0; line-height:1.6;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# TECHNOLOGY & STATS SECTION
# ============================================================
st.markdown("---")

c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:28px;height:100%;">
        <h3 style="color:#D4AF37;font-family:'Playfair Display',serif;
            font-size:22px;margin-bottom:20px;">🔧 Technology Stack</h3>
    """, unsafe_allow_html=True)

    techs = [
        ("🐍", "Python 3.11",     "#4ade80"),
        ("🌊", "Streamlit",       "#60a5fa"),
        ("🤖", "scikit-learn",    "#D4AF37"),
        ("📊", "Plotly",          "#a78bfa"),
        ("🐼", "Pandas",          "#fb923c"),
        ("🔢", "NumPy",           "#f472b6"),
    ]
    for icon, name, color in techs:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:14px;
            padding:12px 16px;border-radius:10px;
            background:rgba(255,255,255,0.02);
            border:1px solid rgba(255,255,255,0.05);
            margin-bottom:10px;">
            <span style="font-size:24px;">{icon}</span>
            <span style="color:{color};font-weight:600;font-size:15px;">{name}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:28px;height:100%;">
        <h3 style="color:#60a5fa;font-family:'Playfair Display',serif;
            font-size:22px;margin-bottom:20px;">📊 Performance Metrics</h3>
    """, unsafe_allow_html=True)

    stats = [
        ("Test Accuracy",     "76.50%",   "#D4AF37"),
        ("Precision",         "64.4%",    "#4ade80"),
        ("Recall",            "48.3%",    "#60a5fa"),
        ("F1-Score",          "55.2%",    "#a78bfa"),
        ("False Negatives",   "31 cases", "#f87171"),
        ("Training Time",     "< 1 min",  "#fb923c"),
    ]
    for label, value, color in stats:
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
            padding:12px 16px;border-radius:10px;
            background:rgba(255,255,255,0.02);
            border:1px solid rgba(255,255,255,0.05);
            margin-bottom:10px;">
            <span style="color:rgba(255,255,255,0.6);font-size:14px;">{label}</span>
            <span style="color:{color};font-weight:700;font-size:16px;">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# FOOTER - DEVELOPER CARD
# ============================================================
st.markdown("---")
st.markdown("""
<div style="
    background: linear-gradient(135deg, #002a1c, #003d28);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 20px;
    padding: 35px 40px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
">
    <div>
        <div style="color:#D4AF37; font-weight:700; font-size:18px;
            font-family:'Cairo',sans-serif; margin-bottom:8px;">
            🏦 NBE Credit Risk Intelligence
        </div>
        <div style="color:rgba(255,255,255,0.5); font-size:14px; line-height:1.6;">
            © 2026 National Bank of Egypt<br>
            Developed by <strong style="color:#D4AF37;">ENG. Goda Emad</strong> | Version 3.0
        </div>
    </div>
    <div style="display:flex; gap:14px; flex-wrap:wrap;">
        <a href="https://www.linkedin.com/in/goda-emad/"
           target="_blank" style="
            background: rgba(10,102,194,0.2);
            border: 2px solid rgba(10,102,194,0.5);
            color: #60a5fa;
            padding: 10px 20px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
            display: inline-block;
        " onmouseover="this.style.background='rgba(10,102,194,0.3)';this.style.transform='translateY(-2px)';"
           onmouseout="this.style.background='rgba(10,102,194,0.2)';this.style.transform='translateY(0)';">
           🔗 LinkedIn - ENG.Goda Emad
        </a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
           target="_blank" style="
            background: rgba(255,255,255,0.05);
            border: 2px solid rgba(255,255,255,0.15);
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
            display: inline-block;
        " onmouseover="this.style.background='rgba(255,255,255,0.1)';this.style.transform='translateY(-2px)';"
           onmouseout="this.style.background='rgba(255,255,255,0.05)';this.style.transform='translateY(0)';">
           ⭐ GitHub Project
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
```

---
"""
Project Structure:

NBE-Credit-Risk-Intelligence/
├── assets/
│   └── nbe_branding/
│       ├── banner.png
│       └── nbe_logo.jpg
└── streamlit_app/
    └── pages/
        └── 1_🏠_Home.py
"""

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
# Helper: Load Image as Base64 (Updated for Cloud & Local)
# ============================================================
def get_image_base64(image_name):
    """
    دالة محسنة للبحث عن الصورة في أكثر من مكان لضمان عملها على السيرفر
    """
    # البحث في نفس مجلد ملف الكود أو مجلد assets
    current_dir = Path(__file__).parent
    potential_paths = [
        current_dir / image_name,
        current_dir / "assets" / "nbe_branding" / image_name,
        current_dir.parent / "assets" / "nbe_branding" / image_name
    ]
    
    for path in potential_paths:
        if path.exists():
            try:
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
            except Exception:
                continue
    return None

# تحميل البانر فقط كما طلبت (بدون لوجو)
banner_b64 = get_image_base64("banner.png")

# ============================================================
# Global CSS - Optimized for White Background & Horizontal Layouts
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');

/* الأساسيات: تغيير الخط والألوان لتناسب الخلفية البيضاء */
:root {
    --nbe-dark:    #003d28; /* أخضر البنك الأهلي الداكن */
    --nbe-green:   #006341; /* أخضر البنك المتوسط */
    --nbe-gold:    #D4AF37; /* اللون الذهبي */
    --text-main:   #1a1a1a; /* أسود خفيف للنصوص الأساسية */
    --text-sub:    #444444; /* رمادي غامق للنصوص الفرعية */
    --bg-light:    #f9fbf9; /* خلفية فاتحة جداً مريحة للعين */
}

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    color: var(--text-main) !important;
}

/* تعديل الـ Banner ليكون متجاوب وحجمه مناسب للعرض */
.banner-container {
    width: 100%;
    max-height: 280px; /* تقليل الارتفاع قليلاً ليكون متناسق مع العرض */
    overflow: hidden;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 8px 24px rgba(0,61,40,0.12); /* ظل أخضر خفيف */
    border: 1px solid rgba(0,61,40,0.05);
}

.banner-img {
    width: 100%;
    height: auto;
    object-fit: cover;
}

/* حل مشكلة التكنولوجيا: تصميم أفقي (Horizontal Tech Stack) */
.tech-container-horizontal {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 15px;
    margin: 20px 0;
}

.tech-card-mini {
    background: white;
    border-left: 4px solid var(--nbe-gold);
    border-radius: 8px;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: transform 0.2s;
}

.tech-card-mini:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* إخفاء الهيدر الافتراضي لستريمليت */
header {visibility: hidden;}

/* تحسين شكل المقياس (Metric) ليناسب الخلفية البيضاء */
[data-testid="stMetric"] {
    background: #ffffff;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border: 1px solid #f0f0f0;
}

[data-testid="stMetricValue"] {
    color: var(--nbe-dark) !important;
}

[data-testid="stMetricLabel"] {
    color: var(--text-sub) !important;
}
</style>
""", unsafe_allow_html=True)
# ============================================================
# 1. Display Banner
# ============================================================
if banner_b64:
    st.markdown(f"""
    <div class="banner-container">
        <img src="data:image/png;base64,{banner_b64}" class="banner-img" alt="NBE Banner">
    </div>
    """, unsafe_allow_html=True)
else:
    # رسالة تنبيه بسيطة وواضحة في حالة عدم وجود الصورة على السيرفر
    st.warning("⚠️ Banner image 'banner.png' not found. Please ensure it's in the project folder for Streamlit Cloud.")

# ============================================================
# 2. Hero Section (Title & Description) - Optimized for Visibility
# ============================================================
st.markdown("""
<div style="padding: 10px 0 30px 0;">
    <h1 style="color: #003d28; font-family: 'Cairo', sans-serif; font-size: 38px; font-weight: 700; margin-bottom: 5px;">
        Credit Risk Intelligence
    </h1>
    <p style="color: #D4AF37; font-family: 'Cairo', sans-serif; font-size: 16px; font-weight: 600; letter-spacing: 3px; margin-bottom: 20px; text-transform: uppercase;">
        National Bank of Egypt | البنك الأهلي المصري
    </p>
    <div style="max-width: 850px; border-left: 5px solid #003d28; padding-left: 20px;">
        <p style="color: #444444; font-family: 'Cairo', sans-serif; font-size: 19px; line-height: 1.6; margin: 0;">
            منصة ذكاء اصطناعي متطورة لتقييم الجدارة الائتمانية وتحليل مخاطر القروض في الوقت الفعلي، 
            مبنية على خوارزميات <strong>Random Forest</strong> بدقة تصل إلى <strong>76.5%</strong>.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
# ============================================================
# CSS - Professional NBE "Light & Elegant" Theme
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Cairo:wght@400;600;700&display=swap');

/* Root Variables - Optimized for Visibility */
:root {
    --nbe-dark:    #003d28; /* الأخضر الغامق للبنك */
    --nbe-gold:    #D4AF37; /* الذهبي */
    --text-main:   #1a1a1a; /* أسود صريح للنصوص */
    --text-sub:    #444444; /* رمادي غامق جداً */
    --bg-light:    #ffffff; /* خلفية بيضاء صريحة */
    --sidebar-bg:  #f4f7f6; /* لون سايدبار هادئ */
}

/* Global Styles */
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    background-color: var(--bg-light) !important;
    color: var(--text-main) !important;
}

/* Hide Streamlit defaults */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 3rem 3rem !important; }

/* Sidebar - Light Mode Professional */
[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg) !important;
    border-right: 2px solid var(--nbe-dark);
}

/* Sidebar Text Fix */
[data-testid="stSidebar"] * { 
    color: var(--nbe-dark) !important; 
}

/* Sidebar Radio Buttons Fix */
[data-testid="stSidebar"] .stRadio label {
    background: rgba(0, 61, 40, 0.05);
    border-radius: 10px;
    padding: 10px 15px;
    margin: 5px 0;
    transition: all 0.3s ease;
    border: 1px solid transparent;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(212, 175, 55, 0.1);
    border-left: 5px solid var(--nbe-gold);
    color: var(--nbe-dark) !important;
}

/* Metrics - High Contrast */
[data-testid="stMetric"] {
    background: white !important;
    border: 1px solid #eee !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    border-radius: 15px !important;
    padding: 20px !important;
}
[data-testid="stMetricValue"] {
    color: var(--nbe-dark) !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
}
[data-testid="stMetricLabel"] { 
    color: var(--text-sub) !important; 
    font-weight: 600 !important;
}

/* Buttons - Gold Theme */
.stButton > button {
    background: linear-gradient(135deg, var(--nbe-dark) 0%, #005236 100%) !important;
    color: white !important; /* النص أبيض هنا لأن الخلفية غامقة */
    font-weight: 700 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 15px 35px !important;
    transition: all 0.4s !important;
    box-shadow: 0 4px 15px rgba(0,61,40,0.2) !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(0,61,40,0.3) !important;
    background: var(--nbe-gold) !important;
    color: var(--nbe-dark) !important;
}

/* Banner Image Adjustment */
.banner-img {
    width: 100%;
    max-height: 250px;
    object-fit: cover;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
}

/* Horizontal Technology Tags */
.tech-tag {
    display: inline-block;
    padding: 8px 18px;
    background: #f0f2f1;
    border: 1px solid var(--nbe-dark);
    color: var(--nbe-dark);
    border-radius: 50px;
    margin-right: 10px;
    margin-bottom: 10px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)
# ============================================================
# BANNER IMAGE (Full Width & Responsive)
# ============================================================
if banner_b64:
    st.markdown(f"""
    <div style="margin: 10px 0 25px 0;">
        <img src="data:image/png;base64,{banner_b64}" class="banner-img" alt="NBE Banner Intelligence">
    </div>
    """, unsafe_allow_html=True)
else:
    # رسالة بديلة احترافية في حالة عدم تحميل الصورة
    st.markdown("""
        <div style="background-color: #f0f2f1; padding: 40px; border-radius: 15px; text-align: center; border: 1px dashed #003d28;">
            <h2 style="color: #003d28; margin: 0;">NBE Credit Risk Intelligence</h2>
            <p style="color: #D4AF37;">National Bank of Egypt | AI Assessment Platform</p>
        </div>
    """, unsafe_allow_html=True)
# ============================================================
# HERO SECTION - Light & Professional (NBE Theme)
# ============================================================
# تم تحويل التصميم من Dark لـ Light لضمان وضوح الخطوط
hero_html = f"""
<div style="
    background: #ffffff;
    border-radius: 20px;
    padding: 30px 0px;
    margin: -10px 0 30px;
    position: relative;
    border-bottom: 2px solid #f0f0f0;
">
    <div style="margin-bottom: 20px;">
        <div style="
            font-family: 'Cairo', sans-serif;
            font-size: 14px;
            color: #D4AF37;
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 5px;
        ">National Bank of Egypt | البنك الأهلي المصري</div>
        <h1 style="
            font-family: 'Playfair Display', serif;
            font-size: 45px;
            font-weight: 800;
            color: #003d28; /* أخضر البنك الأهلي الداكن */
            line-height: 1.1;
            margin: 0;
        ">Credit Risk Intelligence</h1>
    </div>

    <p style="
        color: #444444; /* رمادي داكن للوضوح */
        font-size: 19px;
        max-width: 800px;
        line-height: 1.6;
        margin: 0 0 25px;
        font-family: 'Cairo', sans-serif;
    ">
        منصة ذكاء اصطناعي متكاملة لتقييم مخاطر الائتمان في الوقت الفعلي، 
        مبنية على نموذج <span style="color:#003d28; font-weight:700;">Random Forest</span> بدقة <strong style="color:#D4AF37; font-size:22px;">76.5%</strong> 
        وموافقة لمعايير البنك المركزي المصري.
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 12px;">
        <span style="background:rgba(0, 61, 40, 0.05); border:1px solid #003d28;
              color:#003d28; padding:8px 16px; border-radius:50px; font-size:13px; font-weight:700;">
            ✅ CBE Compliant
        </span>
        <span style="background:rgba(212, 175, 55, 0.1); border:1px solid #D4AF37;
              color:#D4AF37; padding:8px 16px; border-radius:50px; font-size:13px; font-weight:700;">
            🤖 AI Powered
        </span>
        <span style="background:#f8f9fa; border:1px solid #ddd;
              color:#555; padding:8px 16px; border-radius:50px; font-size:13px; font-weight:700;">
            ⚡ Real-time
        </span>
        <span style="background:#f8f9fa; border:1px solid #ddd;
              color:#555; padding:8px 16px; border-radius:50px; font-size:13px; font-weight:700;">
            📊 73 Features
        </span>
    </div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)
# ============================================================
# METRICS ROW - Enhanced Visibility
# ============================================================
# إنشاء الأعمدة الأربعة (تنسيق أفقي طبيعي في Streamlit)
col1, col2, col3, col4 = st.columns(4)

metrics = [
    ("🎯 Model Accuracy", "76.5%", "+2.3%"),
    ("⚡ Features",        "73",     "Engineered"),
    ("📊 Training Data",  "800",    "Samples"),
    ("🌲 Decision Trees", "100",    "Random Forest"),
]

# استخدام CSS داخلي لضمان وضوح أرقام الـ Metrics
st.markdown("""
<style>
    /* تحسين ألوان المقياس ليناسب الخلفية البيضاء */
    [data-testid="stMetricValue"] {
        color: #003d28 !important; /* أخضر البنك الأهلي الداكن */
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] p {
        color: #444444 !important; /* رمادي داكن للعنوان */
        font-size: 16px !important;
    }
    [data-testid="stMetricDelta"] div {
        color: #D4AF37 !important; /* ذهبي للزيادة أو التفاصيل */
    }
</style>
""", unsafe_allow_html=True)

for col, (label, value, delta) in zip([col1, col2, col3, col4], metrics):
    with col:
        # قمنا بتغليف المقياس داخل Container لإعطائه مظهر الكارت الأبيض
        with st.container():
            st.metric(label, value, delta)

st.markdown("<hr style='border-color: #eee;'>", unsafe_allow_html=True)
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
# QUICK START GUIDE - Light Theme Optimized
# ============================================================
st.markdown("""
<h2 style="color:#003d28; font-family:'Cairo',sans-serif;
    font-size:28px; margin-top:40px; margin-bottom:20px; text-align:right;">
    🚀 دليل البدء السريع
</h2>
""", unsafe_allow_html=True)

steps = [
    ("01", "🎯 Risk Assessment", "انتقل إلى صفحة تقييم المخاطر من القائمة الجانبية"),
    ("02", "📋 Fill Details",    "أدخل معلومات العميل في النموذج المخصص"),
    ("03", "🔍 Get Decision",    "اضغط على تقييم المخاطر للحصول على تنبؤ فوري"),
    ("04", "📊 View Analytics",  "استكشف رؤى المحفظة في صفحة التحليلات"),
]

s1, s2, s3, s4 = st.columns(4)

for col, (num, title, desc) in zip([s1, s2, s3, s4], steps):
    with col:
        st.markdown(f"""
        <div style="
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-top: 4px solid #003d28; /* لمسة خضراء من الأعلى */
            border-radius: 12px;
            padding: 25px 15px;
            text-align: center;
            height: 220px; /* توحيد الارتفاع */
            transition: all 0.3s;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        ">
            <div style="
                width:50px; height:50px;
                background: linear-gradient(135deg, #003d28, #006341);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 18px; font-weight: 700;
                color: #D4AF37;
                margin: 0 auto 15px;
                font-family: 'Cairo', sans-serif;
                box-shadow: 0 4px 10px rgba(0,61,40,0.2);
            ">{num}</div>
            <h4 style="color:#003d28; font-size:17px; margin:0 0 12px;
                font-family:'Cairo',sans-serif; font-weight:700;">{title}</h4>
            <p style="color:#555555; font-size:14px;
                margin:0; line-height:1.5; font-family:'Cairo',sans-serif;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
# ============================================================
# TECHNOLOGY & STATS SECTION - Horizontal & High Contrast
# ============================================================
st.markdown("<br>", unsafe_allow_html=True)

# تقسيم الصفحة لعرض التكنولوجيا والنتائج جنب بعض
c1, c2 = st.columns([1.2, 1])

with c1:
    st.markdown("""
    <div style="background:#ffffff; border:1px solid #eef2f1; border-radius:16px; padding:25px; height:100%; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <h3 style="color:#003d28; font-family:'Cairo',serif; font-size:22px; margin-bottom:20px; display:flex; align-items:center; gap:10px;">
            🔧 <span style="border-bottom: 3px solid #D4AF37;">Technology Stack</span>
        </h3>
        <div style="display:flex; flex-wrap:wrap; gap:10px;">
    """, unsafe_allow_html=True)

    # قائمة التكنولوجيا بالألوان الداكنة الواضحة
    techs = [
        ("🐍", "Python 3.11",     "#003d28"),
        ("🌊", "Streamlit",       "#006341"),
        ("🤖", "scikit-learn",    "#D4AF37"),
        ("📊", "Plotly",          "#2c3e50"),
        ("🐼", "Pandas",          "#1f77b4"),
        ("🔢", "NumPy",           "#d62728"),
    ]
    
    for icon, name, color in techs:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:8px; 
            padding:8px 15px; border-radius:50px; 
            background:#f8f9fa; 
            border:1px solid {color}44; /* لون شفاف خفيف للإطار */
            ">
            <span style="font-size:18px;">{icon}</span>
            <span style="color:{color}; font-weight:700; font-size:14px;">{name}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:#003d28; border-radius:16px; padding:25px; height:100%; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="color:#D4AF37; font-family:'Cairo',serif; font-size:22px; margin-bottom:20px;">
            📊 Performance Metrics
        </h3>
    """, unsafe_allow_html=True)

    stats = [
        ("Test Accuracy",     "76.50%",   "#D4AF37"),
        ("Precision",         "64.4%",    "#4ade80"),
        ("Recall",            "48.3%",    "#60a5fa"),
        ("F1-Score",          "55.2%",    "#a78bfa"),
        ("False Negatives",   "31 cases", "#f87171"),
    ]
    
    for label, value, color in stats:
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; align-items:center; 
            padding:10px 0; border-bottom:1px solid rgba(255,255,255,0.1);">
            <span style="color:rgba(255,255,255,0.8); font-size:14px;">{label}</span>
            <span style="color:{color}; font-weight:700; font-size:16px;">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
# ============================================================
# FOOTER - DEVELOPER CARD (Optimized for Visibility)
# ============================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
<div style="
    background: #ffffff;
    border: 1px solid #eef2f1;
    border-radius: 20px;
    padding: 30px 40px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    box-shadow: 0 10px 30px rgba(0,61,40,0.08); /* ظل أخضر خفيف جداً */
">
    <div>
        <div style="color:#003d28; font-weight:700; font-size:20px;
            font-family:'Cairo',sans-serif; margin-bottom:5px;">
            🏦 NBE Credit Risk Intelligence
        </div>
        <div style="color:#666666; font-size:14px; line-height:1.6; font-family:'Cairo',sans-serif;">
            © 2026 National Bank of Egypt<br>
            Developed by <strong style="color:#D4AF37;">ENG. GODA EMAD</strong> | Version 3.0
        </div>
    </div>
    
    <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a href="https://www.linkedin.com/in/goda-emad/"
           target="_blank" style="
            background: #0a66c2;
            color: #ffffff;
            padding: 10px 22px;
            border-radius: 12px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(10,102,194,0.2);
        ">
            🔗 LinkedIn Profile
        </a>
        
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
           target="_blank" style="
            background: #24292e;
            color: #ffffff;
            padding: 10px 22px;
            border-radius: 12px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        ">
            ⭐ GitHub Project
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

"""
NBE Credit Risk Intelligence - Home Page
Professional UI - National Bank of Egypt (البنك الأهلي المصري)
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
# Language Selection (Session State)
# ============================================================
if 'language' not in st.session_state:
    st.session_state.language = 'ar'  # Default: Arabic

# ============================================================
# Load Banner Image
# ============================================================
def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# Find banner in assets/images/
possible_paths = [
    Path(__file__).parent.parent.parent / "assets" / "images" / "banner.png",
    Path("assets") / "images" / "banner.png",
    Path("../assets") / "images" / "banner.png",
]

banner_b64 = None
for banner_path in possible_paths:
    if banner_path.exists():
        banner_b64 = get_image_base64(banner_path)
        break

# ============================================================
# Translations
# ============================================================
TRANSLATIONS = {
    'ar': {
        'title': 'منصة الذكاء الاصطناعي لتقييم مخاطر الائتمان',
        'subtitle': 'البنك الأهلي المصري',
        'description': 'منصة ذكاء اصطناعي متكاملة لتقييم مخاطر الائتمان في الوقت الفعلي، مبنية على نموذج Random Forest بدقة 76.5% ومتوافقة بالكامل مع معايير البنك المركزي المصري',
        'badge_cbe': 'متوافق مع البنك المركزي',
        'badge_ai': 'مدعوم بالذكاء الاصطناعي',
        'badge_realtime': 'الوقت الفعلي',
        'badge_secure': 'آمن ومحمي',
        'badge_features': '73 ميزة',
        'badge_trees': '100 شجرة',
        'metric1': 'دقة النموذج',
        'metric2': 'الميزات',
        'metric3': 'بيانات التدريب',
        'metric4': 'أشجار القرار',
        'capabilities': 'قدرات المنصة',
        'cap1_title': 'تقييم ذكي',
        'cap1_desc': 'تقييم فوري لمخاطر الائتمان باستخدام Random Forest مع 73 ميزة هندسية. النتائج في أقل من ثانيتين.',
        'cap2_title': 'تحليلات المحفظة',
        'cap2_desc': 'رؤى شاملة للمحفظة، تحليل الاتجاهات، ومقاييس الأداء في لوحات تحكم تفاعلية.',
        'cap3_title': 'متوافق مع البنك المركزي',
        'cap3_desc': 'مسار تدقيق كامل، قرارات ذكاء اصطناعي قابلة للتفسير، والامتثال التنظيمي الكامل للبنك المركزي المصري.',
        'cap4_title': 'مراقبة النموذج',
        'cap4_desc': 'تتبع أداء النموذج في الوقت الفعلي، كشف الانحراف، وخط إعادة تدريب تلقائي.',
        'cap5_title': 'قرارات فورية',
        'cap5_desc': 'تنبؤات بأقل من ثانية مع درجات احتمالية وتوصيات تفصيلية لموظفي القروض.',
        'cap6_title': 'إعادة تدريب تلقائية',
        'cap6_desc': 'خط MLOps مع إعادة تدريب تلقائية للنموذج عند انخفاض الأداء تحت العتبة المحددة.',
        'quickstart': 'دليل البدء السريع',
        'step1': 'تقييم المخاطر',
        'step1_desc': 'انتقل إلى صفحة تقييم المخاطر',
        'step2': 'إدخال البيانات',
        'step2_desc': 'أدخل معلومات العميل في النموذج',
        'step3': 'الحصول على القرار',
        'step3_desc': 'احصل على تنبؤ فوري بالذكاء الاصطناعي',
        'step4': 'عرض التحليلات',
        'step4_desc': 'استكشف رؤى المحفظة',
        'tech_stack': 'التقنيات المستخدمة',
        'performance': 'مقاييس الأداء',
        'test_accuracy': 'دقة الاختبار',
        'precision': 'الدقة',
        'recall': 'الاستدعاء',
        'f1_score': 'F1-Score',
        'false_negatives': 'سلبيات كاذبة',
        'training_time': 'وقت التدريب',
        'footer_title': 'منصة الذكاء الاصطناعي لتقييم مخاطر الائتمان',
        'footer_bank': 'البنك الأهلي المصري',
        'footer_rights': '© 2026 البنك الأهلي المصري',
        'footer_dev': 'تطوير',
        'footer_version': 'الإصدار 3.0',
    },
    'en': {
        'title': 'Credit Risk Intelligence Platform',
        'subtitle': 'National Bank of Egypt',
        'description': 'AI-powered credit risk assessment platform with Random Forest model achieving 76.5% accuracy, fully compliant with Central Bank of Egypt regulations',
        'badge_cbe': 'CBE Compliant',
        'badge_ai': 'AI Powered',
        'badge_realtime': 'Real-time',
        'badge_secure': 'Secure',
        'badge_features': '73 Features',
        'badge_trees': '100 Trees',
        'metric1': 'Model Accuracy',
        'metric2': 'Features',
        'metric3': 'Training Data',
        'metric4': 'Decision Trees',
        'capabilities': 'Platform Capabilities',
        'cap1_title': 'Smart Assessment',
        'cap1_desc': 'Real-time credit risk evaluation using Random Forest with 73 engineered features. Results in under 2 seconds.',
        'cap2_title': 'Portfolio Analytics',
        'cap2_desc': 'Comprehensive portfolio insights, trend analysis, and performance metrics in interactive dashboards.',
        'cap3_title': 'CBE Compliant',
        'cap3_desc': 'Full audit trail, explainable AI decisions, and complete regulatory compliance with Central Bank of Egypt.',
        'cap4_title': 'Model Monitoring',
        'cap4_desc': 'Real-time model performance tracking, drift detection, and automated retraining pipeline.',
        'cap5_title': 'Instant Decisions',
        'cap5_desc': 'Sub-second predictions with probability scores and detailed recommendations for loan officers.',
        'cap6_title': 'Auto Retraining',
        'cap6_desc': 'MLOps pipeline with automated model retraining when performance degrades below threshold.',
        'quickstart': 'Quick Start Guide',
        'step1': 'Risk Assessment',
        'step1_desc': 'Go to Risk Assessment page',
        'step2': 'Fill Details',
        'step2_desc': 'Enter customer information',
        'step3': 'Get Decision',
        'step3_desc': 'Get instant AI prediction',
        'step4': 'View Analytics',
        'step4_desc': 'Explore portfolio insights',
        'tech_stack': 'Technology Stack',
        'performance': 'Performance Metrics',
        'test_accuracy': 'Test Accuracy',
        'precision': 'Precision',
        'recall': 'Recall',
        'f1_score': 'F1-Score',
        'false_negatives': 'False Negatives',
        'training_time': 'Training Time',
        'footer_title': 'NBE Credit Risk Intelligence',
        'footer_bank': 'National Bank of Egypt',
        'footer_rights': '© 2026 National Bank of Egypt',
        'footer_dev': 'Developed by',
        'footer_version': 'Version 3.0',
    }
}

lang = st.session_state.language
t = TRANSLATIONS[lang]

# ============================================================
# CSS - Professional NBE Banking Theme
# ============================================================
direction = 'rtl' if lang == 'ar' else 'ltr'
text_align = 'right' if lang == 'ar' else 'left'

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Cairo:wght@400;600;700;800&display=swap');

/* ========== Root Variables - NBE Colors ========== */
:root {{
    --nbe-dark-green:  #004d34;
    --nbe-green:       #006341;
    --nbe-light-green: #008a57;
    --nbe-gold:        #D4AF37;
    --nbe-cream:       #f9f6f0;
    --nbe-white:       #ffffff;
    --nbe-text-dark:   #1a1a1a;
    --nbe-gray:        #666666;
}}

/* ========== Global Styles ========== */
html, body, [class*="css"] {{
    font-family: 'Cairo', sans-serif;
    background-color: var(--nbe-cream) !important;
    color: var(--nbe-text-dark) !important;
    direction: {direction};
}}

/* Hide Streamlit branding */
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 0 2rem 2rem !important; }}

/* ========== Sidebar ========== */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #004d34 0%, #006341 100%) !important;
    border-{text_align}: 2px solid var(--nbe-gold);
}}
[data-testid="stSidebar"] * {{ color: var(--nbe-white) !important; }}
[data-testid="stSidebar"] .stRadio label {{
    background: rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 10px 14px;
    margin: 5px 0;
    transition: all 0.3s;
    font-weight: 600;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: rgba(212,175,55,0.25);
    border-{text_align}: 3px solid var(--nbe-gold);
    transform: translateX({'-5px' if lang == 'ar' else '5px'});
}}

/* ========== Metrics ========== */
[data-testid="stMetricValue"] {{
    color: var(--nbe-dark-green) !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
}}
[data-testid="stMetricLabel"] {{
    color: var(--nbe-gray) !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}}
[data-testid="stMetricDelta"] {{
    color: var(--nbe-green) !important;
    font-weight: 700 !important;
}}

/* ========== Buttons ========== */
.stButton > button {{
    background: linear-gradient(135deg, var(--nbe-gold), #b8962e) !important;
    color: var(--nbe-dark-green) !important;
    font-weight: 700 !important;
    font-family: 'Cairo', sans-serif !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 32px !important;
    font-size: 16px !important;
    transition: all 0.3s !important;
    box-shadow: 0 6px 20px rgba(212,175,55,0.4) !important;
}}
.stButton > button:hover {{
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 30px rgba(212,175,55,0.6) !important;
}}

/* ========== Divider ========== */
hr {{ 
    border-color: rgba(0,99,65,0.2) !important;
    margin: 2rem 0 !important;
}}

/* ========== Banner ========== */
.banner-container {{
    width: 100%;
    max-width: 1200px;
    margin: 20px auto 30px;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 15px 50px rgba(0,77,52,0.25);
}}
.banner-img {{
    width: 100%;
    height: auto;
    display: block;
}}

/* ========== Language Toggle ========== */
.language-toggle {{
    position: fixed;
    top: 20px;
    {text_align}: 20px;
    z-index: 999;
    background: var(--nbe-white);
    border: 2px solid var(--nbe-gold);
    border-radius: 10px;
    padding: 8px 16px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}}
</style>
""", unsafe_allow_html=True)

# ============================================================
# Language Toggle Button (Top Right/Left)
# ============================================================
col_lang1, col_lang2, col_lang3 = st.columns([6, 1, 1])
with col_lang2:
    if st.button("🇪🇬 عربي", use_container_width=True):
        st.session_state.language = 'ar'
        st.rerun()
with col_lang3:
    if st.button("🇬🇧 EN", use_container_width=True):
        st.session_state.language = 'en'
        st.rerun()

# ============================================================
# BANNER IMAGE (Full Width, Proper Size)
# ============================================================
if banner_b64:
    st.markdown(f"""
    <div class="banner-container">
        <img src="data:image/png;base64,{banner_b64}" class="banner-img" alt="NBE Banner">
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, var(--nbe-white) 0%, var(--nbe-cream) 100%);
    border: 2px solid var(--nbe-gold);
    border-radius: 20px;
    padding: 50px 45px;
    margin: 0 0 35px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,99,65,0.15);
    text-align: {text_align};
">
    <!-- Decorative Elements -->
    <div style="
        position: absolute; top: -60px; {'right' if lang == 'ar' else 'left'}: -60px;
        width: 250px; height: 250px;
        border-radius: 50%;
        border: 3px solid rgba(0,99,65,0.08);
    "></div>
    <div style="
        position: absolute; bottom: -40px; {'left' if lang == 'ar' else 'right'}: -40px;
        width: 180px; height: 180px;
        border-radius: 50%;
        border: 3px solid rgba(212,175,55,0.15);
    "></div>

    <!-- Title Section -->
    <div style="margin-bottom: 20px;">
        <div style="
            font-family: 'Cairo', sans-serif;
            font-size: 14px;
            color: var(--nbe-gold);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 8px;
            font-weight: 700;
        ">{t['subtitle']}</div>
        <div style="
            font-family: 'Playfair Display', serif;
            font-size: 48px;
            font-weight: 900;
            color: var(--nbe-dark-green);
            line-height: 1.2;
            margin-bottom: 20px;
        ">{t['title']}</div>
    </div>

    <!-- Description -->
    <p style="
        color: var(--nbe-gray);
        font-size: 18px;
        max-width: 850px;
        line-height: 1.9;
        margin: 0 {'auto 0 0' if lang == 'ar' else '0 0 auto'} 30px;
        font-weight: 500;
    ">
        {t['description']}
    </p>

    <!-- Badges -->
    <div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: {'flex-start' if lang == 'ar' else 'flex-start'};">
        <span style="background:rgba(0,99,65,0.1); border:2px solid rgba(0,99,65,0.3);
              color:var(--nbe-dark-green); padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            ✅ {t['badge_cbe']}
        </span>
        <span style="background:rgba(74,222,128,0.15); border:2px solid rgba(74,222,128,0.4);
              color:#15803d; padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            🤖 {t['badge_ai']}
        </span>
        <span style="background:rgba(59,130,246,0.15); border:2px solid rgba(59,130,246,0.4);
              color:#1d4ed8; padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            ⚡ {t['badge_realtime']}
        </span>
        <span style="background:rgba(168,85,247,0.15); border:2px solid rgba(168,85,247,0.4);
              color:#7c3aed; padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            🔒 {t['badge_secure']}
        </span>
        <span style="background:rgba(212,175,55,0.15); border:2px solid rgba(212,175,55,0.5);
              color:#92400e; padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            📊 {t['badge_features']}
        </span>
        <span style="background:rgba(236,72,153,0.15); border:2px solid rgba(236,72,153,0.4);
              color:#be185d; padding:8px 18px; border-radius:25px; font-size:14px; font-weight:700;">
            🌲 {t['badge_trees']}
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# METRICS ROW
# ============================================================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(t['metric1'], "76.5%", "+2.3%")
with col2:
    st.metric(t['metric2'], "73", t['metric2'])
with col3:
    st.metric(t['metric3'], "800", t['metric3'])
with col4:
    st.metric(t['metric4'], "100", "Random Forest")

st.markdown("---")

# ============================================================
# CAPABILITIES CARDS
# ============================================================
st.markdown(f"""
<h2 style="color:var(--nbe-dark-green); font-family:'Playfair Display',serif;
    font-size:32px; margin-bottom:25px; text-align:{text_align}; font-weight:900;">
    🎯 {t['capabilities']}
</h2>
""", unsafe_allow_html=True)

cards = [
    ("🎯", t['cap1_title'], t['cap1_desc'], "#D4AF37"),
    ("📊", t['cap2_title'], t['cap2_desc'], "#15803d"),
    ("🔒", t['cap3_title'], t['cap3_desc'], "#1d4ed8"),
    ("📈", t['cap4_title'], t['cap4_desc'], "#7c3aed"),
    ("⚡", t['cap5_title'], t['cap5_desc'], "#ea580c"),
    ("🔄", t['cap6_title'], t['cap6_desc'], "#be185d"),
]

c1, c2, c3 = st.columns(3)
cols = [c1, c2, c3]
for i, (icon, title, desc, color) in enumerate(cards):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="
            background: var(--nbe-white);
            border: 2px solid rgba(0,99,65,0.1);
            border-top: 5px solid {color};
            border-radius: 18px;
            padding: 28px;
            margin-bottom: 20px;
            transition: all 0.3s;
            box-shadow: 0 6px 25px rgba(0,0,0,0.08);
            height: 100%;
            text-align: {text_align};
        " onmouseover="this.style.transform='translateY(-8px)';this.style.boxShadow='0 12px 40px rgba(0,99,65,0.2)';"
           onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 6px 25px rgba(0,0,0,0.08)';">
            <div style="font-size:48px; margin-bottom:16px;">{icon}</div>
            <h3 style="color:{color}; font-size:20px; margin:0 0 14px;
                font-family:'Cairo',sans-serif; font-weight:800;">{title}</h3>
            <p style="color:var(--nbe-gray); font-size:15px;
                line-height:1.8; margin:0; font-weight:500;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# QUICK START GUIDE
# ============================================================
st.markdown(f"""
<h2 style="color:var(--nbe-dark-green); font-family:'Playfair Display',serif;
    font-size:32px; margin-bottom:25px; text-align:{text_align}; font-weight:900;">
    🚀 {t['quickstart']}
</h2>
""", unsafe_allow_html=True)

steps = [
    ("01", "🎯", t['step1'], t['step1_desc']),
    ("02", "📋", t['step2'], t['step2_desc']),
    ("03", "🔍", t['step3'], t['step3_desc']),
    ("04", "📊", t['step4'], t['step4_desc']),
]
s1, s2, s3, s4 = st.columns(4)
for col, (num, icon, title, desc) in zip([s1,s2,s3,s4], steps):
    with col:
        st.markdown(f"""
        <div style="
            background: var(--nbe-white);
            border: 2px solid rgba(0,99,65,0.15);
            border-radius: 18px;
            padding: 28px 20px;
            text-align: center;
            height: 100%;
            transition: all 0.3s;
            box-shadow: 0 6px 25px rgba(0,0,0,0.08);
        " onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='var(--nbe-gold)';"
           onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(0,99,65,0.15)';">
            <div style="
                width:70px; height:70px;
                background: linear-gradient(135deg, var(--nbe-gold), #b8962e);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                font-size: 24px; font-weight: 800;
                color: var(--nbe-white);
                margin: 0 auto 18px;
                font-family: 'Cairo', sans-serif;
                box-shadow: 0 8px 25px rgba(212,175,55,0.4);
            ">{num}</div>
            <div style="font-size:40px; margin-bottom:12px;">{icon}</div>
            <h4 style="color:var(--nbe-dark-green); font-size:17px; margin:0 0 12px;
                font-family:'Cairo',sans-serif; font-weight:800;">{title}</h4>
            <p style="color:var(--nbe-gray); font-size:14px;
                margin:0; line-height:1.7; font-weight:500;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# TECH & PERFORMANCE SECTION
# ============================================================
c1, c2 = st.columns(2)

with c1:
    st.markdown(f"""
    <div style="background:var(--nbe-white);border:2px solid rgba(0,99,65,0.1);
        border-radius:18px;padding:32px;height:100%;text-align:{text_align};">
        <h3 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
            font-size:26px;margin-bottom:24px;font-weight:900;">{t['tech_stack']}</h3>
    """, unsafe_allow_html=True)

    techs = [
        ("🐍", "Python 3.11",     "#15803d"),
        ("🌊", "Streamlit",       "#1d4ed8"),
        ("🤖", "scikit-learn",    "#D4AF37"),
        ("📊", "Plotly",          "#7c3aed"),
        ("🐼", "Pandas",          "#ea580c"),
        ("🔢", "NumPy",           "#be185d"),
    ]
    for icon, name, color in techs:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:16px;
            padding:14px 18px;border-radius:12px;
            background:rgba(0,99,65,0.03);
            border:2px solid rgba(0,99,65,0.08);
            margin-bottom:12px;">
            <span style="font-size:28px;">{icon}</span>
            <span style="color:{color};font-weight:700;font-size:16px;">{name}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div style="background:var(--nbe-white);border:2px solid rgba(0,99,65,0.1);
        border-radius:18px;padding:32px;height:100%;text-align:{text_align};">
        <h3 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
            font-size:26px;margin-bottom:24px;font-weight:900;">{t['performance']}</h3>
    """, unsafe_allow_html=True)

    stats = [
        (t['test_accuracy'],     "76.50%",   "#D4AF37"),
        (t['precision'],         "64.4%",    "#15803d"),
        (t['recall'],            "48.3%",    "#1d4ed8"),
        (t['f1_score'],          "55.2%",    "#7c3aed"),
        (t['false_negatives'],   "31",       "#dc2626"),
        (t['training_time'],     "< 1 min",  "#ea580c"),
    ]
    for label, value, color in stats:
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
            padding:14px 18px;border-radius:12px;
            background:rgba(0,99,65,0.03);
            border:2px solid rgba(0,99,65,0.08);
            margin-bottom:12px;">
            <span style="color:var(--nbe-gray);font-size:15px;font-weight:600;">{label}</span>
            <span style="color:{color};font-weight:800;font-size:17px;">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown(f"""
<div style="
    background: linear-gradient(135deg, var(--nbe-dark-green), var(--nbe-green));
    border: 2px solid var(--nbe-gold);
    border-radius: 20px;
    padding: 40px 45px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 28px;
    box-shadow: 0 15px 50px rgba(0,77,52,0.25);
    text-align: {text_align};
">
    <div>
        <div style="color:var(--nbe-gold); font-weight:800; font-size:20px;
            font-family:'Cairo',sans-serif; margin-bottom:10px;">
            🏦 {t['footer_title']}
        </div>
        <div style="color:rgba(255,255,255,0.85); font-size:15px; line-height:1.8; font-weight:500;">
            {t['footer_bank']}<br>
            {t['footer_rights']}<br>
            {t['footer_dev']} <strong style="color:var(--nbe-gold);">ENG. Goda Emad</strong> | {t['footer_version']}
        </div>
    </div>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
        <a href="https://www.linkedin.com/in/goda-emad/"
           target="_blank" style="
            background: rgba(10,102,194,0.25);
            border: 2px solid rgba(10,102,194,0.6);
            color: #60a5fa;
            padding: 12px 24px;
            border-radius: 12px;
            text-decoration: none;
            font-size: 15px;
            font-weight: 700;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
            display: inline-block;
        " onmouseover="this.style.background='rgba(10,102,194,0.4)';this.style.transform='translateY(-3px)';"
           onmouseout="this.style.background='rgba(10,102,194,0.25)';this.style.transform='translateY(0)';">
           🔗 LinkedIn - ENG.Goda Emad
        </a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
           target="_blank" style="
            background: rgba(255,255,255,0.15);
            border: 2px solid rgba(255,255,255,0.3);
            color: var(--nbe-white);
            padding: 12px 24px;
            border-radius: 12px;
            text-decoration: none;
            font-size: 15px;
            font-weight: 700;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
            display: inline-block;
        " onmouseover="this.style.background='rgba(255,255,255,0.25)';this.style.transform='translateY(-3px)';"
           onmouseout="this.style.background='rgba(255,255,255,0.15)';this.style.transform='translateY(0)';">
           ⭐ GitHub Project
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

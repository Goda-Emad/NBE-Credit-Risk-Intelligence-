"""
NBE Credit Risk Intelligence - Home Page (Enhanced v4.0)
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

if 'language' not in st.session_state:
    st.session_state.language = 'ar'

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

possible_paths = [
    Path(__file__).parent.parent / "assets" / "images" / "banner.png",
    Path("assets") / "images" / "banner.png",
]
banner_b64 = None
for p in possible_paths:
    if p.exists():
        banner_b64 = get_image_base64(p)
        break

TRANSLATIONS = {
    'ar': {
        'lang_label': 'اللغة',
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
        'metric2': 'الميزات المهندسة',
        'metric3': 'بيانات التدريب',
        'metric4': 'أشجار القرار',
        'capabilities': 'قدرات المنصة',
        'cap1_title': 'تقييم ذكي',
        'cap1_desc': 'تقييم فوري لمخاطر الائتمان باستخدام Random Forest مع 73 ميزة هندسية. النتائج في أقل من ثانيتين.',
        'cap2_title': 'تحليلات المحفظة',
        'cap2_desc': 'رؤى شاملة للمحفظة، تحليل الاتجاهات، ومقاييس الأداء في لوحات تحكم تفاعلية.',
        'cap3_title': 'متوافق مع البنك المركزي',
        'cap3_desc': 'مسار تدقيق كامل، قرارات ذكاء اصطناعي قابلة للتفسير، والامتثال التنظيمي الكامل.',
        'cap4_title': 'مراقبة النموذج',
        'cap4_desc': 'تتبع أداء النموذج في الوقت الفعلي، كشف الانحراف، وإعادة تدريب تلقائية.',
        'cap5_title': 'قرارات فورية',
        'cap5_desc': 'تنبؤات بأقل من ثانية مع درجات احتمالية وتوصيات تفصيلية.',
        'cap6_title': 'إعادة تدريب تلقائية',
        'cap6_desc': 'خط MLOps مع إعادة تدريب تلقائية عند انخفاض الأداء.',
        'quickstart': 'دليل البدء السريع',
        'step1': 'تقييم المخاطر',
        'step1_desc': 'انتقل إلى صفحة تقييم المخاطر من القائمة الجانبية',
        'step2': 'إدخال البيانات',
        'step2_desc': 'أدخل معلومات العميل في النماذج التفاعلية',
        'step3': 'الحصول على القرار',
        'step3_desc': 'احصل على تنبؤ فوري مع شرح مفصل للأسباب',
        'step4': 'عرض التحليلات',
        'step4_desc': 'استكشف رؤى المحفظة والتقارير التفصيلية',
        'tech_stack': 'التقنيات المستخدمة',
        'performance': 'مقاييس الأداء',
        'test_accuracy': 'دقة الاختبار',
        'precision': 'الدقة',
        'recall': 'الاستدعاء',
        'f1_score': 'F1-Score',
        'false_negatives': 'سلبيات كاذبة',
        'training_time': 'وقت التدريب',
        'footer_title': 'منصة تقييم مخاطر الائتمان',
        'footer_bank': 'البنك الأهلي المصري',
        'footer_rights': '© 2026 البنك الأهلي المصري. جميع الحقوق محفوظة.',
        'footer_dev': 'تطوير',
        'footer_version': 'الإصدار 4.0',
        'footer_contact': 'تواصل معنا',
    },
    'en': {
        'lang_label': 'Language',
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
        'metric2': 'Engineered Features',
        'metric3': 'Training Samples',
        'metric4': 'Decision Trees',
        'capabilities': 'Platform Capabilities',
        'cap1_title': 'Smart Assessment',
        'cap1_desc': 'Real-time credit risk evaluation using Random Forest with 73 engineered features. Results in under 2 seconds.',
        'cap2_title': 'Portfolio Analytics',
        'cap2_desc': 'Comprehensive portfolio insights, trend analysis, and performance metrics in interactive dashboards.',
        'cap3_title': 'CBE Compliant',
        'cap3_desc': 'Full audit trail, explainable AI decisions, and complete regulatory compliance.',
        'cap4_title': 'Model Monitoring',
        'cap4_desc': 'Real-time model performance tracking, drift detection, and automated retraining.',
        'cap5_title': 'Instant Decisions',
        'cap5_desc': 'Sub-second predictions with probability scores and detailed recommendations.',
        'cap6_title': 'Auto Retraining',
        'cap6_desc': 'MLOps pipeline with automated model retraining when performance degrades.',
        'quickstart': 'Quick Start Guide',
        'step1': 'Risk Assessment',
        'step1_desc': 'Navigate to Risk Assessment page from the sidebar',
        'step2': 'Fill Details',
        'step2_desc': 'Enter customer information in interactive forms',
        'step3': 'Get Decision',
        'step3_desc': 'Get instant AI prediction with detailed explanation',
        'step4': 'View Analytics',
        'step4_desc': 'Explore portfolio insights and detailed reports',
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
        'footer_rights': '© 2026 National Bank of Egypt. All rights reserved.',
        'footer_dev': 'Developed by',
        'footer_version': 'Version 4.0',
        'footer_contact': 'Contact Us',
    }
}

lang = st.session_state.language
t    = TRANSLATIONS[lang]
direction  = 'rtl' if lang == 'ar' else 'ltr'
text_align = 'right' if lang == 'ar' else 'left'

# ── PARTICLES (static, no random import needed) ──────────────
PARTICLES = [
    (5,  53, 86, 7.4, 0.1, 0.05),
    (4,  18, 33, 6.5, 0.5, 0.10),
    (5,  47, 65, 6.4, 3.4, 0.08),
    (7,  51, 22, 7.6, 3.2, 0.09),
    (5,  32, 32, 7.3, 3.7, 0.06),
    (8,  45, 39, 7.2, 0.1, 0.11),
    (6,  46, 64, 4.5, 3.9, 0.09),
    (9,  90, 94, 5.6, 3.6, 0.10),
    (9,  42, 62, 4.7, 2.9, 0.05),
    (9,  72, 15, 4.8, 2.7, 0.09),
    (9,  67, 48, 6.9, 1.3, 0.09),
    (4,  17, 69, 5.0, 2.0, 0.10),
]

particles_html = ""
for size, top, left, dur, delay, opacity in PARTICLES:
    particles_html += f"""
    <div style="position:absolute;width:{size}px;height:{size}px;border-radius:50%;
        background:radial-gradient(circle,rgba(201,168,76,{opacity*3:.2f}) 0%,transparent 70%);
        border:1px solid rgba(201,168,76,{opacity:.2f});
        top:{top}%;left:{left}%;
        animation:floatParticle {dur}s ease-in-out {delay}s infinite;
        pointer-events:none;"></div>"""

# ── CSS ───────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap');

:root {{
    --nbe-dark-green:  #003d2a;
    --nbe-green:       #005a3c;
    --nbe-mid-green:   #006341;
    --nbe-gold:        #C9A84C;
    --nbe-gold-light:  #E8C97A;
    --nbe-cream:       #f8f5ef;
    --nbe-white:       #ffffff;
    --nbe-text-dark:   #1a1a1a;
    --nbe-gray:        #5a6474;
    --nbe-border:      rgba(0,99,65,0.12);
    --shadow:          0 8px 32px rgba(0,61,42,0.14);
    --shadow-lg:       0 20px 60px rgba(0,61,42,0.2);
}}

html, body, [class*="css"] {{
    font-family: 'Cairo', sans-serif;
    background-color: var(--nbe-cream) !important;
    color: var(--nbe-text-dark) !important;
    direction: {direction};
}}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ padding: 0 2rem 3rem !important; max-width:1400px; }}

/* SIDEBAR — language selector only */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg,#002a1d 0%,#003d2a 40%,#005a3c 100%) !important;
}}
[data-testid="stSidebar"]::before {{
    content:''; position:absolute; top:0;left:0;right:0;
    height:4px;
    background:linear-gradient(90deg,var(--nbe-gold),var(--nbe-gold-light),var(--nbe-gold));
}}
[data-testid="stSidebar"] * {{ color:rgba(255,255,255,0.92) !important; }}
[data-testid="stSidebar"] .stSelectbox > div > div {{
    background:rgba(255,255,255,0.1) !important;
    border:1px solid rgba(201,168,76,0.4) !important;
    border-radius:10px !important;
}}

/* METRICS */
[data-testid="stMetricValue"] {{
    color:var(--nbe-dark-green) !important;
    font-size:2.4rem !important;
    font-weight:900 !important;
    font-family:'JetBrains Mono',monospace !important;
    animation:countAnim 0.7s cubic-bezier(0.34,1.56,0.64,1) forwards;
}}
[data-testid="stMetricLabel"] {{
    color:var(--nbe-gray) !important;
    font-weight:700 !important;
    font-size:13px !important;
    text-transform:uppercase;
    letter-spacing:0.5px;
}}
[data-testid="metric-container"] {{
    background:var(--nbe-white) !important;
    border:1px solid var(--nbe-border) !important;
    border-top:4px solid var(--nbe-gold) !important;
    border-radius:16px !important;
    padding:20px 24px !important;
    box-shadow:var(--shadow) !important;
    transition:transform 0.3s ease,box-shadow 0.3s ease !important;
}}
[data-testid="metric-container"]:hover {{
    transform:translateY(-6px) !important;
    box-shadow:var(--shadow-lg) !important;
}}

/* ANIMATIONS */
@keyframes countAnim {{
    from {{ opacity:0; transform:scale(0.5) translateY(20px); }}
    to   {{ opacity:1; transform:scale(1) translateY(0); }}
}}
@keyframes gradientShift {{
    0%   {{ background-position:0% 50%; }}
    50%  {{ background-position:100% 50%; }}
    100% {{ background-position:0% 50%; }}
}}
@keyframes floatParticle {{
    0%,100% {{ transform:translateY(0) rotate(0deg);   opacity:0.6; }}
    33%      {{ transform:translateY(-20px) rotate(120deg); opacity:1; }}
    66%      {{ transform:translateY(-10px) rotate(240deg); opacity:0.8; }}
}}
@keyframes slideInLeft {{
    from {{ opacity:0; transform:translateX(-40px); }}
    to   {{ opacity:1; transform:translateX(0); }}
}}
@keyframes fadeInUp {{
    from {{ opacity:0; transform:translateY(30px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
@keyframes shimmer {{
    0%   {{ background-position:-200% center; }}
    100% {{ background-position:200% center; }}
}}
@keyframes pulseGlow {{
    0%,100% {{ box-shadow:0 0 20px rgba(201,168,76,0.3); }}
    50%      {{ box-shadow:0 0 40px rgba(201,168,76,0.6); }}
}}
@keyframes fillBar {{
    from {{ width:0%; }}
    to   {{ width:var(--w); }}
}}
@keyframes blink {{
    0%,100% {{ opacity:1; }}
    50%      {{ opacity:0.3; }}
}}

/* CAPABILITY CARDS */
.cap-card {{
    background:var(--nbe-white);
    border-radius:20px;
    padding:32px 28px;
    margin-bottom:24px;
    box-shadow:var(--shadow);
    border:1px solid var(--nbe-border);
    transition:all 0.35s cubic-bezier(0.34,1.56,0.64,1);
    position:relative; overflow:hidden;
    text-align:{text_align};
    animation:fadeInUp 0.6s ease backwards;
}}
.cap-card:hover {{
    transform:translateY(-10px) scale(1.02);
    box-shadow:0 24px 60px rgba(0,61,42,0.18);
}}
.cap-icon-circle {{
    width:70px; height:70px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:30px; margin-bottom:18px;
    transition:all 0.3s ease;
}}
.cap-card:hover .cap-icon-circle {{
    transform:rotate(10deg) scale(1.1);
    animation:pulseGlow 2s ease infinite;
}}

/* TIMELINE */
.timeline-step {{
    display:flex; align-items:flex-start; gap:20px;
    padding:0 0 32px 0; position:relative; z-index:1;
    flex-direction:{'row-reverse' if lang=='ar' else 'row'};
    animation:fadeInUp 0.6s ease backwards;
}}
.timeline-badge {{
    width:72px; height:72px; min-width:72px;
    border-radius:50%;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    border:3px solid var(--nbe-white);
    transition:all 0.3s ease;
}}
.timeline-step:hover .timeline-badge {{ transform:scale(1.12); }}
.timeline-content {{
    background:var(--nbe-white);
    border:1px solid var(--nbe-border);
    border-radius:16px; padding:20px 24px; flex:1;
    box-shadow:var(--shadow);
    transition:all 0.3s ease;
    text-align:{text_align};
}}
.timeline-step:hover .timeline-content {{
    border-color:var(--nbe-gold);
    box-shadow:0 12px 35px rgba(0,61,42,0.15);
}}

/* BADGE SHIMMER */
.badge-shimmer {{
    background:linear-gradient(90deg,rgba(255,255,255,0) 0%,rgba(255,255,255,0.4) 50%,rgba(255,255,255,0) 100%);
    background-size:200% auto;
    animation:shimmer 3s linear infinite;
    position:absolute; inset:0; border-radius:inherit;
    pointer-events:none;
}}

/* SECTION HEADER */
.sec-header {{
    display:flex; align-items:center; gap:14px;
    margin-bottom:28px;
    flex-direction:{'row-reverse' if lang=='ar' else 'row'};
    animation:slideInLeft 0.6s ease;
}}
.sec-line {{
    flex:1; height:2px;
    background:linear-gradient({'to left' if lang=='ar' else 'to right'},var(--nbe-gold),transparent);
}}
.sec-line-rev {{
    flex:1; height:2px;
    background:linear-gradient({'to right' if lang=='ar' else 'to left'},var(--nbe-gold),transparent);
}}

hr {{ border-color:var(--nbe-border) !important; margin:2.5rem 0 !important; }}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR — Language only ───────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding:24px 16px 20px; text-align:center;
        border-bottom:1px solid rgba(201,168,76,0.25); margin-bottom:20px;">
        <div style="font-size:40px; margin-bottom:10px;">🏦</div>
        <div style="font-size:15px; font-weight:800; color:var(--nbe-gold-light) !important;
            font-family:'Cairo',sans-serif;">NBE Credit Risk</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.55) !important;
            margin-top:4px; font-weight:500;">
            {'البنك الأهلي المصري' if lang=='ar' else 'National Bank of Egypt'}
        </div>
    </div>
    """, unsafe_allow_html=True)

    lang_options = {{'ar': '🇪🇬 العربية', 'en': '🇬🇧 English'}}
    selected = st.selectbox(
        t['lang_label'],
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=0 if st.session_state.language == 'ar' else 1,
        key='lang_selector'
    )
    if selected != st.session_state.language:
        st.session_state.language = selected
        st.rerun()

    # Status indicator
    st.markdown(f"""
    <div style="margin-top:28px; border-top:1px solid rgba(201,168,76,0.2); padding-top:20px;">
        <div style="background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.3);
            border-radius:10px; padding:12px 14px; margin-bottom:8px;">
            <span style="display:inline-block; width:10px; height:10px; border-radius:50%;
                background:#22c55e; animation:blink 2s ease infinite;
                box-shadow:0 0 8px rgba(34,197,94,0.6);
                margin-{'left' if lang=='ar' else 'right'}:8px; vertical-align:middle;"></span>
            <span style="font-size:13px; font-weight:600;">
                {'النموذج نشط' if lang=='ar' else 'Model Active'}
            </span>
        </div>
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1);
            border-radius:10px; padding:10px 14px; font-size:12px;
            color:rgba(255,255,255,0.65) !important;">
            🎯 {'الدقة: 76.5%' if lang=='ar' else 'Accuracy: 76.5%'} &nbsp;|&nbsp; v4.0
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── BANNER ────────────────────────────────────────────────────
if banner_b64:
    st.markdown(f"""
    <div style="width:100%; border-radius:16px; overflow:hidden;
        box-shadow:var(--shadow-lg); margin:20px 0 30px;">
        <img src="data:image/png;base64,{banner_b64}"
             style="width:100%; height:auto; display:block;" alt="NBE Banner">
    </div>
    """, unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
badges_data = [
    ('badge_cbe',      'rgba(0,99,65,0.12)',    'rgba(0,99,65,0.4)',     '#004d34', '✅'),
    ('badge_ai',       'rgba(74,222,128,0.12)', 'rgba(74,222,128,0.35)','#15803d', '🤖'),
    ('badge_realtime', 'rgba(59,130,246,0.12)', 'rgba(59,130,246,0.35)','#1d4ed8', '⚡'),
    ('badge_secure',   'rgba(168,85,247,0.12)', 'rgba(168,85,247,0.35)','#6d28d9', '🔒'),
    ('badge_features', 'rgba(201,168,76,0.15)', 'rgba(201,168,76,0.5)', '#7a5c0e', '📊'),
    ('badge_trees',    'rgba(236,72,153,0.12)', 'rgba(236,72,153,0.35)','#9d174d', '🌲'),
]
badges_html = ""
for key, bg, border, color, icon in badges_data:
    badges_html += f"""
    <span style="position:relative;overflow:hidden;
        background:{bg};border:1.5px solid {border};color:{color};
        padding:8px 18px;border-radius:25px;font-size:13px;font-weight:700;
        display:inline-flex;align-items:center;gap:6px;transition:all 0.3s ease;"
      onmouseover="this.style.transform='translateY(-3px) scale(1.05)';this.style.boxShadow='0 8px 20px {border}';"
      onmouseout="this.style.transform='translateY(0) scale(1)';this.style.boxShadow='none';">
        {icon} {t[key]}<span class="badge-shimmer"></span>
    </span>"""

st.markdown(f"""
<div style="
    background:linear-gradient(135deg,#002a1d 0%,#003d2a 25%,#004d34 50%,#005a3c 75%,#003d2a 100%);
    background-size:300% 300%;
    animation:gradientShift 8s ease infinite;
    border:1px solid rgba(201,168,76,0.3);
    border-radius:24px; padding:60px 52px;
    margin:0 0 32px; position:relative; overflow:hidden;
    box-shadow:var(--shadow-lg); text-align:{text_align};">
    {particles_html}
    <div style="position:absolute;top:-80px;right:-80px;width:280px;height:280px;
        border-radius:50%;border:1px solid rgba(201,168,76,0.08);"></div>
    <div style="position:absolute;top:-50px;right:-50px;width:200px;height:200px;
        border-radius:50%;border:1px solid rgba(201,168,76,0.05);"></div>
    <div style="position:absolute;bottom:-60px;left:-60px;width:220px;height:220px;
        border-radius:50%;border:1px solid rgba(0,138,87,0.1);"></div>
    <div style="position:absolute;top:0;{'right' if lang=='ar' else 'left'}:0;width:5px;height:100%;
        background:linear-gradient(180deg,var(--nbe-gold),var(--nbe-gold-light),var(--nbe-gold));
        border-radius:0 4px 4px 0;"></div>
    <div style="position:relative;z-index:2;animation:slideInLeft 0.8s ease;">
        <div style="font-size:12px;letter-spacing:4px;text-transform:uppercase;
            color:var(--nbe-gold-light);font-weight:700;margin-bottom:10px;
            font-family:'JetBrains Mono',monospace;">{t['subtitle']}</div>
        <h1 style="font-family:'Playfair Display',serif;
            font-size:clamp(32px,4vw,56px);font-weight:900;color:#fff;
            line-height:1.15;margin:0 0 22px;
            text-shadow:0 2px 20px rgba(0,0,0,0.3);">{t['title']}</h1>
        <p style="color:rgba(255,255,255,0.8);font-size:17px;max-width:820px;
            line-height:2;margin:0 0 36px;font-weight:400;">{t['description']}</p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;">{badges_html}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── METRICS ───────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
for col, label, value, delta in [
    (col1, t['metric1'], "76.5%", "↑ +2.3%"),
    (col2, t['metric2'], "73",    "engineered"),
    (col3, t['metric3'], "800",   "samples"),
    (col4, t['metric4'], "100",   "RF trees"),
]:
    with col:
        st.metric(label, value, delta)

st.markdown("---")

# ── CAPABILITIES ──────────────────────────────────────────────
st.markdown(f"""
<div class="sec-header">
    <div class="sec-line"></div>
    <h2 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
        font-size:30px;margin:0;white-space:nowrap;font-weight:900;">
        🎯 {t['capabilities']}
    </h2>
    <div class="sec-line-rev"></div>
</div>""", unsafe_allow_html=True)

cards = [
    ("🎯",'cap1_title','cap1_desc',"#C9A84C","rgba(201,168,76,0.12)",0.1),
    ("📊",'cap2_title','cap2_desc',"#15803d","rgba(21,128,61,0.1)", 0.2),
    ("🔒",'cap3_title','cap3_desc',"#1d4ed8","rgba(29,78,216,0.1)", 0.3),
    ("📈",'cap4_title','cap4_desc',"#7c3aed","rgba(124,58,237,0.1)",0.15),
    ("⚡",'cap5_title','cap5_desc',"#ea580c","rgba(234,88,12,0.1)", 0.25),
    ("🔄",'cap6_title','cap6_desc',"#be185d","rgba(190,24,93,0.1)", 0.35),
]
c1, c2, c3 = st.columns(3)
for i, (icon, tk, dk, color, bg, delay) in enumerate(cards):
    with [c1,c2,c3][i%3]:
        st.markdown(f"""
        <div class="cap-card" style="animation-delay:{delay}s;border-top:4px solid {color};">
            <div class="cap-icon-circle" style="background:{bg};border:2px solid {color}20;">
                <span style="font-size:30px;">{icon}</span>
            </div>
            <h3 style="color:{color};font-size:18px;margin:0 0 12px;
                font-family:'Cairo',sans-serif;font-weight:800;">{t[tk]}</h3>
            <p style="color:var(--nbe-gray);font-size:14px;
                line-height:1.9;margin:0;font-weight:500;">{t[dk]}</p>
        </div>""", unsafe_allow_html=True)

st.markdown("---")

# ── TIMELINE QUICK START ──────────────────────────────────────
st.markdown(f"""
<div class="sec-header">
    <div class="sec-line"></div>
    <h2 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
        font-size:30px;margin:0;white-space:nowrap;font-weight:900;">
        🚀 {t['quickstart']}
    </h2>
    <div class="sec-line-rev"></div>
</div>""", unsafe_allow_html=True)

steps = [
    ("01","🎯",'step1','step1_desc',"#C9A84C",  "#8a6c00",0.0),
    ("02","📋",'step2','step2_desc',"#15803d",  "#0d5c2a",0.15),
    ("03","🔍",'step3','step3_desc',"#1d4ed8",  "#1640b0",0.3),
    ("04","📊",'step4','step4_desc',"#7c3aed",  "#5b28c0",0.45),
]
tl_col, _ = st.columns([3, 1])
with tl_col:
    for num, icon, tk, dk, color, color2, delay in steps:
        st.markdown(f"""
        <div class="timeline-step" style="animation-delay:{delay}s;">
            <div class="timeline-badge" style="
                background:linear-gradient(135deg,{color},{color2});
                box-shadow:0 8px 24px {color}55;">
                <span style="color:white;font-size:14px;font-weight:900;
                    font-family:'JetBrains Mono',monospace;">{num}</span>
                <span style="font-size:20px;margin-top:2px;">{icon}</span>
            </div>
            <div class="timeline-content">
                <h4 style="color:{color};font-size:17px;margin:0 0 8px;
                    font-family:'Cairo',sans-serif;font-weight:800;">{t[tk]}</h4>
                <p style="color:var(--nbe-gray);font-size:14px;
                    margin:0;line-height:1.8;font-weight:500;">{t[dk]}</p>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")

# ── TECH STACK & PERFORMANCE ──────────────────────────────────
st.markdown(f"""
<div class="sec-header" style="margin-bottom:20px;">
    <div class="sec-line"></div>
    <h2 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
        font-size:26px;margin:0;white-space:nowrap;font-weight:900;">
        ⚙️ {t['tech_stack']} &amp; {t['performance']}
    </h2>
    <div class="sec-line-rev"></div>
</div>""", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""
    <div style="background:var(--nbe-white);border:1px solid var(--nbe-border);
        border-radius:20px;padding:32px;box-shadow:var(--shadow);text-align:{text_align};">
        <h3 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
            font-size:22px;margin-bottom:22px;font-weight:900;">{t['tech_stack']}</h3>
    """, unsafe_allow_html=True)
    for icon, name, color, role in [
        ("🐍","Python 3.11", "#15803d","Core Language"),
        ("🌊","Streamlit",   "#1d4ed8","Web Framework"),
        ("🤖","scikit-learn","#C9A84C","ML Engine"),
        ("📊","Plotly",      "#7c3aed","Visualization"),
        ("🐼","Pandas",      "#ea580c","Data Processing"),
        ("🔢","NumPy",       "#be185d","Numerical Computing"),
    ]:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:14px;
            padding:13px 16px;border-radius:12px;
            background:rgba(0,99,65,0.03);border:1px solid var(--nbe-border);
            margin-bottom:10px;transition:all 0.3s ease;"
            onmouseover="this.style.background='rgba(0,99,65,0.07)';this.style.borderColor='{color}40';"
            onmouseout="this.style.background='rgba(0,99,65,0.03)';this.style.borderColor='var(--nbe-border)';">
            <span style="font-size:26px;min-width:30px;text-align:center;">{icon}</span>
            <div>
                <div style="color:{color};font-weight:800;font-size:15px;
                    font-family:'Cairo',sans-serif;">{name}</div>
                <div style="color:var(--nbe-gray);font-size:12px;">{role}</div>
            </div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div style="background:var(--nbe-white);border:1px solid var(--nbe-border);
        border-radius:20px;padding:32px;box-shadow:var(--shadow);text-align:{text_align};">
        <h3 style="color:var(--nbe-dark-green);font-family:'Playfair Display',serif;
            font-size:22px;margin-bottom:22px;font-weight:900;">{t['performance']}</h3>
    """, unsafe_allow_html=True)
    for lk, value, color, pct in [
        ('test_accuracy',  "76.5%",   "#C9A84C", 76.5),
        ('precision',      "64.4%",   "#15803d", 64.4),
        ('recall',         "48.3%",   "#1d4ed8", 48.3),
        ('f1_score',       "55.2%",   "#7c3aed", 55.2),
        ('false_negatives',"31 cases","#dc2626", 31),
        ('training_time',  "< 1 min", "#ea580c", 90),
    ]:
        st.markdown(f"""
        <div style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;
                align-items:center;margin-bottom:6px;">
                <span style="color:var(--nbe-gray);font-size:14px;font-weight:600;">{t[lk]}</span>
                <span style="color:{color};font-weight:800;font-size:15px;
                    font-family:'JetBrains Mono',monospace;">{value}</span>
            </div>
            <div style="height:8px;background:rgba(0,0,0,0.06);border-radius:4px;overflow:hidden;">
                <div style="height:8px;border-radius:4px;
                    width:{min(pct,100)}%;
                    background:linear-gradient(90deg,{color}99,{color});
                    animation:fillBar 1.2s ease forwards;
                    --w:{min(pct,100)}%;"></div>
            </div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("---")

footer_stats_html = ""
for val, lbl, color in [
    ("76.5%", t['test_accuracy'], "#C9A84C"),
    ("73",    t['metric2'],       "#15803d"),
    ("800",   t['metric3'],       "#1d4ed8"),
    ("100",   t['metric4'],       "#7c3aed"),
]:
    footer_stats_html += f"""
    <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(201,168,76,0.2);
        border-radius:12px;padding:16px 20px;text-align:center;min-width:100px;
        transition:all 0.3s ease;"
        onmouseover="this.style.background='rgba(201,168,76,0.12)';this.style.transform='translateY(-3px)';"
        onmouseout="this.style.background='rgba(255,255,255,0.08)';this.style.transform='translateY(0)';">
        <div style="font-size:24px;font-weight:900;color:{color};
            font-family:'JetBrains Mono',monospace;">{val}</div>
        <div style="font-size:11px;color:rgba(255,255,255,0.6);
            margin-top:4px;font-weight:600;text-transform:uppercase;">{lbl}</div>
    </div>"""

st.markdown(f"""
<div style="
    background:linear-gradient(135deg,#002a1d 0%,#003d2a 50%,#004d34 100%);
    border:1px solid rgba(201,168,76,0.3);border-radius:24px;
    padding:44px 48px;box-shadow:var(--shadow-lg);
    position:relative;overflow:hidden;text-align:{text_align};">
    <div style="position:absolute;top:0;left:0;right:0;height:3px;
        background:linear-gradient(90deg,var(--nbe-gold),var(--nbe-gold-light),var(--nbe-gold));"></div>
    <div style="display:flex;flex-wrap:wrap;justify-content:space-between;
        align-items:flex-start;gap:32px;margin-bottom:36px;">
        <div>
            <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;
                flex-direction:{'row-reverse' if lang=='ar' else 'row'};">
                <div style="width:52px;height:52px;
                    background:linear-gradient(135deg,var(--nbe-gold),#a07a1e);
                    border-radius:14px;display:flex;align-items:center;
                    justify-content:center;font-size:24px;
                    box-shadow:0 6px 16px rgba(201,168,76,0.4);">🏦</div>
                <div>
                    <div style="color:var(--nbe-gold-light);font-weight:800;font-size:18px;
                        font-family:'Cairo',sans-serif;">{t['footer_title']}</div>
                    <div style="color:rgba(255,255,255,0.6);font-size:12px;">
                        {t['footer_bank']}</div>
                </div>
            </div>
            <div style="color:rgba(255,255,255,0.5);font-size:13px;line-height:1.8;">
                {t['footer_rights']}<br>
                {t['footer_dev']} <strong style="color:var(--nbe-gold-light);">ENG. Goda Emad</strong>
                &nbsp;|&nbsp; {t['footer_version']}
            </div>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;
            align-items:{'flex-start' if lang=='ar' else 'flex-end'};">
            <div style="color:rgba(201,168,76,0.8);font-size:11px;text-transform:uppercase;
                letter-spacing:2px;font-weight:700;">{t['footer_contact']}</div>
            <a href="mailto:creditrisk@nbe.com.eg" style="
                background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);
                color:rgba(255,255,255,0.85) !important;padding:11px 22px;border-radius:12px;
                text-decoration:none;font-size:14px;font-weight:600;
                font-family:'Cairo',sans-serif;display:inline-block;"
                onmouseover="this.style.background='rgba(255,255,255,0.14)';"
                onmouseout="this.style.background='rgba(255,255,255,0.07)';">
                ✉️ creditrisk@nbe.com.eg
            </a>
            <a href="https://www.linkedin.com/in/goda-emad/" target="_blank" style="
                background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.5);
                color:#93c5fd !important;padding:11px 22px;border-radius:12px;
                text-decoration:none;font-size:14px;font-weight:600;
                font-family:'Cairo',sans-serif;display:inline-block;"
                onmouseover="this.style.background='rgba(10,102,194,0.35)';"
                onmouseout="this.style.background='rgba(10,102,194,0.2)';">
                🔗 LinkedIn — ENG. Goda Emad
            </a>
            <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
               target="_blank" style="
                background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);
                color:rgba(255,255,255,0.85) !important;padding:11px 22px;border-radius:12px;
                text-decoration:none;font-size:14px;font-weight:600;
                font-family:'Cairo',sans-serif;display:inline-block;"
                onmouseover="this.style.background='rgba(255,255,255,0.18)';"
                onmouseout="this.style.background='rgba(255,255,255,0.08)';">
                ⭐ GitHub Project
            </a>
        </div>
    </div>
    <div style="border-top:1px solid rgba(201,168,76,0.15);padding-top:28px;
        display:flex;flex-wrap:wrap;gap:12px;">
        {footer_stats_html}
    </div>
</div>
<div style="text-align:center;margin-top:16px;padding-bottom:8px;
    color:rgba(0,61,42,0.4);font-size:11px;">
    NBE Credit Risk Intelligence Platform v4.0 — Powered by AI 🤖
</div>
""", unsafe_allow_html=True)

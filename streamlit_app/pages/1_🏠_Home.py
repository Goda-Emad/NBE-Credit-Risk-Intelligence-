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
    particles_html += (
        f'<div style="position:absolute;width:{size}px;height:{size}px;border-radius:50%;'
        f'background:radial-gradient(circle,rgba(201,168,76,{opacity*3:.2f}) 0%,transparent 70%);'
        f'border:1px solid rgba(201,168,76,{opacity:.2f});'
        f'top:{top}%;left:{left}%;'
        f'animation:floatParticle {dur}s ease-in-out {delay}s infinite;'
        f'pointer-events:none;"></div>'
    )

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap');

:root {{
    --nbe-dark-green:  #003d2a;
    --nbe-green:       #005a3c;
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
    0%,100% {{ transform:translateY(0) rotate(0deg);       opacity:0.6; }}
    33%      {{ transform:translateY(-20px) rotate(120deg); opacity:1;   }}
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
@keyframes blink {{
    0%,100% {{ opacity:1; }}
    50%      {{ opacity:0.3; }}
}}

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

.timeline-step {{
    display:flex; align-items:flex-start; gap:20px;
    padding:0 0 32px 0; position:relative; z-index:1;
    flex-direction:{'row-reverse' if lang == 'ar' else 'row'};
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

.badge-shimmer {{
    background:linear-gradient(90deg,rgba(255,255,255,0) 0%,rgba(255,255,255,0.4) 50%,rgba(255,255,255,0) 100%);
    background-size:200% auto;
    animation:shimmer 3s linear infinite;
    position:absolute; inset:0; border-radius:inherit;
    pointer-events:none;
}}

.sec-header {{
    display:flex; align-items:center; gap:14px;
    margin-bottom:28px;
    flex-direction:{'row-reverse' if lang == 'ar' else 'row'};
    animation:slideInLeft 0.6s ease;
}}
.sec-line     {{ flex:1; height:2px; background:linear-gradient({'to left' if lang == 'ar' else 'to right'},var(--nbe-gold),transparent); }}
.sec-line-rev {{ flex:1; height:2px; background:linear-gradient({'to right' if lang == 'ar' else 'to left'},var(--nbe-gold),transparent); }}

hr {{ border-color:var(--nbe-border) !important; margin:2.5rem 0 !important; }}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding:24px 16px 20px; text-align:center;
        border-bottom:1px solid rgba(201,168,76,0.25); margin-bottom:20px;">
        <div style="font-size:40px; margin-bottom:10px;">🏦</div>
        <div style="font-size:15px; font-weight:800; color:#E8C97A;
            font-family:'Cairo',sans-serif;">NBE Credit Risk</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.55);
            margin-top:4px; font-weight:500;">
            {'البنك الأهلي المصري' if lang == 'ar' else 'National Bank of Egypt'}
        </div>
    </div>
    """, unsafe_allow_html=True)

    lang_options = {'ar': '🇪🇬 العربية', 'en': '🇬🇧 English'}
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

    st.markdown(f"""
    <div style="margin-top:28px; border-top:1px solid rgba(201,168,76,0.2); padding-top:20px;">
        <div style="background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.3);
            border-radius:10px; padding:12px 14px; margin-bottom:8px;">
            <span style="display:inline-block; width:10px; height:10px; border-radius:50%;
                background:#22c55e; animation:blink 2s ease infinite;
                box-shadow:0 0 8px rgba(34,197,94,0.6); vertical-align:middle;
                margin-right:8px;"></span>
            <span style="font-size:13px; font-weight:600;">
                {'النموذج نشط' if lang == 'ar' else 'Model Active'}
            </span>
        </div>
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1);
            border-radius:10px; padding:10px 14px; font-size:12px;
            color:rgba(255,255,255,0.65);">
            🎯 {'الدقة: 76.5%' if lang == 'ar' else 'Accuracy: 76.5%'} &nbsp;|&nbsp; v4.0
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── BANNER ────────────────────────────────────────────────────
if banner_b64:
    st.markdown(
        f'<div style="width:100%;border-radius:16px;overflow:hidden;'
        f'box-shadow:0 20px 60px rgba(0,61,42,0.2);margin:20px 0 30px;">'
        f'<img src="data:image/png;base64,{banner_b64}" '
        f'style="width:100%;height:auto;display:block;" alt="NBE Banner"></div>',
        unsafe_allow_html=True
    )

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
    badges_html += (
        f'<span style="position:relative;overflow:hidden;'
        f'background:{bg};border:1.5px solid {border};color:{color};'
        f'padding:8px 18px;border-radius:25px;font-size:13px;font-weight:700;'
        f'display:inline-flex;align-items:center;gap:6px;transition:all 0.3s ease;" '
        f'onmouseover="this.style.transform=\'translateY(-3px) scale(1.05)\';this.style.boxShadow=\'0 8px 20px {border}\';" '
        f'onmouseout="this.style.transform=\'translateY(0) scale(1)\';this.style.boxShadow=\'none\';">'
        f'{icon} {t[key]}<span class="badge-shimmer"></span></span>'
    )

hero_accent_side = 'right' if lang == 'ar' else 'left'
st.markdown(
    f'<div style="'
    f'background:linear-gradient(135deg,#002a1d 0%,#003d2a 25%,#004d34 50%,#005a3c 75%,#003d2a 100%);'
    f'background-size:300% 300%;animation:gradientShift 8s ease infinite;'
    f'border:1px solid rgba(201,168,76,0.3);border-radius:24px;padding:60px 52px;'
    f'margin:0 0 32px;position:relative;overflow:hidden;'
    f'box-shadow:0 20px 60px rgba(0,61,42,0.2);text-align:{text_align};">'
    f'{particles_html}'
    f'<div style="position:absolute;top:-80px;right:-80px;width:280px;height:280px;'
    f'border-radius:50%;border:1px solid rgba(201,168,76,0.08);"></div>'
    f'<div style="position:absolute;top:-50px;right:-50px;width:200px;height:200px;'
    f'border-radius:50%;border:1px solid rgba(201,168,76,0.05);"></div>'
    f'<div style="position:absolute;bottom:-60px;left:-60px;width:220px;height:220px;'
    f'border-radius:50%;border:1px solid rgba(0,138,87,0.1);"></div>'
    f'<div style="position:absolute;top:0;{hero_accent_side}:0;width:5px;height:100%;'
    f'background:linear-gradient(180deg,#C9A84C,#E8C97A,#C9A84C);'
    f'border-radius:0 4px 4px 0;"></div>'
    f'<div style="position:relative;z-index:2;animation:slideInLeft 0.8s ease;">'
    f'<div style="font-size:12px;letter-spacing:4px;text-transform:uppercase;'
    f'color:#E8C97A;font-weight:700;margin-bottom:10px;'
    f'font-family:JetBrains Mono,monospace;">{t["subtitle"]}</div>'
    f'<h1 style="font-family:Playfair Display,serif;'
    f'font-size:clamp(32px,4vw,56px);font-weight:900;color:#fff;'
    f'line-height:1.15;margin:0 0 22px;'
    f'text-shadow:0 2px 20px rgba(0,0,0,0.3);">{t["title"]}</h1>'
    f'<p style="color:rgba(255,255,255,0.8);font-size:17px;max-width:820px;'
    f'line-height:2;margin:0 0 36px;font-weight:400;">{t["description"]}</p>'
    f'<div style="display:flex;flex-wrap:wrap;gap:10px;">{badges_html}</div>'
    f'</div></div>',
    unsafe_allow_html=True
)

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
st.markdown(
    f'<div class="sec-header">'
    f'<div class="sec-line"></div>'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:30px;margin:0;white-space:nowrap;font-weight:900;">'
    f'🎯 {t["capabilities"]}</h2>'
    f'<div class="sec-line-rev"></div></div>',
    unsafe_allow_html=True
)

cards = [
    ("🎯", 'cap1_title', 'cap1_desc', "#C9A84C", "rgba(201,168,76,0.12)",  0.10),
    ("📊", 'cap2_title', 'cap2_desc', "#15803d", "rgba(21,128,61,0.1)",    0.20),
    ("🔒", 'cap3_title', 'cap3_desc', "#1d4ed8", "rgba(29,78,216,0.1)",    0.30),
    ("📈", 'cap4_title', 'cap4_desc', "#7c3aed", "rgba(124,58,237,0.1)",   0.15),
    ("⚡", 'cap5_title', 'cap5_desc', "#ea580c", "rgba(234,88,12,0.1)",    0.25),
    ("🔄", 'cap6_title', 'cap6_desc', "#be185d", "rgba(190,24,93,0.1)",    0.35),
]
c1, c2, c3 = st.columns(3)
for i, (icon, tk, dk, color, bg, delay) in enumerate(cards):
    with [c1, c2, c3][i % 3]:
        st.markdown(
            f'<div class="cap-card" style="animation-delay:{delay}s;border-top:4px solid {color};">'
            f'<div class="cap-icon-circle" style="background:{bg};border:2px solid {color}20;">'
            f'<span style="font-size:30px;">{icon}</span></div>'
            f'<h3 style="color:{color};font-size:18px;margin:0 0 12px;'
            f'font-family:Cairo,sans-serif;font-weight:800;">{t[tk]}</h3>'
            f'<p style="color:#5a6474;font-size:14px;line-height:1.9;margin:0;font-weight:500;">{t[dk]}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown("---")

# ── TIMELINE ──────────────────────────────────────────────────
st.markdown(
    f'<div class="sec-header">'
    f'<div class="sec-line"></div>'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:30px;margin:0;white-space:nowrap;font-weight:900;">'
    f'🚀 {t["quickstart"]}</h2>'
    f'<div class="sec-line-rev"></div></div>',
    unsafe_allow_html=True
)

steps = [
    ("01", "🎯", 'step1', 'step1_desc', "#C9A84C", "#8a6c00", 0.00),
    ("02", "📋", 'step2', 'step2_desc', "#15803d", "#0d5c2a", 0.15),
    ("03", "🔍", 'step3', 'step3_desc', "#1d4ed8", "#1640b0", 0.30),
    ("04", "📊", 'step4', 'step4_desc', "#7c3aed", "#5b28c0", 0.45),
]
tl_col, _ = st.columns([3, 1])
with tl_col:
    for num, icon, tk, dk, color, color2, delay in steps:
        st.markdown(
            f'<div class="timeline-step" style="animation-delay:{delay}s;">'
            f'<div class="timeline-badge" style="'
            f'background:linear-gradient(135deg,{color},{color2});'
            f'box-shadow:0 8px 24px {color}55;">'
            f'<span style="color:white;font-size:14px;font-weight:900;'
            f'font-family:JetBrains Mono,monospace;">{num}</span>'
            f'<span style="font-size:20px;margin-top:2px;">{icon}</span></div>'
            f'<div class="timeline-content">'
            f'<h4 style="color:{color};font-size:17px;margin:0 0 8px;'
            f'font-family:Cairo,sans-serif;font-weight:800;">{t[tk]}</h4>'
            f'<p style="color:#5a6474;font-size:14px;margin:0;line-height:1.8;font-weight:500;">{t[dk]}</p>'
            f'</div></div>',
            unsafe_allow_html=True
        )

st.markdown("---")

# ── TECH & PERFORMANCE ────────────────────────────────────────
st.markdown(
    f'<div class="sec-header" style="margin-bottom:20px;">'
    f'<div class="sec-line"></div>'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:26px;margin:0;white-space:nowrap;font-weight:900;">'
    f'⚙️ {t["tech_stack"]} &amp; {t["performance"]}</h2>'
    f'<div class="sec-line-rev"></div></div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    tech_rows = ""
    for icon, name, color, role in [
        ("🐍", "Python 3.11",  "#15803d", "Core Language"),
        ("🌊", "Streamlit",    "#1d4ed8", "Web Framework"),
        ("🤖", "scikit-learn", "#C9A84C", "ML Engine"),
        ("📊", "Plotly",       "#7c3aed", "Visualization"),
        ("🐼", "Pandas",       "#ea580c", "Data Processing"),
        ("🔢", "NumPy",        "#be185d", "Numerical Computing"),
    ]:
        tech_rows += (
            f'<div style="display:flex;align-items:center;gap:14px;'
            f'padding:13px 16px;border-radius:12px;'
            f'background:rgba(0,99,65,0.03);border:1px solid rgba(0,99,65,0.12);'
            f'margin-bottom:10px;transition:all 0.3s ease;"'
            f'onmouseover="this.style.background=\'rgba(0,99,65,0.07)\';this.style.borderColor=\'{color}40\';"'
            f'onmouseout="this.style.background=\'rgba(0,99,65,0.03)\';this.style.borderColor=\'rgba(0,99,65,0.12)\';">'
            f'<span style="font-size:26px;min-width:30px;text-align:center;">{icon}</span>'
            f'<div><div style="color:{color};font-weight:800;font-size:15px;'
            f'font-family:Cairo,sans-serif;">{name}</div>'
            f'<div style="color:#5a6474;font-size:12px;">{role}</div></div></div>'
        )
    st.markdown(
        f'<div style="background:#ffffff;border:1px solid rgba(0,99,65,0.12);'
        f'border-radius:20px;padding:32px;box-shadow:0 8px 32px rgba(0,61,42,0.14);'
        f'text-align:{text_align};">'
        f'<h3 style="color:#003d2a;font-family:Playfair Display,serif;'
        f'font-size:22px;margin-bottom:22px;font-weight:900;">{t["tech_stack"]}</h3>'
        f'{tech_rows}</div>',
        unsafe_allow_html=True
    )

with c2:
    perf_rows = ""
    for lk, value, color, pct in [
        ('test_accuracy',   "76.5%",    "#C9A84C", 76.5),
        ('precision',       "64.4%",    "#15803d", 64.4),
        ('recall',          "48.3%",    "#1d4ed8", 48.3),
        ('f1_score',        "55.2%",    "#7c3aed", 55.2),
        ('false_negatives', "31 cases", "#dc2626", 31),
        ('training_time',   "< 1 min",  "#ea580c", 90),
    ]:
        w = min(pct, 100)
        perf_rows += (
            f'<div style="margin-bottom:16px;">'
            f'<div style="display:flex;justify-content:space-between;'
            f'align-items:center;margin-bottom:6px;">'
            f'<span style="color:#5a6474;font-size:14px;font-weight:600;">{t[lk]}</span>'
            f'<span style="color:{color};font-weight:800;font-size:15px;'
            f'font-family:JetBrains Mono,monospace;">{value}</span></div>'
            f'<div style="height:8px;background:rgba(0,0,0,0.06);border-radius:4px;overflow:hidden;">'
            f'<div style="height:8px;border-radius:4px;width:{w}%;'
            f'background:linear-gradient(90deg,{color}99,{color});"></div>'
            f'</div></div>'
        )
    st.markdown(
        f'<div style="background:#ffffff;border:1px solid rgba(0,99,65,0.12);'
        f'border-radius:20px;padding:32px;box-shadow:0 8px 32px rgba(0,61,42,0.14);'
        f'text-align:{text_align};">'
        f'<h3 style="color:#003d2a;font-family:Playfair Display,serif;'
        f'font-size:22px;margin-bottom:22px;font-weight:900;">{t["performance"]}</h3>'
        f'{perf_rows}</div>',
        unsafe_allow_html=True
    )

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("---")

footer_stats_html = ""
for val, lbl, color in [
    ("76.5%", t['test_accuracy'], "#C9A84C"),
    ("73",    t['metric2'],       "#15803d"),
    ("800",   t['metric3'],       "#1d4ed8"),
    ("100",   t['metric4'],       "#7c3aed"),
]:
    footer_stats_html += (
        f'<div style="background:rgba(255,255,255,0.08);'
        f'border:1px solid rgba(201,168,76,0.2);'
        f'border-radius:12px;padding:16px 20px;text-align:center;min-width:100px;'
        f'transition:all 0.3s ease;"'
        f'onmouseover="this.style.background=\'rgba(201,168,76,0.12)\';this.style.transform=\'translateY(-3px)\';"'
        f'onmouseout="this.style.background=\'rgba(255,255,255,0.08)\';this.style.transform=\'translateY(0)\';">'
        f'<div style="font-size:24px;font-weight:900;color:{color};'
        f'font-family:JetBrains Mono,monospace;">{val}</div>'
        f'<div style="font-size:11px;color:rgba(255,255,255,0.6);'
        f'margin-top:4px;font-weight:600;text-transform:uppercase;">{lbl}</div></div>'
    )

links_align = 'flex-start' if lang == 'ar' else 'flex-end'
logo_dir    = 'row-reverse' if lang == 'ar' else 'row'

st.markdown(
    f'<div style="background:linear-gradient(135deg,#002a1d 0%,#003d2a 50%,#004d34 100%);'
    f'border:1px solid rgba(201,168,76,0.3);border-radius:24px;'
    f'padding:44px 48px;box-shadow:0 20px 60px rgba(0,61,42,0.2);'
    f'position:relative;overflow:hidden;text-align:{text_align};">'
    f'<div style="position:absolute;top:0;left:0;right:0;height:3px;'
    f'background:linear-gradient(90deg,#C9A84C,#E8C97A,#C9A84C);"></div>'
    f'<div style="display:flex;flex-wrap:wrap;justify-content:space-between;'
    f'align-items:flex-start;gap:32px;margin-bottom:36px;">'
    f'<div>'
    f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;'
    f'flex-direction:{logo_dir};">'
    f'<div style="width:52px;height:52px;'
    f'background:linear-gradient(135deg,#C9A84C,#a07a1e);'
    f'border-radius:14px;display:flex;align-items:center;'
    f'justify-content:center;font-size:24px;'
    f'box-shadow:0 6px 16px rgba(201,168,76,0.4);">🏦</div>'
    f'<div>'
    f'<div style="color:#E8C97A;font-weight:800;font-size:18px;'
    f'font-family:Cairo,sans-serif;">{t["footer_title"]}</div>'
    f'<div style="color:rgba(255,255,255,0.6);font-size:12px;">{t["footer_bank"]}</div>'
    f'</div></div>'
    f'<div style="color:rgba(255,255,255,0.5);font-size:13px;line-height:1.8;">'
    f'{t["footer_rights"]}<br>'
    f'{t["footer_dev"]} <strong style="color:#E8C97A;">ENG. Goda Emad</strong>'
    f' &nbsp;|&nbsp; {t["footer_version"]}</div></div>'
    f'<div style="display:flex;flex-direction:column;gap:12px;align-items:{links_align};">'
    f'<div style="color:rgba(201,168,76,0.8);font-size:11px;text-transform:uppercase;'
    f'letter-spacing:2px;font-weight:700;">{t["footer_contact"]}</div>'
    f'<a href="mailto:creditrisk@nbe.com.eg" style="'
    f'background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);'
    f'color:rgba(255,255,255,0.85);padding:11px 22px;border-radius:12px;'
    f'text-decoration:none;font-size:14px;font-weight:600;'
    f'font-family:Cairo,sans-serif;display:inline-block;"'
    f'onmouseover="this.style.background=\'rgba(255,255,255,0.14)\';"'
    f'onmouseout="this.style.background=\'rgba(255,255,255,0.07)\';">✉️ creditrisk@nbe.com.eg</a>'
    f'<a href="https://www.linkedin.com/in/goda-emad/" target="_blank" style="'
    f'background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.5);'
    f'color:#93c5fd;padding:11px 22px;border-radius:12px;'
    f'text-decoration:none;font-size:14px;font-weight:600;'
    f'font-family:Cairo,sans-serif;display:inline-block;"'
    f'onmouseover="this.style.background=\'rgba(10,102,194,0.35)\';"'
    f'onmouseout="this.style.background=\'rgba(10,102,194,0.2)\';">🔗 LinkedIn — ENG. Goda Emad</a>'
    f'<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank" style="'
    f'background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);'
    f'color:rgba(255,255,255,0.85);padding:11px 22px;border-radius:12px;'
    f'text-decoration:none;font-size:14px;font-weight:600;'
    f'font-family:Cairo,sans-serif;display:inline-block;"'
    f'onmouseover="this.style.background=\'rgba(255,255,255,0.18)\';"'
    f'onmouseout="this.style.background=\'rgba(255,255,255,0.08)\';">⭐ GitHub Project</a>'
    f'</div></div>'
    f'<div style="border-top:1px solid rgba(201,168,76,0.15);padding-top:28px;'
    f'display:flex;flex-wrap:wrap;gap:12px;">'
    f'{footer_stats_html}</div></div>'
    f'<div style="text-align:center;margin-top:16px;padding-bottom:8px;'
    f'color:rgba(0,61,42,0.4);font-size:11px;">'
    f'NBE Credit Risk Intelligence Platform v4.0 — Powered by AI 🤖</div>',
    unsafe_allow_html=True
)

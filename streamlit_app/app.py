"""NBE Credit Risk Intelligence - Main Application (Enhanced v4.0)"""
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

lang = st.session_state.language
is_ar = lang == 'ar'
direction  = 'rtl' if is_ar else 'ltr'
text_align = 'right' if is_ar else 'left'
accent = 'right' if is_ar else 'left'

T = {
    'ar': {
        'lang_label':  'اللغة',
        'subtitle':    'البنك الأهلي المصري',
        'title':       'منصة الذكاء الاصطناعي لتقييم مخاطر الائتمان',
        'description': 'منصة متكاملة مبنية على نموذج Random Forest بدقة 76.5% ومتوافقة مع معايير البنك المركزي المصري',
        'badge_cbe':   'متوافق مع البنك المركزي',
        'badge_ai':    'مدعوم بالذكاء الاصطناعي',
        'badge_rt':    'الوقت الفعلي',
        'badge_sec':   'آمن ومحمي',
        'badge_feat':  '73 ميزة',
        'badge_trees': '100 شجرة',
        'm1': 'دقة النموذج',
        'm2': 'الميزات المهندسة',
        'm3': 'بيانات التدريب',
        'm4': 'أشجار القرار',
        'cap_title': 'قدرات المنصة',
        'c1t': 'تقييم ذكي',       'c1d': 'تقييم فوري لمخاطر الائتمان باستخدام Random Forest مع 73 ميزة هندسية.',
        'c2t': 'تحليلات فورية',   'c2d': 'رؤى شاملة للمحفظة وتحليل الاتجاهات في لوحات تحكم تفاعلية.',
        'c3t': 'متوافق مع CBE',   'c3d': 'مسار تدقيق كامل وقرارات ذكاء اصطناعي قابلة للتفسير.',
        'c4t': 'مراقبة النموذج',  'c4d': 'تتبع أداء النموذج في الوقت الفعلي مع كشف الانحراف.',
        'c5t': 'قرارات فورية',    'c5d': 'تنبؤات بأقل من ثانية مع درجات احتمالية وتوصيات.',
        'c6t': 'إعادة تدريب',     'c6d': 'خط MLOps مع إعادة تدريب تلقائية عند انخفاض الأداء.',
        'nav_title': 'دليل التنقل',
        'nav_text':  'استخدم الشريط الجانبي للتنقل بين الصفحات',
        'nav1': 'الرئيسية — نظرة عامة وإحصائيات',
        'nav2': 'تقييم المخاطر — تقييم طلبات الائتمان',
        'nav3': 'التحليلات — تحليل المحفظة والرؤى',
        'nav4': 'أداء النموذج — مقاييس تفصيلية',
        'nav5': 'عن المنصة — توثيق المشروع',
        'nav_tip': 'ابدأ من صفحة تقييم المخاطر لتقييم طلبات الائتمان فوراً',
        'model_active': 'النموذج نشط',
        'accuracy': 'الدقة: 76.5%',
        'footer_copy': '© 2026 البنك الأهلي المصري | م. جودة عماد | الإصدار 4.0',
    },
    'en': {
        'lang_label':  'Language',
        'subtitle':    'National Bank of Egypt',
        'title':       'Credit Risk Intelligence Platform',
        'description': 'AI-powered platform built on Random Forest achieving 76.5% accuracy, fully compliant with Central Bank of Egypt regulations',
        'badge_cbe':   'CBE Compliant',
        'badge_ai':    'AI Powered',
        'badge_rt':    'Real-time',
        'badge_sec':   'Secure',
        'badge_feat':  '73 Features',
        'badge_trees': '100 Trees',
        'm1': 'Model Accuracy',
        'm2': 'Engineered Features',
        'm3': 'Training Samples',
        'm4': 'Decision Trees',
        'cap_title': 'Platform Capabilities',
        'c1t': 'Smart Assessment',  'c1d': 'Real-time credit risk evaluation using Random Forest with 73 engineered features.',
        'c2t': 'Live Analytics',    'c2d': 'Comprehensive portfolio insights and trend analysis in interactive dashboards.',
        'c3t': 'CBE Compliant',     'c3d': 'Full audit trail and explainable AI decisions for regulatory compliance.',
        'c4t': 'Model Monitoring',  'c4d': 'Real-time model performance tracking with drift detection.',
        'c5t': 'Instant Decisions', 'c5d': 'Sub-second predictions with probability scores and recommendations.',
        'c6t': 'Auto Retraining',   'c6d': 'MLOps pipeline with automated retraining when performance degrades.',
        'nav_title': 'Navigation Guide',
        'nav_text':  'Use the sidebar to navigate between pages',
        'nav1': 'Home — Overview and statistics',
        'nav2': 'Risk Assessment — Evaluate credit applications',
        'nav3': 'Analytics — Portfolio analysis and insights',
        'nav4': 'Model Performance — Detailed metrics',
        'nav5': 'About — Project documentation',
        'nav_tip': 'Start with Risk Assessment to evaluate credit applications instantly',
        'model_active': 'Model Active',
        'accuracy': 'Accuracy: 76.5%',
        'footer_copy': '© 2026 National Bank of Egypt | ENG. Goda Emad | Version 4.0',
    }
}
t = T[lang]

# ── Logo helper ───────────────────────────────────────────────
def get_image_base64(path):
    try:
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo_path = Path(__file__).parent.parent / 'assets' / 'nbe_branding' / 'nbe_logo.png'
logo_b64  = get_image_base64(logo_path)

# ── CSS ───────────────────────────────────────────────────────
PARTICLES = [
    (5,53,86,7.4,0.1,0.05),(4,18,33,6.5,0.5,0.10),(5,47,65,6.4,3.4,0.08),
    (7,51,22,7.6,3.2,0.09),(5,32,32,7.3,3.7,0.06),(8,45,39,7.2,0.1,0.11),
    (6,46,64,4.5,3.9,0.09),(9,90,94,5.6,3.6,0.10),(9,42,62,4.7,2.9,0.05),
    (9,72,15,4.8,2.7,0.09),(9,67,48,6.9,1.3,0.09),(4,17,69,5.0,2.0,0.10),
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

css = (
    '@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900'
    '&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap");'
    f'html,body,[class*="css"]{{font-family:Cairo,sans-serif!important;direction:{direction};}}'
    '#MainMenu,footer,header{visibility:hidden}'
    '.block-container{padding:0 2rem 3rem!important;max-width:1400px}'
    '[data-testid="stSidebar"]{'
    '  background:linear-gradient(180deg,#001208 0%,#001f15 50%,#002a1d 100%)!important;'
    '  position:relative;overflow:hidden;}'
    '[data-testid="stSidebar"]::before{'
    '  content:"";position:absolute;top:0;left:0;right:0;height:4px;'
    '  background:linear-gradient(90deg,#C9A84C,#E8C97A,#C9A84C);}'
    '[data-testid="stSidebar"] *{color:rgba(255,255,255,0.9)!important;}'
    '[data-testid="stSidebar"] .stSelectbox>div>div{'
    '  background:rgba(255,255,255,0.08)!important;'
    '  border:1px solid rgba(201,168,76,0.35)!important;border-radius:10px!important;}'
    '[data-testid="stMetricValue"]{'
    '  color:#003d2a!important;font-size:2.4rem!important;font-weight:900!important;'
    '  font-family:JetBrains Mono,monospace!important;'
    '  animation:countAnim 0.7s cubic-bezier(0.34,1.56,0.64,1) forwards;}'
    '[data-testid="stMetricLabel"]{color:#555!important;font-size:13px!important;'
    '  font-weight:700!important;text-transform:uppercase;letter-spacing:0.5px;}'
    '[data-testid="metric-container"]{'
    '  background:#ffffff!important;border:1px solid rgba(0,99,65,0.12)!important;'
    '  border-top:4px solid #C9A84C!important;border-radius:16px!important;'
    '  padding:20px 24px!important;'
    '  box-shadow:0 4px 20px rgba(0,61,42,0.08)!important;'
    '  transition:transform 0.3s,box-shadow 0.3s!important;}'
    '[data-testid="metric-container"]:hover{transform:translateY(-6px)!important;'
    '  box-shadow:0 16px 40px rgba(0,61,42,0.15)!important;}'
    '.cap-card{background:#ffffff;border:1px solid rgba(0,99,65,0.12);'
    '  border-radius:20px;padding:28px;margin-bottom:20px;'
    '  box-shadow:0 4px 20px rgba(0,61,42,0.07);'
    '  transition:all 0.35s cubic-bezier(0.34,1.56,0.64,1);'
    '  animation:fadeInUp 0.5s ease backwards;}'
    '.cap-card:hover{transform:translateY(-8px) scale(1.02);'
    '  box-shadow:0 20px 50px rgba(0,61,42,0.15);}'
    '.nav-item{display:flex;align-items:center;gap:14px;'
    '  padding:14px 18px;border-radius:14px;margin-bottom:10px;'
    '  background:#ffffff;border:1px solid rgba(0,99,65,0.1);'
    '  box-shadow:0 2px 10px rgba(0,61,42,0.05);'
    '  transition:all 0.25s ease;animation:fadeInUp 0.5s ease backwards;}'
    '.nav-item:hover{background:#f0faf5;border-color:rgba(201,168,76,0.4);'
    '  transform:translateX(6px);box-shadow:0 6px 20px rgba(0,61,42,0.12);}'
    '@keyframes countAnim{from{opacity:0;transform:scale(0.5) translateY(20px)}'
    '  to{opacity:1;transform:scale(1) translateY(0)}}'
    '@keyframes fadeInUp{from{opacity:0;transform:translateY(25px)}'
    '  to{opacity:1;transform:translateY(0)}}'
    '@keyframes slideIn{from{opacity:0;transform:translateX(-30px)}'
    '  to{opacity:1;transform:translateX(0)}}'
    '@keyframes gradientShift{0%{background-position:0% 50%}'
    '  50%{background-position:100% 50%}100%{background-position:0% 50%}}'
    '@keyframes floatParticle{0%,100%{transform:translateY(0) rotate(0deg);opacity:0.6}'
    '  33%{transform:translateY(-20px) rotate(120deg);opacity:1}'
    '  66%{transform:translateY(-10px) rotate(240deg);opacity:0.8}}'
    '@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}'
    'hr{border-color:rgba(0,99,65,0.1)!important;margin:2.5rem 0!important;}'
)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div style="padding:24px 16px 20px;text-align:center;'
        'border-bottom:1px solid rgba(201,168,76,0.2);margin-bottom:20px;">'
        '<div style="font-size:38px;margin-bottom:10px;">🏦</div>'
        '<div style="font-size:14px;font-weight:800;color:#E8C97A;'
        'font-family:Cairo,sans-serif;">NBE Credit Risk</div>'
        f'<div style="font-size:11px;color:rgba(255,255,255,0.5);margin-top:4px;">'
        f'{t["subtitle"]}</div></div>',
        unsafe_allow_html=True
    )
    lang_options = {'ar': '🇪🇬 العربية', 'en': '🇬🇧 English'}
    selected = st.selectbox(
        t['lang_label'],
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=0 if is_ar else 1,
        key='lang_selector'
    )
    if selected != st.session_state.language:
        st.session_state.language = selected
        st.rerun()

    st.markdown(
        '<div style="margin-top:24px;border-top:1px solid rgba(201,168,76,0.2);padding-top:20px;">'
        '<div style="background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);'
        'border-radius:10px;padding:11px 14px;margin-bottom:8px;">'
        '<span style="display:inline-block;width:9px;height:9px;border-radius:50%;'
        'background:#22c55e;animation:blink 2s infinite;'
        'box-shadow:0 0 8px rgba(34,197,94,0.6);vertical-align:middle;margin-right:8px;"></span>'
        f'<span style="font-size:13px;font-weight:600;">{t["model_active"]}</span>'
        '</div>'
        '<div style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);'
        f'border-radius:10px;padding:10px 14px;font-size:12px;color:rgba(255,255,255,0.6);">'
        f'🎯 {t["accuracy"]} | v4.0</div></div>',
        unsafe_allow_html=True
    )

# ── LOGO ──────────────────────────────────────────────────────
if logo_b64:
    st.markdown(
        f'<div style="display:flex;justify-content:center;padding:20px 0 10px;">'
        f'<img src="data:image/png;base64,{logo_b64}" '
        f'style="max-width:260px;height:auto;" alt="NBE Logo"></div>',
        unsafe_allow_html=True
    )

# ── HERO ──────────────────────────────────────────────────────
badges = [
    ('badge_cbe',  'rgba(0,99,65,0.15)',    'rgba(0,99,65,0.5)',     '#004d34', '✅'),
    ('badge_ai',   'rgba(74,222,128,0.12)', 'rgba(74,222,128,0.4)', '#15803d', '🤖'),
    ('badge_rt',   'rgba(59,130,246,0.12)', 'rgba(59,130,246,0.4)', '#1d4ed8', '⚡'),
    ('badge_sec',  'rgba(168,85,247,0.12)', 'rgba(168,85,247,0.4)', '#6d28d9', '🔒'),
    ('badge_feat', 'rgba(201,168,76,0.15)', 'rgba(201,168,76,0.5)', '#7a5c0e', '📊'),
    ('badge_trees','rgba(236,72,153,0.12)', 'rgba(236,72,153,0.4)', '#9d174d', '🌲'),
]
badges_html = ""
for key, bg, border, color, icon in badges:
    badges_html += (
        f'<span style="position:relative;overflow:hidden;background:{bg};'
        f'border:1.5px solid {border};color:{color};'
        f'padding:8px 18px;border-radius:25px;font-size:13px;font-weight:700;'
        f'display:inline-flex;align-items:center;gap:6px;'
        f'transition:all 0.3s ease;cursor:default;"'
        f'onmouseover="this.style.transform=\'translateY(-3px) scale(1.05)\';"'
        f'onmouseout="this.style.transform=\'translateY(0) scale(1)\';">'
        f'{icon} {t[key]}</span>'
    )

st.markdown(
    f'<div style="background:linear-gradient(135deg,#002a1d 0%,#003d2a 30%,#004d34 60%,#003d2a 100%);'
    f'background-size:300% 300%;animation:gradientShift 8s ease infinite;'
    f'border:1px solid rgba(201,168,76,0.3);border-radius:24px;'
    f'padding:60px 52px;margin:0 0 32px;position:relative;overflow:hidden;'
    f'box-shadow:0 20px 60px rgba(0,61,42,0.2);text-align:{text_align};">'
    f'{particles_html}'
    f'<div style="position:absolute;top:-80px;right:-80px;width:280px;height:280px;'
    f'border-radius:50%;border:1px solid rgba(201,168,76,0.08);"></div>'
    f'<div style="position:absolute;bottom:-60px;left:-60px;width:220px;height:220px;'
    f'border-radius:50%;border:1px solid rgba(0,138,87,0.1);"></div>'
    f'<div style="position:absolute;top:0;{accent}:0;width:5px;height:100%;'
    f'background:linear-gradient(180deg,#C9A84C,#E8C97A,#C9A84C);'
    f'border-radius:0 4px 4px 0;"></div>'
    f'<div style="position:relative;z-index:2;animation:slideIn 0.8s ease;">'
    f'<div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;'
    f'color:#E8C97A;font-weight:700;margin-bottom:10px;'
    f'font-family:JetBrains Mono,monospace;">{t["subtitle"]}</div>'
    f'<h1 style="font-family:Playfair Display,serif;'
    f'font-size:clamp(28px,4vw,52px);font-weight:900;color:#fff;'
    f'line-height:1.15;margin:0 0 20px;">{t["title"]}</h1>'
    f'<p style="color:rgba(255,255,255,0.8);font-size:16px;max-width:800px;'
    f'line-height:2;margin:0 0 32px;">{t["description"]}</p>'
    f'<div style="display:flex;flex-wrap:wrap;gap:10px;">{badges_html}</div>'
    f'</div></div>',
    unsafe_allow_html=True
)

# ── METRICS ───────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, label, value, delta in [
    (c1, t['m1'], '76.5%', '↑ +2.3%'),
    (c2, t['m2'], '73',    'engineered'),
    (c3, t['m3'], '800',   'samples'),
    (c4, t['m4'], '100',   'RF trees'),
]:
    with col:
        st.metric(label, value, delta)

st.markdown('---')

# ── CAPABILITIES ──────────────────────────────────────────────
st.markdown(
    f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:28px;'
    f'flex-direction:{"row-reverse" if is_ar else "row"};">'
    f'<div style="flex:1;height:2px;background:linear-gradient({"to left" if is_ar else "to right"},#C9A84C,transparent);"></div>'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:28px;margin:0;white-space:nowrap;font-weight:900;">'
    f'🎯 {t["cap_title"]}</h2>'
    f'<div style="flex:1;height:2px;background:linear-gradient({"to right" if is_ar else "to left"},#C9A84C,transparent);"></div>'
    f'</div>',
    unsafe_allow_html=True
)

caps = [
    ("🎯", 'c1t', 'c1d', "#C9A84C", "rgba(201,168,76,0.08)", 0.05),
    ("📊", 'c2t', 'c2d', "#1d6fa8", "rgba(29,111,168,0.06)", 0.15),
    ("🔒", 'c3t', 'c3d', "#16a34a", "rgba(22,163,74,0.06)",  0.25),
    ("📈", 'c4t', 'c4d', "#6d3aad", "rgba(109,58,173,0.06)", 0.10),
    ("⚡", 'c5t', 'c5d', "#c2410c", "rgba(194,65,12,0.06)",  0.20),
    ("🔄", 'c6t', 'c6d', "#be185d", "rgba(190,24,93,0.06)",  0.30),
]
col1, col2, col3 = st.columns(3)
for i, (icon, tk, dk, color, bg, delay) in enumerate(caps):
    with [col1, col2, col3][i % 3]:
        st.markdown(
            f'<div class="cap-card" style="border-top:4px solid {color};'
            f'animation-delay:{delay}s;">'
            f'<div style="width:60px;height:60px;border-radius:50%;'
            f'background:{bg};border:2px solid {color}30;'
            f'display:flex;align-items:center;justify-content:center;'
            f'font-size:26px;margin-bottom:16px;">{icon}</div>'
            f'<h3 style="color:{color};font-size:17px;margin:0 0 10px;'
            f'font-family:Cairo,sans-serif;font-weight:800;'
            f'text-align:{text_align};">{t[tk]}</h3>'
            f'<p style="color:#555;font-size:14px;line-height:1.8;margin:0;'
            f'text-align:{text_align};">{t[dk]}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown('---')

# ── NAVIGATION GUIDE ──────────────────────────────────────────
st.markdown(
    f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:24px;'
    f'flex-direction:{"row-reverse" if is_ar else "row"};">'
    f'<div style="flex:1;height:2px;background:linear-gradient({"to left" if is_ar else "to right"},#C9A84C,transparent);"></div>'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:26px;margin:0;white-space:nowrap;font-weight:900;">'
    f'🧭 {t["nav_title"]}</h2>'
    f'<div style="flex:1;height:2px;background:linear-gradient({"to right" if is_ar else "to left"},#C9A84C,transparent);"></div>'
    f'</div>',
    unsafe_allow_html=True
)

nav_col, _ = st.columns([2, 1])
with nav_col:
    nav_items = [
        ('🏠', t['nav1'], '#C9A84C', 0.05),
        ('🎯', t['nav2'], '#16a34a', 0.15),
        ('📊', t['nav3'], '#1d6fa8', 0.25),
        ('📈', t['nav4'], '#6d3aad', 0.35),
        ('ℹ️', t['nav5'], '#be185d', 0.45),
    ]
    for icon, label, color, delay in nav_items:
        st.markdown(
            f'<div class="nav-item" style="animation-delay:{delay}s;'
            f'flex-direction:{"row-reverse" if is_ar else "row"};">'
            f'<div style="width:42px;height:42px;min-width:42px;border-radius:12px;'
            f'background:linear-gradient(135deg,{color}20,{color}10);'
            f'border:2px solid {color}40;'
            f'display:flex;align-items:center;justify-content:center;font-size:20px;">'
            f'{icon}</div>'
            f'<span style="color:#1a1a1a;font-size:15px;font-weight:600;">{label}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div style="background:linear-gradient(135deg,rgba(201,168,76,0.1),rgba(201,168,76,0.05));'
        f'border:1px solid rgba(201,168,76,0.3);border-{accent}:4px solid #C9A84C;'
        f'border-radius:14px;padding:16px 20px;margin-top:16px;text-align:{text_align};">'
        f'<span style="color:#7a5c0e;font-size:14px;font-weight:700;">💡 {t["nav_tip"]}</span>'
        f'</div>',
        unsafe_allow_html=True
    )

# ── FOOTER ────────────────────────────────────────────────────
st.markdown('---')
st.markdown(
    f'<div style="background:linear-gradient(135deg,#002a1d,#003d2a,#004d34);'
    f'border:1px solid rgba(201,168,76,0.3);border-radius:20px;'
    f'padding:36px 44px;position:relative;overflow:hidden;">'
    f'<div style="position:absolute;top:0;left:0;right:0;height:3px;'
    f'background:linear-gradient(90deg,#C9A84C,#E8C97A,#C9A84C);"></div>'
    f'<div style="display:flex;flex-wrap:wrap;justify-content:space-between;'
    f'align-items:center;gap:20px;">'
    f'<div style="display:flex;align-items:center;gap:14px;'
    f'flex-direction:{"row-reverse" if is_ar else "row"};">'
    f'<div style="width:48px;height:48px;background:linear-gradient(135deg,#C9A84C,#a07a1e);'
    f'border-radius:12px;display:flex;align-items:center;justify-content:center;'
    f'font-size:22px;box-shadow:0 4px 14px rgba(201,168,76,0.4);">🏦</div>'
    f'<div style="text-align:{text_align};">'
    f'<div style="color:#E8C97A;font-weight:800;font-size:16px;">NBE Credit Risk Intelligence</div>'
    f'<div style="color:rgba(255,255,255,0.5);font-size:12px;">{t["footer_copy"]}</div>'
    f'</div></div>'
    f'<div style="display:flex;gap:10px;">'
    f'<a href="https://www.linkedin.com/in/goda-emad/" target="_blank" style="'
    f'background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.4);'
    f'color:#60a5fa;padding:9px 18px;border-radius:10px;text-decoration:none;'
    f'font-size:13px;font-weight:600;"'
    f'onmouseover="this.style.background=\'rgba(10,102,194,0.35)\';"'
    f'onmouseout="this.style.background=\'rgba(10,102,194,0.2)\';">🔗 LinkedIn</a>'
    f'<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank" style="'
    f'background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);'
    f'color:#fff;padding:9px 18px;border-radius:10px;text-decoration:none;'
    f'font-size:13px;font-weight:600;"'
    f'onmouseover="this.style.background=\'rgba(255,255,255,0.18)\';"'
    f'onmouseout="this.style.background=\'rgba(255,255,255,0.08)\';">⭐ GitHub</a>'
    f'</div></div></div>',
    unsafe_allow_html=True
)

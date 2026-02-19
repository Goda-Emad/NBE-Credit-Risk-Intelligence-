"""NBE Credit Risk Intelligence - About Page (Enhanced v4.0)"""
import streamlit as st

st.set_page_config(page_title="About | NBE", page_icon="ℹ️", layout="wide")

if 'language' not in st.session_state:
    st.session_state.language = 'ar'

lang = st.session_state.language
is_ar = lang == 'ar'
direction  = 'rtl' if is_ar else 'ltr'
text_align = 'right' if is_ar else 'left'
accent = 'right' if is_ar else 'left'

T = {
    'ar': {
        'lang_label':    'اللغة',
        'page_title':    'عن المنصة',
        'page_sub':      'توثيق المشروع ومعلومات المطور',
        'overview_title':'نظرة عامة على المشروع',
        'overview_text': 'منصة الذكاء الاصطناعي لتقييم مخاطر الائتمان هي نظام متكامل مصمم للبنك الأهلي المصري. تعتمد على تعلم الآلة لأتمتة تقييم المخاطر الائتمانية، مما يختصر وقت المعالجة من أيام إلى ثوانٍ مع الحفاظ على دقة عالية والامتثال التام للوائح البنك المركزي المصري.',
        'tech_title':    'التقنيات المستخدمة',
        'model_title':   'تفاصيل النموذج',
        'pipeline_title':'خط معالجة البيانات',
        'dev_title':     'م. جودة عماد',
        'dev_sub':       'مهندس ذكاء اصطناعي | تحليلات مخاطر الائتمان | البنك الأهلي المصري',
        'footer_copy':   '© 2026 البنك الأهلي المصري | الإصدار 4.0',
        'model_active':  'النموذج نشط',
        'accuracy':      'الدقة: 76.5%',
        'algorithm':     'الخوارزمية',
        'version':       'الإصدار',
        'acc_label':     'الدقة',
        'features':      'الميزات',
        'dataset':       'البيانات',
        'compliance':    'الامتثال',
    },
    'en': {
        'lang_label':    'Language',
        'page_title':    'About the Platform',
        'page_sub':      'Project documentation and developer information',
        'overview_title':'Project Overview',
        'overview_text': 'The NBE Credit Risk Intelligence Platform is an AI-powered credit assessment system designed for the National Bank of Egypt. It automates credit risk evaluation using machine learning, reducing processing time from days to seconds while maintaining high accuracy and full regulatory compliance.',
        'tech_title':    'Tech Stack',
        'model_title':   'Model Details',
        'pipeline_title':'ML Pipeline',
        'dev_title':     'ENG. Goda Emad',
        'dev_sub':       'AI/ML Engineer | Credit Risk Analytics | National Bank of Egypt',
        'footer_copy':   '© 2026 National Bank of Egypt | Version 4.0',
        'model_active':  'Model Active',
        'accuracy':      'Accuracy: 76.5%',
        'algorithm':     'Algorithm',
        'version':       'Version',
        'acc_label':     'Accuracy',
        'features':      'Features',
        'dataset':       'Dataset',
        'compliance':    'Compliance',
    }
}
t = T[lang]

# ── CSS ───────────────────────────────────────────────────────
css = (
    '@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900'
    '&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap");'
    f'html,body,[class*="css"]{{font-family:Cairo,sans-serif!important;direction:{direction};}}'
    '#MainMenu,footer,header{visibility:hidden}'
    '.block-container{padding:1rem 2rem 3rem!important;max-width:1400px}'
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
    '.info-card{'
    '  background:#ffffff;border:1px solid rgba(0,99,65,0.12);'
    '  border-radius:18px;padding:28px;margin-bottom:20px;'
    '  box-shadow:0 4px 20px rgba(0,61,42,0.08);'
    '  transition:all 0.3s ease;animation:fadeInUp 0.5s ease backwards;}'
    '.info-card:hover{'
    '  transform:translateY(-4px);'
    '  box-shadow:0 12px 40px rgba(0,61,42,0.15);}'
    '.tech-row{'
    '  display:flex;align-items:center;gap:14px;'
    '  padding:12px 14px;border-radius:12px;'
    '  background:rgba(0,99,65,0.04);border:1px solid rgba(0,99,65,0.1);'
    '  margin-bottom:10px;transition:all 0.25s ease;}'
    '.tech-row:hover{'
    '  background:rgba(0,99,65,0.08);border-color:rgba(201,168,76,0.3);'
    '  transform:translateX(4px);}'
    '.pipeline-step{'
    '  background:#ffffff;border:1px solid rgba(0,99,65,0.15);'
    '  border-radius:14px;padding:14px 18px;text-align:center;'
    '  min-width:100px;transition:all 0.3s ease;'
    '  box-shadow:0 2px 10px rgba(0,61,42,0.06);}'
    '.pipeline-step:hover{'
    '  transform:translateY(-5px);'
    '  box-shadow:0 10px 30px rgba(0,61,42,0.15);}'
    '@keyframes fadeInUp{from{opacity:0;transform:translateY(25px)}'
    '  to{opacity:1;transform:translateY(0)}}'
    '@keyframes slideIn{from{opacity:0;transform:translateX(-30px)}'
    '  to{opacity:1;transform:translateX(0)}}'
    '@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}'
    '@keyframes pulseGlow{0%,100%{box-shadow:0 0 20px rgba(201,168,76,0.2)}'
    '  50%{box-shadow:0 0 50px rgba(201,168,76,0.5)}}'
    'hr{border-color:rgba(0,99,65,0.12)!important;margin:2rem 0!important;}'
    'a{color:#1d6fa8!important;}'
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
        f'{"البنك الأهلي المصري" if is_ar else "National Bank of Egypt"}'
        '</div></div>',
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

# ── PAGE HEADER ───────────────────────────────────────────────
st.markdown(
    f'<div style="background:linear-gradient(135deg,#003d2a,#005a3c);'
    f'border:1px solid rgba(201,168,76,0.3);border-{accent}:5px solid #C9A84C;'
    f'border-radius:20px;padding:32px 36px;margin-bottom:28px;'
    f'animation:slideIn 0.6s ease;text-align:{text_align};">'
    f'<div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;'
    f'color:#E8C97A;font-weight:700;margin-bottom:8px;font-family:JetBrains Mono,monospace;">'
    f'{"البنك الأهلي المصري" if is_ar else "National Bank of Egypt"}</div>'
    f'<h1 style="color:#C9A84C;font-family:Playfair Display,serif;'
    f'font-size:clamp(26px,3vw,38px);margin:0 0 10px;font-weight:900;">ℹ️ {t["page_title"]}</h1>'
    f'<p style="color:rgba(255,255,255,0.75);margin:0;font-size:15px;">{t["page_sub"]}</p>'
    f'</div>',
    unsafe_allow_html=True
)

# ── PROJECT OVERVIEW ──────────────────────────────────────────
st.markdown(
    f'<div class="info-card" style="border-{accent}:4px solid #C9A84C;animation-delay:0.05s;">'
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:22px;margin-bottom:14px;text-align:{text_align};">'
    f'🎯 {t["overview_title"]}</h2>'
    f'<p style="color:#333;line-height:2;font-size:15px;margin:0;text-align:{text_align};">'
    f'<strong style="color:#C9A84C;">{"منصة الذكاء الاصطناعي لتقييم مخاطر الائتمان" if is_ar else "NBE Credit Risk Intelligence Platform"}</strong> — '
    f'{t["overview_text"]}'
    f'</p></div>',
    unsafe_allow_html=True
)

# ── TECH + MODEL ──────────────────────────────────────────────
c1, c2 = st.columns(2)

with c1:
    techs = [
        ("🐍", "Python 3.11",      "#16a34a", "Core Language"),
        ("🌊", "Streamlit 1.31",   "#1d6fa8", "Web Framework"),
        ("🤖", "scikit-learn 1.4", "#C9A84C", "ML Engine"),
        ("📊", "Plotly 5.18",      "#6d3aad", "Visualization"),
        ("🐼", "Pandas 2.1",       "#c2410c", "Data Processing"),
        ("🔢", "NumPy 1.26",       "#be185d", "Numerical Computing"),
    ]
    rows_html = ""
    for icon, name, color, role in techs:
        rows_html += (
            f'<div class="tech-row">'
            f'<span style="font-size:24px;min-width:28px;text-align:center;">{icon}</span>'
            f'<div>'
            f'<div style="color:{color};font-weight:800;font-size:15px;">{name}</div>'
            f'<div style="color:#666;font-size:12px;">{role}</div>'
            f'</div></div>'
        )
    st.markdown(
        f'<div class="info-card" style="border-{accent}:4px solid #16a34a;animation-delay:0.15s;">'
        f'<h3 style="color:#003d2a;font-size:18px;margin-bottom:18px;font-weight:800;'
        f'font-family:Cairo,sans-serif;text-align:{text_align};">🔧 {t["tech_title"]}</h3>'
        f'{rows_html}</div>',
        unsafe_allow_html=True
    )

with c2:
    details = [
        (t['algorithm'],   "Random Forest",          "#C9A84C"),
        (t['version'],     "v4.0 (Production)",      "#16a34a"),
        (t['acc_label'],   "76.50%",                 "#1d6fa8"),
        (t['features'],    "73 engineered",          "#6d3aad"),
        (t['dataset'],     "German Credit (1,000)",  "#c2410c"),
        (t['compliance'],  "CBE Regulated",          "#be185d"),
    ]
    detail_rows = ""
    for label, value, color in details:
        detail_rows += (
            f'<div style="display:flex;justify-content:space-between;align-items:center;'
            f'padding:12px 14px;border-radius:12px;'
            f'background:rgba(0,99,65,0.04);border:1px solid rgba(0,99,65,0.1);'
            f'margin-bottom:10px;">'
            f'<span style="color:#555;font-size:13px;font-weight:600;">{label}</span>'
            f'<span style="color:{color};font-weight:800;font-size:14px;'
            f'font-family:JetBrains Mono,monospace;">{value}</span></div>'
        )
    st.markdown(
        f'<div class="info-card" style="border-{accent}:4px solid #1d6fa8;animation-delay:0.25s;">'
        f'<h3 style="color:#003d2a;font-size:18px;margin-bottom:18px;font-weight:800;'
        f'font-family:Cairo,sans-serif;text-align:{text_align};">📊 {t["model_title"]}</h3>'
        f'{detail_rows}</div>',
        unsafe_allow_html=True
    )

# ── ML PIPELINE ───────────────────────────────────────────────
st.markdown('---')
st.markdown(
    f'<h2 style="color:#003d2a;font-family:Playfair Display,serif;'
    f'font-size:22px;margin-bottom:20px;text-align:{text_align};">'
    f'🔄 {t["pipeline_title"]}</h2>',
    unsafe_allow_html=True
)

pipeline_steps = [
    ("📥", "Raw Data",        "#C9A84C"),
    ("🔧", "Preprocessing",   "#16a34a"),
    ("⚙️", "Feature Eng.",    "#1d6fa8"),
    ("⚖️", "Scaling",         "#6d3aad"),
    ("🤖", "Random Forest",   "#C9A84C"),
    ("📊", "Risk Score",      "#16a34a"),
    ("✅", "Decision",        "#be185d"),
]

steps_html = ""
for i, (icon, label, color) in enumerate(pipeline_steps):
    steps_html += (
        f'<div class="pipeline-step" style="border-top:3px solid {color};">'
        f'<div style="font-size:26px;margin-bottom:8px;">{icon}</div>'
        f'<div style="color:{color};font-size:12px;font-weight:800;">{label}</div>'
        f'</div>'
    )
    if i < len(pipeline_steps) - 1:
        steps_html += (
            f'<div style="color:#aaa;font-size:22px;font-weight:300;'
            f'padding:0 4px;">{"→" if not is_ar else "←"}</div>'
        )

st.markdown(
    f'<div class="info-card" style="animation-delay:0.35s;">'
    f'<div style="display:flex;flex-wrap:wrap;justify-content:center;'
    f'align-items:center;gap:8px;">{steps_html}</div>'
    f'</div>',
    unsafe_allow_html=True
)

# ── DEVELOPER CARD ────────────────────────────────────────────
st.markdown('---')
st.markdown(
    f'<div style="background:linear-gradient(135deg,#002a1d 0%,#003d2a 50%,#004d34 100%);'
    f'border:2px solid rgba(201,168,76,0.35);border-radius:24px;padding:48px 40px;'
    f'text-align:center;position:relative;overflow:hidden;'
    f'box-shadow:0 20px 60px rgba(0,61,42,0.25);animation:fadeInUp 0.6s ease 0.4s backwards;">'
    f'<div style="position:absolute;top:-50px;right:-50px;width:180px;height:180px;'
    f'border-radius:50%;border:2px solid rgba(201,168,76,0.08);"></div>'
    f'<div style="position:absolute;bottom:-50px;left:-50px;width:180px;height:180px;'
    f'border-radius:50%;border:2px solid rgba(201,168,76,0.08);"></div>'
    f'<div style="position:absolute;top:0;left:0;right:0;height:3px;'
    f'background:linear-gradient(90deg,transparent,#C9A84C,#E8C97A,#C9A84C,transparent);"></div>'
    f'<div style="width:96px;height:96px;'
    f'background:linear-gradient(135deg,#C9A84C,#a07a1e);'
    f'border-radius:50%;display:flex;align-items:center;justify-content:center;'
    f'font-size:44px;margin:0 auto 22px;'
    f'box-shadow:0 8px 30px rgba(201,168,76,0.4);'
    f'animation:pulseGlow 3s ease infinite;">👨‍💻</div>'
    f'<h2 style="color:#C9A84C;font-family:Playfair Display,serif;'
    f'font-size:30px;margin:0 0 10px;font-weight:900;">{t["dev_title"]}</h2>'
    f'<p style="color:rgba(255,255,255,0.65);font-size:15px;margin:0 0 28px;'
    f'line-height:1.7;">{t["dev_sub"]}</p>'
    f'<div style="height:1px;background:linear-gradient(90deg,transparent,rgba(201,168,76,0.4),transparent);'
    f'margin:0 auto 28px;max-width:400px;"></div>'
    f'<div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:28px;">'
    f'<a href="https://www.linkedin.com/in/goda-emad/" target="_blank" style="'
    f'display:flex;align-items:center;gap:8px;'
    f'background:rgba(10,102,194,0.2);border:2px solid rgba(10,102,194,0.5);'
    f'color:#60a5fa;padding:13px 26px;border-radius:14px;text-decoration:none;'
    f'font-size:15px;font-weight:700;font-family:Cairo,sans-serif;'
    f'transition:all 0.3s;"'
    f'onmouseover="this.style.background=\'rgba(10,102,194,0.4)\';this.style.transform=\'translateY(-3px)\';"'
    f'onmouseout="this.style.background=\'rgba(10,102,194,0.2)\';this.style.transform=\'translateY(0)\';">'
    f'🔗 LinkedIn Profile</a>'
    f'<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank" style="'
    f'display:flex;align-items:center;gap:8px;'
    f'background:rgba(255,255,255,0.08);border:2px solid rgba(255,255,255,0.25);'
    f'color:#fff;padding:13px 26px;border-radius:14px;text-decoration:none;'
    f'font-size:15px;font-weight:700;font-family:Cairo,sans-serif;'
    f'transition:all 0.3s;"'
    f'onmouseover="this.style.background=\'rgba(255,255,255,0.18)\';this.style.transform=\'translateY(-3px)\';"'
    f'onmouseout="this.style.background=\'rgba(255,255,255,0.08)\';this.style.transform=\'translateY(0)\';">'
    f'⭐ GitHub Project</a>'
    f'</div>'
    f'<p style="color:rgba(255,255,255,0.3);font-size:12px;margin:0;">{t["footer_copy"]}</p>'
    f'</div>',
    unsafe_allow_html=True
)

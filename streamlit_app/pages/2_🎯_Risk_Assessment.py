"""NBE Credit Risk Intelligence - Risk Assessment Page (Enhanced v4.0)"""
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Risk Assessment | NBE",
    page_icon="🎯",
    layout="wide"
)

if 'language' not in st.session_state:
    st.session_state.language = 'ar'

lang = st.session_state.language
is_ar = lang == 'ar'
direction  = 'rtl' if is_ar else 'ltr'
text_align = 'right' if is_ar else 'left'

T = {
    'ar': {
        'page_title': 'تقييم مخاطر الائتمان',
        'page_sub':   'تقييم ذكي بالوقت الفعلي — Random Forest v4.0',
        'form_title': 'بيانات طلب القرض',
        'sec1': 'المعلومات الشخصية',
        'sec2': 'التفاصيل المالية',
        'sec3': 'التوظيف والسكن',
        'sec4': 'معلومات الائتمان',
        'age': 'العمر (سنة)',
        'personal': 'الحالة الاجتماعية',
        'foreign': 'عامل أجنبي',
        'credit_amount': 'مبلغ القرض (DM)',
        'duration': 'المدة (شهر)',
        'installment': 'معدل القسط (%)',
        'account_status': 'حالة الحساب',
        'savings': 'حساب التوفير',
        'existing_credits': 'القروض الحالية',
        'employment': 'مدة العمل',
        'housing': 'السكن',
        'job': 'نوع الوظيفة',
        'residence': 'سنوات الإقامة',
        'dependents': 'المعالين',
        'telephone': 'الهاتف',
        'credit_history': 'تاريخ الائتمان',
        'purpose': 'الغرض من القرض',
        'other_debtors': 'مدينون آخرون',
        'property': 'الممتلكات',
        'other_plans': 'خطط أقساط أخرى',
        'submit': '🔍 تقييم مخاطر الائتمان',
        'results_title': 'نتائج التقييم',
        'low_risk': 'مخاطر منخفضة',
        'med_risk': 'مخاطر متوسطة',
        'high_risk': 'مخاطر عالية',
        'approved': 'موافق عليه',
        'review': 'يحتاج مراجعة',
        'rejected': 'مرفوض',
        'risk_score': 'درجة المخاطرة',
        'good_prob': 'احتمال السداد',
        'bad_prob':  'احتمال التعثر',
        'rec_low':  'التوصية: المضي بشروط القرض القياسية. العميل يُظهر جدارة ائتمانية قوية.',
        'rec_med':  'التوصية: مراجعة يدوية مطلوبة. يُنصح بطلب تحقق إضافي من الدخل أو تخفيض مبلغ القرض بنسبة 20%.',
        'rec_high': 'التوصية: احتمال تعثر عالٍ. يُنصح بطلب ضمانات (150% من قيمة القرض) أو رفض الطلب.',
        'footer_copy': '© 2026 البنك الأهلي المصري | م. جودة عماد | الإصدار 4.0',
        'model_active': 'النموذج نشط',
        'accuracy': 'الدقة: 76.5%',
        'lang_label': 'اللغة',
        'decision': 'القرار',
        'rec_label': 'التوصية',
    },
    'en': {
        'page_title': 'Credit Risk Assessment',
        'page_sub':   'AI-powered real-time evaluation — Random Forest v4.0',
        'form_title': 'Application Details',
        'sec1': 'Personal Information',
        'sec2': 'Financial Details',
        'sec3': 'Employment & Housing',
        'sec4': 'Credit Information',
        'age': 'Age (years)',
        'personal': 'Personal Status',
        'foreign': 'Foreign Worker',
        'credit_amount': 'Credit Amount (DM)',
        'duration': 'Duration (months)',
        'installment': 'Installment Rate (%)',
        'account_status': 'Account Status',
        'savings': 'Savings Account',
        'existing_credits': 'Existing Credits',
        'employment': 'Employment Duration',
        'housing': 'Housing',
        'job': 'Job Type',
        'residence': 'Years at Residence',
        'dependents': 'Num Dependents',
        'telephone': 'Telephone',
        'credit_history': 'Credit History',
        'purpose': 'Loan Purpose',
        'other_debtors': 'Other Debtors',
        'property': 'Property',
        'other_plans': 'Other Installment Plans',
        'submit': '🔍 Assess Credit Risk',
        'results_title': 'Assessment Results',
        'low_risk': 'LOW RISK',
        'med_risk': 'MEDIUM RISK',
        'high_risk': 'HIGH RISK',
        'approved': 'APPROVED',
        'review': 'REVIEW',
        'rejected': 'REJECTED',
        'risk_score': 'Risk Score',
        'good_prob': 'Good Probability',
        'bad_prob':  'Bad Probability',
        'rec_low':  'Recommendation: Proceed with standard loan terms. Customer shows strong creditworthiness.',
        'rec_med':  'Recommendation: Manual review required. Consider requesting additional income verification or reducing loan amount by 20%.',
        'rec_high': 'Recommendation: High default probability. Consider requiring collateral (150% of loan value) or reject application.',
        'footer_copy': '© 2026 National Bank of Egypt | ENG. Goda Emad | Version 4.0',
        'model_active': 'Model Active',
        'accuracy': 'Accuracy: 76.5%',
        'lang_label': 'Language',
        'decision': 'Decision',
        'rec_label': 'Recommendation',
    }
}
t = T[lang]

OPTIONS = {
    'Status_Account':  {'A11':'< 0 DM (Overdrawn)','A12':'0-200 DM','A13':'>= 200 DM','A14':'No Account'},
    'Credit_History':  {'A30':'All Paid','A31':'Paid at Bank','A32':'Existing Paid','A33':'Delay in Past','A34':'Critical Account'},
    'Purpose':         {'A40':'New Car','A41':'Used Car','A42':'Furniture','A43':'Radio/TV','A44':'Appliances','A45':'Repairs','A46':'Education','A48':'Retraining','A49':'Business','A410':'Other'},
    'Savings':         {'A61':'< 100 DM','A62':'100-500 DM','A63':'500-1000 DM','A64':'>= 1000 DM','A65':'Unknown'},
    'Employment':      {'A71':'Unemployed','A72':'< 1 Year','A73':'1-4 Years','A74':'4-7 Years','A75':'>= 7 Years'},
    'Personal_Status': {'A91':'Male Divorced','A92':'Female','A93':'Male Single','A94':'Male Married'},
    'Other_Debtors':   {'A101':'None','A102':'Co-applicant','A103':'Guarantor'},
    'Property':        {'A121':'Real Estate','A122':'Life Insurance','A123':'Car/Other','A124':'No Property'},
    'Other_Plans':     {'A141':'Bank','A142':'Stores','A143':'None'},
    'Housing':         {'A151':'Rent','A152':'Own','A153':'For Free'},
    'Job':             {'A171':'Unskilled Non-Resident','A172':'Unskilled Resident','A173':'Skilled','A174':'Management'},
    'Telephone':       {'A191':'None','A192':'Registered'},
    'Foreign_Worker':  {'A201':'Yes','A202':'No'},
}

def make_label(d): return list(d.values())
def get_key(d, v): return list(d.keys())[list(d.values()).index(v)]

# ── CSS ───────────────────────────────────────────────────────
css = (
    '@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900'
    '&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap");'
    ':root {'
    '  --gold:#C9A84C; --gold-l:#E8C97A;'
    '  --bg:#001f15; --border:rgba(201,168,76,0.25); --gray:#8a9bb0;'
    '}'
    'html,body,[class*="css"]{'
    f'  font-family:Cairo,sans-serif!important;'
    f'  background:#001f15!important;color:#fff!important;direction:{direction};}}'
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
    '.stSelectbox>div>div,.stNumberInput>div>div>input{'
    '  background:rgba(255,255,255,0.05)!important;'
    '  border:1px solid rgba(201,168,76,0.2)!important;'
    '  border-radius:10px!important;color:#fff!important;}'
    '.stSelectbox label,.stNumberInput label,.stSlider label{'
    '  color:rgba(255,255,255,0.75)!important;font-weight:600!important;font-size:13px!important;}'
    '[data-testid="stMetricValue"]{'
    '  color:#C9A84C!important;font-size:2rem!important;'
    '  font-weight:900!important;font-family:JetBrains Mono,monospace!important;'
    '  animation:countAnim 0.7s cubic-bezier(0.34,1.56,0.64,1) forwards;}'
    '[data-testid="stMetricLabel"]{color:#8a9bb0!important;font-size:12px!important;'
    '  font-weight:700!important;text-transform:uppercase;letter-spacing:0.5px;}'
    '[data-testid="metric-container"]{'
    '  background:rgba(255,255,255,0.04)!important;'
    '  border:1px solid rgba(201,168,76,0.2)!important;'
    '  border-top:3px solid #C9A84C!important;'
    '  border-radius:14px!important;padding:18px 20px!important;'
    '  transition:transform 0.3s,box-shadow 0.3s!important;}'
    '[data-testid="metric-container"]:hover{transform:translateY(-4px)!important;'
    '  box-shadow:0 12px 30px rgba(201,168,76,0.15)!important;}'
    '.stButton>button{'
    '  background:linear-gradient(135deg,#C9A84C,#a07a1e)!important;'
    '  color:#001208!important;font-weight:800!important;border:none!important;'
    '  border-radius:12px!important;padding:16px 32px!important;'
    '  font-size:17px!important;width:100%!important;'
    '  font-family:Cairo,sans-serif!important;'
    '  box-shadow:0 6px 20px rgba(201,168,76,0.4)!important;'
    '  transition:all 0.3s!important;}'
    '.stButton>button:hover{'
    '  transform:translateY(-3px)!important;'
    '  box-shadow:0 12px 35px rgba(201,168,76,0.6)!important;}'
    '@keyframes countAnim{from{opacity:0;transform:scale(0.5) translateY(20px)}'
    '  to{opacity:1;transform:scale(1) translateY(0)}}'
    '@keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}'
    '  to{opacity:1;transform:translateY(0)}}'
    '@keyframes slideIn{from{opacity:0;transform:translateX(-30px)}'
    '  to{opacity:1;transform:translateX(0)}}'
    '@keyframes pulseResult{0%,100%{box-shadow:0 0 20px rgba(201,168,76,0.15)}'
    '  50%{box-shadow:0 0 50px rgba(201,168,76,0.4)}}'
    '@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}'
    'hr{border-color:rgba(201,168,76,0.15)!important;margin:2rem 0!important;}'
    '.sec-card{border-radius:16px;padding:20px 24px;margin-bottom:20px;'
    '  animation:fadeInUp 0.5s ease backwards;}'
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

# ── Load Model ────────────────────────────────────────────────
@st.cache_resource(show_spinner='🤖 Loading AI Model...')
def load_model():
    paths = [
        Path(__file__).parent.parent.parent / 'models',
        Path('models'), Path('../models'),
    ]
    for p in paths:
        if (p / 'final_model.pkl').exists():
            with open(p / 'final_model.pkl',         'rb') as f: model    = pickle.load(f)
            with open(p / 'scaler_final.pkl',        'rb') as f: scaler   = pickle.load(f)
            with open(p / 'feature_names_final.pkl', 'rb') as f: features = pickle.load(f)
            return model, scaler, features
    return None, None, None

model, scaler, feature_names = load_model()
if model is None:
    st.error('Model files not found! Please check models/ directory.')
    st.stop()

# ── Page Header ───────────────────────────────────────────────
accent = 'right' if is_ar else 'left'
st.markdown(
    f'<div style="background:linear-gradient(135deg,rgba(0,18,8,0.95),rgba(0,42,29,0.95));'
    f'border:1px solid rgba(201,168,76,0.3);border-{accent}:5px solid #C9A84C;'
    f'border-radius:20px;padding:32px 36px;margin-bottom:28px;'
    f'animation:slideIn 0.6s ease;text-align:{text_align};">'
    f'<div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;'
    f'color:#E8C97A;font-weight:700;margin-bottom:8px;font-family:JetBrains Mono,monospace;">'
    f'{"البنك الأهلي المصري" if is_ar else "National Bank of Egypt"}</div>'
    f'<h1 style="color:#C9A84C;font-family:Playfair Display,serif;'
    f'font-size:clamp(26px,3vw,38px);margin:0 0 10px;font-weight:900;">🎯 {t["page_title"]}</h1>'
    f'<p style="color:rgba(255,255,255,0.6);margin:0;font-size:15px;">{t["page_sub"]}</p>'
    f'</div>',
    unsafe_allow_html=True
)

# ── Form ──────────────────────────────────────────────────────
st.markdown(
    f'<h2 style="color:#fff;font-family:Cairo,sans-serif;'
    f'font-size:20px;margin-bottom:18px;text-align:{text_align};">'
    f'📋 {t["form_title"]}</h2>',
    unsafe_allow_html=True
)

def sec_header(icon, title, color, bg, delay):
    st.markdown(
        f'<div class="sec-card" style="background:{bg};border:1px solid {color}40;'
        f'border-{accent}:4px solid {color};animation-delay:{delay}s;">'
        f'<h3 style="color:{color};margin:0 0 18px;font-size:16px;font-weight:800;'
        f'font-family:Cairo,sans-serif;text-align:{text_align};">{icon} {title}</h3>',
        unsafe_allow_html=True
    )

def sec_end():
    st.markdown('</div>', unsafe_allow_html=True)

with st.form('credit_form', clear_on_submit=False):

    sec_header('👤', t['sec1'], '#C9A84C', 'rgba(201,168,76,0.06)', 0.0)
    c1, c2, c3 = st.columns(3)
    with c1: age      = st.number_input(t['age'],      19, 75, 35)
    with c2: personal = st.selectbox(t['personal'],    make_label(OPTIONS['Personal_Status']))
    with c3: foreign  = st.selectbox(t['foreign'],     make_label(OPTIONS['Foreign_Worker']))
    sec_end()

    sec_header('💰', t['sec2'], '#60a5fa', 'rgba(96,165,250,0.05)', 0.1)
    c1, c2, c3 = st.columns(3)
    with c1: credit_amount   = st.number_input(t['credit_amount'], 250, 20000, 5000, 100)
    with c2: duration        = st.number_input(t['duration'],        4,    72,   24)
    with c3: installment     = st.number_input(t['installment'],     1,     4,    2)
    c1, c2, c3 = st.columns(3)
    with c1: status_account  = st.selectbox(t['account_status'],  make_label(OPTIONS['Status_Account']))
    with c2: savings         = st.selectbox(t['savings'],          make_label(OPTIONS['Savings']))
    with c3: existing_credits = st.number_input(t['existing_credits'], 1, 4, 1)
    sec_end()

    sec_header('🏠', t['sec3'], '#4ade80', 'rgba(74,222,128,0.05)', 0.2)
    c1, c2, c3 = st.columns(3)
    with c1: employment = st.selectbox(t['employment'], make_label(OPTIONS['Employment']))
    with c2: housing    = st.selectbox(t['housing'],    make_label(OPTIONS['Housing']))
    with c3: job        = st.selectbox(t['job'],        make_label(OPTIONS['Job']))
    c1, c2, c3 = st.columns(3)
    with c1: residence  = st.number_input(t['residence'],  1, 4, 2)
    with c2: dependents = st.number_input(t['dependents'], 1, 2, 1)
    with c3: telephone  = st.selectbox(t['telephone'],  make_label(OPTIONS['Telephone']))
    sec_end()

    sec_header('📄', t['sec4'], '#a78bfa', 'rgba(167,139,250,0.05)', 0.3)
    c1, c2, c3 = st.columns(3)
    with c1: credit_history = st.selectbox(t['credit_history'], make_label(OPTIONS['Credit_History']))
    with c2: purpose        = st.selectbox(t['purpose'],        make_label(OPTIONS['Purpose']))
    with c3: other_debtors  = st.selectbox(t['other_debtors'],  make_label(OPTIONS['Other_Debtors']))
    c1, c2, c3 = st.columns(3)
    with c1: property_   = st.selectbox(t['property'],    make_label(OPTIONS['Property']))
    with c2: other_plans = st.selectbox(t['other_plans'], make_label(OPTIONS['Other_Plans']))
    with c3: pass
    sec_end()

    submitted = st.form_submit_button(t['submit'], use_container_width=True)

# ── Prediction ────────────────────────────────────────────────
if submitted:
    input_data = {
        'Status_Account':   get_key(OPTIONS['Status_Account'],   status_account),
        'Duration':         duration,
        'Credit_History':   get_key(OPTIONS['Credit_History'],   credit_history),
        'Purpose':          get_key(OPTIONS['Purpose'],          purpose),
        'Credit_Amount':    credit_amount,
        'Savings':          get_key(OPTIONS['Savings'],          savings),
        'Employment':       get_key(OPTIONS['Employment'],       employment),
        'Installment_Rate': installment,
        'Personal_Status':  get_key(OPTIONS['Personal_Status'],  personal),
        'Other_Debtors':    get_key(OPTIONS['Other_Debtors'],    other_debtors),
        'Residence_Since':  residence,
        'Property':         get_key(OPTIONS['Property'],         property_),
        'Age':              age,
        'Other_Plans':      get_key(OPTIONS['Other_Plans'],      other_plans),
        'Housing':          get_key(OPTIONS['Housing'],          housing),
        'Existing_Credits': existing_credits,
        'Job':              get_key(OPTIONS['Job'],              job),
        'Num_Dependents':   dependents,
        'Telephone':        get_key(OPTIONS['Telephone'],        telephone),
        'Foreign_Worker':   get_key(OPTIONS['Foreign_Worker'],   foreign),
    }

    df = pd.DataFrame([input_data])
    df['age_young']  = (df['Age'] < 25).astype(int)
    df['age_middle'] = ((df['Age'] >= 25) & (df['Age'] < 60)).astype(int)
    df['age_senior'] = (df['Age'] >= 60).astype(int)
    df['credit_low']    = (df['Credit_Amount'] < 2500).astype(int)
    df['credit_medium'] = ((df['Credit_Amount'] >= 2500) & (df['Credit_Amount'] < 5000)).astype(int)
    df['credit_high']   = (df['Credit_Amount'] >= 5000).astype(int)
    df['duration_short']  = (df['Duration'] <= 12).astype(int)
    df['duration_medium'] = ((df['Duration'] > 12) & (df['Duration'] <= 24)).astype(int)
    df['duration_long']   = (df['Duration'] > 24).astype(int)
    df['credit_duration_ratio']  = df['Credit_Amount'] / (df['Duration'] + 1)
    df['credit_age_ratio']       = df['Credit_Amount'] / (df['Age'] + 1)
    df['age_credit_interaction'] = df['Age'] * df['Credit_Amount'] / 1000

    cat_cols = ['Status_Account','Credit_History','Purpose','Savings','Employment',
                'Personal_Status','Other_Debtors','Property','Other_Plans','Housing',
                'Job','Telephone','Foreign_Worker']
    df = pd.get_dummies(df, columns=cat_cols, drop_first=False, dtype=int)
    for feat in feature_names:
        if feat not in df.columns:
            df[feat] = 0
    df = df[feature_names]

    X_scaled = scaler.transform(df)
    pred     = model.predict(X_scaled)[0]
    proba    = model.predict_proba(X_scaled)[0]
    score    = float(proba[1]) * 100

    if score >= 70:
        risk_cat = t['low_risk'];  border_c = '#4ade80'; bg_c = 'rgba(74,222,128,0.08)';  icon = '✅'; decision = t['approved']; rec = t['rec_low']
    elif score >= 50:
        risk_cat = t['med_risk'];  border_c = '#fbbf24'; bg_c = 'rgba(251,191,36,0.08)';  icon = '⚠️'; decision = t['review'];   rec = t['rec_med']
    else:
        risk_cat = t['high_risk']; border_c = '#f87171'; bg_c = 'rgba(248,113,113,0.08)'; icon = '❌'; decision = t['rejected']; rec = t['rec_high']

    st.markdown('---')

    st.markdown(
        f'<h2 style="color:#C9A84C;font-family:Playfair Display,serif;'
        f'font-size:28px;margin-bottom:20px;text-align:{text_align};">'
        f'📊 {t["results_title"]}</h2>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown(
            f'<div style="background:{bg_c};border:2px solid {border_c};'
            f'border-radius:24px;padding:36px;text-align:center;margin-bottom:20px;'
            f'animation:pulseResult 3s ease infinite;">'
            f'<div style="font-size:72px;margin-bottom:14px;">{icon}</div>'
            f'<div style="color:{border_c};font-size:26px;font-weight:800;'
            f'font-family:Cairo,sans-serif;margin-bottom:10px;">{risk_cat}</div>'
            f'<div style="color:rgba(255,255,255,0.75);font-size:18px;margin-bottom:20px;">'
            f'{t["decision"]}: <strong style="color:{border_c};font-size:20px;">{decision}</strong></div>'
            f'<div style="background:rgba(0,0,0,0.25);border-radius:16px;'
            f'padding:20px;display:inline-block;min-width:200px;">'
            f'<div style="color:rgba(255,255,255,0.5);font-size:12px;text-transform:uppercase;'
            f'letter-spacing:2px;margin-bottom:6px;">{t["risk_score"]}</div>'
            f'<div style="color:{border_c};font-size:52px;font-weight:900;'
            f'font-family:JetBrains Mono,monospace;line-height:1;">{score:.1f}%</div>'
            f'</div></div>',
            unsafe_allow_html=True
        )
        m1, m2 = st.columns(2)
        with m1: st.metric(t['good_prob'], f'{proba[1]*100:.1f}%')
        with m2: st.metric(t['bad_prob'],  f'{proba[0]*100:.1f}%')

    with c2:
        gc = '#4ade80' if score >= 70 else ('#fbbf24' if score >= 50 else '#f87171')
        fig = go.Figure(go.Indicator(
            mode='gauge+number',
            value=score,
            number={'suffix':'%', 'font': {'size':40, 'color':gc, 'family':'JetBrains Mono'}},
            title={'text': t['risk_score'], 'font': {'size':16, 'color':'#ffffff', 'family':'Cairo'}},
            gauge={
                'axis': {'range':[0,100], 'tickcolor':'#444', 'tickfont': {'color':'#888'}},
                'bar':  {'color':gc, 'thickness':0.25},
                'bgcolor': 'rgba(0,0,0,0)',
                'bordercolor': '#2a2a2a',
                'steps': [
                    {'range':[0,50],   'color':'rgba(248,113,113,0.12)'},
                    {'range':[50,70],  'color':'rgba(251,191,36,0.12)'},
                    {'range':[70,100], 'color':'rgba(74,222,128,0.12)'},
                ],
                'threshold': {
                    'line': {'color':gc, 'width':5},
                    'thickness':0.8, 'value':score
                }
            }
        ))
        fig.update_layout(
            height=320,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color':'#fff','family':'Cairo'},
            margin=dict(t=50,b=10,l=20,r=20)
        )
        st.plotly_chart(fig, use_container_width=True)

        good_w = f'{proba[1]*100:.1f}'
        bad_w  = f'{proba[0]*100:.1f}'
        st.markdown(
            f'<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(201,168,76,0.15);'
            f'border-radius:16px;padding:20px;margin-top:8px;">'
            f'<div style="margin-bottom:14px;">'
            f'<div style="display:flex;justify-content:space-between;margin-bottom:6px;">'
            f'<span style="color:#4ade80;font-size:13px;font-weight:700;">✅ {t["good_prob"]}</span>'
            f'<span style="color:#4ade80;font-weight:800;font-family:JetBrains Mono,monospace;">{good_w}%</span></div>'
            f'<div style="height:10px;background:rgba(255,255,255,0.06);border-radius:5px;overflow:hidden;">'
            f'<div style="height:10px;width:{good_w}%;background:linear-gradient(90deg,#15803d,#4ade80);border-radius:5px;"></div></div></div>'
            f'<div>'
            f'<div style="display:flex;justify-content:space-between;margin-bottom:6px;">'
            f'<span style="color:#f87171;font-size:13px;font-weight:700;">❌ {t["bad_prob"]}</span>'
            f'<span style="color:#f87171;font-weight:800;font-family:JetBrains Mono,monospace;">{bad_w}%</span></div>'
            f'<div style="height:10px;background:rgba(255,255,255,0.06);border-radius:5px;overflow:hidden;">'
            f'<div style="height:10px;width:{bad_w}%;background:linear-gradient(90deg,#991b1b,#f87171);border-radius:5px;"></div></div></div>'
            f'</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div style="background:rgba(255,255,255,0.03);border:1px solid {border_c}40;'
        f'border-{accent}:5px solid {border_c};border-radius:16px;'
        f'padding:22px 28px;margin-top:20px;animation:fadeInUp 0.6s ease;">'
        f'<div style="color:{border_c};font-size:13px;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:2px;margin-bottom:10px;">'
        f'💡 {t["rec_label"]}</div>'
        f'<div style="color:rgba(255,255,255,0.85);font-size:15px;line-height:1.8;">{rec}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# ── Footer ────────────────────────────────────────────────────
st.markdown('---')
st.markdown(
    f'<div style="background:linear-gradient(135deg,#001208,#001f15);'
    f'border:1px solid rgba(201,168,76,0.2);border-radius:16px;'
    f'padding:24px 32px;display:flex;flex-wrap:wrap;'
    f'justify-content:space-between;align-items:center;gap:16px;">'
    f'<div style="color:rgba(255,255,255,0.4);font-size:13px;">{t["footer_copy"]}</div>'
    f'<div style="display:flex;gap:10px;">'
    f'<a href="https://www.linkedin.com/in/goda-emad/" target="_blank" style="'
    f'background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.4);'
    f'color:#60a5fa;padding:8px 16px;border-radius:10px;text-decoration:none;'
    f'font-size:13px;font-weight:600;"'
    f'onmouseover="this.style.background=\'rgba(10,102,194,0.35)\';"'
    f'onmouseout="this.style.background=\'rgba(10,102,194,0.2)\';">🔗 LinkedIn</a>'
    f'<a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank" style="'
    f'background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.15);'
    f'color:rgba(255,255,255,0.8);padding:8px 16px;border-radius:10px;text-decoration:none;'
    f'font-size:13px;font-weight:600;"'
    f'onmouseover="this.style.background=\'rgba(255,255,255,0.12)\';"'
    f'onmouseout="this.style.background=\'rgba(255,255,255,0.05)\';">⭐ GitHub</a>'
    f'</div></div>',
    unsafe_allow_html=True
)

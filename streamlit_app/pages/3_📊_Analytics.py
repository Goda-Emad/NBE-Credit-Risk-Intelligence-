"""NBE Credit Risk Intelligence - Analytics Page (Enhanced v4.0)"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Analytics | NBE", page_icon="📊", layout="wide")

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
        'page_title':    'تحليلات المحفظة',
        'page_sub':      'رؤى شاملة للمحفظة الائتمانية وتحليل الاتجاهات',
        'total_apps':    'إجمالي الطلبات',
        'good_risk':     'مخاطر منخفضة',
        'bad_risk':      'مخاطر عالية',
        'avg_credit':    'متوسط القرض',
        'chart1':        'توزيع المخاطر',
        'chart2':        'توزيع العمر حسب المخاطر',
        'chart3':        'مبلغ القرض حسب المخاطر',
        'chart4':        'المدة مقابل مبلغ القرض',
        'chart5':        'الغرض من القرض',
        'chart6':        'توزيع حسب العمل',
        'stats_title':   'الملخص الإحصائي',
        'good_label':    'مخاطر منخفضة',
        'bad_label':     'مخاطر عالية',
        'age_axis':      'العمر',
        'count_axis':    'العدد',
        'credit_axis':   'مبلغ القرض (DM)',
        'duration_axis': 'المدة (شهر)',
        'model_active':  'النموذج نشط',
        'accuracy':      'الدقة: 76.5%',
        'footer_copy':   '© 2026 البنك الأهلي المصري | م. جودة عماد | الإصدار 4.0',
        'data_error':    'البيانات غير موجودة!',
    },
    'en': {
        'lang_label':    'Language',
        'page_title':    'Portfolio Analytics',
        'page_sub':      'Comprehensive credit portfolio insights and trend analysis',
        'total_apps':    'Total Applications',
        'good_risk':     'Good Risk',
        'bad_risk':      'Bad Risk',
        'avg_credit':    'Avg Credit',
        'chart1':        'Risk Distribution',
        'chart2':        'Age Distribution by Risk',
        'chart3':        'Credit Amount by Risk',
        'chart4':        'Duration vs Credit Amount',
        'chart5':        'Loan Purpose Breakdown',
        'chart6':        'Job Type Distribution',
        'stats_title':   'Statistical Summary',
        'good_label':    'Good Risk',
        'bad_label':     'Bad Risk',
        'age_axis':      'Age',
        'count_axis':    'Count',
        'credit_axis':   'Credit Amount (DM)',
        'duration_axis': 'Duration (months)',
        'model_active':  'Model Active',
        'accuracy':      'Accuracy: 76.5%',
        'footer_copy':   '© 2026 National Bank of Egypt | ENG. Goda Emad | Version 4.0',
        'data_error':    'Data not found!',
    }
}
t = T[lang]

css = (
    '@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900'
    '&family=Cairo:wght@300;400;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap");'
    ':root{'
    '  --gold:#C9A84C;--gold-l:#E8C97A;--bg:#001f15;'
    '  --border:rgba(201,168,76,0.2);--gray:#8a9bb0;'
    '}'
    'html,body,[class*="css"]{'
    '  font-family:Cairo,sans-serif!important;'
    '  background:#001f15!important;color:#fff!important;'
    f'  direction:{direction};}}'
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
    '[data-testid="stMetricValue"]{'
    '  color:#C9A84C!important;font-size:2.2rem!important;font-weight:900!important;'
    '  font-family:JetBrains Mono,monospace!important;'
    '  animation:countAnim 0.7s cubic-bezier(0.34,1.56,0.64,1) forwards;}'
    '[data-testid="stMetricLabel"]{color:#8a9bb0!important;font-size:12px!important;'
    '  font-weight:700!important;text-transform:uppercase;letter-spacing:0.5px;}'
    '[data-testid="metric-container"]{'
    '  background:rgba(255,255,255,0.04)!important;'
    '  border:1px solid rgba(201,168,76,0.2)!important;'
    '  border-top:3px solid #C9A84C!important;'
    '  border-radius:14px!important;padding:18px 20px!important;'
    '  transition:transform 0.3s,box-shadow 0.3s!important;}'
    '[data-testid="metric-container"]:hover{transform:translateY(-5px)!important;'
    '  box-shadow:0 12px 30px rgba(201,168,76,0.15)!important;}'
    '.chart-card{'
    '  background:rgba(255,255,255,0.03);border:1px solid rgba(201,168,76,0.15);'
    '  border-radius:18px;padding:24px;margin-bottom:24px;'
    '  transition:all 0.3s ease;animation:fadeInUp 0.5s ease backwards;}'
    '.chart-card:hover{'
    '  border-color:rgba(201,168,76,0.35);'
    '  box-shadow:0 8px 32px rgba(0,61,42,0.3);}'
    '.chart-title{'
    '  font-size:16px;font-weight:800;color:#C9A84C;'
    f'  font-family:Cairo,sans-serif;margin-bottom:16px;text-align:{text_align};}}'
    '@keyframes countAnim{from{opacity:0;transform:scale(0.5) translateY(20px)}'
    '  to{opacity:1;transform:scale(1) translateY(0)}}'
    '@keyframes fadeInUp{from{opacity:0;transform:translateY(25px)}'
    '  to{opacity:1;transform:translateY(0)}}'
    '@keyframes slideIn{from{opacity:0;transform:translateX(-30px)}'
    '  to{opacity:1;transform:translateX(0)}}'
    '@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}'
    'hr{border-color:rgba(201,168,76,0.15)!important;margin:2rem 0!important;}'
    '[data-testid="stDataFrame"]{border-radius:12px;overflow:hidden;}'
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

# ── Load Data ─────────────────────────────────────────────────
@st.cache_data
def load_data():
    paths = [
        Path(__file__).parent.parent.parent / 'data/processed/german_credit_fe_v3.csv',
        Path('data/processed/german_credit_fe_v3.csv'),
    ]
    for p in paths:
        if p.exists():
            return pd.read_csv(p)
    return None

df = load_data()
if df is None:
    st.error(f'⚠️ {t["data_error"]}')
    st.stop()

# ── Page Header ───────────────────────────────────────────────
st.markdown(
    f'<div style="background:linear-gradient(135deg,rgba(0,18,8,0.95),rgba(0,42,29,0.95));'
    f'border:1px solid rgba(201,168,76,0.3);border-{accent}:5px solid #C9A84C;'
    f'border-radius:20px;padding:32px 36px;margin-bottom:28px;'
    f'animation:slideIn 0.6s ease;text-align:{text_align};">'
    f'<div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;'
    f'color:#E8C97A;font-weight:700;margin-bottom:8px;font-family:JetBrains Mono,monospace;">'
    f'{"البنك الأهلي المصري" if is_ar else "National Bank of Egypt"}</div>'
    f'<h1 style="color:#C9A84C;font-family:Playfair Display,serif;'
    f'font-size:clamp(26px,3vw,38px);margin:0 0 10px;font-weight:900;">📊 {t["page_title"]}</h1>'
    f'<p style="color:rgba(255,255,255,0.6);margin:0;font-size:15px;">{t["page_sub"]}</p>'
    f'</div>',
    unsafe_allow_html=True
)

# ── KPIs ──────────────────────────────────────────────────────
good_count = (df['Risk'] == 1).sum()
bad_count  = (df['Risk'] == 0).sum()
good_pct   = (df['Risk'] == 1).mean() * 100
bad_pct    = (df['Risk'] == 0).mean() * 100
avg_credit = df['Credit_Amount'].mean()

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric(f'📋 {t["total_apps"]}', f'{len(df):,}')
with c2: st.metric(f'✅ {t["good_risk"]}',  f'{good_count:,}', f'{good_pct:.1f}%')
with c3: st.metric(f'❌ {t["bad_risk"]}',   f'{bad_count:,}',  f'{bad_pct:.1f}%')
with c4: st.metric(f'💰 {t["avg_credit"]}', f'{avg_credit:,.0f} DM')

st.markdown('---')

# ── Chart Config ──────────────────────────────────────────────
GOOD_C = '#4ade80'
BAD_C  = '#f87171'
GOLD_C = '#C9A84C'
BLUE_C = '#60a5fa'
PURPLE_C = '#a78bfa'

LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#ffffff', family='Cairo'),
    margin=dict(t=20, b=30, l=20, r=20),
    legend=dict(
        bgcolor='rgba(255,255,255,0.05)',
        bordercolor='rgba(201,168,76,0.2)',
        borderwidth=1,
        font=dict(size=13)
    )
)

def chart_wrap(title, delay, content_fn):
    st.markdown(
        f'<div class="chart-card" style="animation-delay:{delay}s;">'
        f'<div class="chart-title">📈 {title}</div>',
        unsafe_allow_html=True
    )
    content_fn()
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 1: Donut + Age Histogram ──────────────────────────────
c1, c2 = st.columns(2)

with c1:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.1s;">'
        f'<div class="chart-title">🍩 {t["chart1"]}</div>',
        unsafe_allow_html=True
    )
    rc = df['Risk'].value_counts()
    fig = go.Figure(go.Pie(
        labels=[t['bad_label'], t['good_label']],
        values=[rc.get(0, 0), rc.get(1, 0)],
        hole=0.55,
        marker_colors=[BAD_C, GOOD_C],
        textfont=dict(size=13, color='#ffffff'),
        textinfo='label+percent',
    ))
    fig.update_layout(
        **LAYOUT, height=300,
        annotations=[dict(
            text=f'<b>{len(df)}</b>',
            x=0.5, y=0.5, font_size=22,
            font_color='#C9A84C', showarrow=False
        )]
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.2s;">'
        f'<div class="chart-title">👥 {t["chart2"]}</div>',
        unsafe_allow_html=True
    )
    fig = go.Figure()
    for risk, label, color in [(0, t['bad_label'], BAD_C), (1, t['good_label'], GOOD_C)]:
        fig.add_trace(go.Histogram(
            x=df[df['Risk'] == risk]['Age'],
            name=label, marker_color=color,
            opacity=0.75, nbinsx=15
        ))
    fig.update_layout(
        **LAYOUT, height=300,
        barmode='overlay',
        xaxis_title=t['age_axis'],
        yaxis_title=t['count_axis'],
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 2: Box + Scatter ──────────────────────────────────────
c1, c2 = st.columns(2)

with c1:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.3s;">'
        f'<div class="chart-title">📦 {t["chart3"]}</div>',
        unsafe_allow_html=True
    )
    fig = go.Figure()
    for risk, label, color in [(0, t['bad_label'], BAD_C), (1, t['good_label'], GOOD_C)]:
        fig.add_trace(go.Box(
            y=df[df['Risk'] == risk]['Credit_Amount'],
            name=label, marker_color=color,
            boxmean=True, line_width=2,
        ))
    fig.update_layout(
        **LAYOUT, height=300,
        yaxis_title=t['credit_axis'],
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.4s;">'
        f'<div class="chart-title">🔵 {t["chart4"]}</div>',
        unsafe_allow_html=True
    )
    fig = go.Figure()
    for risk, label, color in [(0, t['bad_label'], BAD_C), (1, t['good_label'], GOOD_C)]:
        sub = df[df['Risk'] == risk]
        fig.add_trace(go.Scatter(
            x=sub['Duration'], y=sub['Credit_Amount'],
            mode='markers', name=label,
            marker=dict(color=color, size=6, opacity=0.6,
                        line=dict(width=0.5, color='rgba(255,255,255,0.2)')),
        ))
    fig.update_layout(
        **LAYOUT, height=300,
        xaxis_title=t['duration_axis'],
        yaxis_title=t['credit_axis'],
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Row 3: Purpose Bar + Job Donut ───────────────────────────
c1, c2 = st.columns(2)

with c1:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.5s;">'
        f'<div class="chart-title">🎯 {t["chart5"]}</div>',
        unsafe_allow_html=True
    )
    if 'Purpose' in df.columns:
        purpose_risk = df.groupby('Purpose')['Risk'].mean().reset_index()
        purpose_risk.columns = ['Purpose', 'GoodRate']
        purpose_risk = purpose_risk.sort_values('GoodRate', ascending=True)
        fig = go.Figure(go.Bar(
            x=purpose_risk['GoodRate'] * 100,
            y=purpose_risk['Purpose'],
            orientation='h',
            marker=dict(
                color=purpose_risk['GoodRate'],
                colorscale=[[0, BAD_C], [0.5, GOLD_C], [1, GOOD_C]],
                showscale=False,
            ),
            text=[f'{v*100:.0f}%' for v in purpose_risk['GoodRate']],
            textposition='outside',
            textfont=dict(color='#ffffff', size=11),
        ))
        fig.update_layout(
            **LAYOUT, height=300,
            xaxis_title='Good Risk Rate %',
            xaxis=dict(gridcolor='rgba(255,255,255,0.05)', range=[0, 110]),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
        )
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown(
        f'<div class="chart-card" style="animation-delay:0.6s;">'
        f'<div class="chart-title">💼 {t["chart6"]}</div>',
        unsafe_allow_html=True
    )
    if 'Job' in df.columns:
        job_counts = df['Job'].value_counts()
        colors_palette = [GOLD_C, GOOD_C, BLUE_C, PURPLE_C]
        fig = go.Figure(go.Pie(
            labels=job_counts.index.tolist(),
            values=job_counts.values.tolist(),
            hole=0.45,
            marker_colors=colors_palette[:len(job_counts)],
            textfont=dict(size=12, color='#ffffff'),
            textinfo='label+percent',
        ))
        fig.update_layout(**LAYOUT, height=300)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── Stats Table ───────────────────────────────────────────────
st.markdown('---')
st.markdown(
    f'<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(201,168,76,0.2);'
    f'border-{accent}:4px solid #C9A84C;border-radius:18px;padding:24px;'
    f'animation:fadeInUp 0.5s ease 0.7s backwards;">'
    f'<div class="chart-title">📊 {t["stats_title"]}</div>',
    unsafe_allow_html=True
)
num_cols = ['Age', 'Credit_Amount', 'Duration', 'Installment_Rate', 'Existing_Credits']
existing = [c for c in num_cols if c in df.columns]
st.dataframe(
    df[existing].describe().round(2),
    use_container_width=True
)
st.markdown('</div>', unsafe_allow_html=True)

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

"""NBE Credit Risk Intelligence - Analytics Page"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Analytics | NBE", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Cairo:wght@400;600;700&display=swap');
html,body,[class*="css"]{font-family:'Cairo',sans-serif!important;background:#003d28!important;color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:1rem 2rem 2rem!important;}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#002a1c,#003d28)!important;border-right:1px solid rgba(212,175,55,0.3);}
[data-testid="stSidebar"] *{color:#fff!important;}
[data-testid="stMetricValue"]{color:#D4AF37!important;font-size:2rem!important;font-weight:700!important;}
hr{border-color:rgba(212,175,55,0.2)!important;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:linear-gradient(135deg,#002a1c,#003d28);
    border:1px solid rgba(212,175,55,0.3);border-left:5px solid #D4AF37;
    border-radius:16px;padding:28px 32px;margin-bottom:28px;">
    <h1 style="color:#D4AF37;font-family:'Playfair Display',serif;font-size:32px;margin:0 0 8px;">
        📊 Portfolio Analytics
    </h1>
    <p style="color:rgba(255,255,255,0.65);margin:0;font-size:16px;">
        Comprehensive credit portfolio insights and trend analysis
    </p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    paths = [
        Path(__file__).parent.parent.parent / "data/processed/german_credit_fe_v3.csv",
        Path("data/processed/german_credit_fe_v3.csv"),
    ]
    for p in paths:
        if p.exists():
            return pd.read_csv(p)
    return None

df = load_data()
if df is None:
    st.error("⚠️ Data not found!")
    st.stop()

# KPIs
c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("📋 Total Applications", f"{len(df):,}")
with c2: st.metric("✅ Good Risk",  f"{(df['Risk']==1).sum():,}", f"{(df['Risk']==1).mean()*100:.1f}%")
with c3: st.metric("❌ Bad Risk",   f"{(df['Risk']==0).sum():,}", f"{(df['Risk']==0).mean()*100:.1f}%")
with c4: st.metric("💰 Avg Credit", f"{df['Credit_Amount'].mean():,.0f} DM")

st.markdown("---")

COLORS = {"good":"#4ade80","bad":"#f87171","gold":"#D4AF37","blue":"#60a5fa"}
LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#ffffff",family="Cairo"),
    margin=dict(t=50,b=30,l=20,r=20),
)

# Row 1
c1, c2 = st.columns(2)

with c1:
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>Risk Distribution</h3>", unsafe_allow_html=True)
    rc = df["Risk"].value_counts()
    fig = go.Figure(go.Pie(
        labels=["Bad Risk","Good Risk"],
        values=[rc.get(0,0), rc.get(1,0)],
        hole=0.5,
        marker_colors=[COLORS["bad"], COLORS["good"]],
        textfont=dict(size=14,color="#ffffff"),
    ))
    fig.update_layout(**LAYOUT, height=320)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>Age Distribution by Risk</h3>", unsafe_allow_html=True)
    fig = go.Figure()
    for risk, label, color in [(0,"Bad Risk",COLORS["bad"]),(1,"Good Risk",COLORS["good"])]:
        fig.add_trace(go.Histogram(
            x=df[df["Risk"]==risk]["Age"],
            name=label, marker_color=color,
            opacity=0.75, nbinsx=15
        ))
    fig.update_layout(**LAYOUT, height=320, barmode="overlay",
        xaxis_title="Age", yaxis_title="Count",
        legend=dict(bgcolor="rgba(0,0,0,0)"))
    st.plotly_chart(fig, use_container_width=True)

# Row 2
c1, c2 = st.columns(2)

with c1:
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>Credit Amount by Risk</h3>", unsafe_allow_html=True)
    fig = go.Figure()
    for risk, label, color in [(0,"Bad Risk",COLORS["bad"]),(1,"Good Risk",COLORS["good"])]:
        fig.add_trace(go.Box(
            y=df[df["Risk"]==risk]["Credit_Amount"],
            name=label, marker_color=color,
            boxmean=True,
        ))
    fig.update_layout(**LAYOUT, height=320,
        yaxis_title="Credit Amount (DM)",
        legend=dict(bgcolor="rgba(0,0,0,0)"))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>Duration vs Credit Amount</h3>", unsafe_allow_html=True)
    fig = go.Figure()
    for risk, label, color in [(0,"Bad Risk",COLORS["bad"]),(1,"Good Risk",COLORS["good"])]:
        sub = df[df["Risk"]==risk]
        fig.add_trace(go.Scatter(
            x=sub["Duration"], y=sub["Credit_Amount"],
            mode="markers", name=label,
            marker=dict(color=color, size=6, opacity=0.6),
        ))
    fig.update_layout(**LAYOUT, height=320,
        xaxis_title="Duration (months)",
        yaxis_title="Credit Amount (DM)",
        legend=dict(bgcolor="rgba(0,0,0,0)"))
    st.plotly_chart(fig, use_container_width=True)

# Stats table
st.markdown("---")
st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>📊 Statistical Summary</h3>", unsafe_allow_html=True)
num_cols = ["Age","Credit_Amount","Duration","Installment_Rate","Existing_Credits"]
existing = [c for c in num_cols if c in df.columns]
st.dataframe(
    df[existing].describe().round(2),
    use_container_width=True
)

# Footer
st.markdown("---")
st.markdown("""
<div style="background:linear-gradient(135deg,#002a1c,#003d28);
    border:1px solid rgba(212,175,55,0.2);border-radius:16px;
    padding:24px 32px;display:flex;flex-wrap:wrap;
    justify-content:space-between;align-items:center;gap:16px;">
    <div style="color:rgba(255,255,255,0.5);font-size:13px;">
        © 2026 National Bank of Egypt | ENG.Goda Emad | Version 3.0
    </div>
    <div style="display:flex;gap:12px;">
        <a href="https://www.linkedin.com/in/goda-emad/" target="_blank"
           style="background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.5);
           color:#60a5fa;padding:7px 14px;border-radius:8px;text-decoration:none;font-size:13px;">
           🔗 LinkedIn - ENG.Goda Emad
        </a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank"
           style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.15);
           color:#fff;padding:7px 14px;border-radius:8px;text-decoration:none;font-size:13px;">
           ⭐ GitHub Project
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

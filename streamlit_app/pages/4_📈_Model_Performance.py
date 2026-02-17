"""NBE Credit Risk Intelligence - Model Performance Page"""
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import yaml
from pathlib import Path

st.set_page_config(page_title="Model Performance | NBE", page_icon="📈", layout="wide")

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
        📈 Model Performance
    </h1>
    <p style="color:rgba(255,255,255,0.65);margin:0;font-size:16px;">
        Detailed evaluation metrics for Random Forest v3.0
    </p>
</div>
""", unsafe_allow_html=True)

LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#ffffff",family="Cairo"),
    margin=dict(t=50,b=30,l=20,r=20),
)

# Performance metrics
c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("🎯 Test Accuracy",  "76.50%", "+2.3%")
with c2: st.metric("📊 Precision",      "64.4%")
with c3: st.metric("🔄 Recall",         "48.3%")
with c4: st.metric("⚖️ F1-Score",       "55.2%")

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    # Confusion Matrix
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>📊 Confusion Matrix</h3>", unsafe_allow_html=True)
    cm = np.array([[124, 16], [31, 29]])
    fig = go.Figure(go.Heatmap(
        z=cm,
        text=[[f"TN\n{cm[0,0]}", f"FP\n{cm[0,1]}"],
              [f"FN\n{cm[1,0]}", f"TP\n{cm[1,1]}"]],
        texttemplate="%{text}",
        textfont={"size":18,"color":"white"},
        colorscale=[[0,"#002a1c"],[1,"#006341"]],
        showscale=False,
        x=["Predicted Bad","Predicted Good"],
        y=["Actual Bad","Actual Good"],
    ))
    fig.update_layout(**LAYOUT, height=320)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    # Model Comparison
    st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>🏆 Models Comparison</h3>", unsafe_allow_html=True)
    models  = ["V1 Logistic\nRegression","V2 RF\nOptimized","V3 RF\nFinal ✅"]
    train_a = [74.62, 88.12, 99.12]
    test_a  = [71.00, 71.00, 76.50]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="Train", x=models, y=train_a,
        marker_color="#006341", opacity=0.85))
    fig.add_trace(go.Bar(name="Test",  x=models, y=test_a,
        marker_color="#D4AF37", opacity=0.85))
    fig.update_layout(**LAYOUT, height=320, barmode="group",
        yaxis=dict(range=[60,105], title="Accuracy (%)"),
        legend=dict(bgcolor="rgba(0,0,0,0)"))
    st.plotly_chart(fig, use_container_width=True)

# Feature Importance
st.markdown("---")
st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>🎯 Top Features Importance</h3>", unsafe_allow_html=True)

try:
    paths = [
        Path(__file__).parent.parent.parent / "reports/feature_importance.csv",
        Path("reports/feature_importance.csv"),
    ]
    fi_df = None
    for p in paths:
        if p.exists():
            fi_df = pd.read_csv(p).sort_values("importance", ascending=False).head(15)
            break

    if fi_df is not None:
        fig = go.Figure(go.Bar(
            x=fi_df["importance"],
            y=fi_df["feature"],
            orientation="h",
            marker=dict(
                color=fi_df["importance"],
                colorscale=[[0,"#003d28"],[0.5,"#006341"],[1,"#D4AF37"]],
            ),
            text=[f"{v:.3f}" for v in fi_df["importance"]],
            textposition="outside",
            textfont=dict(color="#ffffff"),
        ))
        fig.update_layout(**LAYOUT, height=500,
            xaxis_title="Importance Score",
            yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Feature importance file not found")
except Exception as e:
    st.info(f"Feature importance: {e}")

# Model Info
st.markdown("---")
st.markdown("<h3 style='color:#D4AF37;font-size:18px;'>🤖 Model Configuration</h3>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
configs = [
    ("Algorithm",       "Random Forest",     "#D4AF37"),
    ("N Estimators",    "100 Trees",         "#4ade80"),
    ("Max Depth",       "15 Levels",         "#60a5fa"),
    ("Features",        "73 Engineered",     "#a78bfa"),
    ("Class Weight",    "Balanced",          "#fb923c"),
    ("Random State",    "42",                "#f472b6"),
]
for i, (label, value, color) in enumerate(configs):
    with [c1,c2,c3][i%3]:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
            border-top:3px solid {color};border-radius:12px;padding:16px;margin-bottom:12px;text-align:center;">
            <div style="color:rgba(255,255,255,0.5);font-size:12px;margin-bottom:6px;">{label}</div>
            <div style="color:{color};font-size:18px;font-weight:700;">{value}</div>
        </div>
        """, unsafe_allow_html=True)

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

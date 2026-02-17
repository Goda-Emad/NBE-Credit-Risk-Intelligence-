"""NBE Credit Risk Intelligence - Risk Assessment Page"""
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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Cairo:wght@400;600;700&display=swap');
:root {
    --nbe-dark:  #003d28;
    --nbe-green: #006341;
    --nbe-gold:  #D4AF37;
}
html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif !important;
    background-color: #003d28 !important;
    color: #ffffff !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 2rem 2rem !important; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#002a1c,#003d28) !important;
    border-right: 1px solid rgba(212,175,55,0.3);
}
[data-testid="stSidebar"] * { color:#ffffff !important; }

/* Form inputs */
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(212,175,55,0.3) !important;
    border-radius: 8px !important;
    color: #ffffff !important;
}
.stSelectbox label, .stNumberInput label,
.stSlider label { color: rgba(255,255,255,0.8) !important; }
[data-testid="stMetricValue"] {
    color: #D4AF37 !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}
.stButton > button {
    background: linear-gradient(135deg,#D4AF37,#b8962e) !important;
    color: #002a1c !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 14px 32px !important;
    font-size: 17px !important;
    width: 100% !important;
    font-family: 'Cairo', sans-serif !important;
    box-shadow: 0 4px 15px rgba(212,175,55,0.4) !important;
    transition: all 0.3s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(212,175,55,0.6) !important;
}
hr { border-color: rgba(212,175,55,0.2) !important; }
</style>
""", unsafe_allow_html=True)

# ── Page Header ──────────────────────────────────────────────
st.markdown("""
<div style="
    background:linear-gradient(135deg,#002a1c,#003d28);
    border:1px solid rgba(212,175,55,0.3);
    border-left:5px solid #D4AF37;
    border-radius:16px; padding:28px 32px; margin-bottom:28px;
">
    <h1 style="color:#D4AF37;font-family:'Playfair Display',serif;
        font-size:32px;margin:0 0 8px;">🎯 Credit Risk Assessment</h1>
    <p style="color:rgba(255,255,255,0.65);margin:0;font-size:16px;">
        AI-powered credit evaluation using Random Forest Model v3.0
    </p>
</div>
""", unsafe_allow_html=True)

# ── Load Model ───────────────────────────────────────────────
@st.cache_resource(show_spinner="🤖 Loading AI Model...")
def load_model():
    paths = [
        Path(__file__).parent.parent.parent / "models",
        Path("models"), Path("../models"),
    ]
    for p in paths:
        if (p / "final_model.pkl").exists():
            with open(p / "final_model.pkl",         "rb") as f: model    = pickle.load(f)
            with open(p / "scaler_final.pkl",        "rb") as f: scaler   = pickle.load(f)
            with open(p / "feature_names_final.pkl", "rb") as f: features = pickle.load(f)
            return model, scaler, features
    return None, None, None

model, scaler, feature_names = load_model()

if model is None:
    st.error("⚠️ Model files not found! Please check models/ directory.")
    st.stop()

# ── Input Options ─────────────────────────────────────────────
OPTIONS = {
    "Status_Account":   {"A11":"< 0 DM (Overdrawn)","A12":"0–200 DM","A13":"≥ 200 DM","A14":"No Account"},
    "Credit_History":   {"A30":"All Paid","A31":"Paid at Bank","A32":"Existing Paid","A33":"Delay in Past","A34":"Critical Account"},
    "Purpose":          {"A40":"New Car","A41":"Used Car","A42":"Furniture","A43":"Radio/TV","A44":"Appliances","A45":"Repairs","A46":"Education","A48":"Retraining","A49":"Business","A410":"Other"},
    "Savings":          {"A61":"< 100 DM","A62":"100–500 DM","A63":"500–1000 DM","A64":"≥ 1000 DM","A65":"Unknown"},
    "Employment":       {"A71":"Unemployed","A72":"< 1 Year","A73":"1–4 Years","A74":"4–7 Years","A75":"≥ 7 Years"},
    "Personal_Status":  {"A91":"Male Divorced","A92":"Female","A93":"Male Single","A94":"Male Married"},
    "Other_Debtors":    {"A101":"None","A102":"Co-applicant","A103":"Guarantor"},
    "Property":         {"A121":"Real Estate","A122":"Life Insurance","A123":"Car/Other","A124":"No Property"},
    "Other_Plans":      {"A141":"Bank","A142":"Stores","A143":"None"},
    "Housing":          {"A151":"Rent","A152":"Own","A153":"For Free"},
    "Job":              {"A171":"Unskilled Non-Resident","A172":"Unskilled Resident","A173":"Skilled","A174":"Management"},
    "Telephone":        {"A191":"None","A192":"Registered"},
    "Foreign_Worker":   {"A201":"Yes","A202":"No"},
}

def make_label(d): return list(d.values())
def get_key(d, v): return list(d.keys())[list(d.values()).index(v)]

# ── Form ──────────────────────────────────────────────────────
st.markdown("""
<h2 style="color:#ffffff;font-family:'Cairo',sans-serif;
    font-size:22px;margin-bottom:16px;">📋 Application Details</h2>
""", unsafe_allow_html=True)

with st.form("credit_form", clear_on_submit=False):
    # Section 1: Personal
    st.markdown("""
    <div style="background:rgba(212,175,55,0.08);border:1px solid rgba(212,175,55,0.2);
        border-radius:12px;padding:16px 20px;margin-bottom:16px;">
        <h3 style="color:#D4AF37;margin:0 0 16px;font-size:17px;">
            👤 Personal Information
        </h3>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age (years)", 19, 75, 35)
    with c2:
        personal = st.selectbox("Personal Status",
            make_label(OPTIONS["Personal_Status"]))
    with c3:
        foreign = st.selectbox("Foreign Worker",
            make_label(OPTIONS["Foreign_Worker"]))
    st.markdown("</div>", unsafe_allow_html=True)

    # Section 2: Financial
    st.markdown("""
    <div style="background:rgba(96,165,250,0.05);border:1px solid rgba(96,165,250,0.15);
        border-radius:12px;padding:16px 20px;margin-bottom:16px;">
        <h3 style="color:#60a5fa;margin:0 0 16px;font-size:17px;">
            💰 Financial Details
        </h3>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        credit_amount = st.number_input("Credit Amount (DM)", 250, 20000, 5000, 100)
    with c2:
        duration = st.number_input("Duration (months)", 4, 72, 24)
    with c3:
        installment = st.number_input("Installment Rate (%)", 1, 4, 2)

    c1, c2, c3 = st.columns(3)
    with c1:
        status_account = st.selectbox("Account Status",
            make_label(OPTIONS["Status_Account"]))
    with c2:
        savings = st.selectbox("Savings Account",
            make_label(OPTIONS["Savings"]))
    with c3:
        existing_credits = st.number_input("Existing Credits", 1, 4, 1)
    st.markdown("</div>", unsafe_allow_html=True)

    # Section 3: Employment & Housing
    st.markdown("""
    <div style="background:rgba(74,222,128,0.05);border:1px solid rgba(74,222,128,0.15);
        border-radius:12px;padding:16px 20px;margin-bottom:16px;">
        <h3 style="color:#4ade80;margin:0 0 16px;font-size:17px;">
            🏠 Employment & Housing
        </h3>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        employment = st.selectbox("Employment Duration",
            make_label(OPTIONS["Employment"]))
    with c2:
        housing = st.selectbox("Housing",
            make_label(OPTIONS["Housing"]))
    with c3:
        job = st.selectbox("Job Type",
            make_label(OPTIONS["Job"]))

    c1, c2, c3 = st.columns(3)
    with c1:
        residence = st.number_input("Years at Residence", 1, 4, 2)
    with c2:
        dependents = st.number_input("Num Dependents", 1, 2, 1)
    with c3:
        telephone = st.selectbox("Telephone",
            make_label(OPTIONS["Telephone"]))
    st.markdown("</div>", unsafe_allow_html=True)

    # Section 4: Credit Info
    st.markdown("""
    <div style="background:rgba(167,139,250,0.05);border:1px solid rgba(167,139,250,0.15);
        border-radius:12px;padding:16px 20px;margin-bottom:20px;">
        <h3 style="color:#a78bfa;margin:0 0 16px;font-size:17px;">
            📄 Credit Information
        </h3>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        credit_history = st.selectbox("Credit History",
            make_label(OPTIONS["Credit_History"]))
    with c2:
        purpose = st.selectbox("Loan Purpose",
            make_label(OPTIONS["Purpose"]))
    with c3:
        other_debtors = st.selectbox("Other Debtors",
            make_label(OPTIONS["Other_Debtors"]))

    c1, c2, c3 = st.columns(3)
    with c1:
        property_ = st.selectbox("Property",
            make_label(OPTIONS["Property"]))
    with c2:
        other_plans = st.selectbox("Other Installment Plans",
            make_label(OPTIONS["Other_Plans"]))
    with c3:
        pass
    st.markdown("</div>", unsafe_allow_html=True)

    submitted = st.form_submit_button("🔍 Assess Credit Risk", use_container_width=True)

# ── Prediction ────────────────────────────────────────────────
if submitted:
    input_data = {
        "Status_Account":   get_key(OPTIONS["Status_Account"],   status_account),
        "Duration":         duration,
        "Credit_History":   get_key(OPTIONS["Credit_History"],   credit_history),
        "Purpose":          get_key(OPTIONS["Purpose"],          purpose),
        "Credit_Amount":    credit_amount,
        "Savings":          get_key(OPTIONS["Savings"],          savings),
        "Employment":       get_key(OPTIONS["Employment"],       employment),
        "Installment_Rate": installment,
        "Personal_Status":  get_key(OPTIONS["Personal_Status"],  personal),
        "Other_Debtors":    get_key(OPTIONS["Other_Debtors"],    other_debtors),
        "Residence_Since":  residence,
        "Property":         get_key(OPTIONS["Property"],         property_),
        "Age":              age,
        "Other_Plans":      get_key(OPTIONS["Other_Plans"],      other_plans),
        "Housing":          get_key(OPTIONS["Housing"],          housing),
        "Existing_Credits": existing_credits,
        "Job":              get_key(OPTIONS["Job"],              job),
        "Num_Dependents":   dependents,
        "Telephone":        get_key(OPTIONS["Telephone"],        telephone),
        "Foreign_Worker":   get_key(OPTIONS["Foreign_Worker"],   foreign),
    }

    # Feature engineering
    df = pd.DataFrame([input_data])

    df["age_young"]  = (df["Age"] < 25).astype(int)
    df["age_middle"] = ((df["Age"] >= 25) & (df["Age"] < 60)).astype(int)
    df["age_senior"] = (df["Age"] >= 60).astype(int)
    df["credit_low"]    = (df["Credit_Amount"] < 2500).astype(int)
    df["credit_medium"] = ((df["Credit_Amount"] >= 2500) & (df["Credit_Amount"] < 5000)).astype(int)
    df["credit_high"]   = (df["Credit_Amount"] >= 5000).astype(int)
    df["duration_short"]  = (df["Duration"] <= 12).astype(int)
    df["duration_medium"] = ((df["Duration"] > 12) & (df["Duration"] <= 24)).astype(int)
    df["duration_long"]   = (df["Duration"] > 24).astype(int)
    df["credit_duration_ratio"]  = df["Credit_Amount"] / (df["Duration"] + 1)
    df["credit_age_ratio"]       = df["Credit_Amount"] / (df["Age"] + 1)
    df["age_credit_interaction"] = df["Age"] * df["Credit_Amount"] / 1000

    cat_cols = ["Status_Account","Credit_History","Purpose","Savings","Employment",
                "Personal_Status","Other_Debtors","Property","Other_Plans","Housing",
                "Job","Telephone","Foreign_Worker"]
    df = pd.get_dummies(df, columns=cat_cols, drop_first=False, dtype=int)

    for feat in feature_names:
        if feat not in df.columns:
            df[feat] = 0
    df = df[feature_names]

    X_scaled = scaler.transform(df)
    pred     = model.predict(X_scaled)[0]
    proba    = model.predict_proba(X_scaled)[0]
    score    = float(proba[1]) * 100

    # Results
    st.markdown("---")
    st.markdown("""
    <h2 style="color:#D4AF37;font-family:'Playfair Display',serif;
        font-size:28px;margin-bottom:20px;">📊 Assessment Results</h2>
    """, unsafe_allow_html=True)

    # Determine risk
    if score >= 70:
        risk_cat = "LOW RISK";    border_c = "#4ade80"; bg_c = "rgba(74,222,128,0.1)";  icon = "✅"; decision = "APPROVED"
    elif score >= 50:
        risk_cat = "MEDIUM RISK"; border_c = "#fbbf24"; bg_c = "rgba(251,191,36,0.1)";  icon = "⚠️"; decision = "REVIEW"
    else:
        risk_cat = "HIGH RISK";   border_c = "#f87171"; bg_c = "rgba(248,113,113,0.1)"; icon = "❌"; decision = "REJECTED"

    c1, c2 = st.columns([1, 1])

    with c1:
        # Result card
        st.markdown(f"""
        <div style="
            background:{bg_c};
            border:2px solid {border_c};
            border-radius:20px;
            padding:32px;
            text-align:center;
            margin-bottom:20px;
        ">
            <div style="font-size:64px;margin-bottom:12px;">{icon}</div>
            <div style="color:{border_c};font-size:28px;font-weight:700;
                font-family:'Cairo',sans-serif;margin-bottom:8px;">{risk_cat}</div>
            <div style="color:#ffffff;font-size:22px;margin-bottom:16px;">
                Decision: <strong style="color:{border_c};">{decision}</strong>
            </div>
            <div style="
                background:rgba(255,255,255,0.05);
                border-radius:12px;padding:16px;
                display:inline-block;min-width:180px;
            ">
                <div style="color:rgba(255,255,255,0.6);font-size:13px;">Risk Score</div>
                <div style="color:{border_c};font-size:42px;font-weight:700;
                    font-family:'Cairo',sans-serif;">{score:.1f}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Metrics
        m1, m2 = st.columns(2)
        with m1: st.metric("Good Probability", f"{proba[1]*100:.1f}%")
        with m2: st.metric("Bad Probability",  f"{proba[0]*100:.1f}%")

    with c2:
        # Gauge
        if score >= 70: gc = "#4ade80"
        elif score >= 50: gc = "#fbbf24"
        else: gc = "#f87171"

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix":"%","font":{"size":36,"color":gc}},
            title={"text":"Risk Score","font":{"size":18,"color":"#ffffff"}},
            gauge={
                "axis":{"range":[0,100],"tickcolor":"#666","tickfont":{"color":"#aaa"}},
                "bar":{"color":gc},
                "bgcolor":"rgba(0,0,0,0)",
                "bordercolor":"#333",
                "steps":[
                    {"range":[0,50],  "color":"rgba(248,113,113,0.15)"},
                    {"range":[50,70], "color":"rgba(251,191,36,0.15)"},
                    {"range":[70,100],"color":"rgba(74,222,128,0.15)"},
                ],
                "threshold":{
                    "line":{"color":gc,"width":4},
                    "thickness":0.75,"value":score
                }
            }
        ))
        fig.update_layout(
            height=300,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color":"#ffffff","family":"Cairo"},
            margin=dict(t=40,b=0,l=20,r=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    # Recommendation box
    recs = {
        "LOW RISK":    ("✅ Recommendation: Proceed with standard loan terms. Customer shows strong creditworthiness.", "#4ade80"),
        "MEDIUM RISK": ("⚠️ Recommendation: Manual review required. Consider requesting additional income verification or reducing loan amount by 20%.", "#fbbf24"),
        "HIGH RISK":   ("❌ Recommendation: High default probability. Consider requiring collateral (150% of loan value) or reject application.", "#f87171"),
    }
    msg, color = recs[risk_cat]
    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.03);
        border:1px solid {color};
        border-left:5px solid {color};
        border-radius:12px;
        padding:20px 24px;
        margin-top:16px;
        color:rgba(255,255,255,0.85);
        font-size:15px;
        line-height:1.7;
    ">💡 {msg}</div>
    """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="
    background:linear-gradient(135deg,#002a1c,#003d28);
    border:1px solid rgba(212,175,55,0.2);
    border-radius:16px; padding:24px 32px;
    display:flex; flex-wrap:wrap;
    justify-content:space-between; align-items:center; gap:16px;
">
    <div style="color:rgba(255,255,255,0.5);font-size:13px;">
        © 2026 National Bank of Egypt | ENG.Goda Emad | Version 3.0
    </div>
    <div style="display:flex;gap:12px;">
        <a href="https://www.linkedin.com/in/goda-emad/" target="_blank"
           style="background:rgba(10,102,194,0.2);border:1px solid rgba(10,102,194,0.5);
           color:#60a5fa;padding:7px 14px;border-radius:8px;text-decoration:none;font-size:13px;">
           🔗 LinkedIn
        </a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-" target="_blank"
           style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.15);
           color:#ffffff;padding:7px 14px;border-radius:8px;text-decoration:none;font-size:13px;">
           ⭐ GitHub
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

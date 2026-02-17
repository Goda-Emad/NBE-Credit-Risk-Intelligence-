"""NBE Credit Risk Intelligence - About Page"""
import streamlit as st

st.set_page_config(page_title="About | NBE", page_icon="ℹ️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Cairo:wght@400;600;700&display=swap');
html,body,[class*="css"]{font-family:'Cairo',sans-serif!important;background:#003d28!important;color:#fff!important;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:1rem 2rem 2rem!important;}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#002a1c,#003d28)!important;border-right:1px solid rgba(212,175,55,0.3);}
[data-testid="stSidebar"] *{color:#fff!important;}
hr{border-color:rgba(212,175,55,0.2)!important;}
a{color:#60a5fa!important;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:linear-gradient(135deg,#002a1c,#003d28);
    border:1px solid rgba(212,175,55,0.3);border-left:5px solid #D4AF37;
    border-radius:16px;padding:28px 32px;margin-bottom:28px;">
    <h1 style="color:#D4AF37;font-family:'Playfair Display',serif;font-size:32px;margin:0 0 8px;">
        ℹ️ About the Platform
    </h1>
    <p style="color:rgba(255,255,255,0.65);margin:0;font-size:16px;">
        Project documentation and developer information
    </p>
</div>
""", unsafe_allow_html=True)

# Project Overview
st.markdown("""
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
    border-radius:16px;padding:28px;margin-bottom:20px;">
    <h2 style="color:#D4AF37;font-family:'Playfair Display',serif;font-size:24px;margin-bottom:16px;">
        🎯 Project Overview
    </h2>
    <p style="color:rgba(255,255,255,0.8);line-height:1.8;font-size:15px;">
        The <strong style="color:#D4AF37;">NBE Credit Risk Intelligence Platform</strong> is an AI-powered
        credit assessment system designed for the <strong>National Bank of Egypt</strong>.
        It automates credit risk evaluation using machine learning, reducing processing time from days to seconds
        while maintaining high accuracy and full regulatory compliance.
    </p>
</div>
""", unsafe_allow_html=True)

# Tech Stack
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:24px;margin-bottom:16px;">
        <h3 style="color:#4ade80;font-size:18px;margin-bottom:16px;">🔧 Tech Stack</h3>
    """, unsafe_allow_html=True)

    techs = [
        ("🐍", "Python 3.11",     "#4ade80"),
        ("🌊", "Streamlit 1.31",  "#60a5fa"),
        ("🤖", "scikit-learn 1.4","#D4AF37"),
        ("📊", "Plotly 5.18",     "#a78bfa"),
        ("🐼", "Pandas 2.1",      "#fb923c"),
        ("🔢", "NumPy 1.26",      "#f472b6"),
    ]
    for icon, name, color in techs:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:12px;
            padding:10px;border-radius:8px;
            background:rgba(255,255,255,0.02);
            border:1px solid rgba(255,255,255,0.05);
            margin-bottom:8px;">
            <span style="font-size:20px;">{icon}</span>
            <span style="color:{color};font-weight:600;">{name}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
        border-radius:16px;padding:24px;margin-bottom:16px;">
        <h3 style="color:#60a5fa;font-size:18px;margin-bottom:16px;">📊 Model Details</h3>
    """, unsafe_allow_html=True)

    details = [
        ("Algorithm",    "Random Forest Classifier",  "#D4AF37"),
        ("Version",      "v3.0 (Production)",         "#4ade80"),
        ("Accuracy",     "76.50% on test set",        "#60a5fa"),
        ("Features",     "73 engineered features",    "#a78bfa"),
        ("Dataset",      "German Credit (1,000)",     "#fb923c"),
        ("Compliance",   "CBE Regulated",             "#f472b6"),
    ]
    for label, value, color in details:
        st.markdown(f"""
        <div style="display:flex;justify-content:space-between;align-items:center;
            padding:10px;border-radius:8px;
            background:rgba(255,255,255,0.02);
            border:1px solid rgba(255,255,255,0.05);
            margin-bottom:8px;">
            <span style="color:rgba(255,255,255,0.5);font-size:13px;">{label}</span>
            <span style="color:{color};font-weight:600;font-size:14px;">{value}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Pipeline
st.markdown("---")
st.markdown("""
<h2 style="color:#D4AF37;font-family:'Playfair Display',serif;font-size:24px;margin-bottom:16px;">
    🔄 ML Pipeline
</h2>
<div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
    border-radius:16px;padding:24px;">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;align-items:center;">
""", unsafe_allow_html=True)

steps = [
    ("📥", "Raw Data",         "#D4AF37"),
    ("→",  "",                 "transparent"),
    ("🔧", "Preprocessing",    "#4ade80"),
    ("→",  "",                 "transparent"),
    ("⚙️", "Feature Eng.",    "#60a5fa"),
    ("→",  "",                 "transparent"),
    ("⚖️", "Scaling",         "#a78bfa"),
    ("→",  "",                 "transparent"),
    ("🤖", "Random Forest",   "#D4AF37"),
    ("→",  "",                 "transparent"),
    ("📊", "Risk Score",       "#4ade80"),
    ("→",  "",                 "transparent"),
    ("✅", "Decision",         "#f472b6"),
]
for icon, label, color in steps:
    if icon == "→":
        st.markdown(f"<span style='color:rgba(255,255,255,0.3);font-size:20px;'>→</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.05);border:1px solid {color};
            border-radius:10px;padding:10px 16px;text-align:center;min-width:90px;">
            <div style="font-size:22px;">{icon}</div>
            <div style="color:{color};font-size:12px;font-weight:600;margin-top:4px;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Developer Card
st.markdown("---")
st.markdown("""
<div style="
    background: linear-gradient(135deg, #002a1c 0%, #003d28 50%, #004d35 100%);
    border: 1px solid rgba(212,175,55,0.4);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
">
    <!-- Decorative -->
    <div style="position:absolute;top:-40px;right:-40px;width:150px;height:150px;
        border-radius:50%;border:2px solid rgba(212,175,55,0.1);"></div>
    <div style="position:absolute;bottom:-40px;left:-40px;width:150px;height:150px;
        border-radius:50%;border:2px solid rgba(212,175,55,0.1);"></div>

    <!-- Avatar -->
    <div style="
        width:90px;height:90px;
        background:linear-gradient(135deg,#D4AF37,#b8962e);
        border-radius:50%;
        display:flex;align-items:center;justify-content:center;
        font-size:40px;
        margin:0 auto 20px;
        box-shadow:0 8px 25px rgba(212,175,55,0.4);
    ">👨‍💻</div>

    <!-- Name -->
    <h2 style="color:#D4AF37;font-family:'Playfair Display',serif;
        font-size:28px;margin:0 0 8px;">ENG. Goda Emad</h2>

    <!-- Title -->
    <p style="color:rgba(255,255,255,0.65);font-size:16px;margin:0 0 24px;">
        AI/ML Engineer | Credit Risk Analytics | National Bank of Egypt
    </p>

    <!-- Divider -->
    <div style="height:1px;background:linear-gradient(90deg,transparent,rgba(212,175,55,0.4),transparent);
        margin:0 auto 24px;max-width:400px;"></div>

    <!-- Links -->
    <div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;">
        <a href="https://www.linkedin.com/in/goda-emad/"
           target="_blank" style="
            display:flex;align-items:center;gap:8px;
            background:rgba(10,102,194,0.2);
            border:2px solid rgba(10,102,194,0.6);
            color:#60a5fa;
            padding:12px 24px;
            border-radius:12px;
            text-decoration:none;
            font-size:15px;
            font-weight:600;
            font-family:'Cairo',sans-serif;
            transition:all 0.3s;
        ">
            🔗 LinkedIn Profile
        </a>
        <a href="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"
           target="_blank" style="
            display:flex;align-items:center;gap:8px;
            background:rgba(255,255,255,0.05);
            border:2px solid rgba(255,255,255,0.2);
            color:#ffffff;
            padding:12px 24px;
            border-radius:12px;
            text-decoration:none;
            font-size:15px;
            font-weight:600;
            font-family:'Cairo',sans-serif;
        ">
            ⭐ GitHub Project
        </a>
    </div>

    <!-- Copyright -->
    <p style="color:rgba(255,255,255,0.3);font-size:12px;margin:24px 0 0;">
        © 2026 National Bank of Egypt | NBE Credit Risk Intelligence v3.0
    </p>
</div>
""", unsafe_allow_html=True)

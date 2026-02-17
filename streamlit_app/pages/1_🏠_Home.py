"""Home Page"""
import streamlit as st

st.set_page_config(
    page_title="NBE Credit Risk - Home",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>
h1, h2, h3 { color: #006341; }
.stButton>button {
    background-color: #006341;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #006341;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='text-align:center; padding:30px;
     background: linear-gradient(135deg, #006341, #004d32);
     border-radius: 15px; margin-bottom: 30px;'>
    <h1 style='color:white; font-size:48px; margin:0;'>
        🏦 NBE Credit Risk Intelligence
    </h1>
    <p style='color:#D4AF37; font-size:20px; margin:10px 0 0;'>
        AI-Powered Credit Assessment Platform
    </p>
    <p style='color:#ccc; font-size:16px;'>
        National Bank of Egypt | Version 3.0
    </p>
</div>
""", unsafe_allow_html=True)

# Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🎯 Model Accuracy", "76.5%",  "+2.3%")
with col2:
    st.metric("⚡ Features",        "73",      "Engineered")
with col3:
    st.metric("📊 Training Data",   "800",     "Samples")
with col4:
    st.metric("🌲 Decision Trees",  "100",     "Random Forest")

st.markdown("---")

# Feature cards
st.subheader("🎯 Platform Capabilities")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <h3>🎯 Smart Assessment</h3>
        <p>Real-time credit risk evaluation using
        Random Forest with 73 engineered features.
        Results in under 2 seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <h3>📊 Portfolio Analytics</h3>
        <p>Comprehensive portfolio insights,
        trend analysis, and performance
        metrics in interactive dashboards.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <h3>🔒 CBE Compliant</h3>
        <p>Full audit trail, explainable AI
        decisions, and regulatory compliance
        with Central Bank of Egypt standards.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Navigation guide
st.subheader("🧭 Navigation Guide")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Use the sidebar to navigate:**

    - **🎯 Risk Assessment** → Evaluate new applications
    - **📊 Analytics** → Portfolio insights
    - **📈 Model Performance** → Model metrics
    - **ℹ️ About** → Documentation
    """)

with col2:
    st.info("""
    💡 **Quick Start:**
    1. Go to **Risk Assessment**
    2. Fill in customer details
    3. Click **Assess Risk**
    4. Get instant AI-powered decision
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; padding:20px;'>
    <p>© 2026 National Bank of Egypt | Credit Risk Analytics Team</p>
    <p>📞 creditrisk@nbe.com.eg | Version 3.0 | Powered by ML</p>
</div>
""", unsafe_allow_html=True)

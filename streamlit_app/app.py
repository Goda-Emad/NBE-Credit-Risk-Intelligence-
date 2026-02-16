"""NBE Credit Risk Intelligence - Main Application"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="NBE Credit Risk",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
.stButton>button {
    background-color: #006341;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 12px 24px;
}
.stButton>button:hover {
    background-color: #004d32;
}
h1, h2, h3 { color: #006341; }
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Logo (if exists)
logo_path = Path(__file__).parent.parent / 'assets' / 'nbe_branding' / 'nbe_logo.png'
if logo_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(logo_path), width=300)

# Header
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1>🏦 NBE Credit Risk Intelligence</h1>
    <p style='font-size: 18px; color: #666;'>
        AI-Powered Credit Assessment Platform<br>
        National Bank of Egypt
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Model Accuracy", "76.5%", "+2.3%")
with col2:
    st.metric("Features", "73")
with col3:
    st.metric("Training Data", "800")
with col4:
    st.metric("Test Accuracy", "76.5%")

st.markdown("---")

# Features
st.subheader("🎯 Platform Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <h3>🎯 Smart Assessment</h3>
        <p>Automated credit risk evaluation using Random Forest ML model with 73 engineered features</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <h3>📊 Real-time Analytics</h3>
        <p>Comprehensive portfolio insights, performance metrics, and trend analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <h3>🔒 Compliant & Secure</h3>
        <p>CBE regulations compliant with full audit trail and data encryption</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Navigation
st.subheader("🧭 Navigation Guide")
st.markdown("""
Use the **sidebar** to navigate:

1. **🏠 Home** - Overview and statistics (current page)
2. **🎯 Risk Assessment** - Evaluate new credit applications
3. **📊 Analytics** - Portfolio analysis and insights
4. **📈 Model Performance** - Detailed model metrics
5. **ℹ️ About** - Project documentation

💡 **Quick Start:** Click on **Risk Assessment** in the sidebar to begin evaluating applications
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>© 2026 National Bank of Egypt | Credit Risk Analytics Team</p>
    <p>Version 3.0 | Powered by Machine Learning</p>
</div>
""", unsafe_allow_html=True)

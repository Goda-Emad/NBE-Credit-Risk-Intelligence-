"""Risk Assessment Page"""

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.graph_objects as go

st.set_page_config(page_title="Risk Assessment", page_icon="🎯", layout="wide")

# CSS
st.markdown("""
<style>
.risk-low { background: #d4edda; border: 2px solid #28a745; padding: 15px; border-radius: 8px; color: #155724; text-align: center; font-weight: bold; }
.risk-medium { background: #fff3cd; border: 2px solid #ffc107; padding: 15px; border-radius: 8px; color: #856404; text-align: center; font-weight: bold; }
.risk-high { background: #f8d7da; border: 2px solid #dc3545; padding: 15px; border-radius: 8px; color: #721c24; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        project_root = Path(__file__).parent.parent.parent
        with open(project_root / 'models' / 'final_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open(project_root / 'models' / 'scaler_final.pkl', 'rb') as f:
            scaler = pickle.load(f)
        with open(project_root / 'models' / 'feature_names_final.pkl', 'rb') as f:
            features = pickle.load(f)
        return model, scaler, features
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

model, scaler, feature_names = load_model()

st.title("🎯 Credit Risk Assessment")
st.markdown("Evaluate credit applications using AI")
st.markdown("---")

if model is None:
    st.error("⚠️ Model files not found!")
    st.stop()

# Form
with st.form("credit_form"):
    st.subheader("📋 Application Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", 19, 75, 35)
        duration = st.number_input("Duration (months)", 4, 72, 24)
        credit_amount = st.number_input("Credit Amount", 250, 20000, 5000, 100)
    
    with col2:
        status_account = st.selectbox("Account Status", ['A11', 'A12', 'A13', 'A14'])
        savings = st.selectbox("Savings", ['A61', 'A62', 'A63', 'A64', 'A65'])
        employment = st.selectbox("Employment", ['A71', 'A72', 'A73', 'A74', 'A75'])
    
    with col3:
        housing = st.selectbox("Housing", ['A151', 'A152', 'A153'])
        job = st.selectbox("Job", ['A171', 'A172', 'A173', 'A174'])
        purpose = st.selectbox("Purpose", ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A48', 'A49', 'A410'])
    
    submitted = st.form_submit_button("🔍 Assess Risk", use_container_width=True)

if submitted:
    st.markdown("---")
    st.subheader("📊 Assessment Results")
    
    # Simple prediction (you'll need to implement proper feature engineering)
    # This is a placeholder - adjust based on your actual feature engineering
    
    # Mock result for demonstration
    risk_score = np.random.uniform(0.3, 0.9)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Risk Score", f"{risk_score*100:.1f}%")
    with col2:
        decision = "APPROVED" if risk_score > 0.7 else "REVIEW" if risk_score > 0.5 else "REJECTED"
        st.metric("Decision", decision)
    with col3:
        confidence = max(risk_score, 1-risk_score) * 100
        st.metric("Confidence", f"{confidence:.1f}%")
    
    # Risk visualization
    if risk_score >= 0.7:
        st.markdown('<div class="risk-low">✅ LOW RISK - Approved</div>', unsafe_allow_html=True)
        recommendation = "Customer shows strong creditworthiness. Recommend approval."
    elif risk_score >= 0.5:
        st.markdown('<div class="risk-medium">⚠️ MEDIUM RISK - Manual Review</div>', unsafe_allow_html=True)
        recommendation = "Requires additional review by senior officer."
    else:
        st.markdown('<div class="risk-high">❌ HIGH RISK - Rejected</div>', unsafe_allow_html=True)
        recommendation = "High default probability. Recommend rejection."
    
    st.info(f"💡 **Recommendation:** {recommendation}")
    
    # Gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score*100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Score"},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#006341"},
            'steps': [
                {'range': [0, 50], 'color': "lightcoral"},
                {'range': [50, 70], 'color': "lightyellow"},
                {'range': [70, 100], 'color': "lightgreen"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

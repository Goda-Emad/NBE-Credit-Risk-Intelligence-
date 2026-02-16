"""Analytics Dashboard"""

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

st.title("📊 Portfolio Analytics")
st.markdown("Comprehensive credit portfolio insights")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    try:
        project_root = Path(__file__).parent.parent.parent
        df = pd.read_csv(project_root / 'data' / 'processed' / 'german_credit_fe_v3.csv')
        return df
    except:
        return None

df = load_data()

if df is None:
    st.error("Data not found!")
    st.stop()

# KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Applications", len(df))
with col2:
    approval_rate = (df['Risk'] == 1).mean() * 100
    st.metric("Approval Rate", f"{approval_rate:.1f}%")
with col3:
    avg_amount = df['Credit_Amount'].mean()
    st.metric("Avg Credit", f"${avg_amount:,.0f}")
with col4:
    avg_duration = df['Duration'].mean()
    st.metric("Avg Duration", f"{avg_duration:.0f}m")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    # Risk distribution
    risk_dist = df['Risk'].value_counts()
    fig = px.pie(values=risk_dist.values, names=['Bad', 'Good'],
                 title="Risk Distribution",
                 color_discrete_sequence=['#dc3545', '#28a745'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Age distribution
    fig = px.histogram(df, x='Age', nbins=20, title="Age Distribution",
                      color_discrete_sequence=['#006341'])
    st.plotly_chart(fig, use_container_width=True)

# More charts
col1, col2 = st.columns(2)

with col1:
    # Credit amount distribution
    fig = px.box(df, y='Credit_Amount', title="Credit Amount Distribution",
                color_discrete_sequence=['#006341'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Duration vs Risk
    fig = px.scatter(df, x='Duration', y='Credit_Amount', color='Risk',
                    title="Duration vs Credit Amount",
                    color_discrete_map={0: '#dc3545', 1: '#28a745'})
    st.plotly_chart(fig, use_container_width=True)

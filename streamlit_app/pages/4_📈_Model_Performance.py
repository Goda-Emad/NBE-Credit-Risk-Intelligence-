"""Model Performance Page"""

import streamlit as st
import pandas as pd
import yaml
from pathlib import Path

st.set_page_config(page_title="Model Performance", page_icon="📈", layout="wide")

st.title("📈 Model Performance Metrics")
st.markdown("Detailed evaluation and statistics")
st.markdown("---")

# Load config
@st.cache_data
def load_config():
    try:
        project_root = Path(__file__).parent.parent.parent
        with open(project_root / 'config' / 'config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except:
        return None

config = load_config()

if config:
    # Model info
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤖 Model Details")
        st.write(f"**Algorithm:** {config['model']['algorithm']}")
        st.write(f"**Version:** {config['model']['version']}")
        st.write(f"**Features:** {config['model']['features']}")
        st.write(f"**Trees:** {config['model']['n_estimators']}")
        st.write(f"**Max Depth:** {config['model']['max_depth']}")
    
    with col2:
        st.subheader("📊 Performance")
        perf = config['performance']
        st.metric("Test Accuracy", f"{perf['test_accuracy']*100:.2f}%")
        st.metric("Recall (Good)", f"{perf['recall_good']*100:.2f}%")
        st.write(f"**True Negatives:** {perf['true_negatives']}")
        st.write(f"**False Positives:** {perf['false_positives']}")
        st.write(f"**False Negatives:** {perf['false_negatives']}")
        st.write(f"**True Positives:** {perf['true_positives']}")

st.markdown("---")

# Confusion Matrix
st.subheader("📊 Confusion Matrix")
if config:
    perf = config['performance']
    cm_data = [[perf['true_negatives'], perf['false_positives']],
               [perf['false_negatives'], perf['true_positives']]]
    
    cm_df = pd.DataFrame(cm_data, 
                         columns=['Predicted Bad', 'Predicted Good'],
                         index=['Actual Bad', 'Actual Good'])
    st.dataframe(cm_df, use_container_width=True)

st.markdown("---")

# Feature Importance
st.subheader("🎯 Top Features")
try:
    project_root = Path(__file__).parent.parent.parent
    fi_df = pd.read_csv(project_root / 'reports' / 'feature_importance.csv')
    st.dataframe(fi_df.head(15), use_container_width=True)
except:
    st.info("Feature importance data not available")

# False Negatives
st.markdown("---")
st.subheader("⚠️ False Negatives Analysis")
try:
    fn_df = pd.read_csv(project_root / 'reports' / 'false_negatives_analysis.csv')
    st.write(f"**Total False Negatives:** {len(fn_df)} cases")
    st.dataframe(fn_df.head(10), use_container_width=True)
except:
    st.info("False negatives data not available")

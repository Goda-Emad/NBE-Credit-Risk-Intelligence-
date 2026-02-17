"""Footer Component"""
import streamlit as st
from datetime import datetime


def render_footer(show_model_info: bool = True) -> None:
    """Render page footer with NBE branding"""
    st.markdown("---")

    if show_model_info:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            **🤖 Model Info**
            - Algorithm: Random Forest
            - Version: 3.0
            - Accuracy: 76.5%
            """)

        with col2:
            st.markdown("""
            **📊 Data Info**
            - Dataset: German Credit
            - Samples: 1,000
            - Features: 73
            """)

        with col3:
            st.markdown("""
            **🔒 Compliance**
            - CBE Regulated
            - Full Audit Trail
            - Human Oversight
            """)

        st.markdown("---")

    st.markdown(f"""
    <div style='
        text-align: center;
        color: #666;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 8px;
        font-size: 13px;
    '>
        <p style='margin:0;'>
            © 2026 National Bank of Egypt |
            Credit Risk Analytics Team |
            Version 3.0
        </p>
        <p style='margin:5px 0 0;'>
            📞 creditrisk@nbe.com.eg |
            Last updated: {datetime.now().strftime("%B %Y")}
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_disclaimer() -> None:
    """Render compliance disclaimer"""
    st.warning("""
    ⚠️ **Disclaimer:** This AI model is a decision-support tool only.
    All final credit decisions must be reviewed and approved by
    authorized NBE personnel in accordance with CBE regulations.
    """)

"""Sidebar Component"""
import streamlit as st
from pathlib import Path


def render_sidebar():
    """Render the application sidebar"""
    with st.sidebar:
        # Logo
        logo_path = Path(__file__).parent.parent.parent / "assets" / "nbe_branding" / "nbe_logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=200)
        else:
            st.markdown("""
            <div style='text-align:center; padding:15px;
                 background:#006341; border-radius:10px; margin-bottom:15px;'>
                <h2 style='color:white; margin:0;'>🏦 NBE</h2>
                <p style='color:#D4AF37; margin:0; font-size:12px;'>
                    Credit Risk Intelligence
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # Model Status
        st.markdown("### 🤖 Model Status")
        st.success("✅ Model Active (v3.0)")
        st.markdown("""
        <small>
        - Algorithm: Random Forest<br>
        - Features: 73<br>
        - Accuracy: 76.5%<br>
        - Updated: Feb 2026
        </small>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Good", "30%")
        with col2:
            st.metric("Bad", "70%")

        st.markdown("---")

        # Risk Legend
        st.markdown("### 🎨 Risk Legend")
        st.markdown("""
        <div style='padding:8px; background:#d4edda;
             border-radius:5px; margin:3px 0;
             border-left:4px solid #28a745;'>
            ✅ Low Risk (≥70%)
        </div>
        <div style='padding:8px; background:#fff3cd;
             border-radius:5px; margin:3px 0;
             border-left:4px solid #ffc107;'>
            ⚠️ Medium Risk (50-70%)
        </div>
        <div style='padding:8px; background:#f8d7da;
             border-radius:5px; margin:3px 0;
             border-left:4px solid #dc3545;'>
            ❌ High Risk (<50%)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.caption("© 2026 NBE | v3.0")

"""About Page"""

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About NBE Credit Risk Intelligence")
st.markdown("---")

st.markdown("""
### 🎯 Project Overview

This AI-powered Credit Risk Intelligence Platform is designed for the **National Bank of Egypt (NBE)** 
to automate and enhance credit application assessment processes.

### 🔧 Technical Details

- **Model:** Random Forest Classifier
- **Accuracy:** 76.5%
- **Features:** 73 engineered features
- **Dataset:** German Credit Risk (1,000 applications)

### 📊 Capabilities

1. **Automated Risk Assessment**
   - Real-time credit scoring
   - Probability-based recommendations
   - Confidence intervals

2. **Portfolio Analytics**
   - Application trends
   - Risk distribution
   - Performance metrics

3. **Model Monitoring**
   - Accuracy tracking
   - False negative analysis
   - Feature importance

### 🏗️ Architecture
```
Data → Feature Engineering → Random Forest → Risk Score → Decision
```

### 👥 Team

**Credit Risk Analytics Team**  
National Bank of Egypt

### 📞 Contact

- **Email:** creditrisk@nbe.com.eg
- **Version:** 3.0
- **Last Updated:** February 2026

### 📚 Documentation

For detailed documentation, see:
- Model Card: `docs/model_card.md`
- Performance Report: `reports/model_performance_report.md`
- GitHub: [View Repository](https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-)

### 📄 License

MIT License © 2026 National Bank of Egypt
""")

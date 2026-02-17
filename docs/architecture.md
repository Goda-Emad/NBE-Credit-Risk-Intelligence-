# System Architecture

## 🏗️ High-Level Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACE                        │
│              Streamlit Web Application                   │
│   ┌──────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐  │
│   │ Home │ │ Risk     │ │Analytics │ │   Model      │  │
│   │      │ │Assessment│ │Dashboard │ │ Performance  │  │
│   └──────┘ └──────────┘ └──────────┘ └──────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                  APPLICATION LAYER                       │
│   ┌────────────────────────────────────────────────┐    │
│   │              Feature Engineering               │    │
│   │   Age Groups | Credit Bins | Duration Bins     │    │
│   │   Financial Ratios | One-Hot Encoding          │    │
│   └────────────────────────────────────────────────┘    │
│   ┌────────────────────────────────────────────────┐    │
│   │              Prediction Pipeline               │    │
│   │   Input → Transform → Scale → Predict         │    │
│   └────────────────────────────────────────────────┘    │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                    MODEL LAYER                           │
│   ┌──────────────────┐   ┌────────────────────────┐    │
│   │  Random Forest   │   │   StandardScaler       │    │
│   │  (100 trees)     │   │   (73 features)        │    │
│   │  final_model.pkl │   │   scaler_final.pkl     │    │
│   └──────────────────┘   └────────────────────────┘    │
└─────────────────────┬───────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────┐
│                    DATA LAYER                            │
│   ┌──────────────┐  ┌─────────────┐  ┌──────────────┐  │
│   │   Raw Data   │  │  Processed  │  │    Models    │  │
│   │  german.data │  │  fe_v3.csv  │  │    .pkl      │  │
│   └──────────────┘  └─────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure
```
NBE-Credit-Risk-Intelligence/
├── streamlit_app/          # UI Layer
├── src/                    # Business Logic
├── models/                 # ML Models
├── data/                   # Data Storage
├── config/                 # Configuration
└── tests/                  # Quality Assurance
```

---

## 🔄 Data Flow
```
Raw Input
    │
    ▼
Validation
    │
    ▼
Feature Engineering (73 features)
    │
    ▼
Standard Scaling
    │
    ▼
Random Forest Prediction
    │
    ▼
Risk Score (0-100%)
    │
    ▼
Decision (Approve/Review/Reject)
```

---

## 🔒 Security Architecture
```
User → HTTPS → Streamlit Cloud → App → Models
              (TLS 1.3)
```

---

## 📊 Model Architecture
```
Input (73 features)
       │
       ▼
┌─────────────────────────────┐
│     Random Forest           │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐  │
│  │ T1│ │ T2│ │ T3│ │...│  │  (100 Trees)
│  └─┬─┘ └─┬─┘ └─┬─┘ └─┬─┘  │
│    └──────┴──────┴─────┘    │
│           │                 │
│      Majority Vote          │
└───────────┬─────────────────┘
            │
            ▼
    Risk Score (0-1)
            │
       ┌────┴─────┐
       │          │
    Bad (0)    Good (1)
```

---

## ⚡ Performance

| Metric | Value |
|--------|-------|
| Prediction Time | < 200ms |
| Model Load Time | ~2s (cached) |
| Memory Usage | ~512MB |
| Concurrent Users | Up to 50 |

---

**Version:** 3.0 | **Last Updated:** February 2026

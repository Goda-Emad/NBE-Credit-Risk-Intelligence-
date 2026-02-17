# Changelog
All notable changes to NBE Credit Risk Intelligence Platform.

---

## [3.0.0] - 2026-02-17 - Production Release 🚀

### Added
- Complete Streamlit multi-page dashboard
- 73 engineered features
- MLOps: Monitoring, drift detection, retraining pipeline
- Docker & Docker Compose support
- Comprehensive test suite
- GitHub Actions CI/CD pipeline
- Full documentation

### Model Performance
- Algorithm:       Random Forest (100 trees)
- Train Accuracy:  99.12%
- Test Accuracy:   76.50%
- False Negatives: 31 cases
- Features:        73

---

## [2.0.0] - 2026-02-15 - Optimized Model

### Added
- SMOTE oversampling
- Feature selection (73 → 30)
- Hyperparameter tuning

### Model Performance
- Train Accuracy:  88.12%
- Test Accuracy:   71.00%
- False Negatives: 30 cases

---

## [1.0.0] - 2026-02-14 - Baseline Model

### Added
- German Credit Dataset
- Logistic Regression baseline
- Basic feature engineering

### Model Performance
- Train Accuracy:  74.62%
- Test Accuracy:   71.00%
- False Negatives: 15 cases

---

## [0.1.0] - 2026-02-10 - Project Init

### Added
- Project structure
- GitHub repository
- Initial documentation

---

## 📊 Version Comparison

| Version | Algorithm | Test Acc | FN | Status |
|---------|-----------|----------|----|--------|
| v1.0 | Logistic Regression | 71.00% | 15 | Baseline |
| v2.0 | RF Optimized | 71.00% | 30 | Alternative |
| **v3.0** | **RF Final** | **76.50%** | **31** | **✅ Production** |

---

## 🔮 Planned (v4.0)

- [ ] Retrain on Egyptian banking data
- [ ] XGBoost ensemble
- [ ] SHAP explainability
- [ ] I-Score integration
- [ ] Real-time API

---
*February 2026 | NBE Credit Risk Analytics Team*

# NBE Credit Risk Intelligence - Model Card

## Model Details
- **Model Name:** Random Forest Credit Risk Classifier
- **Version:** 3.0 (Final)
- **Date:** 2026-02-16
- **Developer:** NBE Credit Risk Analytics Team
- **Model Type:** Random Forest Classifier
- **License:** MIT

## Intended Use
- **Primary Use:** Automated credit risk assessment for loan applications
- **Target Users:** Loan officers, risk analysts, credit committee members
- **Out-of-Scope:** Final lending decisions (requires human review)

## Training Data
- **Dataset:** UCI German Credit Dataset
- **Size:** 1,000 samples (800 train, 200 test)
- **Features:** 73 engineered features
- **Target Distribution:** 70% Bad Risk, 30% Good Risk

## Model Performance
- **Test Accuracy:** 0.7650 (76.50%)
- **Precision (Good):** 0.6444
- **Recall (Good):** 0.4833
- **False Negatives:** 31 cases (customers incorrectly rejected)

## Limitations
- Trained on German credit data (may need adaptation for Egyptian market)
- Imbalanced dataset (70/30 split)
- Does not account for external economic factors
- Requires periodic retraining

## Ethical Considerations
- Monitor for demographic bias (age, gender)
- Ensure explainability of decisions for regulatory compliance
- Maintain audit trail for all predictions
- Human oversight required for final decisions

## Model Maintenance
- **Retraining Frequency:** Quarterly
- **Monitoring Metrics:** Accuracy, False Negative Rate, Data Drift
- **Contact:** creditrisk@nbe.com.eg

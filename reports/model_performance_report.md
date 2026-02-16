# NBE Credit Risk Model - Performance Report
Generated: 2026-02-16 09:08:09

## Executive Summary
The Random Forest model achieves **76.50% test accuracy** with **31 false negatives**.

## Model Comparison

### Old Model (Selected - 73 Features)
- Training Accuracy: 0.9912 (99.12%)
- Test Accuracy: 0.7650 (76.50%)
- Overfitting Gap: 22.62%
- False Negatives: 31 cases
- Features: 73

### Optimized Model (Alternative - 30 Features + SMOTE)
- Training Accuracy: 0.8812 (88.12%)
- Test Accuracy: 0.7100 (71.00%)
- Overfitting Gap: 17.12%
- False Negatives: 30 cases
- Features: 30

## Confusion Matrix (Final Model)
```
                Predicted
                Bad    Good
Actual Bad      124     16
Actual Good     31     29
```

## Business Impact
- **Missed Good Customers:** 31 (need manual review process)
- **Correctly Identified Bad:** 124 customers
- **Recommendation:** Implement tiered review for scores 50-70%

## Next Steps
1. Deploy to staging environment
2. A/B test with current manual process
3. Collect feedback from loan officers
4. Monitor false negative rate monthly
5. Retrain with Egyptian banking data

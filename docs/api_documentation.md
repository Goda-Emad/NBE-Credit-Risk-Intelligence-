# API Documentation

## Overview
NBE Credit Risk Intelligence REST API documentation.

---

## Base URL
```
https://nbe-credit-risk.streamlit.app/
```

---

## 🎯 Prediction Endpoint

### POST `/api/predict`

**Description:** Evaluate credit risk for a single application

**Request Body:**
```json
{
  "Status_Account": "A11",
  "Duration": 24,
  "Credit_History": "A34",
  "Purpose": "A43",
  "Credit_Amount": 5000,
  "Savings": "A61",
  "Employment": "A73",
  "Installment_Rate": 2,
  "Personal_Status": "A93",
  "Other_Debtors": "A101",
  "Residence_Since": 2,
  "Property": "A121",
  "Age": 35,
  "Other_Plans": "A143",
  "Housing": "A152",
  "Existing_Credits": 1,
  "Job": "A173",
  "Num_Dependents": 1,
  "Telephone": "A191",
  "Foreign_Worker": "A201"
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability_good": 0.785,
  "probability_bad": 0.215,
  "risk_category": "Low Risk",
  "recommendation": "APPROVED",
  "confidence": 0.785,
  "model_version": "v3.0",
  "timestamp": "2026-02-16T10:30:00Z"
}
```

**Status Codes:**

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Invalid input |
| 422 | Validation error |
| 500 | Server error |

---

## 📊 Analytics Endpoint

### GET `/api/analytics/summary`

**Response:**
```json
{
  "total_applications": 1000,
  "approval_rate": 0.30,
  "avg_credit_amount": 3271.25,
  "avg_duration": 20.90,
  "risk_distribution": {
    "good": 300,
    "bad": 700
  }
}
```

---

## 📈 Model Info Endpoint

### GET `/api/model/info`

**Response:**
```json
{
  "algorithm": "Random Forest Classifier",
  "version": "v3.0",
  "accuracy": 0.765,
  "features": 73,
  "training_date": "2026-02-15",
  "status": "active"
}
```

---

## 🔒 Authentication
```bash
# Include API key in headers
curl -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -X POST https://nbe-credit-risk.streamlit.app/api/predict \
     -d '{"Age": 35, "Credit_Amount": 5000, ...}'
```

---

**Version:** 1.0 | **Last Updated:** February 2026


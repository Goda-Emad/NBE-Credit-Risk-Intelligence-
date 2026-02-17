# User Guide

## 🏦 NBE Credit Risk Intelligence Platform

### Welcome!
This guide helps you use the Credit Risk Assessment Platform effectively.

---

## 🧭 Navigation

The platform has **5 main pages** accessible from the sidebar:

| Page | Icon | Purpose |
|------|------|---------|
| Home | 🏠 | Overview and system stats |
| Risk Assessment | 🎯 | Evaluate credit applications |
| Analytics | 📊 | Portfolio insights |
| Model Performance | 📈 | Model accuracy metrics |
| About | ℹ️ | Documentation |

---

## 🎯 How to Assess Credit Risk

### Step 1: Go to Risk Assessment
Click **🎯 Risk Assessment** in the sidebar.

### Step 2: Fill Application Details

**Personal Information:**
- **Age:** Customer's age (19-75 years)
- **Duration:** Loan duration in months (4-72)
- **Credit Amount:** Requested amount in EGP

**Account Information:**
- **Account Status:** Current checking account balance
- **Savings:** Savings account balance
- **Employment:** Years at current job

**Other Details:**
- **Housing:** Rent / Own / Free
- **Job:** Employment level
- **Purpose:** Reason for the loan

### Step 3: Submit Assessment
Click **🔍 Assess Risk** button.

### Step 4: Interpret Results

| Score | Category | Action |
|-------|----------|--------|
| 70-100% | ✅ Low Risk | Recommend Approval |
| 50-70% | ⚠️ Medium Risk | Manual Review Required |
| 0-50% | ❌ High Risk | Recommend Rejection |

---

## 📊 Understanding Analytics

### Key Metrics
- **Total Applications:** Number of applications processed
- **Approval Rate:** Percentage of approved applications
- **Avg Credit:** Average credit amount requested
- **Avg Duration:** Average loan duration

### Charts
- **Risk Distribution:** Pie chart showing Good vs Bad risk
- **Age Distribution:** Histogram of applicant ages
- **Credit Amount:** Box plot of credit amounts
- **Duration vs Amount:** Scatter plot correlation

---

## 📈 Model Performance

### Metrics Explained

| Metric | Description | Target |
|--------|-------------|--------|
| Accuracy | Overall correct predictions | > 75% |
| Precision | Correct positive predictions | > 80% |
| Recall | Actual positives identified | > 70% |
| F1-Score | Balance of precision/recall | > 75% |

### Confusion Matrix
```
                  Predicted
                  Bad    Good
Actual    Bad     TN     FP
          Good    FN     TP
```

- **TN (124):** Correctly identified bad customers ✅
- **TP (29):** Correctly identified good customers ✅
- **FP (16):** Good customers rejected (missed revenue) ⚠️
- **FN (31):** Bad customers approved (default risk) ❌

---

## 🔒 Security & Privacy

- All data is processed locally
- No customer data is stored permanently
- Predictions are logged for compliance only
- Access requires valid credentials

---

## 🆘 Support

**Technical Issues:**
- Email: creditrisk@nbe.com.eg
- Phone: +20 2 xxxx xxxx

**Training:**
- Request training session from your manager
- Online tutorials available on the intranet

---

**Version:** 3.0 | **Last Updated:** February 2026

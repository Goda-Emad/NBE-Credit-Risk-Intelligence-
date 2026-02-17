# Data Dictionary - German Credit Dataset

## Overview
Complete description of all features used in the NBE Credit Risk Intelligence model.

---

## 📊 Original Features (21 columns)

### 1. Status_Account
**Type:** Categorical | **Values:** A11, A12, A13, A14

| Code | Description |
|------|-------------|
| A11 | < 0 DM (Overdrawn) |
| A12 | 0 ≤ x < 200 DM |
| A13 | ≥ 200 DM / salary for at least 1 year |
| A14 | No checking account |

---

### 2. Duration
**Type:** Numerical | **Unit:** Months | **Range:** 4 - 72

Duration of the credit in months.

---

### 3. Credit_History
**Type:** Categorical | **Values:** A30 - A34

| Code | Description |
|------|-------------|
| A30 | No credits taken / all credits paid back |
| A31 | All credits at this bank paid back |
| A32 | Existing credits paid back till now |
| A33 | Delay in paying off in the past |
| A34 | Critical account / other credits existing |

---

### 4. Purpose
**Type:** Categorical | **Values:** A40 - A410

| Code | Description |
|------|-------------|
| A40 | Car (new) |
| A41 | Car (used) |
| A42 | Furniture / equipment |
| A43 | Radio / television |
| A44 | Domestic appliances |
| A45 | Repairs |
| A46 | Education |
| A48 | Retraining |
| A49 | Business |
| A410 | Others |

---

### 5. Credit_Amount
**Type:** Numerical | **Unit:** DM | **Range:** 250 - 18,424

Total credit amount requested.

---

### 6. Savings
**Type:** Categorical | **Values:** A61 - A65

| Code | Description |
|------|-------------|
| A61 | < 100 DM |
| A62 | 100 ≤ x < 500 DM |
| A63 | 500 ≤ x < 1000 DM |
| A64 | ≥ 1000 DM |
| A65 | Unknown / no savings account |

---

### 7. Employment
**Type:** Categorical | **Values:** A71 - A75

| Code | Description |
|------|-------------|
| A71 | Unemployed |
| A72 | < 1 year |
| A73 | 1 ≤ x < 4 years |
| A74 | 4 ≤ x < 7 years |
| A75 | ≥ 7 years |

---

### 8. Installment_Rate
**Type:** Numerical | **Range:** 1 - 4

Installment rate as percentage of disposable income.

---

### 9. Personal_Status
**Type:** Categorical | **Values:** A91 - A94

| Code | Description |
|------|-------------|
| A91 | Male: divorced/separated |
| A92 | Female: divorced/separated/married |
| A93 | Male: single |
| A94 | Male: married/widowed |

---

### 10. Other_Debtors
**Type:** Categorical | **Values:** A101, A102, A103

| Code | Description |
|------|-------------|
| A101 | None |
| A102 | Co-applicant |
| A103 | Guarantor |

---

### 11. Residence_Since
**Type:** Numerical | **Range:** 1 - 4

Years at current residence.

---

### 12. Property
**Type:** Categorical | **Values:** A121 - A124

| Code | Description |
|------|-------------|
| A121 | Real estate |
| A122 | Building society / life insurance |
| A123 | Car or other property |
| A124 | Unknown / no property |

---

### 13. Age
**Type:** Numerical | **Unit:** Years | **Range:** 19 - 75

Customer age in years.

---

### 14. Other_Plans
**Type:** Categorical | **Values:** A141, A142, A143

| Code | Description |
|------|-------------|
| A141 | Bank |
| A142 | Stores |
| A143 | None |

---

### 15. Housing
**Type:** Categorical | **Values:** A151, A152, A153

| Code | Description |
|------|-------------|
| A151 | Rent |
| A152 | Own |
| A153 | For free |

---

### 16. Existing_Credits
**Type:** Numerical | **Range:** 1 - 4

Number of existing credits at this bank.

---

### 17. Job
**Type:** Categorical | **Values:** A171 - A174

| Code | Description |
|------|-------------|
| A171 | Unemployed / unskilled - non-resident |
| A172 | Unskilled - resident |
| A173 | Skilled employee / official |
| A174 | Management / self-employed / officer |

---

### 18. Num_Dependents
**Type:** Numerical | **Range:** 1 - 2

Number of people being liable for maintenance.

---

### 19. Telephone
**Type:** Categorical | **Values:** A191, A192

| Code | Description |
|------|-------------|
| A191 | None |
| A192 | Yes, registered under customer name |

---

### 20. Foreign_Worker
**Type:** Categorical | **Values:** A201, A202

| Code | Description |
|------|-------------|
| A201 | Yes |
| A202 | No |

---

### 21. Risk (Target)
**Type:** Binary | **Values:** 0, 1

| Value | Description |
|-------|-------------|
| 0 | Bad Risk (default) |
| 1 | Good Risk (creditworthy) |

---

## 🔧 Engineered Features (12 columns)

### Age Group Features

| Feature | Description | Formula |
|---------|-------------|---------|
| age_young | Customer is young | Age < 25 → 1, else 0 |
| age_middle | Customer is middle-aged | 25 ≤ Age < 60 → 1, else 0 |
| age_senior | Customer is senior | Age ≥ 60 → 1, else 0 |

### Credit Amount Features

| Feature | Description | Formula |
|---------|-------------|---------|
| credit_low | Low credit amount | Amount < 2,500 → 1, else 0 |
| credit_medium | Medium credit amount | 2,500 ≤ Amount < 5,000 → 1, else 0 |
| credit_high | High credit amount | Amount ≥ 5,000 → 1, else 0 |

### Duration Features

| Feature | Description | Formula |
|---------|-------------|---------|
| duration_short | Short term loan | Duration ≤ 12 months → 1, else 0 |
| duration_medium | Medium term loan | 12 < Duration ≤ 24 → 1, else 0 |
| duration_long | Long term loan | Duration > 24 months → 1, else 0 |

### Ratio Features

| Feature | Description | Formula |
|---------|-------------|---------|
| credit_duration_ratio | Credit per month | Amount / (Duration + 1) |
| credit_age_ratio | Credit relative to age | Amount / (Age + 1) |
| age_credit_interaction | Age × Credit interaction | (Age × Amount) / 1,000 |

---

## 📊 Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Samples | 1,000 |
| Features (after encoding) | 73 |
| Good Risk (1) | 300 (30%) |
| Bad Risk (0) | 700 (70%) |
| Missing Values | 0 |
| Duplicates | 0 |

---

## 📈 Key Feature Statistics

| Feature | Min | Max | Mean | Std |
|---------|-----|-----|------|-----|
| Age | 19 | 75 | 35.5 | 11.4 |
| Credit_Amount | 250 | 18,424 | 3,271 | 2,823 |
| Duration | 4 | 72 | 20.9 | 12.1 |
| Installment_Rate | 1 | 4 | 2.97 | 1.12 |
| Existing_Credits | 1 | 4 | 1.41 | 0.58 |

---

**Last Updated:** February 2026
**Dataset Source:** UCI Machine Learning Repository - German Credit

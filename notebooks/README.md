# 📓 Notebooks Guide

## Overview
This directory contains all Jupyter notebooks for the NBE Credit Risk Intelligence project.

## 📁 Structure
```
notebooks/
├── exploratory/                    # Research & Analysis
│   ├── 01_data_exploration.ipynb  # EDA & Data Understanding
│   ├── 02_feature_engineering.ipynb # Feature Creation
│   └── 03_model_training.ipynb    # Model Experiments
└── production/
    └── model_training_final.ipynb  # Final Training Pipeline
```

## 🚀 How to Run

### Option 1: Google Colab (Recommended)
1. Open notebook in Colab
2. Mount Google Drive
3. Run all cells

### Option 2: Local Jupyter
```bash
pip install jupyter
jupyter notebook
```

## 📊 Notebook Descriptions

| Notebook | Purpose | Key Outputs |
|----------|---------|-------------|
| 01_data_exploration | Understand data structure | EDA charts, statistics |
| 02_feature_engineering | Create 73 features | Processed dataset |
| 03_model_training | Experiment with models | Model comparison |
| model_training_final | Production pipeline | final_model.pkl |

## ⚠️ Notes
- Always run notebooks in order (01 → 02 → 03)
- Ensure data files exist in `data/raw/`
- Model files saved to `models/`

---
**Last Updated:** February 2026

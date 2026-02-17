# Deployment Guide

## 🚀 Quick Deploy to Streamlit Cloud

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to: https://share.streamlit.io
2. Click **New app**
3. Select repository: `Goda-Emad/NBE-Credit-Risk-Intelligence`
4. Branch: `main`
5. Main file: `streamlit_app/app.py`
6. Click **Deploy**

### Step 3: Configure Secrets
In Streamlit Cloud → App Settings → Secrets:
```toml
[model]
active_model_version = "v3.0"

[feature_flags]
enable_advanced_analytics = true
```

---

## 🐳 Docker Deployment

### Build image
```bash
docker build -t nbe-credit-risk .
```

### Run container
```bash
docker run -p 8501:8501 nbe-credit-risk
```

### Docker Compose
```bash
docker-compose up -d
```

---

## 💻 Local Development

### Setup
```bash
# Clone repository
git clone https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence.git
cd NBE-Credit-Risk-Intelligence

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run streamlit_app/app.py
```

---

## ⚙️ Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| MODEL_VERSION | Active model version | No |
| DEBUG_MODE | Enable debug logging | No |
| API_KEY | API authentication key | Yes (production) |

---

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.9+ | 3.11 |
| RAM | 512MB | 2GB |
| Storage | 500MB | 2GB |
| CPU | 1 core | 2 cores |

---

## 🔧 Troubleshooting

### Model not loading
```bash
# Check model files exist
ls -la models/
# Should show: final_model.pkl, scaler_final.pkl, feature_names_final.pkl
```

### Module not found
```bash
pip install -r requirements.txt --upgrade
```

### Port already in use
```bash
streamlit run streamlit_app/app.py --server.port 8502
```

---

**Last Updated:** February 2026

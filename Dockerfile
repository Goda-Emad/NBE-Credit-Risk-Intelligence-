# =============================================================================
# NBE Credit Risk Intelligence - Dockerfile
# =============================================================================

FROM python:3.11-slim

LABEL maintainer="NBE Credit Risk Team <creditrisk@nbe.com.eg>"
LABEL version="3.0"
LABEL description="NBE Credit Risk Intelligence Platform"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_THEME_PRIMARY_COLOR=#006341

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN mkdir -p logs/monitoring \
             logs/drift \
             logs/retraining \
             reports/figures

EXPOSE 8501

HEALTHCHECK --interval=30s \
            --timeout=10s \
            --start-period=30s \
            --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

RUN useradd -m -u 1000 nbeuser && \
    chown -R nbeuser:nbeuser /app
USER nbeuser

CMD ["streamlit", "run", "streamlit_app/app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]

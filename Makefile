# =============================================================================
# NBE Credit Risk Intelligence - Makefile
# =============================================================================

.PHONY: help install run test lint format clean docker deploy

GREEN  := \033[0;32m
GOLD   := \033[0;33m
BLUE   := \033[0;34m
NC     := \033[0m

APP_NAME  := NBE Credit Risk Intelligence
MAIN_FILE := streamlit_app/app.py
PORT      := 8501
PYTHON    := python3
PIP       := pip

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(BLUE)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Install dependencies
	$(PIP) install -r requirements.txt

install-dev: ## Install dev dependencies
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .

install-lfs: ## Setup Git LFS
	git lfs install
	git lfs track "*.pkl"
	git lfs track "*.csv"
	git add .gitattributes

run: ## Run Streamlit app
	streamlit run $(MAIN_FILE) --server.port=$(PORT)

run-debug: ## Run with debug mode
	streamlit run $(MAIN_FILE) --server.port=$(PORT) --logger.level=debug

download-data: ## Download dataset
	$(PYTHON) scripts/download_data.py

train: ## Train model
	$(PYTHON) scripts/train_pipeline.py

train-lr: ## Train Logistic Regression
	$(PYTHON) scripts/train_pipeline.py --model logistic_regression

evaluate: ## Evaluate model
	$(PYTHON) scripts/evaluate_pipeline.py

pipeline: download-data train evaluate ## Full pipeline

test: ## Run all tests
	pytest tests/ -v

test-cov: ## Tests with coverage
	pytest tests/ -v --cov=src --cov-report=html

test-preprocessing: ## Preprocessing tests
	pytest tests/test_data_preprocessing.py -v

test-features: ## Feature tests
	pytest tests/test_feature_engineering.py -v

test-model: ## Model tests
	pytest tests/test_model.py -v

lint: ## Run linter
	flake8 src/ streamlit_app/ tests/ --max-line-length=100

format: ## Format code
	black src/ streamlit_app/ tests/ --line-length=100
	isort src/ streamlit_app/ tests/

security: ## Security check
	bandit -r src/ streamlit_app/ -f screen

check: lint security test ## All checks

docker-build: ## Build Docker image
	docker build -t nbe-credit-risk:latest .

docker-run: ## Run Docker container
	docker run -p $(PORT):8501 --name nbe-credit-risk nbe-credit-risk:latest

docker-stop: ## Stop container
	docker stop nbe-credit-risk || true
	docker rm nbe-credit-risk || true

docker-compose-up: ## Start with Docker Compose
	docker-compose up -d

docker-compose-down: ## Stop Docker Compose
	docker-compose down

deploy-local: ## Deploy locally
	bash scripts/deploy.sh local

deploy-streamlit: ## Deploy to Streamlit Cloud
	bash scripts/deploy.sh streamlit

deploy-docker: ## Deploy with Docker
	bash scripts/deploy.sh docker

monitor: ## Run monitoring check
	$(PYTHON) -c "from mlops.monitoring import ModelMonitor; m=ModelMonitor(); print(m.generate_report())"

retrain: ## Trigger retraining
	$(PYTHON) -c "from mlops.retraining_pipeline import RetrainingPipeline; p=RetrainingPipeline(); p.run_full_pipeline('Manual')"

clean: ## Clean cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

info: ## Project info
	@echo "Project: $(APP_NAME)"
	@echo "Python:  $(shell $(PYTHON) --version)"
	@echo "Branch:  $(shell git branch --show-current 2>/dev/null || echo N/A)"

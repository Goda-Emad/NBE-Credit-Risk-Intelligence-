#!/bin/bash
# =============================================================================
# NBE Credit Risk Intelligence - Deployment Script
# Usage: bash scripts/deploy.sh [local|streamlit|docker]
# =============================================================================

set -e  # Exit on error

# Colors
GREEN="\033[0;32m"
GOLD="\033[0;33m"
RED="\033[0;31m"
BLUE="\033[0;34m"
NC="\033[0m"  # No Color

# Config
APP_NAME="NBE Credit Risk Intelligence"
VERSION="3.0"
MAIN_FILE="streamlit_app/app.py"
REPO_URL="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-"

print_header() {
    echo ""
    echo -e "${GREEN}=====================================================================${NC}"
    echo -e "${GREEN}  🏦 ${APP_NAME} v${VERSION}${NC}"
    echo -e "${GREEN}  Deployment Script${NC}"
    echo -e "${GREEN}=====================================================================${NC}"
    echo ""
}

print_step() {
    echo -e "${BLUE}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${GOLD}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# =============================================================================
# CHECKS
# =============================================================================

check_requirements() {
    print_step "Checking requirements..."

    # Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1)
        print_success "Python: ${PYTHON_VERSION}"
    else
        print_error "Python 3 not found!"
        exit 1
    fi

    # pip
    if command -v pip &> /dev/null; then
        print_success "pip: available"
    else
        print_error "pip not found!"
        exit 1
    fi

    # Streamlit
    if python3 -c "import streamlit" &> /dev/null; then
        ST_VERSION=$(python3 -c "import streamlit; print(streamlit.__version__)")
        print_success "Streamlit: ${ST_VERSION}"
    else
        print_warning "Streamlit not installed. Installing..."
        pip install streamlit
    fi

    # Model files
    if [ -f "models/final_model.pkl" ]; then
        print_success "Model file: found"
    else
        print_error "Model file not found: models/final_model.pkl"
        exit 1
    fi

    if [ -f "models/scaler_final.pkl" ]; then
        print_success "Scaler file: found"
    else
        print_error "Scaler file not found!"
        exit 1
    fi
}

check_files() {
    print_step "Checking required files..."

    REQUIRED_FILES=(
        "streamlit_app/app.py"
        "requirements.txt"
        ".streamlit/config.toml"
        "models/final_model.pkl"
        "models/scaler_final.pkl"
        "models/feature_names_final.pkl"
    )

    ALL_OK=true
    for file in "${REQUIRED_FILES[@]}"; do
        if [ -f "$file" ]; then
            print_success "$file"
        else
            print_warning "Missing: $file"
            ALL_OK=false
        fi
    done

    if [ "$ALL_OK" = false ]; then
        print_warning "Some files missing. Deployment may fail."
    fi
}

# =============================================================================
# INSTALL
# =============================================================================

install_dependencies() {
    print_step "Installing dependencies..."
    pip install -r requirements.txt --quiet
    print_success "Dependencies installed!"
}

# =============================================================================
# DEPLOY: LOCAL
# =============================================================================

deploy_local() {
    print_step "Starting local deployment..."

    PORT=${PORT:-8501}

    echo ""
    echo -e "${GREEN}🚀 Starting Streamlit app...${NC}"
    echo -e "   URL: ${BLUE}http://localhost:${PORT}${NC}"
    echo -e "   Press ${RED}Ctrl+C${NC} to stop"
    echo ""

    streamlit run ${MAIN_FILE} \
        --server.port=${PORT} \
        --server.address=localhost \
        --browser.gatherUsageStats=false \
        --theme.primaryColor="#006341" \
        --theme.backgroundColor="#FFFFFF"
}

# =============================================================================
# DEPLOY: STREAMLIT CLOUD
# =============================================================================

deploy_streamlit_cloud() {
    print_step "Preparing for Streamlit Cloud deployment..."

    # Check Git
    if ! command -v git &> /dev/null; then
        print_error "Git not found!"
        exit 1
    fi

    # Check if repo is clean
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "Uncommitted changes found. Committing..."
        git add .
        git commit -m "Deploy: v${VERSION} - $(date '+%Y-%m-%d %H:%M')"
    else
        print_success "Repository is clean"
    fi

    # Push to GitHub
    print_step "Pushing to GitHub..."
    git push origin main
    print_success "Pushed to GitHub!"

    echo ""
    echo -e "${GREEN}=====================================================================${NC}"
    echo -e "${GREEN}  📡 Streamlit Cloud Deployment Instructions${NC}"
    echo -e "${GREEN}=====================================================================${NC}"
    echo ""
    echo -e "  1. Go to: ${BLUE}https://share.streamlit.io${NC}"
    echo -e "  2. Click: ${GOLD}New app${NC}"
    echo -e "  3. Repository: ${BLUE}${REPO_URL}${NC}"
    echo -e "  4. Branch: ${GOLD}main${NC}"
    echo -e "  5. Main file: ${GOLD}${MAIN_FILE}${NC}"
    echo -e "  6. Click: ${GREEN}Deploy!${NC}"
    echo ""
    echo -e "  ⚠️  Note: Add secrets in App Settings → Secrets"
    echo ""
}

# =============================================================================
# DEPLOY: DOCKER
# =============================================================================

deploy_docker() {
    print_step "Starting Docker deployment..."

    # Check Docker
    if ! command -v docker &> /dev/null; then
        print_error "Docker not found! Install from: https://docker.com"
        exit 1
    fi

    IMAGE_NAME="nbe-credit-risk"
    CONTAINER_NAME="nbe-credit-risk-app"
    PORT=${PORT:-8501}

    # Stop existing container
    if docker ps -a --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        print_warning "Stopping existing container..."
        docker stop ${CONTAINER_NAME} 2>/dev/null || true
        docker rm ${CONTAINER_NAME} 2>/dev/null || true
    fi

    # Build image
    print_step "Building Docker image..."
    docker build -t ${IMAGE_NAME}:${VERSION} -t ${IMAGE_NAME}:latest .
    print_success "Docker image built: ${IMAGE_NAME}:${VERSION}"

    # Run container
    print_step "Starting container..."
    docker run -d \
        --name ${CONTAINER_NAME} \
        -p ${PORT}:8501 \
        --restart unless-stopped \
        -v $(pwd)/models:/app/models:ro \
        -v $(pwd)/data:/app/data:ro \
        ${IMAGE_NAME}:latest

    print_success "Container started: ${CONTAINER_NAME}"

    echo ""
    echo -e "${GREEN}=====================================================================${NC}"
    echo -e "${GREEN}  🐳 Docker Deployment Complete!${NC}"
    echo -e "${GREEN}=====================================================================${NC}"
    echo -e "  URL:       ${BLUE}http://localhost:${PORT}${NC}"
    echo -e "  Container: ${GOLD}${CONTAINER_NAME}${NC}"
    echo ""
    echo -e "  Commands:"
    echo -e "  - View logs:  ${BLUE}docker logs ${CONTAINER_NAME}${NC}"
    echo -e "  - Stop:       ${BLUE}docker stop ${CONTAINER_NAME}${NC}"
    echo -e "  - Restart:    ${BLUE}docker restart ${CONTAINER_NAME}${NC}"
    echo ""
}

# =============================================================================
# RUN TESTS
# =============================================================================

run_tests() {
    print_step "Running tests before deployment..."

    if command -v pytest &> /dev/null; then
        pytest tests/ -v --tb=short 2>&1

        if [ $? -eq 0 ]; then
            print_success "All tests passed!"
        else
            print_warning "Some tests failed. Proceeding anyway..."
        fi
    else
        print_warning "pytest not found. Skipping tests."
    fi
}

# =============================================================================
# MAIN
# =============================================================================

print_header

DEPLOY_TARGET=${1:-"local"}

echo -e "  Deploy target: ${GOLD}${DEPLOY_TARGET}${NC}"
echo -e "  Timestamp:     $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Run checks
check_requirements
check_files

# Install dependencies
install_dependencies

# Run tests (skip for local quick deploy)
if [ "${DEPLOY_TARGET}" != "local" ]; then
    run_tests
fi

# Deploy
case ${DEPLOY_TARGET} in
    "local")
        deploy_local
        ;;
    "streamlit")
        deploy_streamlit_cloud
        ;;
    "docker")
        deploy_docker
        ;;
    *)
        print_error "Unknown target: ${DEPLOY_TARGET}"
        echo ""
        echo "Usage: bash scripts/deploy.sh [local|streamlit|docker]"
        echo ""
        echo "  local      - Run locally (default)"
        echo "  streamlit  - Deploy to Streamlit Cloud"
        echo "  docker     - Deploy with Docker"
        exit 1
        ;;
esac

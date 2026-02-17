"""
Package Setup for NBE Credit Risk Intelligence
"""

from setuptools import setup, find_packages
from pathlib import Path

readme = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

requirements = (
    Path(__file__).parent / "requirements.txt"
).read_text().strip().splitlines()

setup(
    name="nbe-credit-risk",
    version="3.0.0",
    author="NBE Credit Risk Team",
    author_email="creditrisk@nbe.com.eg",
    description="AI-Powered Credit Risk Intelligence Platform for NBE",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Goda-Emad/NBE-Credit-Risk-Intelligence-",
    packages=find_packages(exclude=["tests*", "notebooks*"]),
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.12.0",
            "flake8>=7.0.0",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "nbe-train=scripts.train_pipeline:run_pipeline",
            "nbe-evaluate=scripts.evaluate_pipeline:run_evaluation",
        ]
    },
    include_package_data=True,
)

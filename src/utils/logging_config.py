"""
Logging Configuration
Sets up logging for the entire project
"""

import logging
import logging.handlers
import os
from pathlib import Path
from datetime import datetime


def setup_logging(
    log_level: str = "INFO",
    log_dir: str = "logs",
    app_name: str = "nbe_credit_risk"
) -> logging.Logger:
    """
    Setup logging configuration

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_dir:   Directory to save log files
        app_name:  Application name for logger

    Returns:
        Configured logger instance
    """
    # Create logs directory
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)

    # Log file with date
    log_file = log_path / f"{app_name}_{datetime.now().strftime('%Y%m%d')}.log"

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s | %(name)-20s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            # Console handler
            logging.StreamHandler(),
            # File handler with rotation
            logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10 * 1024 * 1024,  # 10 MB
                backupCount=5,
                encoding="utf-8"
            )
        ]
    )

    logger = logging.getLogger(app_name)
    logger.info(f"Logging initialized | Level: {log_level} | File: {log_file}")

    return logger


def get_logger(name: str) -> logging.Logger:
    """Get logger for a specific module"""
    return logging.getLogger(f"nbe_credit_risk.{name}")

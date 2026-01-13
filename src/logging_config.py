import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logging():
    """Configure logging for the application."""
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create formatters and add them to handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create console handler and set level
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Create file handler for general logs with rotation
    file_handler = RotatingFileHandler(
        'app.log', 
        maxBytes=1024*1024*5,  # 5MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Prevent duplicate logs if logging is set up multiple times
    logger.propagate = False

    return logger
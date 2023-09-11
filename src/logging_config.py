import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    """
    Setup logging configuration with a rotating policy
    """

    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create rotating file handler that writes log messages to a file, with a
    # maximum log file size of 1MB, keeping 4 old log files.
    handler = RotatingFileHandler(
        os.path.join(log_dir, "app.log"), maxBytes=1e6, backupCount=4
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(handler)

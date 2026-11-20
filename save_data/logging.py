import logging
import os


def log():
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        os.makedirs("reports", exist_ok=True)
        file_handler = logging.FileHandler("reports/logs.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
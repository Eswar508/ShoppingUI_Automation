import logging,os
def log():
    logger=logging.getLogger(__name__)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        file_handler=logging.FileHandler('results/logs.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
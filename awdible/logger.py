import logging


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s  - %(filename)s - %(levelname)s - %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


logger = get_logger(__name__)

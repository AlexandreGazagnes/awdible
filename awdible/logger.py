"""
Logger module to log the messages
"""

import os
import logging


# LOG_LEVEL = logging.INFO


def get_logger(name, log_folder="logs", log_level="INFO"):
    """Get the logger."""

    # create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(filename)s - %(module)s - %(lineno)s - %(funcName)s()]",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # create file handler
    fn = os.path.join(log_folder, "awdible.log")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # add file handlers to the logger
    fileHandler = logging.FileHandler(fn)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    # add console handler to the logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    return logger


logger = get_logger(__name__)

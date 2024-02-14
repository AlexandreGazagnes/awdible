"""
Fixtures for the tests
"""

import os

import pytest

from awdible.logger import logger
from awdible.core.awdible import Awdible


VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
VIDEO_ID = "V62oKsHdsLU"
VIDEO_QUERY = "jo l'rigolo"


@pytest.fixture
def awdible() -> Awdible:
    """Lod an Awdible instance"""

    return Awdible()


@pytest.fixture
def list_ids() -> list:
    """List of video ids"""

    pwd = os.getcwd()
    logger.warning(f"pwd: {pwd}")
    logger.warning(f"ls: {os.listdir(pwd)}")

    with open("./assets/list_ids.txt", "r") as file:
        return file.read().splitlines()


@pytest.fixture
def list_urls() -> list:
    """List of video urls"""

    pwd = os.getcwd()
    logger.warning(f"pwd: {pwd}")
    logger.warning(f"ls: {os.listdir(pwd)}")

    with open("./assets/list_urls.txt", "r") as file:
        return file.read().splitlines()


@pytest.fixture
def list_queries() -> list:
    """List of video queries"""

    pwd = os.getcwd()
    logger.warning(f"pwd: {pwd}")
    logger.warning(f"ls: {os.listdir(pwd)}")

    with open("./assets/list_queries.txt", "r") as file:
        return file.read().splitlines()


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    if os.path.exists(Awdible.DEFAULT_TMP):
        for file in os.listdir(Awdible.DEFAULT_TMP):
            os.remove(Awdible.DEFAULT_TMP + file)
        os.rmdir(Awdible.DEFAULT_TMP)

    if not os.path.exists(Awdible.DEFAULT_TMP):
        os.makedirs(Awdible.DEFAULT_TMP)

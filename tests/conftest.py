"""
Fixtures for the tests
"""

import os

import pytest

from awdible.core.awdible import Awdible
from awdible.logger import logger

VIDEO_URL_ONE = "https://www.youtube.com/watch?v=9diaThxYnKA"
VIDEO_ID_ONE = "V62oKsHdsLU"

VIDEO_QUERY_ONE = "jo l'rigolo"
VIDEO_QUERY_LIST = ["jo l'rigolo", "c'est de la merde kaamelott"]


def read_file(fn: str) -> str:
    """Read a fn"""

    base = "docs/assets/tests"

    pwd = os.getcwd()
    logger.warning(f"pwd: {pwd}")
    logger.warning(f"ls: {os.listdir(pwd)}")

    _fn = os.path.join(pwd, base, fn)

    if not os.path.exists(_fn):
        raise FileNotFoundError(f"File not found: {_fn}")

    with open(_fn, "r") as _fn:
        out = _fn.readlines()

    if not isinstance(out, list):
        raise ValueError(f"Expected list, got {type(out)}")

    if not len(out):
        raise ValueError(f"Empty file: {_fn}")

    return out


@pytest.fixture
def awdible() -> Awdible:
    """Lod an Awdible instance"""

    return Awdible()


def clean_tmp():
    """Clean the tmp folder"""

    if os.path.exists(Awdible.DEFAULT_TMP):
        for file in os.listdir(Awdible.DEFAULT_TMP):
            os.remove(Awdible.DEFAULT_TMP + file)
        os.rmdir(Awdible.DEFAULT_TMP)

    if not os.path.exists(Awdible.DEFAULT_TMP):
        os.makedirs(Awdible.DEFAULT_TMP)


def pytest_sessionstart(session):
    """Code executed at the start of the session"""

    clean_tmp()
    logger.warning("Session started")

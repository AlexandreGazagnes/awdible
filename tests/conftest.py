"""
Fixtures for the tests
"""

import os

import pytest

from awdible.core.awdible import Awdible


@pytest.fixture
def awdible() -> Awdible:
    """Lod an Awdible instance"""

    return Awdible()


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

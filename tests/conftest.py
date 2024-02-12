"""
Fixtures for the tests
"""

import os

import pytest

from audible.core.audible import Audible


@pytest.fixture
def audible() -> Audible:
    """Lod an Audible instance"""

    return Audible()


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    if os.path.exists(Audible.DEFAULT_TMP):

        for file in os.listdir(Audible.DEFAULT_TMP):
            os.remove(Audible.DEFAULT_TMP + file)
        os.rmdir(Audible.DEFAULT_TMP)

    if not os.path.exists(Audible.DEFAULT_TMP):
        os.makedirs(Audible.DEFAULT_TMP)

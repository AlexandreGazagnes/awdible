"""
Test the Awdible class.
"""

import pytest

from awdible.core.awdible import Awdible
from awdible.logger import logger

from awdible.config import config

from tests.conftest import VIDEO_URL, VIDEO_ID, VIDEO_QUERY

# VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
# VIDEO_ID = "V62oKsHdsLU"
# VIDEO_QUERY = "jo l'rigolo"


class TestAwdible:
    """Test the Awdible class."""

    def test___init__(self):
        Awdible(test_mode=True)

    def test_three(self):
        """Test the Awdible class."""

        print(f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}")
        logger.warning(
            f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}"
        )

        video = VIDEO_QUERY

        awdible = Awdible(video=video, test_mode=True, search=True, config=config)
        assert awdible

        awdible.run()

    def test_one(self):
        """Test the Awdible class."""

        VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
        video = VIDEO_URL

        awdible = Awdible(video=video, test_mode=True, config=config)
        assert awdible

        awdible.run()

    def test_two(self):
        """Test the Awdible class."""

        video = VIDEO_ID

        awdible = Awdible(video=video, test_mode=True, prefix=True, config=config)
        assert awdible

        awdible.run()

"""
Test the Awdible class.
"""

import pytest

from awdible.core.awdible import Awdible
from awdible.logger import logger

from awdible.config import config

VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
VIDEO_ID = "V62oKsHdsLU"
VIDEO_QUERY = "jo l'rigolo"


class TestAwdible:
    """Test the Awdible class."""

    def test___init__(self):
        Awdible(test_mode=True)

    def test_three(self):
        """Test the Awdible class."""

        print(config)
        logger.warning(config)

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
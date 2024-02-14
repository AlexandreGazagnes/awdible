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

    def test_search_mode(self):
        """Test the Awdible class."""

        print(f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}")
        logger.warning(
            f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}"
        )

        video = VIDEO_QUERY

        awdible = Awdible(video=video, test_mode=True, search=True, config=config)
        assert awdible

        awdible.run()

    def test_standard_mode(self):
        """Test the Awdible class."""

        VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
        video = VIDEO_URL

        awdible = Awdible(video=video, test_mode=True, config=config)
        assert awdible

        awdible.run()

    def test_prefix_mode(self):
        """Test the Awdible class."""

        video = VIDEO_ID

        awdible = Awdible(video=video, test_mode=True, prefix=True, config=config)
        assert awdible

        awdible.run()

    def test_list_urls_mode(self, list_urls):
        """Test the Awdible class."""

        awdible = Awdible(video=list_urls, test_mode=True, config=config)
        assert awdible

        awdible.run()

    def test_list_ids_mode(self, list_ids):
        """Test the Awdible class."""

        awdible = Awdible(video=list_ids, test_mode=True, prefix=True, config=config)
        assert awdible

        awdible.run()

    # DISABLE TO PREVENT UNWANTED API CALLS
    # def test_list_queries_mode(self, list_queries):
    #     """Test the Awdible class."""

    #     awdible = Awdible(video=list_queries, test_mode=True, search=True, config=config)
    #     assert awdible

    #     awdible.run()

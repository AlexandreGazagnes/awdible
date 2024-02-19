"""
Test the Awdible class.
"""

import pytest

from awdible.core.awdible import Awdible
from awdible.logger import logger

from awdible.config import config

from tests.conftest import (
    VIDEO_URL_ONE,
    VIDEO_ID_ONE,
    VIDEO_QUERY_ONE,
    VIDEO_QUERY_LIST,
)

# VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
# VIDEO_ID = "V62oKsHdsLU"
# VIDEO_QUERY = "jo l'rigolo"


class TestAwdible:
    """Test the Awdible class."""

    def test___init__(self):
        Awdible(test_mode=True)

    # def test_search_mode_one(self):
    #     """Test the Awdible class."""

    #     # print(f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}")

    #     logger.warning(
    #         f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}"
    #     )

    #     video = VIDEO_QUERY_ONE

    #     awdible = Awdible(
    #         video=video,
    #         test_mode=True,
    #         search=True,
    #         config=config,
    #     )
    #     assert awdible

    #     awdible.run()

    def test_search_mode_list(self):
        """Test the Awdible class."""

        # print(f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}")

        logger.warning(
            f"About config : {config.get('X-RapidAPI-Host', 'No Key found')}"
        )

        video_list = VIDEO_QUERY_LIST

        awdible = Awdible(
            video=video_list,
            search=True,
            prefix=False,
            test_mode=True,
            config=config,
        )

        assert awdible

        awdible.run()

    def test_standard_mode_one(self):
        """Test the Awdible class."""

        video = VIDEO_URL_ONE

        awdible = Awdible(
            video=video,
            search=False,
            prefix=False,
            test_mode=True,
            config=config,
        )
        assert awdible

        awdible.run()

    def test_prefix_mode_one(self):
        """Test the Awdible class."""

        video = VIDEO_ID_ONE

        awdible = Awdible(
            video=video,
            prefix=True,
            search=False,
            test_mode=True,
            config=config,
        )
        assert awdible

        awdible.run()

    # def test_list_urls_mode(self, list_urls):
    #     """Test the Awdible class."""

    #     awdible = Awdible(video=list_urls, test_mode=True, config=config)
    #     assert awdible

    #     awdible.run()

    # def test_list_ids_mode(self, list_ids):
    #     """Test the Awdible class."""

    #     awdible = Awdible(video=list_ids, test_mode=True, prefix=True, config=config)
    #     assert awdible

    #     awdible.run()

    # DISABLE TO PREVENT UNWANTED API CALLS
    # def test_list_queries_mode(self, list_queries):
    #     """Test the Awdible class."""

    #     awdible = Awdible(video=list_queries, test_mode=True, search=True, config=config)
    #     assert awdible

    #     awdible.run()

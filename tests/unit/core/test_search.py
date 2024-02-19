"""
Unit test for the Search module
"""

import pytest

from awdible.core.search import Search
from awdible.logger import logger

QUERY = "jo l'rigolo"


class TestSearch:
    """Test the search module."""

    def test_find(self) -> None:
        """Test the find method"""

        result = Search.find(QUERY)

        # # logger.info(result[:1000])
        # assert result is not None
        # # logger.info(result)

        raise NotImplementedError("Test not implemented.")

    def test_parse(self) -> None:
        """Test the parse method"""

        # json = Search.find(QUERY, context="fr")

        # result = Search.parse(json)

        # logger.info(result)

        raise NotImplementedError("Test not implemented.")

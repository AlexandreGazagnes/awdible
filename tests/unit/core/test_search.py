from audible.core.search import Search
from audible.logger import logger

QUERY = "jo l'rigolo"


class TestSearch:
    def test_find(self) -> None:
        """Test the find method"""

        result = Search.find(QUERY)

        # logger.info(result[:1000])
        assert result is not None
        # logger.info(result)

    def test_parse(self) -> None:
        """Test the parse method"""

        json = Search.find(QUERY, context="fr")

        result = Search.parse(json)

        logger.info(result)

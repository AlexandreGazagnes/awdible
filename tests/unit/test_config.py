"""
Unit Test the config.
"""

from awdible.config import get_config
from awdible.core.defaults import DEFAULT_CONFIG


class TestConfig:
    """Test the config."""

    def test_config(self):
        """Test the config."""

        config = get_config()
        assert config.get("RAPID_API_HOST") == "youtube-data8.p.rapidapi.com"

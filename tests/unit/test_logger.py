"""
Test the logger.
"""

from awdible.logger import get_logger


class TestLogger:
    """Test the logger."""

    def test_logger(self):
        """Test the logger."""

        logger = get_logger(__name__)
        logger.warning("This is a warning message")

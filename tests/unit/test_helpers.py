"""
Unit tests for the awdible.helpers module.
"""

from awdible.helpers import asciize


class TestAsciizeUnit:
    """Ascii conversion tests."""

    def test_asciize_1(self) -> None:
        """Test the asciize function with a simple string."""

        assert asciize("Hello, world!") == "Hello_world"

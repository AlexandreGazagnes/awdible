import pytest

from audible.download.get import Get


class TestGet:
    """Test the Get class."""

    def test_get_audio(self):
        """Test the Get.audio method."""

        url = "https://www.youtube.com/watch?v=EesQolfp9gQ,EesQolfp9gQ"
        out = Get.audio(url)
        assert isinstance(out, tuple)

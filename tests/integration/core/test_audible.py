"""
Test the Audible class.
"""

import pytest

from audible.core.audible import Audible
from audible.logger import logger

VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
VIDEO_ID = "V62oKsHdsLU"
VIDEO_QUERY = "jo l'rigolo"


class TestAudible:
    """Test the Audible class."""

    def test___init__(self):
        Audible(test_mode=True)

    # def test_run_one(self):
    #     assert False  # TODO: implement your test here

    # def test__get_audio(self):
    #     assert False  # TODO: implement your test here

    # def test__save(self):
    #     assert False  # TODO: implement your test here

    # def test__get_save(self):
    #     assert False  # TODO: implement your test here

    # def test__find(self):
    #     assert False  # TODO: implement your test here

    def test_one(self):
        """Test the Audible class."""

        VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
        video = VIDEO_URL

        audible = Audible(video=video, test_mode=True)
        assert audible

        audible.run()

    def test_two(self):
        """Test the Audible class."""

        video = VIDEO_ID

        audible = Audible(video=video, test_mode=True, prefix=True)
        assert audible

        audible.run()

    def test_three(self):
        """Test the Audible class."""

        video = VIDEO_QUERY

        audible = Audible(video=video, test_mode=True, search=True)
        assert audible

        audible.run()

"""
"""

import os
import os

# import logging


# import logging

import requests

from bs4 import BeautifulSoup

from audible.logger import logger

from pytube import YouTube


from .convert import Convert
from .crop import Crop
from .search import Search
from .video import Video
from .defaults import (
    VIDEO_PREFIX,
    DEFAULT_VIDEO_URL,
    DEFAULT_VIDEO_ID,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_OUTPUT,
    DEFAULT_SEARCH,
    DEFAULT_PREFIX,
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_TMP,
    DEFAULT_STREAMLIT,
    DEFAULT_PORT,
    DEFAULT_CROP_LIMIT,
    DEFAULT_TEST_MODE,
)


class Audible:
    """The Audible class is the core of the audible package. It is the main class that
    is used to download the audio from a youtube video. It can be used to download

    Agrs :

    video : str | list : The video url to download from youtube. If you want to input a search query, use the --search option

    dest : str : The destination directory of the file
    file : str : The input file With list of urls/videos
    output : str : The output file name
    crop_limit : int : The limit of duration of the video to download. If the video is longer than the limit, it will be cropped into smaller parts.

    search : bool : If set, the video argument will be treated as a search query and the first result will be downloaded.
    prefix : bool : If set, can ommit the url prefix 'https://www.youtube.com/watch?v=' when passing the video url.
    asynchronous : bool : If set, the download will be asynchronous.

    streamlit : bool : If set, the download will be asynchronous.
    port : int : The port of the streamlit web app.

    test_mode : bool : If set, the download will be asynchronous.
    """

    VIDEO_PREFIX = VIDEO_PREFIX
    DEFAULT_VIDEO_URL = DEFAULT_VIDEO_URL
    DEFAULT_VIDEO_ID = DEFAULT_VIDEO_ID
    DEFAULT_DEST = DEFAULT_DEST
    DEFAULT_FILE = DEFAULT_FILE
    DEFAULT_OUTPUT = DEFAULT_OUTPUT
    DEFAULT_SEARCH = DEFAULT_SEARCH
    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS
    DEFAULT_PREFIX = DEFAULT_PREFIX
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_STREAMLIT = DEFAULT_STREAMLIT
    DEFAULT_PORT = DEFAULT_PORT
    DEFAULT_CROP_LIMIT = DEFAULT_CROP_LIMIT
    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE
    DEFAULT_VIDEO_ID = DEFAULT_VIDEO_ID

    def __init__(
        self,
        video: str | list = DEFAULT_VIDEO_URL,
        dest: str = DEFAULT_DEST,
        file: str = DEFAULT_FILE,
        output: str = DEFAULT_OUTPUT,
        crop_limit: int = DEFAULT_CROP_LIMIT,
        search: bool = DEFAULT_SEARCH,
        default_prefix: bool = DEFAULT_PREFIX,
        asynchronous: bool = DEFAULT_ASYNCHRONOUS,
        streamlit: bool = DEFAULT_STREAMLIT,
        port: int = DEFAULT_PORT,
        test_mode: bool = DEFAULT_TEST_MODE,
    ):
        """Init the Audible class"""
        self._audible = None
        self.video = video
        self.video_list = video if isinstance(video, list) else [video]
        self.dest = dest
        self.file = file
        self.output = output
        self.crop_limit = crop_limit

        self.search = search
        self.default_prefix = default_prefix
        self.asynchronous = asynchronous

        self.streamlit = streamlit
        self.port = port

        self.test_mode = test_mode

    def run(self):
        """Run the audible session"""

        # check default tmp do exist

        if self.test_mode or self.streamlit:
            if not os.path.exists(self.DEFAULT_TMP):
                os.makedirs(self.DEFAULT_TMP)

            self.dest = self.DEFAULT_TMP

        for video in self.video_list:
            self.run_one(video)

    def run_one(self, video: str):
        """Run the audible session for one video"""

        out = ""

        # good case
        if video.startswith(self.VIDEO_PREFIX):
            out = self._get_stream_save_convert(video)

        # if not valid and search is True:
        if not video.startswith(self.VIDEO_PREFIX) and self.search:
            url = self._find_parse(video)[0]
            out = self._get_stream_save_convert(url)

        # try  adding the prefix
        if not video.startswith(self.VIDEO_PREFIX):  # and self.default_prefix
            video = self.VIDEO_PREFIX + video

            try:
                out = self._get_stream_save_convert(video)
            except Exception as e:
                logger.error(f"Error: {e}")

            try:
                url = self._find_parse(video)[0]
                out = self._get_stream_save_convert(url)
            except Exception as e:
                logger.error(f"Error: {e}")

        logger.warning(f"Downloaded  OK: {out}")

        return out

    def _get(self, url: str) -> tuple:
        """Get the audio from the video"""

        return Video.get(url)

    def _stream(self, yt: YouTube) -> tuple:
        """Get the audio from the video"""

        return Video.stream(yt)

    def _save(self, title: str, media: YouTube) -> str:
        """Save the audio from the video"""

        return Video.save(title, media, self.dest)

    def _get_stream(self, url: str) -> tuple:
        """Get the audio from the video"""

        yt = self._get(url)
        title, media = self._stream(yt)
        return title, media

    def _get_stream_save(self, url):
        """Get the audio from the video and save it"""

        title, media = self._get_stream(url)
        out = self._save(title, media)
        return out

    def _get_stream_save_convert(self, url):
        """Get the audio from the video and save it"""

        src = self._get_stream_save(url)
        out = self._convert_to_mp3(src)
        return out

    def _find(self, keywords: str) -> list[str]:
        """Find the video"""

        html = Search.find(keywords)
        return html

    def _parse(self, html: str) -> list[str]:
        """Parse the video"""

        href_list = Search.parse(html)
        return href_list

    def _find_parse(self, keywords: str) -> list[str]:
        """Find and parse the video"""

        html = self._find(keywords)
        href_list = self._parse(html)
        return href_list

    def _convert_to_mp3(self, src: str) -> str:
        """Convert the video to mp3"""

        dest = Convert.to_mp3(src)
        return dest

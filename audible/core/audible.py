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

DEFAULT_VIDEO = "https://www.youtube.com/watch?v=9diaThxYnKA"
DEFAULT_DEST = "./"
DEFAULT_FILE = None
DEFAULT_OUTPUT = "mp4"
DEFAULT_SEARCH = False
DEFAULT_PREFIX = False
DEFAULT_ASYNCHRONOUS = False
VIDEO_PREFIX = "https://www.youtube.com/watch?v="
DEFAULT_TMP = "./tmp/"
DEFAULT_STREAMLIT = False
DEFAULT_PORT = 8501
DEFAULT_CROP_LIMIT = 3600


class Audible:
    """The Audible class is the core of the audible package. It is the main class that"""

    DEFAULT_VIDEO = DEFAULT_VIDEO
    DEFAULT_DEST = DEFAULT_DEST
    DEFAULT_FILE = DEFAULT_FILE
    DEFAULT_OUTPUT = DEFAULT_OUTPUT
    DEFAULT_SEARCH = DEFAULT_SEARCH
    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS
    DEFAULT_PREFIX = DEFAULT_PREFIX
    VIDEO_PREFIX = VIDEO_PREFIX
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_STREAMLIT = DEFAULT_STREAMLIT
    DEFAULT_PORT = DEFAULT_PORT
    DEFAULT_CROP_LIMIT = DEFAULT_CROP_LIMIT

    def __init__(
        self,
        video: str | list = DEFAULT_VIDEO,
        dest: str = DEFAULT_DEST,
        file: str = DEFAULT_FILE,
        output: str = DEFAULT_OUTPUT,
        search: bool = DEFAULT_SEARCH,
        default_prefix: bool = DEFAULT_PREFIX,
        asynchronous: bool = DEFAULT_ASYNCHRONOUS,
        streamlit: bool = DEFAULT_STREAMLIT,
        port: int = DEFAULT_PORT,
        crop_limit: int = DEFAULT_CROP_LIMIT,
    ):
        self._audible = None
        self.video = video
        self.video_list = video if isinstance(video, list) else [video]
        self.dest = dest
        self.file = file
        self.output = output
        self.search = search
        self.default_prefix = default_prefix
        self.asynchronous = asynchronous
        self.streamlit = streamlit
        self.port = port
        self.crop_limit = crop_limit

    def run(self):
        """Run the audible session"""

        # check default tmp do exist
        if not os.path.exists(self.DEFAULT_TMP):
            os.makedirs(self.DEFAULT_TMP)

        for video in self.video_list:
            self.run_one(video)

    def run_one(self, video: str):
        """Run the audible session for one video"""

        out = ""

        # good case
        if video.startswith(self.VIDEO_PREFIX):
            out = self._get_save(video)

        # if not valid and search is True:
        if not video.startswith(self.VIDEO_PREFIX) and self.search:
            video = self._find_parse(video)[0]
            out = self._get_save(video)

        # try  adding the prefix
        if not video.startswith(self.VIDEO_PREFIX):  # and self.default_prefix
            video = self.VIDEO_PREFIX + video
            try:
                out = self._get_save(video)
            except Exception as e:
                logger.error(f"Error: {e}")
                logger.error(f"Video {video} not found")
                raise e

        logger.warning(f"Downloaded  OK: {out}")

    def _get_audio(self, url: str) -> tuple:
        """Get the audio from the video"""

        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        title = yt.title.replace(" ", "_")

        return title, video

    def _save(self, title: str, video: YouTube) -> str:
        """Save the audio from the video"""

        out = video.download(self.dest)

        title += ".mp4"
        os.rename(out, self.dest + title)

        return self.dest + title

    def _get_save(self, url: str) -> str:
        """Get and save the audio from the video"""

        title, video = self._get_audio(url)
        out = self._save(title, video)

        return out

    def _find(self, keywords: str) -> list[str]:
        """Find the video"""

        keywords = keywords.replace(" ", "+")

        url = self.BASE_URL + keywords

        response = requests.get(url)
        response.raise_for_status()

        return response.text

    def _parse(self, html: str) -> list[str]:
        """Parse the video"""

        soup = BeautifulSoup(html, "html.parser")
        a_list = soup.find_all("a", {"id": "video-title"})
        href_list = [a["href"] for a in a_list]

        return href_list

    def _find_parse(self, keywords: str) -> list[str]:
        """Find and parse the video"""

        html = self._find(keywords)
        href_list = self._parse(html)
        return href_list

"""
Awidble is a package that allows you to download the audio from a youtube video. It can be used to download the audio from a single video or from a list of videos. It can also be used to download the audio from a video that is longer than a certain duration. It can also be used to download the audio from a video that is the result of a search query.
"""

import subprocess
import os

import requests
from bs4 import BeautifulSoup
from pytube import YouTube

from awdible.logger import logger
from awdible.config import config
from .convert import Convert
from .crop import Crop
from .defaults import (
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_CONTEXT,
    DEFAULT_CROP_LIMIT,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_OUTPUT,
    DEFAULT_PORT,
    DEFAULT_PREFIX,
    DEFAULT_SEARCH,
    DEFAULT_STREAMLIT,
    DEFAULT_TEST_MODE,
    DEFAULT_TMP,
    DEFAULT_LOG,
    DEFAULT_VIDEO_ID,
    DEFAULT_VIDEO_URL,
    VIDEO_PREFIX,
    DEFAULT_CONFIG,
    DEFAULT_FORCE,
)

import asyncio

from .validators import (
    Dir,
    File,
    Output,
    # Config,
    Context,
    Bool,
)
from .search import Search
from .video import Video

# import logging


# import logging


class Awdible:
    """The Awdible class is the core of the awdible package. It is the main class that
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
    DEFAULT_CROP_LIMIT = DEFAULT_CROP_LIMIT
    DEFAULT_CONTEXT = DEFAULT_CONTEXT

    DEFAULT_SEARCH = DEFAULT_SEARCH
    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS
    DEFAULT_PREFIX = DEFAULT_PREFIX

    DEFAULT_FORCE = DEFAULT_FORCE
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_LOG = DEFAULT_LOG

    DEFAULT_STREAMLIT = DEFAULT_STREAMLIT
    DEFAULT_PORT = DEFAULT_PORT

    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE

    DEFAULT_CONFIG = DEFAULT_CONFIG

    dest = Dir()
    file = File()
    output = Output()
    crop_limit = Crop()
    context = Context()
    search = Bool()
    prefix = Bool()
    asynchronous = Bool()
    streamlit = Bool()
    test_mode = Bool()
    # config = Config()

    def __init__(
        self,
        video: str | list = DEFAULT_VIDEO_URL,
        dest: str = DEFAULT_DEST,
        file: str = DEFAULT_FILE,
        output: str = DEFAULT_OUTPUT,
        force: bool = DEFAULT_FORCE,
        crop_limit: int = DEFAULT_CROP_LIMIT,
        context: str = DEFAULT_CONTEXT,
        search: bool = DEFAULT_SEARCH,
        prefix: bool = DEFAULT_PREFIX,
        asynchronous: bool = DEFAULT_ASYNCHRONOUS,
        streamlit: bool = DEFAULT_STREAMLIT,
        port: int = DEFAULT_PORT,
        test_mode: bool = DEFAULT_TEST_MODE,
        config: dict = config,
    ):
        """Init the Awdible class"""

        self._awdible = None

        self.video = video

        _video_list = video if isinstance(video, list) else [video]
        self.video_list = list(set(_video_list))

        self.dest = dest
        self.file = file
        self.output = output
        self.crop_limit = crop_limit
        self.context = context

        self.search = search
        self.prefix = prefix
        self.asynchronous = asynchronous

        self.streamlit = streamlit
        self.port = port

        self.test_mode = test_mode

        self.config = config

        self.log = self.DEFAULT_LOG
        self.tmp = self.DEFAULT_TMP

        self.force = force
        self.ffmpeg_installed = self._is_ffmpeg_installed()

        if not self.ffmpeg_installed:
            self._manage_ffmpeg()

    def run(self):
        """Run the awdible session"""

        logger.info(f"Before celanfille")

        if self.file:
            self._clean_file()

        logger.info(f"After celanfille")

        if not os.path.exists(self.DEFAULT_TMP):
            os.makedirs(self.DEFAULT_TMP)

        if not os.path.exists(self.DEFAULT_LOG):
            os.makedirs(self.DEFAULT_LOG)

        if not os.path.exists(self.DEFAULT_DEST):
            os.makedirs(self.DEFAULT_DEST)

        if self.asynchronous:
            outs = self.run_asynch()
        else:
            outs = self.run_synch()

        return outs

    def run_synch(self):
        """Run the awdible session synchronously"""

        logger.info("Ok Here")

        self.video_list = [
            video for video in self.video_list if (video and not video.startswith("#"))
        ]

        logger.warning(f"Video list: {self.video_list}")

        outs = [self.run_one(video) for video in self.video_list]

        logger.info("12345")

        if len(outs) == 1:
            return outs[0]

        return outs

    async def run_asynch(self):
        """Run the awdible session asynchronously"""

        # out = await asyncio.gather(
        raise NotImplementedError("Sorry Bro! ")

    def run_one(self, video: str):
        """Run the awdible session for one video"""

        out = ""

        # good case
        if video.startswith(self.VIDEO_PREFIX):
            out = self._get_stream_save_convert(video)

        # if not valid and search is True:
        elif (not video.startswith(self.VIDEO_PREFIX)) and self.search:
            url = self._find_parse(video)[0]
            out = self._get_stream_save_convert(url)

        # if not valid and search is True:
        elif (not video.startswith(self.VIDEO_PREFIX)) and self.prefix:
            video = self.VIDEO_PREFIX + video
            out = self._get_stream_save_convert(video)

        # try  adding the prefix
        else:  # and self.default_prefix
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

        json = Search.find(keywords, context=self.context, config=self.config)
        return json

    def _parse(self, json: str) -> list[str]:
        """Parse the video"""

        href_list = Search.parse(json)
        return href_list

    def _find_parse(self, keywords: str) -> list[str]:
        """Find and parse the video"""

        json = self._find(keywords)
        href_list = self._parse(json)
        return href_list

    def _convert_to_mp3(self, src: str) -> str:
        """Convert the video to mp3"""

        dest = Convert.to_mp3(src, self.ffmpeg_installed)
        return dest

    def _clean_file(self):
        """Clean the file"""

        with open(self.file, "r") as f:
            lines = f.readlines()

        lines = [line.strip() for line in lines if line]
        lines = list(set(lines))
        lines = sorted(lines)

        hastag = [line for line in lines if not line.startswith("#")]
        self.video_list = hastag
        not_hastag = [line for line in lines if not line.startswith("#")]

        # TODO :  CLEAN éà typo errors "  " or  "- " etc

        final = not_hastag + hastag
        final = [f"{line}\n" for line in final]
        final = [i for i in final if i.strip()]

        with open(self.file, "w") as f:
            f.writelines(final)

    def _is_ffmpeg_installed(self) -> bool:
        """Check if ffmpeg is installed"""

        try:
            out = subprocess.run(["ffmpeg", "-version"], capture_output=True)
            # r = os.system("ffmpeg -version")
        except Exception as e:
            logger.error(f"Error: {e}")
            return False
        else:
            return True if not int(out.returncode) else False

    def _manage_ffmpeg(self):

        if self.force:
            logger.warning("ffmpeg is not installed, output will be in mp4 format")

        else:
            raise AttributeError(
                "ffmpeg is not installed - pass the --force option to continue adn force the download in mp4 format."
            )

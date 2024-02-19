"""
Awidble is a package that allows you to download the audio from a youtube video. It can be used to download the audio from a single video or from a list of videos. It can also be used to download the audio from a video that is longer than a certain duration. It can also be used to download the audio from a video that is the result of a search query.
"""

import subprocess
import os

import requests
from bs4 import BeautifulSoup
from pytube import YouTube

from ..logger import logger
from ..config import config
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

# import asyncio

# from .validators import (
#     Dir,
#     File,
#     Output,
#     # Config,
#     Context,
#     Bool,
# )
from .search import Search
from .video import Video
from .io import Io
from .prerequires import Prerequires

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

    # dest = Dir()
    # file = File()
    # output = Output()
    # crop_limit = Crop()
    # context = Context()
    # search = Bool()
    # prefix = Bool()
    # asynchronous = Bool()
    # streamlit = Bool()
    # test_mode = Bool()
    # # config = Config()

    def __init__(
        self,
        video: str | list = DEFAULT_VIDEO_URL,
        dest: str = DEFAULT_DEST,
        file: str = DEFAULT_FILE,
        output: str = DEFAULT_OUTPUT,
        force: bool = DEFAULT_FORCE,
        crop_limit: int = DEFAULT_CROP_LIMIT,
        context: str = DEFAULT_CONTEXT,
        lang: str = "NotImplemented",
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

        self.ok_video_list = []
        self.ko_video_list = []

        self.dest = dest
        self.file = file
        self.output = output
        self.crop_limit = crop_limit
        self.force = force
        # TODO : Change context to "song" / "video" "audiobook" "podcast" "live"
        # TODO : enabla lang isntead of context en "fr" "es" or None
        # TODO add auto context and lang detection
        self.context = context
        self.lang = lang

        self.search = search
        self.prefix = prefix
        self.asynchronous = asynchronous

        self.streamlit = streamlit
        self.port = port

        self.test_mode = test_mode

        self.config = config

        self.log = self.DEFAULT_LOG
        self.tmp = self.DEFAULT_TMP

        self.ffmpeg_installed = Prerequires.has_ffmpeg()
        self.connection = Prerequires.has_connection()

    def _pre_run(self):
        """Perform the pre run checks"""

        # manage if not ffmpeg installed
        if (not self.ffmpeg_installed) and self.force:
            logger.warning("ffmpeg is not installed BUT force option activated")

        if (not self.ffmpeg_installed) and (not self.force):
            logger.error(f"ffmpeg is not installed and --force option not activated")
            logger.error(f"consider installing ffmpeg or using --force option")
            raise AttributeError(
                "ffmpeg is not installed => Install ffmpeg or use --force option"
            )

        # manage if not connection
        if not self.connection:
            raise ConnectionError("No internet connection found")

        # manage if not not folders
        Io.build_folders([self.dest, self.tmp, self.log], create=True)

        # manage if file
        if self.file:
            self.video_list = Io.clean_list_videos(self.file)

        # last clean
        self.video_list = [
            v for v in self.video_list if (v and (not v.startswith("#")))
        ]
        self.video_list = [v.strip() for v in self.video_list if v.strip()]
        self.video_list = list(set(self.video_list))

    def run(self):
        """Run the awdible session"""

        # pre run checks
        self._pre_run()

        # manage synch vs asynch
        if self.asynchronous:
            outs = self.run_asynch()
        else:
            outs = self.run_synch()

        logger.info(f"Outs : {outs}")

    def run_synch(self):
        """Run the awdible session synchronously"""

        outs = []

        # loop over the video list
        for video in self.video_list:
            # run one
            out = self.run_one_synch(video)
            outs.append(out)

            # add to relevant list
            if out:
                self.ok_video_list.append([video, out])
            else:
                self.ko_video_list.append([video, out])

        logger.info(f"Video list: {self.video_list}")
        logger.warning(f"OK video list: {self.ok_video_list}")
        logger.error(f"KO video list: {self.ko_video_list}")

        return outs

    async def run_asynch(self):
        """Run the awdible session asynchronously"""

        # out = await asyncio.gather(
        raise NotImplementedError("Sorry Bro! ")

    def run_one_synch(self, video: str):
        """Run the awdible session for one video"""

        # good case
        if video.startswith(self.VIDEO_PREFIX):
            try:
                fn = self._get_stream_save_convert(video)
                return fn
            except Exception as e:
                logger.error(f"Error: {e}")
                return None

        # if not valid and search is True:
        elif (not video.startswith(self.VIDEO_PREFIX)) and self.search:
            # get urls from search
            urls = self._find_parse(video, n_results=5)
            logger.info(f"Urls found : {urls}")

            for url in urls:
                logger.info(f"Trying to download from url : {url}")
                try:
                    fn = self._get_stream_save_convert(url)
                    return fn
                except Exception as e:
                    logger.error(f"Error: {e}")
            return None

        # if not valid and search is True:
        elif (not video.startswith(self.VIDEO_PREFIX)) and self.prefix:
            VIDEO_PREFIX = (
                self.VIDEO_PREFIX
                if self.VIDEO_PREFIX.endswith("/")
                else self.VIDEO_PREFIX + "/"
            )
            video = VIDEO_PREFIX + video
            try:
                fn = self._get_stream_save_convert(video)
                return fn
            except Exception as e:
                logger.error(f"Error: {e}")
                return None

        else:  # and self.default_prefix
            raise AttributeError("Sorry Bro! ")

    def _get_stream_save(self, url):
        """Get the audio from the video and save it"""

        fn = Video.get_stream_save(url, self.dest)

        return fn

    def _get_stream_save_convert(self, url):
        """Get the audio from the video and save it"""

        fn = Video.get_stream_save(url, self.dest)
        fn = self._convert(fn)

        return fn

    def _find_parse(
        self,
        keywords: str,
        n_results=5,
    ) -> list[str]:
        """Find and parse the video"""

        urls = Search.find_parse(
            keywords,
            config=self.config,
            context=self.context,
            n_results=n_results,
            lang=self.lang,
            silent_mode=False,
        )

        return urls

    def _convert(
        self,
        src: str,
        overwrite=True,
        remove_src=True,
    ) -> str:
        """Convert the video to mp3"""

        # convert
        fn = Convert.to_mp3(src, overwrite=True, remove_src=True)

        return fn

"""
Awdible module
"""

import time


from ..config import config
from ..logger import logger

from .convert import Convert
from .crop import Crop
from .io import Io
from .prerequires import Prerequires
from .search import Search
from .video import Video
from .defaults import (
    DEFAULT_ASYNCHRONOUS,
    DEFAULT_CONFIG,
    DEFAULT_CONTEXT,
    DEFAULT_CROP_LIMIT,
    DEFAULT_DEST,
    DEFAULT_FILE,
    DEFAULT_FORCE,
    DEFAULT_LOG,
    DEFAULT_OUTPUT,
    DEFAULT_PORT,
    DEFAULT_PREFIX,
    DEFAULT_SEARCH,
    DEFAULT_SEARCH_NUMBER,
    DEFAULT_SLEEPER,
    DEFAULT_STREAMLIT,
    DEFAULT_TEST_MODE,
    DEFAULT_TMP,
    DEFAULT_VIDEO_ID,
    DEFAULT_VIDEO_URL,
    MAX_SEARCH_NUMBER,
    VIDEO_PREFIX,
)


class Awdible:
    """
    Awidble is a package that allows you to download the audio from a youtube video.
    It can be used to download the audio from a single video or from a list of videos.
    It can also be used to download the audio from a video that is longer than a certain duration.
    It can also be used to download the audio from a video that is the result of a search query.

    ----

    The Awdible class is the core of the awdible package.

    Agrs :

        video : str | list | None :
            The video url / list of videos to download from youtube. If you want to input a search query, use the --search option
            This attribute can be null only if the search option is set to True.

        dest : str :
            The destination directory of the file to download

        file : str | None :
            The input filewWith list of urls/videos. Default is None.
            If set, the video argument will be ignored.
            If not set and video not set, an error sound be raised.

        output : str :
            The output format of the file to download. Default is mp3.
            No other format is supported for now.

        crop_limit : int :
            The limit of duration of the video to download. If the video is longer than the limit, it will be cropped into smaller parts.
            This feature is not yet implemented.

        force : bool :
            If set, the download will be forced even if the ffmpeg is not installed.
            If not set and ffmpeg is not installed, an error will be raised.

        context: str :
            The language context of the video to download. Default is "en".
            This feature is not yet implemented.
            DEPRECIATION WARNING : This feature will be changed in the future.
            Context will be "song" / "video" "audiobook" "podcast" "live" and "en" "fr" "es" or None

        lang: str :
            This feature is not yet implemented.
            DEPRECIATION WARNING : This feature will be overlap the context feature in the future.

        search : bool :
            If set, the video argument will be treated as a search query and the first result will be downloaded.

        search_number : int :
            The number of results to download from the search query, if the search option is set to True.
            ie : search_number=5 will download the first 5 results from the search query.
            default is 1.
            MAX_SEARCH_NUMBER = 5

        prefix : bool :
            If set, can ommit the url prefix 'https://www.youtube.com/watch?v=' when passing the video url.
            DEPRECIATION WARNING : This feature will be removed in the future.

        asynchronous : bool :
            If set, the download will be asynchronous.
            This feature is not yet implemented.

        streamlit : bool :
            If set, a streamlit session should be launched.

        port : int :
            The port of the streamlit web app.

        test_mode : bool :
            If set, the test mode will be activated.

        config : dict :
            The config of the awdible package.
            Most important is the RAPID_API_KEY and RAPID_API_HOST for the youtube search allowed with the --search option.

        sleeper : int :
            The time to sleep between two downloads.
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
    DEFAULT_SEARCH_NUMBER = DEFAULT_SEARCH_NUMBER
    MAX_SEARCH_NUMBER = MAX_SEARCH_NUMBER

    DEFAULT_ASYNCHRONOUS = DEFAULT_ASYNCHRONOUS
    DEFAULT_PREFIX = DEFAULT_PREFIX

    DEFAULT_FORCE = DEFAULT_FORCE
    DEFAULT_TMP = DEFAULT_TMP
    DEFAULT_LOG = DEFAULT_LOG

    DEFAULT_STREAMLIT = DEFAULT_STREAMLIT
    DEFAULT_PORT = DEFAULT_PORT

    DEFAULT_TEST_MODE = DEFAULT_TEST_MODE

    DEFAULT_CONFIG = DEFAULT_CONFIG

    DEFAULT_SLEEPER = DEFAULT_SLEEPER

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
        search_number: int = DEFAULT_SEARCH_NUMBER,
        prefix: bool = DEFAULT_PREFIX,
        asynchronous: bool = DEFAULT_ASYNCHRONOUS,
        streamlit: bool = DEFAULT_STREAMLIT,
        port: int = DEFAULT_PORT,
        test_mode: bool = DEFAULT_TEST_MODE,
        config: dict = config,
        sleeper=DEFAULT_SLEEPER,
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
        self.search_number = search_number

        # TODO ADD A VALIDATOR
        if self.search_number > self.MAX_SEARCH_NUMBER:
            self.search_number = self.MAX_SEARCH_NUMBER
        self.prefix = prefix
        self.asynchronous = asynchronous

        self.streamlit = streamlit
        self.port = port

        self.test_mode = test_mode

        self.config = config

        self.log = self.DEFAULT_LOG
        self.tmp = self.DEFAULT_TMP

        self.sleeper = sleeper

        self.ffmpeg_installed = Prerequires.has_ffmpeg()
        self.connection = Prerequires.has_connection()

        logger.warning(f"\n\n\n---NEW INIT---\n\n\n")

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
            self.video_list = Io.clean_list_videos(
                self.file,
                sort=True,
                rewrite=True,
            )

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

            # sleep
            time.sleep(self.sleeper)

        outs = self._outro(outs)
        return outs

    def _outro(self, outs=None):
        """Outro of the awdible session"""

        logger.info(f"Video list: {self.video_list}")
        logger.warning(f"OK video list: {self.ok_video_list}")
        logger.warning(f"KO video list: {self.ko_video_list}")

        # TODO : add an io method to clean dest from .mp4 ONLY if 2 different files type
        # if only mp4, keep the files => maybe ffmpeg is not installed and --force option activated

        return outs

    async def run_asynch(self):
        """Run the awdible session asynchronously"""

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
                # self._outro()
                return None

        # if not valid and search is True:
        elif (not video.startswith(self.VIDEO_PREFIX)) and self.search:
            # get urls from search
            urls = self._find_parse(video, n_results=5)

            # manage if no urls
            logger.info(f"Urls found : {urls}")
            if not urls:
                return None

            # TODO to really enable this possibility of dowloading the first n results
            # TODO of the search we need, at least, to have a return [fn]
            # TODO and to manage the run_one out management of our attributes

            for url in urls[: self.search_number]:
                logger.info(f"Trying to download from url : {url}")
                try:
                    fn = self._get_stream_save_convert(url)
                    return fn
                except Exception as e:
                    logger.error(f"Error: {e}")
                    time.sleep(3)

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
                # self._outro()
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
        retry=5,
    ) -> list[str]:
        """Find and parse the video"""

        urls = []

        logger.warning(f"Searching for video with keywords : {keywords}")

        for i in range(retry):
            try:
                urls = Search.find_parse(
                    keywords,
                    config=self.config,
                    context=self.context,
                    n_results=n_results,
                    lang=self.lang,
                    silent_mode=False,
                )

                logger.info(f"Urls found : {urls}")

                if urls:
                    return urls

            except Exception as e:
                logger.error(f"Error: {e}")

            time.sleep(3)
            logger.warning(
                f"Retry... {i+1} / {retry} for keywords : {keywords}, context : {self.context}, lang : {self.lang}"
            )

        return []

    def _convert(
        self,
        src: str,
        overwrite=True,
        remove_src=True,
    ) -> str:
        """Convert the video to mp3"""

        # convert
        fn = Convert.to_mp3(
            src,
            overwrite=overwrite,
            remove_src=remove_src,
        )

        return fn

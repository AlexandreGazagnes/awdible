"""
Video module
"""

import os
import secrets

from pytube import YouTube

from awdible.core.defaults import VIDEO_PREFIX
from awdible.logger import logger


class Video:
    """Get the video from Youtube, extract audio from the video and save it"""

    @classmethod
    def _get(
        cls,
        url: str,
        silent_mode=False,
    ) -> tuple:
        """Get the audio from the url with Youtube"""

        # MANAGE URL PROBLEM
        # TODO : better tot raise an error
        # This code should not be here
        if not url.startswith(VIDEO_PREFIX):
            url = VIDEO_PREFIX + url

        try:
            yt = YouTube(url)
            return yt

        except Exception as e:
            logger.critical(f"Error: {e}")
            logger.critical(f"url {url} not correct ")
            if not silent_mode:
                raise AttributeError(f"Video {url} not correct")

    @classmethod
    def _stream(
        cls,
        yt: YouTube,
        url: str,
        silent_mode=False,
    ) -> tuple:
        """Get the audio from the stream from the video"""

        try:
            media = yt.streams.filter(only_audio=True).first()
            title = yt.title.replace(" ", "_")
            return title, media

        except Exception as e:
            logger.critical(f"Error: {e}")
            logger.critical(f"Video {url} not found")
            if not silent_mode:
                raise FileNotFoundError(f"Video {url} not found")

    @classmethod
    def _save(
        cls,
        title: str,
        media: YouTube,
        dest: str,
        silent_mode=False,
    ) -> str:
        """Save the audio from the media"""

        # # this code sould not be here
        # if not os.path.exists(cls.DEST):
        #     os.makedirs(cls.DEST)

        #  download
        out = media.download(dest)

        # TODO : ascize the title
        # title = ascize(title)

        # addd the extension
        title += ".mp4"

        # rename the title
        fn = os.path.join(dest, title)
        os.rename(out, fn)

        return fn

    @classmethod
    def get_stream(cls, url, silent_mode=False):
        """Get and stream"""

        yt = cls._get(url, silent_mode=silent_mode)
        title, media = cls._stream(yt, url, silent_mode=silent_mode)

        return title, media

    @classmethod
    def get_stream_save(cls, url, dest, silent_mode=False):
        """Get and stream and save"""

        yt = cls._get(url, silent_mode=silent_mode)
        title, media = cls._stream(yt, url, silent_mode=silent_mode)
        fn = cls._save(title, media, dest, silent_mode=silent_mode)

        return fn

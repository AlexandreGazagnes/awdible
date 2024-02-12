import os
import logging

import secrets

from pytube import YouTube

from audible.core.defaults import (
    VIDEO_PREFIX,
    DEFAULT_VIDEO_ID,
    DEFAULT_VIDEO_URL,
)


class Video:
    """Get the audio from the video"""

    DEST = "./tmp/"

    @classmethod
    def get(self, url: str) -> tuple:
        """Get the audio from the video"""

        try:
            yt = YouTube(url)
            return yt

        except Exception as e:
            logging.error(f"Error: {e}")
            logging.error(f"url {url} not correct ")
            raise AttributeError(f"Video {url} not correct")

    @classmethod
    def stream(self, yt: YouTube) -> tuple:
        try:
            media = yt.streams.filter(only_audio=True).first()
            title = yt.title.replace(" ", "_")
            return title, media

        except Exception as e:
            logging.error(f"Error: {e}")
            logging.error(f"Video {url} not found")
            raise FileNotFoundError(f"Video {url} not found")

    @classmethod
    def save(self, title: str, media: YouTube, dest: str | None = None) -> str:
        """Save the audio from the media"""

        dest = dest if dest else self.DEST

        if not os.path.exists(dest):
            os.makedirs(dest)

        out = media.download(dest)

        title += ".mp4"
        os.rename(out, dest + title)

        return dest + title


if __name__ == "__main__":
    # TEST

    url = DEFAULT_VIDEO_URL
    YouTube(url)

    # title, video = Get.audio(url)
    # out = Get.save(title, video)
    # print(out)

    url = VIDEO_PREFIX + secrets.token_hex(64)

    YouTube(url)

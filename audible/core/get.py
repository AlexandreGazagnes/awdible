import os
import logging

from pytube import YouTube


class Get:
    """Get the audio from the video"""

    DEST = "./tmp/"

    @classmethod
    def audio(self, url: str) -> tuple:
        """Get the audio from the video"""

        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        title = yt.title.replace(" ", "_")

        return title, video

    @classmethod
    def save(self, title: str, video: YouTube) -> str:
        """Save the audio from the video"""

        out = video.download(self.DEST)

        title += ".mp4"
        os.rename(out, self.DEST + title)

        return self.DEST + title

import os

from pytube import YouTube


class Get:
    """Get the audio from the video"""

    @classmethod
    def audio(self, url):
        """Get the audio from the video"""

        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        title = yt.title.replace(" ", "_")
        # os.rename(title + ".mp4", title + ".mp3")

        return title, video

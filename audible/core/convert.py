import os
import ffmpeg

from audible.logger import logger


class Convert:

    @classmethod
    def to_mp3(cls, src: str) -> str:
        """Convert the video to mp3"""

        logger.debug(f"Converting {src} to mp3")

        # get the destination
        dest = src.split(".")[:-1]
        dest = ".".join(dest) + ".mp3"

        # logger.debug(f"Destination: {dest}")

        # the command
        cmd = {"q:a": 0, "map": "a"}

        # do the conversion
        ffmpeg.input(src).output(dest, **cmd).run()

        # del  old file
        os.remove(src)

        return dest

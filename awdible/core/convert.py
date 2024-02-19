"""
Convert the video to mp3
"""

import os

# import ffmpeg

from awdible.logger import logger


class Convert:
    """Convert the video to mp3"""

    @classmethod
    def to_mp3(
        cls,
        src: str,
        is_ffmpeg_installed: bool,
    ) -> str:
        """Convert the video to mp3"""

        if not is_ffmpeg_installed:
            logger.warning("ffmpeg is not installed")

        logger.debug(f"Converting {src} to mp3")

        # get the destination
        dest = src.split(".")[:-1]
        dest = ".".join(dest) + ".mp3"

        # logger.debug(f"Destination: {dest}")

        ############## Old method ################
        # the command
        # cmd = {
        #     "q:a": 0,
        #     "map": "a",
        #     "loglevel": "quiet",
        # }

        # do the conversion
        # ffmpeg.input(src).output(dest, **cmd).run()

        ############## New method ################
        cmd = f"ffmpeg -i {src} -q:a 0 -loglevel error -map a {dest} -y"
        out = os.system(cmd)

        # subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)

        # del  old file
        os.remove(src)

        return dest

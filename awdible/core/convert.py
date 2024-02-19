"""
Convert module 
"""

import os

from awdible.logger import logger

import subprocess


class Convert:
    """Convert the video in various formats"""

    @classmethod
    def to_mp3(
        cls,
        src: str,
        overwrite: bool = False,
        remove_src: bool = True,
        silent_mode: False = False,
    ) -> str:
        """Convert the video to mp3"""

        if not os.path.exists(src):
            logger.error(f"File not found: {src}")
            if not silent_mode:
                raise FileNotFoundError(f"File not found: {src}")

        # get the destination
        dest = src.split(".")[:-1]
        dest = ".".join(dest) + ".mp3"

        logger.info(f"Converting  src : {src} to mp3 with dest : {dest}")

        # creating cmd
        cmd = f"ffmpeg -i {src} -q:a 0 -loglevel error -map a {dest}"
        if overwrite:
            cmd += " -y"

        # run the command
        logger.info(f"Running the command : cmd : {cmd}")
        prc = subprocess.run(cmd.split(" "), capture_output=True)

        # manage the output
        if prc.returncode:
            logger.warning(
                f"Subprocess  : code : {prc.returncode}, stdout : {prc.stdout} = > stderr : {prc.stderr}"
            )
            # raise an error if not silent mode
            if not silent_mode:
                raise ValueError(f"Error in the conversion : {prc.stderr}")

        logger.info(f"Conversion successful : {prc.stdout}")

        if remove_src:
            logger.info(f"Removing the source file : {src}")
            os.remove(src)

        return dest

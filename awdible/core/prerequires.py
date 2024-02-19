"""
Pre-requirements module
"""

import subprocess

import requests

from awdible.logger import logger


class Prerequires:
    """Check the prerequires such as connection and ffmpeg availability"""

    @classmethod
    def has_connection(cls, silent_mode=False):
        """Check if the connection is available"""

        try:
            resp = requests.get("https://www.google.com")
            resp.raise_for_status()
            logger.info("Connection available")
            return True

        except Exception as e:
            logger.error(f"Error: {e}")
            logger.warning("Connection not available")
            if not silent_mode:
                raise e
            return False

    @classmethod
    def has_ffmpeg(cls, silent_mode=False):
        """Check if ffmpeg is installed"""

        try:
            cmd = "ffmpeg -version"
            prc = subprocess.run(cmd.split(" "), capture_output=True)

        except Exception as e:
            logger.error(f"Error: {e}")
            if not silent_mode:
                raise e
            return False

        if prc.returncode:
            logger.error(f"Error: {prc.stderr}")
            logger.error(
                f"Error: returncode : {prc.returncode}, stdout : {prc.stdout}, stderr : {prc.stderr}"
            )
            return False

        return True

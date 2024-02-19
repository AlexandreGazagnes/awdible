"""
Default values and constants.
"""

QUERY_PREFIX = "https://www.youtube.com/results?search_query="
VIDEO_PREFIX = "https://www.youtube.com/watch?v="

DEFAULT_VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
DEFAULT_VIDEO_ID = "9diaThxYnKA"

DEFAULT_DEST = "./"
DEFAULT_FILE = None
DEFAULT_OUTPUT = "mp3"
DEFAULT_CROP_LIMIT = 3600
DEFAULT_CONTEXT = "fr"

DEFAULT_SEARCH = False
DEFAULT_PREFIX = False
DEFAULT_ASYNCHRONOUS = False

DEFAULT_TMP = "./tmp/"
DEFAULT_LOG = "./log/"

DEFAULT_STREAMLIT = False
DEFAULT_PORT = 8501

DEFAULT_TEST_MODE = False

DEFAULT_CONFIG = {
    "X-RapidAPI-Key": "No API Key Found sush as 'X-RapidAPI-Key' found in the environment variables or in .env file",
    "X-RapidAPI-Host": "No API Host Found as 'X-RapidAPI-Host' found in the environment variables or in .env file",
}


DEFAULT_FORCE = False

"""
Default values and constants.
"""

# Urls
VIDEO_PREFIX = "https://www.youtube.com/watch?v="
QUERY_PREFIX = "https://www.youtube.com/results?search_query="

# Videos
DEFAULT_VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
DEFAULT_VIDEO_ID = "9diaThxYnKA"

# folders
DEFAULT_DEST = "./"
DEFAULT_TMP = "./tmp/"
DEFAULT_LOG = "./log/"
DEFAULT_FILE = None

# Audio output
DEFAULT_OUTPUT = "mp3"
OUTPUT_OPTIONS = ["mp3"]  # "wav", "ogg", "m4a", "flac", "opus"

# Crop
# TODO :Set as minutes ????
DEFAULT_CROP_LIMIT = 3600
CROP_LIMIT = [15 * 60, 3_600]

# TODO enable this as None and es
# TODO change as lang
DEFAULT_CONTEXT = "fr"
CONTEXT_OPTIONS = [
    "fr",
    "en",
    "es",
    None,
    "",
    "auto",
    "None",
    0,
    "0",
]


# Searc: perform an api search to find video ID
DEFAULT_SEARCH = False
DEFAULT_SEARCH_NUMBER = 1
MAX_SEARCH_NUMBER = 3

# DEFAULT_SEARCH_TOP_RESULTS = 1
# SEARCH_OPTIONS = [
#     True,
#     False,
#     "True",
#     "False",
#     "true",
#     "false",
#     0,
#     1,
#     "0",
#     "1",
# ]

# Force dowload even if ffmpeg is installed
DEFAULT_FORCE = False

# prefix
DEFAULT_PREFIX = False

# Asynchronous
DEFAULT_ASYNCHRONOUS = False

# Streamlit
DEFAULT_STREAMLIT = False
DEFAULT_PORT = 8501

# Test mode
DEFAULT_TEST_MODE = False

# API config
DEFAULT_CONFIG = {
    "X-RapidAPI-Key": "No API Key Found sush as 'X-RapidAPI-Key' found in the environment variables or in .env file",
    "X-RapidAPI-Host": "No API Host Found as 'X-RapidAPI-Host' found in the environment variables or in .env file",
}


DEFAULT_SLEEPER = 1.0
DEFAULT_SLEEPER_LONG = 3.0

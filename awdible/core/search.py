"""
Search for the video
"""

import requests
from bs4 import BeautifulSoup

from awdible.core.defaults import QUERY_PREFIX, VIDEO_PREFIX, DEFAULT_CONFIG
from awdible.logger import logger


class Search:
    """Search for the video"""

    QUERY_PREFIX = QUERY_PREFIX
    VIDEO_PREFIX = VIDEO_PREFIX
    DEFAULT_CONFIG = DEFAULT_CONFIG

    # @classmethod
    # def find(self, keywords: str) -> list[str]:
    #     """Find the video"""

    #     keywords = keywords.replace(" ", "+")

    #     url = self.QUERY_PREFIX + keywords

    #     response = requests.get(url)
    #     response.raise_for_status()

    #     return response.text

    # @classmethod
    # def parse(self, html: str) -> list[str]:
    #     """Parse the video"""

    #     soup = BeautifulSoup(html, "html.parser")
    #     a_list = soup.find_all("a", {"id": "video-title"})

    #     logger.info(a_list[:10])
    #     href_list = [a["href"] for a in a_list]

    #     return href_list

    @classmethod
    def find(
        self,
        keywords: str,
        context: str = "fr",
        config: dict = DEFAULT_CONFIG,
    ) -> list[str]:
        """Get the list of videos"""

        context = context.lower().strip()[:2]

        params = {"q": keywords}

        if context == "fr":
            params["hl"], params["gl"] = "fr", "FR"
        else:
            params["hl"], params["gl"] = "en", "US"

        url = "https://youtube-data8.p.rapidapi.com/search/"

        if config.get("X-RapidAPI-Key", None) is None:
            raise ValueError(
                f"No API Key found in the environment variables : {config.get('X-RapidAPI-Key', None)}"
            )

        if config.get("X-RapidAPI-Host", None) is None:
            raise ValueError(
                f"No API Host found in the environment variables : {config.get('X-RapidAPI-Host', None)}"
            )

        if config.get("X-RapidAPI-Host", None) != "youtube-data8.p.rapidapi.com":
            raise ValueError(
                f"No API Host found in the environment variables : {config.get('X-RapidAPI-Host', None)}"
            )

        response = requests.get(url, headers=config, params=params)

        return response.json()

    @classmethod
    def parse(self, json: str) -> list[str]:
        """Parse the video"""

        contents = json["contents"]

        contents = contents[:10]

        videos = [x.get("video", None) for x in contents]

        li = [(x["title"], x["videoId"]) for x in videos]

        logger.info(li)

        videos = [x["videoId"] for x in videos]

        return [self.VIDEO_PREFIX + x for x in videos]

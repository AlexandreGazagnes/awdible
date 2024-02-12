import os
import logging

import requests

from bs4 import BeautifulSoup

from audible.logger import logger
from audible.core.defaults import QUERY_PREFIX, VIDEO_PREFIX


from audible.config import config


class Search:
    """Search for the video"""

    QUERY_PREFIX = QUERY_PREFIX
    VIDEO_PREFIX = VIDEO_PREFIX

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
    def find(self, keywords: str, context: str = "fr") -> list[str]:
        """Get the list of videos"""

        context = context.lower().strip()[:2]

        querystring = {"q": keywords}

        if context == "fr":
            querystring["hl"] = "fr"
            querystring["gl"] = "FR"

        if context == "en":
            querystring["hl"] = "en"
            querystring["gl"] = "US"

        # import requests

        url = "https://youtube-data8.p.rapidapi.com/search/"

        headers = config

        response = requests.get(url, headers=headers, params=querystring)

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

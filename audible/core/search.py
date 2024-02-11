import os
import logging

import requests

from bs4 import BeautifulSoup

from audible.core.defaults import QUERY_PREFIX


class Search:
    """Search for the video"""

    QUERY_PREFIX = QUERY_PREFIX

    @classmethod
    def find(self, keywords: str) -> list[str]:
        """Find the video"""

        keywords = keywords.replace(" ", "+")

        url = self.QUERY_PREFIX + keywords

        response = requests.get(url)
        response.raise_for_status()

        return response.text

    @classmethod
    def parse(self, html: str) -> list[str]:
        """Parse the video"""

        soup = BeautifulSoup(html, "html.parser")
        a_list = soup.find_all("a", {"id": "video-title"})
        href_list = [a["href"] for a in a_list]

        return href_list

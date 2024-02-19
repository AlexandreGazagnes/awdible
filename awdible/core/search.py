"""
Search for the video
"""

import requests
from bs4 import BeautifulSoup

from awdible.core.defaults import QUERY_PREFIX, VIDEO_PREFIX
from awdible.logger import logger

from awdible.logger import logger


class Search:
    """Search for the video"""

    QUERY_PREFIX = QUERY_PREFIX
    VIDEO_PREFIX = VIDEO_PREFIX

    @classmethod
    def _find(
        cls,
        keywords: str,
        config: dict,
        context: str = None,
        lang: str = "NotImplemented",
        silent_mode: bool = False,
    ) -> list[str]:
        """Get the list of videos"""

        # params
        params = {"q": keywords}
        # NOTE : is it a good thing to udpate keywords ???
        logger.info(f"searching for  params {params}")

        # context as lang for now, netx will be different
        context = context.lower().strip()[:2]
        if "fr" in context:
            params["hl"], params["gl"] = "fr", "FR"
        elif "en" in context:
            params["hl"], params["gl"] = "en", "US"
        elif "us" in context:
            params["hl"], params["gl"] = "en", "US"
        elif "uk" in context:
            params["hl"], params["gl"] = "en", "GB"
        elif "es" in context:
            params["hl"], params["gl"] = "es", "ES"
        else:
            pass

        # log params
        logger.info(f"searching for  params {params}")

        if not config:
            config = {}
        # manage keys if needed
        if config.get("X-RapidAPI-Key", None) is None:
            if not silent_mode:
                raise ValueError(
                    f"No API Key found in the environment variables : {config.get('X-RapidAPI-Key', None)}"
                )

        if config.get("X-RapidAPI-Host", None) is None:
            if not silent_mode:
                raise ValueError(
                    f"No API Host found in the environment variables : {config.get('X-RapidAPI-Host', None)}"
                )

        if config.get("X-RapidAPI-Host", None) != "youtube-data8.p.rapidapi.com":
            if not silent_mode:
                raise ValueError(
                    f"No API Host found in the environment variables : {config.get('X-RapidAPI-Host', None)}"
                )

        url = "https://youtube-data8.p.rapidapi.com/search/"
        response = requests.get(url, headers=config, params=params)

        # raise for status
        # TODO : manage side effect
        if not silent_mode:
            response.raise_for_status()  # raise an error if the request fails

        json = response.json()

        return json

    @classmethod
    def _parse(
        cls,
        json: str,
        n_results=5,
        silent_mode=False,
    ) -> list[str]:
        """Parse the video"""

        contents = json["contents"]

        contents = contents[:n_results]

        # if contents are not found
        if not len(contents):
            logger.error(f"No video found in parsing the json : contents = {contents}")
            logger.error(json)
            if not silent_mode:
                raise ValueError(
                    f"No video found in parsing the json : contents = {contents}"
                )

        logger.info(contents)

        # extract video
        try:
            videos = [x.get("video", None) for x in contents]
        except AttributeError as e:
            logger.error(f"Error in parsing the json with get('video') : {e}")
            # logger.error(f"contents is : {contents}")
            if not silent_mode:
                raise e

        # extract video id and title
        try:
            li = [(x["title"], x["videoId"]) for x in videos]
            logger.info(li)

        except Exception as e:
            logger.error(f"Error in parsing the json with 'title' and 'ID') : {e}")
            # logger.error(f"contents is : {contents}")
            if not silent_mode:
                raise e

        # filter id
        # get video id
        videos = [x["videoId"] for x in videos]

        # make final url
        VIDEO_PREFIX = (
            cls.VIDEO_PREFIX
            if cls.VIDEO_PREFIX.endswith("/")
            else cls.VIDEO_PREFIX + "/"
        )
        videos = [VIDEO_PREFIX + x for x in videos]

        return videos

    @classmethod
    def find_parse(
        cls,
        keywords: str,
        config: dict,
        context: str = None,
        n_results=5,
        lang: str = "NotImplemented",
        silent_mode=False,
    ):
        """Find and parse the video"""

        json = cls._find(
            keywords=keywords,
            config=config,
            context=context,
            lang=lang,
            silent_mode=silent_mode,
        )
        videos = cls._parse(
            json,
            n_results=n_results,
            silent_mode=silent_mode,
        )

        return videos

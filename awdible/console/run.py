"""
Run command
"""

import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

from awdible.core.awdible import Awdible
from awdible.logger import logger


class RunCommand(Command):
    """Run Awdible session"""

    name = "run"

    description = "Run Awdible session"

    arguments = [
        argument(
            "video",
            description="The video url to download from youtube. \nIf you want to input a search query, use the --search option",
            optional=True,
            default=Awdible.DEFAULT_VIDEO_URL,
        )
    ]
    options = [
        option(
            "dest",
            "d",
            description="The destination directory of the file",
            flag=False,
            default=Awdible.DEFAULT_DEST,
        ),
        option(
            "file",
            "f",
            description="The input file With list of urls/videos",
            flag=False,
        ),
        option(
            "output",
            "o",
            description="The output file name",
            flag=False,
            default=Awdible.DEFAULT_OUTPUT,
        ),
        option(
            "crop_limit",
            "l",
            description="The limit of duration of the video to download. If the video is longer than the limit, it will be cropped into smaller parts.",
            flag=False,
            default=Awdible.DEFAULT_CROP_LIMIT,
        ),
        option(
            "context",
            "c",
            description="The context of the search query. Can be 'fr' or 'en'",
            flag=False,
            default=Awdible.DEFAULT_CONTEXT,
        ),
        option(
            "search",
            "s",
            description="If set, the video argument will be treated as a search query and the first result will be downloaded.",
            flag=True,
        ),
        option(
            "prefix",
            "p",
            description=f"If set, can ommit the url prefix '{Awdible.VIDEO_PREFIX}' when passing the video url.",
            flag=True,
        ),
        option(
            "asynchronous",
            "a",
            description="If set, the download will be asynchronous.",
            # This means that the download will be done in the background and the command will return immediately. The download progress can be checked using the `awdible progress` command.
            flag=True,
        ),
    ]

    def handle(self):
        """handle the command"""

        # arguments
        video = self.argument("video")

        # no flags options
        dest = self.option("dest")
        file = self.option("file")
        output = self.option("output")
        crop_limit = self.option("crop_limit")
        context = self.option("context")

        # flags options
        search = self.option("search")
        asynchronous = self.option("asynchronous")
        prefix = self.option("prefix")

        # useless logging
        logger.debug(f"video: {video}")

        logger.debug(f"dest: {dest}")
        logger.debug(f"file: {file}")
        logger.debug(f"output: {output}")
        logger.debug(f"crop_limit: {crop_limit}")
        logger.debug(f"context: {context}")

        logger.debug(f"search: {search}")
        logger.debug(f"prefix: {prefix}")
        logger.debug(f"asynchronous: {asynchronous}")

        # check context
        if context not in ["fr", "en"]:
            raise Exception("Invalid context. Should be 'fr' or 'en'")

        # check if the dest is a valid directory
        if dest:
            if not os.path.isdir(dest):
                raise Exception("Invalid directory path")

        # check if the file is a valid file
        if file:
            if not os.path.isfile(file):
                raise Exception("Invalid file path")

        # check if the output is a valid file format
        if output not in ["mp3", "mp4"]:
            raise Exception("Invalid output file format : Only supports mp3 and mp4")

        # check if the crop limit is a valid number
        try:
            crop_limit = int(crop_limit)
        except ValueError:
            raise Exception("Invalid crop limit. Should be a number")
        if crop_limit < 0 or crop_limit > 3600 * 10:
            raise Exception(
                "Invalid crop limit. Should be between 0 and 36 000 seconds (10 hours)"
            )

        # check incompatible options video args and file otions are not passed together
        # unless default video is passed
        if (video and file) and (video != Awdible.DEFAULT_VIDEO_URL):
            raise AttributeError(
                "You can only pass either a video url or a file with list of urls"
            )

        # if file: make a liste of videos
        if file:
            with open(file, "r") as f:
                video_list = f.readlines()

        else:
            video_list = video.split(",")

        # strip items in the list
        video_list = [v.strip() for v in video_list]
        video_list = [v for v in video_list if v]
        video_list = [v for v in video_list if not v.startswith("#")]

        # # if prefix is set, add the prefix to the video list
        # if prefix:
        #     video_list = [Awdible.VIDEO_PREFIX + v for v in video_list]

        # # check video list
        # for v in video_list:
        #     if not v.startswith(Awdible.VIDEO_PREFIX):
        #         raise AttributeError(
        #             f"Invalid youtube video url. Should be in the format '{Awdible.VIDEO_PREFIX}', recieved : '{v}'\n Consier using the --search option to search for the video url or add the --prefix option to add the prefix to the video url."
        #         )

        self.line("Eh! I'm running the command")
        Awdible(
            video=video_list,
            dest=dest,
            file=file,
            output=output,
            context=context,
            prefix=prefix,
            search=search,
            asynchronous=asynchronous,
            crop_limit=crop_limit,
            streamlit=False,
        ).run()

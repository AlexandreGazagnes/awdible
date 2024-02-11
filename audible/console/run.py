import os

from cleo.commands.command import Command
from cleo.helpers import argument, option


class RunCommand(Command):
    # """
    # Run Audible session

    # run
    #     {video?="https://www.youtube.com/watch?v=9diaThxYnKA" : The video url to download from youtube. If you want to input a search query, use the --search option}
    #     {--d|dest="./" : The destination directory of the file}
    #     {--f|file="" : The input file With list of urls/videos}
    #     {--o|output="mp3" : The output file name}
    #     {--s|search : If set, you can pass a search query to download the video from youtube}
    # """

    name = "run"
    description = "Run Audible session"
    arguments = [
        argument(
            "video",
            description="The video url to download from youtube. If you want to input a search query, use the --search option",
            optional=True,
            default="https://www.youtube.com/watch?v=9diaThxYnKA",
        )
    ]
    options = [
        option(
            "dest",
            "d",
            description="The destination directory of the file",
            flag=False,
            default="./",
        ),
        option(
            "file",
            "f",
            description="The input file With list of urls/videos",
            flag=False,
            default="",
        ),
        option(
            "output",
            "o",
            description="The output file name",
            flag=False,
            default="mp4",
        ),
        option(
            "search",
            "y",
            description="If set, the task will yell in uppercase letters",
            flag=True,
        ),
    ]

    def handle(self):
        """handle the command"""

        dest = self.option("dest")
        file = self.option("file")
        output = self.option("output")
        search = self.option("search")
        video = self.argument("video")

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
            raise Exception(
                "Invalid output file format : Only supports mp3 and mp4"
            )

        # check incompatible options video args and file otions are not passed together
        # unless default video is passed
        if (
            video and file
        ) and video != "https://www.youtube.com/watch?v=9diaThxYnKA":
            raise Exception(
                "You can only pass either a video url or a file with list of urls"
            )

        # validate video url
        if not "https://www.youtube.com/watch?v=" in video:
            raise Exception(
                "Invalid youtube video url. Should be in the format 'https://www.youtube.com/watch?v=...'\n...or consier using the --search option to search for the video"
            )

        # if file: make a liste of videos
        if file:
            with open(file, "r") as f:
                video_list = f.readlines()

        else:
            video_list = video.split(",")

        # strip items in the list
        video_list = [v.strip() for v in video_list]

        # check video list
        for v in video_list:
            if not "https://www.youtube.com/watch?v=" in v:
                raise Exception(
                    "Invalid youtube video url. Should be in the format 'https://www.youtube.com/watch?v=...' \n...or consier using the --search option to search for the video"
                )

        self.line("Eh! I'm running the command")

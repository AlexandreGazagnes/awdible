"""
IO module
"""

import os
from awdible.logger import logger


class Io:
    """Class for input/output operations"""

    @classmethod
    def build_folders(
        cls,
        folders: list,
        create=True,
        silent_mode=True,
    ) -> list:
        """Build the folders"""

        folders = [folders] if isinstance(folders, str) else folders

        # check if the folders are available
        for folder in folders:
            if not os.path.isdir(folder):
                logger.error(f"File not found : {folder}")
                if not silent_mode:
                    raise FileNotFoundError(f"File not found : {folder}")

                if create:
                    os.makedirs(folder)
                    logger.warning(f"Folder created : {folder}")

    @classmethod
    def build_files(
        cls,
        files: list,
        create=False,
        silent_mode=True,
    ) -> list:
        """Build the files"""

        files = [files] if isinstance(files, str) else files

        # check if the files are available
        for file in files:
            if not os.path.isfile(file):
                logger.error(f"File not found : {file}")
                if not silent_mode:
                    raise FileNotFoundError(f"File not found : {file}")

                if create:
                    with open(file, "w") as f:
                        f.write("")
                    logger.warning(f"File created : {file}")

    @classmethod
    def clean_list_videos(
        cls,
        fn,
        rewrite=True,
        create=False,
        sort=True,
        silent_mode=False,
    ):
        """Clean the list of videos"""

        # build the file if needed
        cls.build_files(
            fn,
            create=create,  # sould be false
            silent_mode=silent_mode,  # sould be true
        )

        # load the file
        with open(fn, "r") as f:
            lines = f.readlines()

        # clean the file
        lines = [line for line in lines if line]
        lines = [line.strip() for line in lines if line]
        lines = list(set(lines))

        # sort the file if needed
        lines = sorted(lines) if sort else lines

        # sep of hastag and not hastag
        not_hastag = [line for line in lines if not line.startswith("#")]
        hastag = [line for line in lines if not line.startswith("#")]

        # final
        final = not_hastag + hastag
        # final = [i for i in final if i.strip()]
        # final = list(set(final))
        final = [f"{line}\n" for line in final]

        # rewrite the file
        if rewrite:
            with open(fn, "w") as f:
                f.writelines(final)

        return hastag

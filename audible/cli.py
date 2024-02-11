import subprocess
import sys
import os
import logging
from audible.get import Get


def main():
    """Main function for the CLI"""

    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    args = sys.argv[1:]

    if not args:
        raise SystemExit(f"Usage: {sys.argv[0]} <url>")

    if args[0] == "-f":
        fn = args[1]
        with open(fn, "r") as f:
            urls = f.readlines()
        urls = [url.strip() for url in urls]
    else:
        urls = args

    for url in urls:
        title, video = Get.audio(url)
        logging.info(f"Filename is : {title}")
        fn = Get.save(title, video)


if __name__ == "__main__":
    main()

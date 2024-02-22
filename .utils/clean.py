"""
just take a file with a list of url and sort it, removing duplicates and cleaning the strings.
"""

import os
import sys

# import string


def _clean(txt: str, capitalize: bool = True) -> str:
    txt = txt.split("&")[0]

    return txt


def main():
    """ """

    # manage argv errors
    if len(sys.argv) < 2:
        raise AttributeError(
            f"You must provide the filename. len sys argv : {len(sys.argv)}"
        )

    # get fn
    cwd = os.getcwd()
    fn = sys.argv[1]
    fn = os.path.join(cwd, fn)

    # manage not fn
    if not os.path.isfile(fn):
        raise AttributeError(f"File : {fn} not found!")

    # read file
    with open(fn, "r") as f:
        lines = f.readlines()

    # basic ops
    lines = [i for i in lines]
    lines = list(set(lines))
    lines = sorted(lines)

    # clean
    lines = [_clean(i) for i in lines]

    # last
    lines = [i.strip() for i in lines if i.strip() != ""]
    lines = [i + "\n" for i in lines]

    # load
    with open(fn, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()

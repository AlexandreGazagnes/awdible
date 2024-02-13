"""
Helper functions for the awdible package.
"""

import string


def asciize(txt: str) -> str:
    """Convert a string to ascii"""

    punct = list(string.punctuation)

    keep = "()[].-_"
    punct = [p for p in punct if p not in keep]

    for p in punct:
        txt = txt.replace(p, "")

    replace_dict = {
        "é": "e",
        "è": "e",
        "ê": "e",
        "à": "a",
        "â": "a",
        "î": "i",
        "ï": "i",
        "ô": "o",
        "ù": "u",
        "û": "u",
        "ç": "c",
        "œ": "oe",
        "æ": "ae",
        "'": "",
        "`": "",
    }

    for k, v in replace_dict.items():
        txt = txt.replace(k, v)

    for k, v in replace_dict.items():
        txt = txt.replace(k.upper(), v.upper())

    keep2 = "()[]-_"
    for k in keep2:
        txt = txt.replace(k, "_")

    txt = (
        txt.replace("__", "_")
        .replace("__", "_")
        .replace("__", "_")
        .replace("__", "_")
        .replace("__", "_")
    )

    txt = txt.strip()

    return txt

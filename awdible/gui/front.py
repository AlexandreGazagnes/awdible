"""
Streamlit front-end for the Awdible app.
"""

import streamlit as st

from awdible.core.awdible import Awdible
from awdible.helpers import asciize

DEFAULT_VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
DEFAULT_VIDEO_ID = "V62oKsHdsLU"
DEFAULT_VIDEO_QUERY = "jo l'rigolo"


def user_out(out, dest="./tmp/"):
    """User output"""

    out = out.replace(dest, "")
    out = asciize(out)
    out = out.removeprefix(".")

    return out


# header image
img = "./docs/assets/img/image.png"
st.image(img)  # caption="Thanks to DALL-E for the image ;) "


# title
st.title("Awdible - Just the best free version of audible")
st.write(
    """
Just paste the url of the video you want to download and click the button.
"""
)

# Text input
pos_url = DEFAULT_VIDEO_URL
url = st.text_input("Youtube url", pos_url)


# Button
if st.button("Submit"):
    # init the Awdible class
    awdible = Awdible(video=url, test_mode=True, streamlit=True)

    awdible.dest

    # do run
    outs = awdible.run()
    out = outs[0] if isinstance(outs, list) else outs

    # deliver the file
    with open(out, "rb") as f:
        st.download_button(
            "Download", f, file_name=user_out(out, awdible.dest)
        )  # mime="audio/mp4"

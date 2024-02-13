"""
Streamlit front-end for the Awdible app.
"""

import streamlit as st

from awdible.core.awdible import Awdible


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
pos_url = "https://youtube.com/shorts/fcCpXScFxfM?si=xVSQZWa7MgsWOl9E"
url = st.text_input("Youtube url", pos_url)


# Button
if st.button("Submit"):

    # init the Awdible class
    awdible = Awdible(video=url, test_mode=True, streamlit=True)

    # do run
    outs = awdible.run()
    out = outs[0] if isinstance(outs, list) else outs

    # deliver the file
    with open(out, "rb") as f:
        st.download_button("Download", f, file_name=out)  # mime="audio/mp4"

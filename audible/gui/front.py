import streamlit as st

from audible.core.audible import Audible


# header image
img = "./docs/assets/img/image.png"
st.image(img)  # caption="Thanks to DALL-E for the image ;) "


# title
st.title("The Best Free Audible App Ever Made")
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
    audible = Audible(video=url, test_mode=False, streamlit=True)
    out = audible.run()
    with open(out, "rb") as f:
        st.download_button("Download", f, file_name=out)  # mime="audio/mp4"

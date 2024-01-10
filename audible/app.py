import subprocess
import sys
import streamlit as st

from audible.get import Get


img = "./assets/img/image.png"

st.image(img, caption="image header")

st.write(
    """
# Free Audible App
Hello *user!*
"""
)


# pos_url = "https://www.youtube.com/watch?v=EesQolfp9gQ,EesQolfp9gQ"

pos_url = "https://youtube.com/shorts/fcCpXScFxfM?si=xVSQZWa7MgsWOl9E"
url = st.text_input("Youtube url", pos_url)
st.write("video url is", url)


if st.button("Go"):
    title, video = Get.audio(url)
    st.write(title)

    fn = Get.save(title, video)

    # list_files = subprocess.run(["ls", "-l"])
    # assert isinstance(list_files, subprocess.CompletedProcess)
    # print("The exit code was: %d" % list_files.returncode)

    with open(fn, "rb") as f:
        st.download_button("Download", f, file_name=fn)  # mime="audio/mp4"


# df = pd.read_csv("my_data.csv")
# st.line_chart(df)

import subprocess
import sys
import streamlit as st

# from audible.get import Get


# # header image
# img = "./assets/img/image.png"
# st.image(img)  # caption="Thanks to DALL-E for the image ;) "


# # title
# st.title("The Best Free Audible App Ever Made")
# st.write(
#     """
# Just paste the url of the video you want to download and click the button.
# """
# )

# # Text input
# pos_url = "https://youtube.com/shorts/fcCpXScFxfM?si=xVSQZWa7MgsWOl9E"
# url = st.text_input("Youtube url", pos_url)


# # Button
# if st.button("Submit"):
#     title, video = Get.audio(url)
#     st.write(f"Filename is : {title}")
#     fn = Get.save(title, video)
#     with open(fn, "rb") as f:
#         st.download_button("Download", f, file_name=fn)  # mime="audio/mp4"


st.write("Hello world")

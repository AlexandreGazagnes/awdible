import streamlit as st

# import pandas as pd

img = "./assets/img/image.png"

st.image(img, caption="image header")

st.write(
    """
# Free Audible App
Hello *user!*
"""
)


pos_url = "https://www.youtube.com/watch?v=EesQolfp9gQ,EesQolfp9gQ"

url = st.text_input("Youtube url", pos_url)
st.write("video url is", url)


# df = pd.read_csv("my_data.csv")
# st.line_chart(df)

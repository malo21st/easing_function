import streamlit as st
import pandas as pd

df = pd.read_json("easing.json")

st.dataframe(df)

num = 40
st.image(f"./gif/{df.iloc[num, 1]}", format = 'GIF')
st.code(f"{df.iloc[num, 2]}", language="python")
st.image(, format = 'GIF')

"""### gif from local file"""
with open("./gif/easing_light.gif", "rb") as file_ :
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

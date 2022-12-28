import streamlit as st
import pandas as pd

df = pd.read_json("easing.json")

st.dataframe(df)

num = 40
st.image(f"./gif/{df.iloc[num, 1]}")
st.code(f"{df.iloc[num, 2]}", language="python")
st.image("./gif/easing_light.gif")

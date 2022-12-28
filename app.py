import streamlit as st
import pandas as pd

df = pd.read_json("easing.json")

st.dataframe(df)

st.image(f"./gif/{df.iloc[0, 1]}")
st.code(f"./gif/{df.iloc[0, 2]}")

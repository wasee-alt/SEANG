import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="S.E.A.N.G • ProPlugin", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    page = f.read()

# Render full HTML app
html(page, height=1100, scrolling=True)

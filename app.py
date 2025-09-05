import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="S.E.A.N.G • ProPlugin", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    page = f.read()

# ฝัง HTML ลงใน Streamlit
html(page, height=1000, scrolling=True)

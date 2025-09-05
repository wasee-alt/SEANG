import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="S.E.A.N.G • ProPlugin", layout="wide")

# อ่านไฟล์ HTML เต็มหน้า (ที่อยู่ข้างๆ app.py)
with open("index.html", "r", encoding="utf-8") as f:
    page = f.read()

# ✅ ต้องใช้ components.html (ห้ามใช้ st.markdown/st.write กับ HTML เต็มหน้า)
html(page, height=1100, scrolling=True)

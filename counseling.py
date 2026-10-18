import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="수학 & 진로 상담실",
    layout="wide"
)

# index.html 파일을 읽어서 스트리밋에 렌더링
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)

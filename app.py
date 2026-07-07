import pathlib

import streamlit as st
import streamlit.components.v1 as components

# ── 기본 페이지 설정 ─────────────────────────────────────────
st.set_page_config(
    page_title="다듬체 · 보내기 전, 한 번 더 다듬다",
    page_icon="✂️",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최대한 숨겨서 index.html이 화면 전체를 쓰도록 함
st.markdown(
    """
    <style>
        #MainMenu {display: none;}
        header {display: none;}
        footer {display: none;}
        div.block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        [data-testid="stAppViewContainer"] {padding-top: 0 !important;}
        iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── index.html 로드 ─────────────────────────────────────────
HTML_PATH = pathlib.Path(__file__).parent / "index.html"
html_code = HTML_PATH.read_text(encoding="utf-8")

# index.html은 완전히 독립적인 HTML/CSS/JS(순수 프론트엔드)로 작성되어 있으므로
# Streamlit 컴포넌트(iframe) 안에 그대로 렌더링합니다.
components.html(html_code, height=1100, scrolling=False)

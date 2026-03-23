import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Happy Birthday Monika 🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI completely
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Load HTML
with open("monika_birthday.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render full-screen experience
components.html(
    html_code,
    height=1000,   # enough for full viewport
    scrolling=False
)

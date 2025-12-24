import streamlit as st
from Helper import *

st.set_page_config(
    page_title="הפרויקטים של נהוראי",
    page_icon="👑",
    layout="wide"
)

setRTL()

st.title("בוט שיעורי בית")

API_KEY = getAPIkey()

Message("AI","היי איך אפשר לעזור")

userinput = st.chat_input("השאלה שלך ...")

if userinput:
    Message("User",userinput)
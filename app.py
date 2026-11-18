import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice" , layout = 'centered')
st.title('Afra Farseen')
st.caption('AI Placement Assistant')
st.caption('Practice and prepare for the interview')
try:
  client = Groq(api_key = "GROQ_API_KEY")
except (Keyerror,FileNotFound):
  st.error("API key is missing.Add it in Advanced settings")
  st.stop()

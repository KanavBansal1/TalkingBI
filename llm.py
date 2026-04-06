import os
import streamlit as st
from langchain_groq import ChatGroq

api_key = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)
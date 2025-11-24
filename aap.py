import os
import streamlit as st
from langchain_openai import OpenAI
from constants import openai_key
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Enter your text here")

# Create LLM object
llm = OpenAI(temperature=0.8)

if input_text:
    output = llm.invoke(input_text)
    st.write(output)

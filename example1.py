import os
import streamlit as st
from dotenv import load_dotenv
from constants import openai_key

# Updated imports (LangChain v0.2+)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence

# Load API key
load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title("Celebrity Search Result")
input_text = st.text_input("Enter celebrity name")

# --- Prompt ---
prompt = ChatPromptTemplate.from_template(
    "Tell me about the celebrity {name}."
)

# --- LLM ---
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8
)

# --- Chain using RunnableSequence ---
chain = RunnableSequence(
    prompt,
    llm,
    StrOutputParser()
)

# Show result
if input_text:
    result = chain.invoke({"name": input_text})
    st.write(result)

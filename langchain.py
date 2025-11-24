import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from constants import openai_key
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title("Language Translator")


language = st.text_input("Enter the language you want to translate to:", "Malayalam")
text_to_translate = st.text_area("Enter text to translate:", "Hi nice to meet you")

if st.button("Translate"):
#Creating llm
    llm = ChatOpenAI()

    system_template = "Translate the follong form English to {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system",system_template),"user","{text}"]
    )

    prompt = prompt_template.invoke({"language":language ,"text":text_to_translate})

    response=llm.invoke(prompt)
    print(response.content)
    st.subheader("Translated Text:")
    st.write(response.content)

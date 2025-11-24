import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from constants import openai_key
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

#Creating llm
llm = ChatOpenAI()
#response = llm.invoke("Suggest me a title of movie in malayalam to watch ")
#print(response.content)

messages=[
    SystemMessage("Translate the following from English to hindi"),
    HumanMessage("Hi nice to meet you")
]
response=llm.invoke(messages)
print(response.content)

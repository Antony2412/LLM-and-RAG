import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from constants import openai_key
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

#Creating llm
llm = ChatOpenAI()
#response = llm.invoke("Suggest me a title of movie in malayalam to watch ")
#print(response.content)

#messages=[
#    SystemMessage("Translate the following from English to hindi"),
#    HumanMessage("Hi nice to meet you")
#]

system_template = "Translate the follong form English to {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system",system_template),"user","{text}"]
)

prompt = prompt_template.invoke({"language":"Malayalam", "text":"Hi nice to meet you"})

response=llm.invoke(prompt)
print(response.content)

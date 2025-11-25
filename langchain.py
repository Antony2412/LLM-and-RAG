import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from constants import openai_key
from dotenv import load_dotenv


load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title("Joke Generator")


topic = st.text_input("Enter a topic to generate a joke about:", "Cats")

if st.button("Tell me a joke"):
#Creating llm
    llm = ChatOpenAI()

    prompt_template2 = PromptTemplate.from_template("Tell me a joke about {topic}")
    prompt2 = prompt_template2.invoke({"topic",topic})

    response=llm.invoke(prompt2)
    print(response.content)
    st.subheader("Here's your joke:")
    st.write(response.content)

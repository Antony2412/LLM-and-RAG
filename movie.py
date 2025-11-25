import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from constants import openai_key
from dotenv import load_dotenv


load_dotenv()
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title("Movie summary generator")


topic = st.text_input("Enter the genre ", "Comedy")
language = st.text_input("Enter the movie language ", "Malayalam")

if st.button("Generate summary"):
#Creating llm
    llm = ChatOpenAI()

#Creaing movie title chain 
    movie_title_template= PromptTemplate.from_template("Suggest me a movie to watch in language {language} and of genre{topic}")
    movie_titile_chain = movie_title_template | llm | StrOutputParser()

#Summary Chain
    movie_summary_Prompt = PromptTemplate.from_template(
        "Give me 2-3 lines summary of the movie{movie_title}")
    
    composed_chain = {"movie_title":movie_titile_chain} | movie_summary_Prompt| llm | StrOutputParser()
    response = composed_chain.invoke({"language":language,"topic":topic})    

    print(movie_titile_chain)
    st.subheader("Here's your summary :")
    st.write(response)

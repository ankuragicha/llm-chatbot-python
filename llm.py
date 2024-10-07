import streamlit as st

# Create the LLM
#from langchain_groq import ChatGroq
#llm = ChatGroq(model=st.secrets["GROQ_MODEL"],groq_api_key=st.secrets["GROQ_API_KEY"])
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)
# Create the Embedding model

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)

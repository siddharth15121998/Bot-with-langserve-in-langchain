import requests
import streamlit as st

def get_codellama_response(input_text1):
    response=requests.post("http://localhost:8000/codellama/invoke",
    json={'input':{'question':input_text1}})

    return response.json()['output']

def get_ollama_response(input_text2):
    response=requests.post(
    "http://localhost:8000/llama2/invoke",
    json={'input':{'question':input_text2}})

    return response.json()['output']

    ## streamlit framework

st.title('Langserve in Langchain')
input_text1=st.text_input("Generate basic python code of your choice with codellama.")
input_text2=st.text_input("Ask Anything to llama2 model.")

if input_text1:
    st.write(get_codellama_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))

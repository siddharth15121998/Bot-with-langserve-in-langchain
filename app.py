from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app=FastAPI(
    title="Langchain Server POC",
    version="1.0",
    decsription="A POC API Server"
)

llm1=Ollama(model="codellama")
llm2=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
prompt2=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

add_routes(
    app,
    prompt1|llm1,
    path="/codellama"
)

add_routes(
    app,
    prompt2|llm2,
    path="/llama2"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

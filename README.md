# Bot-with-langserve-in-langchain

* **Note**: To cover wider audience we are using opensource model. We can use any model either paid or opensource.


* **Prerequisites**:

1. Python3 should be installed in your system.
2. Create virtual environment and activate it. Steps can be found on internet according to your Operating system.
3. Developer should have OPENAI(https://openai.com) API KEY.
4. Download and install Ollama(https://ollama.com) locally to run open source LLM models. Models supported by Ollama can be found at https://github.com/ollama/ollama 

* **Steps to be followed**:
1. Download the packages --> pip install langchain langchain-openai streamlit langchain_community uvicorn sse_starlette langserve fastapi python-dotenv
2. Create "app.py" and "main.py" files and use the code provided.
3. In your terminal/command prompt run command "ollama run llama2". This will pull the files of the llama2 model from Ollama and run that model locally on your system. Don't quit the terminal
4. In other terminal run command "ollama run codellama". Don't quit the terminal
5. Run the command in one of the terminal: python app.py
6. Run the command in other terminal: streamlit run main.py

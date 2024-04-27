# Bot-with-langserve-in-langchain


Prerequisites:

1. Python3 should be installed in your system.
2. Create virtual environment and activate it. Steps can be found on internet according to your Operating system.
3. Developer should have OPENAI(https://openai.com) API KEY.
4. Download and install Ollama(https://ollama.com) locally to run open source LLM models. Models supported by Ollama can be found at https://github.com/ollama/ollama 

Steps to be followed:
1. Download the packages --> pip install langchain langchain-openai streamlit langchain_community uvicorn sse_starlette langserve fastapi --> python -m pip install python-dotenv
2. Create ".env" file with below variables and their correct values. --> OPENAI_API_KEY="your key"
3. Create "app.py" and "main.py" files and use the code provided.
4. In your terminal/command prompt run command "ollama run llama3". This will pull the files of the llama3 model from Ollama and run that model locally on your system.
5. Run the command in terminal: streamlit run main.py

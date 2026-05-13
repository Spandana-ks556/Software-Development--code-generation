from langchain_groq import ChatGroq

def get_llm():
    return {
        "llm_type": "litellm",
        "model": "groq/llama-3.1-8b-instant",
        #"model": "groq/llama-3.1-8b-instant", 
        "api_key": "",
        "temperature": 0.4,
        "max_tokens": 200
    }



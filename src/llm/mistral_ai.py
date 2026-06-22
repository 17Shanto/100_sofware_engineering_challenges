import os
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()
api_key: str | None = os.getenv("MISTRAL_API_KEY")

class MistralLLM:
    def __init__(self):
        self.mistral_llm = ChatMistralAI(
            model_name= "mistral-large-latest",
            api_key=api_key, #type: ignore
            temperature=0.2
        )
import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
LLM_API_VERSION = os.getenv("LLM_API_VERSION")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
MODEL = os.getenv("MODEL")
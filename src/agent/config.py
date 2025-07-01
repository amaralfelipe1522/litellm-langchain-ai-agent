import os
from dotenv import load_dotenv

load_dotenv()

# Azure Credentials
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
LLM_API_VERSION = os.getenv("LLM_API_VERSION")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
MODEL = os.getenv("MODEL")

# AWS Credentials for Bedrock
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
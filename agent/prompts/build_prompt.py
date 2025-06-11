from langchain.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate.from_template("Responda de forma breve: {input}")

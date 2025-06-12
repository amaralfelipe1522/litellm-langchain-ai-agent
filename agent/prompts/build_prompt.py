# from langchain.prompts import PromptTemplate

# def get_prompt():
#     return PromptTemplate.from_template("Responda de forma breve: {input}")

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_prompt():
    # promptTemplate = """Com base no seguinte contexto, caso houver: {context} e responda a pergunta: {input}; Historico: {history}"""
    promptTemplate = """Responda de forma breve: {input} - Historico: {history}"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", promptTemplate),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])

    return prompt
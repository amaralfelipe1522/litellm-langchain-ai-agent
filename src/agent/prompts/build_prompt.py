from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_prompt():
    promptTemplate = """Responda de forma breve: {input} - Historico: {history}"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", promptTemplate),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])

    return prompt
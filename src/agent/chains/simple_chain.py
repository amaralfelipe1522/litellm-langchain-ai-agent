from src.agent.prompts.build_prompt import get_prompt
from src.agent.llm.lite_llm_provider import get_llm
from langchain_core.runnables import RunnableLambda

def build_chain():
    prompt = get_prompt()
    print(prompt)
    llm = get_llm()

    def run_chain(input_data):
        formatted_prompt = prompt.format(input=input_data["input"], history=input_data.get("history", ""))
        return llm(formatted_prompt)

    return RunnableLambda(run_chain)
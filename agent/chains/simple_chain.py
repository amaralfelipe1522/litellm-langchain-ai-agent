from agent.prompts.build_prompt import get_prompt
from agent.llm.lite_llm_provider import get_llm

def build_chain():
    prompt = get_prompt()
    print(prompt)
    llm = get_llm()

    def run_chain(input_data):
        formatted_prompt = prompt.format(input=input_data["input"])
        return llm(formatted_prompt)

    return run_chain
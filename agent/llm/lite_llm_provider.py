import litellm
# litellm._turn_on_debug()
from agent.config import LLM_API_KEY, LLM_ENDPOINT, LLM_API_VERSION, LLM_PROVIDER, MODEL

def get_llm():
    def call_llm(prompt):
        response = litellm.completion(
            model=f"{LLM_PROVIDER}/{MODEL}",
            messages=[{"role": "user", "content": prompt}],
            custom_llm_provider=LLM_PROVIDER,
            api_key=LLM_API_KEY,
            api_base=LLM_ENDPOINT,
            api_version=LLM_API_VERSION
        )
        return response["choices"][0]["message"]["content"]
    return call_llm
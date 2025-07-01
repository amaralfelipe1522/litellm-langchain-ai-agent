import litellm
from src.agent.config import LLM_API_KEY, LLM_ENDPOINT, LLM_API_VERSION, LLM_PROVIDER, MODEL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION
# litellm._turn_on_debug()

def get_llm_azure():
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

def get_llm_bedrock():
    def call_llm(prompt):
        model = "bedrock/amazon.titan-text-lite-v1"

        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
            top_p=0.9,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_region_name=AWS_DEFAULT_REGION
        )

        # Exibe a resposta
        return response["choices"][0]["message"]["content"]
    return call_llm
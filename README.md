# litellm-langchain-ai-agent
Repositório criado para armazenar um caso de estudo de agente de IA em Python utilizando tecnologias como LiteLLM, LangChain e OpenSearch.

## Passo a Passo

1. Instale as dependências do projeto:
```sh
pip install -r requirements.txt
```
2. Subir a aplicação na porta 8080
```sh
uvicorn main:app --reload --port 8080
```
3. Teste via cURL
```sh
curl -X POST "http://127.0.0.1:8080/agent/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "Olá", "session_id": "user123"}'
```

## Usando Docker

```sh
docker build -t agent-api .
docker run -d -p 8080:8080 --name agent_api agent-api
```

### Documentação estará disponível em http://127.0.0.1:8080/docs
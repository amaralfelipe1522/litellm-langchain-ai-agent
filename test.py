import boto3

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

response_stream = client.invoke_agent(
    agentId="XXXXXXXXXXX",
    agentAliasId="XXXXXXXXXXX",
    sessionId="test-session",
    inputText="Olá, tudo bem?"
)

full_response = ""

for event in response_stream["completion"]:
    if "chunk" in event:
        chunk = event["chunk"]
        if "bytes" in chunk:
            full_response += chunk["bytes"].decode("utf-8")

print("Resposta da IA:", full_response)


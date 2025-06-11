from agent.chains.simple_chain import build_chain

if __name__ == "__main__":
    chain = build_chain()
    input = input("Digite sua pergunta: ")
    resp = chain({"input": input})
    print("Resposta: ", resp)
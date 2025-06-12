from agent.history.build_history import build_chain_with_history

if __name__ == "__main__":
    chain = build_chain_with_history()
    while True:
        user_input = input("Digite sua pergunta: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        resp = chain.invoke({"input": user_input}, config={"configurable": {"session_id": "usuario_123"}})
        print("Resposta: ", resp)
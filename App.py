
def responder(pergunta):
    pergunta = pergunta.lower()

    if "olá" in pergunta or "oi" in pergunta:
        return "Olá! Eu sou ARGOS. Como posso ajudar?"

    elif "seu nome" in pergunta:
        return "Meu nome é ARGOS!"

    elif "tudo bem" in pergunta:
        return "Estou funcionando perfeitamente!"

    else:
        return "Ainda estou aprendendo. Pode perguntar outra coisa!"


print("ARGOS - Sua primeira inteligência artificial")
print("Digite sair para encerrar.")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("ARGOS: Até logo!")
        break

    resposta = responder(pergunta)
    print("ARGOS:", resposta)
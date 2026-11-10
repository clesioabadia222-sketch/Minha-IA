
import random
from datetime import datetime

nome_usuario = ""

def responder(pergunta):
    global nome_usuario

    pergunta = pergunta.lower().strip()

    if "olá" in pergunta or "oi" in pergunta:
        respostas = [
            "Olá! Que bom falar com você!",
            "E aí! Sou o ARGOS. Como posso ajudar?",
            "Olá! Estou aqui para conversar."
        ]
        return random.choice(respostas)

    elif "seu nome" in pergunta:
        return "Meu nome é ARGOS, seu assistente virtual!"

    elif "quem é você" in pergunta:
        return "Sou ARGOS, uma inteligência artificial em desenvolvimento."

    elif "tudo bem" in pergunta or "como você está" in pergunta:
        return "Estou funcionando perfeitamente! E você?"

    elif "seu criador" in pergunta:
        return "Fui criado pelo meu desenvolvedor usando Python!"

    elif "obrigado" in pergunta or "valeu" in pergunta:
        return "Por nada! Estou aqui para ajudar."

    elif "que horas" in pergunta:
        hora = datetime.now().strftime("%H:%M")
        return f"Agora são {hora}."

    elif "qual seu objetivo" in pergunta:
        return "Meu objetivo é conversar, ajudar e aprender novas funções."

    elif "tchau" in pergunta:
        return "Até mais! Estarei aqui quando precisar."

    else:
        return "Ainda não sei responder isso. Mas podemos me ensinar!"

print("================================")
print("       ARGOS INTELIGÊNCIA")
print("================================")
print("Digite sair para encerrar.")

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower().strip() == "sair":
        print("ARGOS: Até logo!")
        break

    resposta = responder(pergunta)
    print("ARGOS:", resposta)

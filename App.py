
# ==========================================
# ARGOS 1.0 - INTELIGENCIA ARTIFICIAL
# Desenvolvido em Python + Google Gemini
# ==========================================

!pip install -q -U google-genai

from google import genai
from google.genai import types
from getpass import getpass

import sys

print("=" * 45)
print("          ARGOS - INTELIGENCIA ARTIFICIAL")
print("=" * 45)

# 1. CONEXAO COM O GOOGLE GEMINI

chave = getpass("Digite sua chave API do Google: ")

cliente = genai.Client(api_key=chave)

# 2. PERSONALIDADE DO ARGOS

personalidade = """
Você é ARGOS, um assistente de inteligência artificial.

Sua missão é conversar, ensinar, aprender com o
contexto e ajudar as pessoas.

PERSONALIDADE:
- Inteligente e educado.
- Natural e comunicativo.
- Analítico e curioso.
- Paciente ao ensinar.
- Criativo na resolução de problemas.

REGRAS:
- Fale sempre em português brasileiro.
- Entenda perguntas escritas de diferentes maneiras.
- Explique assuntos complexos de maneira simples.
- Ajude com matemática, ciência, tecnologia,
  programação, história e conhecimentos gerais.
- Não invente informações.
- Admita quando não souber alguma coisa.
- Mantenha o contexto da conversa.
- Evite respostas repetitivas.
- Faça perguntas quando precisar esclarecer algo.
- Não responda apenas com frases prontas.

Você se chama ARGOS.
"""

# 3. CRIAR A CONVERSA

conversa = cliente.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=personalidade,
        temperature=0.7
    )
)

# 4. INICIAR O ARGOS

print("\nARGOS: Olá! Eu sou ARGOS.")
print("ARGOS: Estou pronto para conversar com você.")
print("ARGOS: Digite 'sair' para encerrar.")
print("-" * 45)

# 5. SISTEMA DE CONVERSACAO

while True:

    pergunta = input("\nVocê: ").strip()

    if not pergunta:
        continue

    if pergunta.lower() in ["sair", "exit", "fechar"]:
        print("\nARGOS: Até a próxima!")
        break

    try:

        resposta = conversa.send_message(pergunta)

        print("\nARGOS:", resposta.text)

    except Exception as erro:

        print("\nARGOS: Encontrei um problema.")
        print("Detalhes:", erro)

print("\nARGOS encerrado.")

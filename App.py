
!pip install -q -U google-genai

import os
import json
from datetime import datetime
from getpass import getpass
from google import genai
from google.genai import types

NOME = "ARGOS"
MODELO = "gemini-2.5-flash"
ARQUIVO_MEMORIA = "/content/argos_memoria.json"

chave = getpass("Digite sua chave API do Google: ")
cliente = genai.Client(api_key=chave)

PERSONALIDADE = """
Você é ARGOS, uma inteligência artificial avançada,
com identidade e personalidade próprias.

Você é inteligente, analítico, curioso, educado e natural.

Suas capacidades incluem:
- Conversação natural.
- Raciocínio lógico.
- Conhecimentos gerais.
- Matemática e ciências.
- Programação e tecnologia.
- Ensino de idiomas.
- Produção e análise de textos.
- Resolução de problemas.
- Explicação de assuntos complexos.
- Análise crítica de ideias.

Comportamento:
- Fale em português brasileiro.
- Seja claro, profundo e objetivo.
- Não invente informações.
- Admita quando não souber.
- Explique suas respostas quando necessário.
- Considere o contexto da conversa.
- Evite respostas genéricas e repetitivas.
- Faça perguntas relevantes.
- Trate o usuário com respeito.
- Tenha personalidade própria.

Seu nome é ARGOS.
"""

def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados if isinstance(dados, list) else []
        except Exception:
            return []
    return []

def salvar_memoria():
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)

historico = carregar_memoria()

def criar_conversa():
    mensagens = []
    for item in historico[-30:]:
        mensagens.append(
            types.Content(
                role=item["role"],
                parts=[types.Part.from_text(text=item["text"])]
            )
        )

    return cliente.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(
            system_instruction=PERSONALIDADE,
            temperature=0.7
        ),
        history=mensagens
    )

conversa = criar_conversa()

def responder(pergunta):
    try:
        resposta = conversa.send_message(pergunta)
        texto = resposta.text or "Não consegui formular uma resposta."

        historico.append({
            "role": "user",
            "text": pergunta,
            "data": datetime.now().isoformat()
        })

        historico.append({
            "role": "model",
            "text": texto,
            "data": datetime.now().isoformat()
        })

        salvar_memoria()
        return texto

    except Exception as erro:
        return f"Encontrei um erro: {erro}"

def executar_comando(comando):
    global historico, conversa

    if comando == "/ajuda":
        print("""
ARGOS - COMANDOS

/ajuda   - Mostrar comandos
/info    - Informações do sistema
/memoria - Consultar histórico
/limpar  - Apagar histórico
/salvar  - Salvar memória
/sair    - Encerrar ARGOS
""")
        return True

    if comando == "/info":
        print("Nome:", NOME)
        print("Modelo:", MODELO)
        print("Registros:", len(historico))
        print("Memória: ativa")
        return True

    if comando == "/memoria":
        print("Registros armazenados:", len(historico))
        return True

    if comando == "/salvar":
        salvar_memoria()
        print("ARGOS: Histórico salvo.")
        return True

    if comando == "/limpar":
        confirmacao = input("Apagar todo o histórico? (sim/não): ")
        if confirmacao.lower() == "sim":
            historico.clear()
            salvar_memoria()
            conversa = criar_conversa()
            print("ARGOS: Histórico apagado.")
        return True

    if comando == "/sair":
        salvar_memoria()
        print("ARGOS: Até a próxima!")
        return False

    return None

def iniciar_argos():
    print("=" * 50)
    print("ARGOS - INTELIGÊNCIA ARTIFICIAL")
    print("Sistema iniciado com sucesso.")
    print("Digite /ajuda para consultar os comandos.")
    print("=" * 50)

    while True:
        pergunta = input("\nVOCÊ: ").strip()

        if not pergunta:
            continue

        resultado = executar_comando(pergunta.lower())

        if resultado is False:
            break

        if resultado is True:
            continue

        print("\nARGOS:", responder(pergunta))

iniciar_argos()

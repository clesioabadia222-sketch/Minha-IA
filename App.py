def responder(pergunta); pergunta=.lower()
if "Olá" in pergunta or "oi" in pergunta:return "Olá! Eu sou minha IA.como posso ajudar?"
elif "seu nome" in pergunta:return " Meu nome é  ARGOS!"
elif " tudo bem"in pergunta:return "Estou funcionando perfeitamente!"
else:return "Ainda estou aprendendo.pode perguntar outra coisa!"
  print("ARGOS-Sua primeira inteligência artificial")
print("Digite sair para encerrar.")
while True: pergunta= input("Você:")
  if pergunta.lower()=="sair":print("MinhaIA: Até logo!")
    break resposta=responder) pergunta)print("MinhaIA:", resposta)

# Programa Educativo: Descarte Correto de Medicamentos
# Objetivo: Conscientizar usuários sobre o descarte responsável de medicamentos

print("=== Bem-vindo ao Programa de Descarte Consciente de Medicamentos ===\n")

# Pergunta o nome do usuário e inicia o diálogo
nome = input("Qual é o seu nome? ")
print(f"\nOlá, {nome}! Vamos aprender como descartar medicamentos da forma correta.\n")

print("Responda com 'sim' ou 'não' às perguntas abaixo:\n")

# Coleta as respostas do usuário
agua = input("Você já descartou medicamentos na pia ou no vaso sanitário? ").strip().lower()
lixo = input("Você costuma jogar medicamentos vencidos no lixo comum? ").strip().lower()
posto = input("Você conhece algum ponto de coleta de medicamentos na sua cidade? ").strip().lower()

# Apresenta resultados e orientações personalizadas
print("\n--- Resultados e Orientações ---")

if agua == "sim":
    print("- Evite descartar medicamentos na água! Isso contamina rios e solos, prejudicando o meio ambiente.")
else:
    print("- Ótimo! Nunca descarte medicamentos na água.")

if lixo == "sim":
    print("- Medicamentos no lixo comum podem causar contaminação. Procure um ponto de coleta autorizado.")
else:
    print("- Excelente! Evitar o lixo comum é uma atitude responsável.")

if posto == "não":
    print("- Informe-se nas farmácias e postos de saúde sobre locais de coleta de medicamentos vencidos.")
else:
    print("- Muito bem! Continue utilizando os pontos de coleta de forma correta.")

# Mensagem final personalizada com o nome do usuário
print(f"\nObrigado por participar, {nome}! Sua atitude ajuda a proteger o meio ambiente e a saúde pública.")
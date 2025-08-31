import json 
import os 

ARQUIVO_CONTATOS = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        try:
            with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao carregar os contatos. O arquivo pode estar corrompido.")
            return {}
    return {}

def salva_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w", encoding="utf=8") as arquivo:
        json.dump(contatos, arquivo, indent=4, ensure_ascii=False)

def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ").strip()
    if nome in contatos:
        print(f"O contatos `{nome}` já existe.")
        return 
    
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o e-mail: ").strip()

    contatos[nome] = {"telefone": telefone, "email": email}
    salva_contatos(contatos)
    print(f"”Contato ‘{nome}’ adicionado com sucesso!")

def remover_contato(contatos):
    nome = input("Digite o nome do contato a ser removido: ").strip()
    if nome in contatos:
        del contatos[nome]
        salva_contatos(contatos)
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"”O contato '{nome}' não foi encontrado.")

def listar_contatos(contatos):
    if contatos:
        print("\nLista de Contatos:")
        for nome, dados in contatos.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, E-mail: {dados['email']}")
    else:
        print("Nenhum contato cadastrado.")

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Listar contatos")
    print("4. Sair")

contatos = carregar_contatos()

while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_contato(contatos)
        elif opcao == 2:
            remover_contato(contatos)
        elif opcao == 3:
            listar_contatos(contatos)
        elif opcao == 4:
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro no sistema, tente novamente.")



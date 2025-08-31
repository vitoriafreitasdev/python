def exibir_menu():
    print("Menu: ")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sai")
def adicionar_item(lista):
    item = input("Digite o nome do item a ser adicionado: ").strip()
    if item in lista:
        print(f"O item ‘{item}’ já está na lista.")
    else:
        lista.append(item)
        print(f"Item ‘{item}’ adicionado com sucesso!")
def remover_item(lista):
    item = input("Digite o nome do item a ser removido: ").strip()
    if item in lista:
        lista.remove(item)
        print(f"Item ‘{item}’ removido com sucesso!")
    else:
        print(f"O item ‘{item}’ não está na lista.")
def listar_itens(lista):
    if lista:
        print("nItens na lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("A lista de compras está vazia.")

lista_de_compra = []

while True:
    exibir_menu()
    try: 
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_item(lista_de_compra)
        elif opcao == 2:
            remover_item(lista_de_compra)
        elif opcao == 3:
            listar_itens(lista_de_compra)
        elif opcao == 4:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente")
    except ValueError:
        print("Ouve um erro, tente novamente.")

    
        

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Listar tarefas pendentes")
    print("4. Listar tarefas concluídas")
    print("5. Sair")
def adicionar_tarefa(lista_tarefas):
    tarefa = input("Digite a descrição da tarefa: ").strip()
    if any(tarefa == item['descricao'] for item in lista_tarefas):
        print(f"A tarefa ‘{tarefa}’ já está na lista.")
    else:
        lista_tarefas.append({"descricao": tarefa, "concluida": False})
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
        print(f"Lista atual: {lista_tarefas}")
def marcar_concluida(lista_tarefas):
    tarefa = input("Digite a descrição da tarefa a ser marcada como concluída: ").strip()
    for item in lista_tarefas:
        if item["descricao"] == tarefa:
            if item["concluida"]:
                print(f"A tarefa '{tarefa}' já está marcada como concluída.")
        else:
            item["concluida"] = True
            print(f"Tarefa '{tarefa}' marcada como concluída com sucesso!")
        return
    print(f"Tarefa ‘{tarefa}’ não encontrada na lista.")
          
def listar_tarefas(lista_tarefas, concluida):
    status = "concluídas" if concluida else "pendentes"
    tarefas = [item["descricao"] for item in lista_tarefas if item["concluida"] == concluida]
    if tarefas:
        print(f"\nTarefas {status}:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print(f"Não há tarefas {status} no momento.")
# Programa principal
lista_tarefas = []
while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            adicionar_tarefa(lista_tarefas)
        elif opcao == 2:
            marcar_concluida(lista_tarefas)
        elif opcao == 3:
            listar_tarefas(lista_tarefas, concluida=False)
        elif opcao == 4:
            listar_tarefas(lista_tarefas, concluida=True)
        elif opcao == 5:
            print("Encerrando o programa. Boa sorte com suas tarefas!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente à opção.")
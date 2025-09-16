

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from avltree import AVLarvore

"""

rotinas de aprendizado de máquina para estratificação de pacientes
fazer um analise com aprendizado de maquina para pegar os pacientes que estao em situações mais graves, 1 para grave, 0 para nao grave
pacientes graves seram prioridade => entraram na fila de pioridade

"""


if __name__ == "__main__":
    # Criando a árvore AVL
    avl_tree = AVLarvore()
    dados_para_inserir = []

    def menu():
        remedios_quantidade = int(input("Quantos remedios se vai inserir para analise: "))
    
        for i in range(remedios_quantidade):
            # Inserindo dados na árvore
            eficiencia = input("Remedio é eficiente (s/n): ")

            if(eficiencia != "s" and eficiencia != "n"):
                print("Insira os dados corretamente.")
                break
            
            colateral = input("Remedio tem colateral (sem colateral/colateral medio/colateral forte): ")
            
            if(colateral != "sem colateral" and colateral != "colateral medio" and colateral != "colateral forte"):
                print("Insira os dados corretamente.")
                break
            
            if colateral == "sem colateral" or colateral == "colateral medio":
                colateral_aceitavel = True 
            
            if colateral == "colateral forte":
                colateral_aceitavel = False

            if colateral_aceitavel and eficiencia == "s":
                passa = 1
            else:
                passa = 0

            dados_para_inserir.append((f'Remedio {i}', f'{eficiencia}', f'{colateral}', passa))
    
    menu()

    print(dados_para_inserir)
    for remedio, efetivo, colateral, passa in dados_para_inserir:
        avl_tree.insert(remedio, efetivo, colateral, passa)

    data_list = []
    avl_tree.transforme_data(avl_tree.root, data_list)

    df = pd.DataFrame(data_list) 

    inputs = df.drop('passa', axis='columns')
    target = df['passa']

    le_remedio = LabelEncoder()
    le_efetivo = LabelEncoder()
    le_colateral = LabelEncoder()

    inputs["remedio_n"] = le_remedio.fit_transform(inputs['remedio'])
    inputs["efetivo_n"] = le_colateral.fit_transform(inputs['efetivo'])
    inputs["colateral_n"]= le_colateral.fit_transform(inputs['colateral'])

    inputs_n = inputs.drop(['remedio', 'efetivo', 'colateral'], axis="columns")
    
    print("Dados da Árvore AVL:")
    print(df)
    print("\nDados Codificados:")
    print(inputs_n)

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)
    porcetagem_acerto = model.score(inputs_n, target)
    while True:

        try:
            print("De acordo com a tabela de de dados codificados, coloque abaixo os numeros, dos seguintes dados: remedio, efetivo, colateral.")
            n1 = int(input("Numero do remedio: "))
            n2 = int(input("Numero do efetivo: "))
            n3 = int(input("Numero do colateral: "))
            resultado = model.predict([[n1, n2, n3]])

            if resultado == 1:
                print("Aprovado para fase 2")
            else:
                print("Reporovado, precisa de mais testes e mais reajustes a serem feitos.")

            continuar = input("Deseja continuar (s/n): ")

            if continuar != "s":
                print("Encerrando...")
                break

        except ValueError:
            print("Deu algum erro, tente novamente.")   
            break   
    
    print("\n")
    passaram =  avl_tree.bfs_remedios_que_passaram(avl_tree.root)
    todos_remedios = []
    avl_tree.dfs_todos_remedios_do_teste(avl_tree.root, todos_remedios)

    print("=== Remedios que passaram no teste ===")
    for remedio in passaram:
        print(remedio) 

    print("=== Todos remedios que estão no teste ===")
    for remedio in todos_remedios:
        print(remedio) 

    # print("Árvore AVL completa (ordenada por (passa, remedio)):")
    # avl_tree.print_tree()
   
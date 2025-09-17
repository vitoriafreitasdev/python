

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from avltree import AVLarvore
from grafo import Grafo

"""
- colacar mais um atributo na arvore => seguro de administrar
- Fazer detecção de remédios se desviam muito dos outros

"""


if __name__ == "__main__":
    # Criando a árvore AVL
    avl_tree = AVLarvore()
    dados_para_inserir = []
    vertices = []

    def menu():
        remedios_quantidade = int(input("Quantos remedios se vai inserir para analise: "))
    
        for _ in range(remedios_quantidade):
            # Inserindo dados na árvore
            nome_remedio = input("Coloque o nome do remedio: ")

            eficiencia = input("Remedio é eficiente (s/n): ")

            if(eficiencia != "s" and eficiencia != "n"):
                print("Insira os dados corretamente.")
                return
            
            colateral = input("Remedio tem colateral (sem colateral/colateral medio/colateral forte): ")
            
            if(colateral != "sem colateral" and colateral != "colateral medio" and colateral != "colateral forte"):
                print("Insira os dados corretamente.")
                return
            
            if colateral == "sem colateral" or colateral == "colateral medio":
                colateral_aceitavel = True 
            
            if colateral == "colateral forte":
                colateral_aceitavel = False

            if colateral_aceitavel and eficiencia == "s":
                passa = 1
            else:
                passa = 0

            dados_para_inserir.append((f'{nome_remedio}', f'{eficiencia}', f'{colateral}', passa))

        pacientes_quantidade = int(input("Quantos pacientes participaram do teste: "))

    
        for i in range(pacientes_quantidade):
            
            nome = input("Nome do paciente: ")
            gravidade_input = input("Doença é grave (s/n): ")
            if gravidade_input != "s" and gravidade_input != "n":
                print("Insira os dados corretos.")
                return
            
            if gravidade_input == "s":
                gravidade = 1
            
            if gravidade_input == "n":
                gravidade = 0

            vertices.append((nome, gravidade))

    menu()


    for remedio, efetivo, colateral, passa in dados_para_inserir:
        avl_tree.insert(remedio, efetivo, colateral, passa)

    data_list = []

    

    avl_tree.transforme_data(avl_tree.root, data_list)

    df = pd.DataFrame(data_list) 

    inputs = df.drop('passa', axis='columns')
    target = df['passa']

    print(target)

    le_remedio = LabelEncoder()
    le_efetivo = LabelEncoder()
    le_colateral = LabelEncoder()

    inputs["remedio_n"] = le_remedio.fit_transform(inputs['remedio'])
    inputs["efetivo_n"] = le_colateral.fit_transform(inputs['efetivo'])
    inputs["colateral_n"]= le_colateral.fit_transform(inputs['colateral'])

    inputs_n = inputs.drop(['remedio', 'efetivo', 'colateral'], axis="columns")
    inputs_sem_numero = inputs.drop(['remedio_n', 'efetivo_n', 'colateral_n'], axis="columns")
    print("Dados:")
    print(inputs_sem_numero)
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
                print("Aprovado para venda.")
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


    ## grafo parte

    grafo = Grafo(vertices)

    data = grafo.alocar_dados()


    dfpacientes = pd.DataFrame(data)
    dfpacientes['gravidade'] = dfpacientes['gravidade'].apply(lambda x: x[0])
 
    inputs_pacientes = dfpacientes.drop('gravidade', axis="columns")
    target_pacientes = dfpacientes['gravidade']

    le_nome = LabelEncoder()

    inputs_pacientes["nome_numero"] = le_nome.fit_transform(inputs_pacientes['nome'])


    inputs_n_pacientes = inputs_pacientes.drop(['nome'], axis="columns")
    
    modelPacientes = tree.DecisionTreeClassifier()

    modelPacientes.fit(inputs_n_pacientes, target_pacientes)
    
    print("=== tabela dos pacientes ===")

    print(inputs_pacientes)
    pacientes_prioritarios = []

    for _ in range(len(inputs_n_pacientes)):
        nome = input("Coloque o nome do paciente: ")
        n = int(input("Coloque o numero respectivo ao nome do paciente para ser feito o relocamento para a fila de prioridade: "))
        resultadopacientes = modelPacientes.predict([[n]])
        
        if resultadopacientes == 1:
            pacientes_prioritarios.append((nome))
   


    fila =  grafo.alocar_fila_de_pioridade(pacientes_prioritarios)

    print("=== Ordem de atendimento dos prioritários ===")
    grafo.mostrar_prioritarios(fila)


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from avltree import AVLarvore
from grafo import Grafo

"""
otimizição
ver o porque demora segundos para aparecer o menu
tentar resolver o problema dos warnings do terminal, se nao resolver, mas o codigo funcionar perfeitamente tirar eles

"""


if __name__ == "__main__":
    # Criando a árvore  para alimentar os dados da rotina de aprendizado de maquina dos remédios.
    avl_tree = AVLarvore()
    dados_para_inserir = []
    vertices = []

    def menu():
        #Coletando dados para arvore AVL
        remedios_quantidade = int(input("Quantos remédios se vai inserir para analise: "))
    
        for _ in range(remedios_quantidade):
            
            nome_remedio = input("Coloque o nome do remédio: ")

            eficiencia = input("Remédio é eficiente (s/n): ")

            if(eficiencia != "s" and eficiencia != "n"):
                print("Insira os dados corretamente.")
                return
            
            seguro = input("Remédio é seguro de administrar (s/n): ")

            if(seguro != "s" and seguro != "n"):
                print("Insira os dados corretamente.")
                return
            
            colateral = input("Remédio tem colateral (sem colateral/colateral medio/colateral alto): ")
            
            if(colateral != "sem colateral" and colateral != "colateral medio" and colateral != "colateral alto"):
                print("Insira os dados corretamente.")
                return
            
            if colateral == "sem colateral" or colateral == "colateral medio":
                colateral_aceitavel = True 
            
            if colateral == "colateral alto":
                colateral_aceitavel = False

            if colateral_aceitavel and eficiencia == "s" and seguro == "s":
                passa = 1
            else:
                passa = 0

            dados_para_inserir.append((f'{nome_remedio}', f'{eficiencia}', f'{colateral}', f'{seguro}', passa))

        #Coletando dados para o grafo que vai alimentas a rotina de aprendizado de maquina dos pacientes.
        pacientes_quantidade = int(input("Quantos pacientes participaram do teste: "))

        for _ in range(pacientes_quantidade):
            
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

    for remedio, efetivo, colateral, seguro, passa in dados_para_inserir:
        avl_tree.insert(remedio, efetivo, colateral, seguro, passa)

    data_list = []

    avl_tree.transforme_data(avl_tree.root, data_list)

    df = pd.DataFrame(data_list) 

    inputs = df.drop('passa', axis='columns')
    target = df['passa']


    le_remedio = LabelEncoder()
    le_efetivo = LabelEncoder()
    le_colateral = LabelEncoder()
    le_seguro = LabelEncoder()

    inputs["remedio_n"] = le_remedio.fit_transform(inputs['remedio'])
    inputs["efetivo_n"] = le_colateral.fit_transform(inputs['efetivo'])
    inputs["colateral_n"]= le_colateral.fit_transform(inputs['colateral'])
    inputs["seguro_n"]= le_seguro.fit_transform(inputs['seguro'])

    inputs_n = inputs.drop(['remedio', 'efetivo', 'colateral', 'seguro'], axis="columns")
    inputs_sem_numero = inputs.drop(['remedio_n', 'efetivo_n', 'colateral_n', 'seguro_n'], axis="columns")
    print("Dados:")
    print(inputs_sem_numero)
    print("\nDados Codificados:")
    print(inputs_n)

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)
    
    outliers = []

    while True:

        try:
            print("De acordo com a tabela de de dados codificados, coloque abaixo os números, dos seguintes dados: remedio, efetivo, seguro, colateral.")
            n1 = int(input("Número do remédio: "))
            n2 = int(input("Número respectivo a efetividade: "))
            n3 = int(input("Número do colateral: "))
            n4 = int(input("Número respectivo a efetividade a segurança: "))
            resultado = model.predict([[n1, n2, n3, n4]])

            if resultado == 1:
                print("Aprovado para venda.")
            else:
                print("Reporovado, precisa de mais testes e mais reajustes a serem feitos.")
                outliers.append((f"Número do remédio: {n1}"))

            continuar = input("Deseja continuar (s/n): ")

            if continuar != "s":
                print("Encerrando...")
                break

        except ValueError:
            print("Deu algum erro, tente novamente.")   
            break   
    
    print("\n")
    passaram =  avl_tree.bfs(avl_tree.root)
    todos_remedios = []
    avl_tree.dfs(avl_tree.root, todos_remedios)

    print("=== Remédios que passaram no teste ===")
    for remedio in passaram:
        print(remedio) 

    print("=== Todos remédios que estão no teste ===")
    for remedio in todos_remedios:
        print(remedio) 

    print("=== Outliers dectados durantes os testes ===")
    for outlier in outliers:
        print(outlier)

    #Criando o grafo
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
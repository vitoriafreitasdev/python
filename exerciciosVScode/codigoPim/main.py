
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from avltree import AVLarvore
from grafo import Grafo



if __name__ == "__main__":

    # Criando a árvore  para alimentar os dados da rotina de aprendizado de maquina dos remédios.
    avl_tree = AVLarvore()
    dados_para_inserir = []
    vertices = []

    def menu():
        # Coletando dados para arvore AVL
        
        remedios_quantidade = int(input("Quantos remédios se vai inserir para analise: "))
    
        for _ in range(remedios_quantidade):

            print("\n-----------------------------------------------\n")   
            nome_remedio = input("Coloque o nome do remédio: ")

            eficiencia = input("Remédio é eficiente (s/n): ").lower().strip()

            if eficiencia not in ("s", "n"):
                print("Insira os dados corretamente.")
                return
            
            seguro = input("Remédio é seguro de administrar (s/n): ").lower().strip()

            if seguro not in ("s", "n"):
                print("Insira os dados corretamente.")
                return
            
            colateral = input("Colateral do remédio: (sem/medio/alto): ").lower().strip()
            
            if colateral not in ("sem", "medio", "alto"):
                print("Insira os dados corretamente.")
                return
            
            if colateral in ("sem", "medio"):
                colateral_aceitavel = True 
            else:
                colateral_aceitavel = False

            if colateral_aceitavel and eficiencia == "s" and seguro == "s":
                passa = 1
            else:
                passa = 0

            dados_para_inserir.append((f'{nome_remedio}', f'{eficiencia}', f'{colateral}', f'{seguro}', passa))
            print("\n-----------------------------------------------\n")   

        print("\n================= Coleta de dados dos pacientes =================\n")
        # Coletando dados para o grafo que vai alimentar a rotina de aprendizado de maquina dos pacientes.
        pacientes_quantidade = int(input("Quantos pacientes participaram do teste: "))

        for _ in range(pacientes_quantidade):
            
            nome = input("Nome do paciente: ")
            gravidade_input = input("Doença é grave (s/n): ").lower().strip()
            if gravidade_input not in ("s", "n"):
                print("Insira os dados corretos.")
                return
            
            gravidade = 1 if gravidade_input == "s" else 0
            vertices.append((nome, gravidade))
        
        print("\n====================================\n")

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
    
    print("\n ----- Dados -----")
    print(inputs_sem_numero)
    print("\n ----- Dados Codificados -----")
    print(inputs_n)

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)

    outliers = []
    print("\n====== Análise de remédios ======\n")
    for i in range(len(inputs_n)):
        n1 = inputs_n.iloc[i]["remedio_n"]
        n2 = inputs_n.iloc[i]["efetivo_n"]
        n3 = inputs_n.iloc[i]["colateral_n"]
        n4 = inputs_n.iloc[i]["seguro_n"]

        nome_remedio = inputs.iloc[i]["remedio"]

        # Criando DataFrame para evitar warning
        treinamento_remedios = pd.DataFrame([[n1, n2, n3, n4]], 
                                  columns=["remedio_n", "efetivo_n", "colateral_n", "seguro_n"])
        resultado = model.predict(treinamento_remedios)

        print("========================")
        if resultado == 1:
            print(f"Remédio: {nome_remedio}. Aprovado para venda.")
        else:
            print(f"Remédio: {nome_remedio}. Reprovado, precisa de mais testes e reajustes a serem feitos.")
            outliers.append((f"Nome do remédio: {nome_remedio}"))
        print("========================")
 
    passaram = avl_tree.bfs(avl_tree.root)
    todos_remedios = []
    avl_tree.dfs(avl_tree.root, todos_remedios)

    print("\n===== Remédios que passaram no teste =====")
    for remedio in passaram:
        print(remedio) 

    print("\n===== Todos remédios que estão no teste =====")
    for remedio in todos_remedios:
        print(remedio) 

    print("\n===== Outliers detectados durante os testes =====")
    for outlier in outliers:
        print(outlier)
    print("\n")

    # Criando o grafo
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
    
    print("\n===== Tabela dos pacientes ====")
    print(inputs_pacientes)

    pacientes_prioritarios = []

    print("\n===== Prevendo os pacientes =====")
    for i in range(len(inputs_n_pacientes)):
        n = inputs_n_pacientes.iloc[i]["nome_numero"]
        nome = inputs_pacientes.iloc[i]["nome"]

        # Criando DataFrame para evitar warning
        treinamento_paciente = pd.DataFrame([[n]], columns=["nome_numero"])
        resultadopacientes = modelPacientes.predict(treinamento_paciente)

        print(f"\nFazendo o relocamento de pacientes para fila de prioritários. Paciente: {nome}\n")
        if resultadopacientes == 1:
            pacientes_prioritarios.append(nome)

    fila = grafo.alocar_fila_de_pioridade(pacientes_prioritarios)

    print("\n===== Ordem de atendimento dos prioritários =====")
    grafo.mostrar_prioritarios(fila)

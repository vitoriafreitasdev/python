

from collections import defaultdict

from collections import deque
"""

encadeamento de tarefas com grafos

- primeiro coletamos os dados do pacientes, nome e gravidade da doença
- colocamos esses dados em grafo
- depois pegamos os que são pioridade com um rotina de aprendizado de maquina e colocamos na lila de pioridade
"""
# as vertices vao ser o nome e a gravidade da doenca

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.grafo = defaultdict(list)

        for nome, gravidade in self.vertices:
            self.grafo[nome].append(gravidade)
        
    
    def todos_pacientes(self):
        for vizinhos in self.grafo:
            print(vizinhos)

    def alocar_fila_de_pioridade(self, pacientes_prioritarios):
        fila = deque([])
        for paciente in pacientes_prioritarios:
            fila.append(paciente)
        
        return fila 
    
    def mostrar_prioritarios(self, fila):
        
        for i in range(len(fila)):
            print(f"Paciente número {i+1}:", fila.popleft()) 

    def alocar_dados(self):
        data = []
    
        for key, value in self.grafo.items():
            data.append({"nome": key, "gravidade": value})
    
        return data

        
        
        
   


pacientes = [
    ("B", "sim"),
    ("C", "nao"),
    ("D", "sim"),
    ("E", "nao"),
    ("F", "sim"),
    ("G", "nao"),
]
# vertices = []
# print(pacientes)
# for i in range(4):
#     nome = input("Nome: ")
#     gravidade = input("gravidade: ")
#     vertices.append((nome, gravidade))

# print(vertices)
# grafo = Grafo(pacientes)

# grafo.todos_pacientes()

# pacientes_prioritarios = [("C"), ("E"), ("G")]

# fila_de_prioridade = grafo.alocar_fila_de_pioridade(pacientes_prioritarios)

# grafo.mostrar_prioritarios(fila_de_prioridade)

# data = grafo.alocar_dados()

# print(data)

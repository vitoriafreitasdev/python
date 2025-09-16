

from collections import defaultdict

from collections import deque
"""
focar na parte de estraficação de pacientes
para  encadeamento de tarefas =. 1.fazer um grafo que vai representar os pacientes que participaram do teste
dividir em => nome, gravidade da doença 
2. pegar os que estão com gravidade alta e colocar na fila de prioridade, mostrar essa fila de prioridade na tela
0 para não grave, 1 para grave
"""
# as vertices vao ser o nome e a gravidade da doenca

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.grafo = defaultdict(list)

        for nome, gravidade in self.vertices:
            self.grafo[nome].append(gravidade)
        
        print(self.grafo)
    
    def todos_pacientes(self):
        
        for vizinhos in self.grafo:
            print(vizinhos)

            
            




pacientes = [
    ("B", 0),
    ("C", 1),
    ("D", 0),
    ("E", 1),
    ("F", 0),
]

grafo = Grafo(pacientes)

grafo.todos_pacientes()


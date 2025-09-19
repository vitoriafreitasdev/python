

from collections import defaultdict

from collections import deque

# as vertices vao ser o nome e a gravidade da doenca

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.grafo = defaultdict(list)

        for nome, gravidade in self.vertices:
            self.grafo[nome].append(gravidade)
        
    #Análise Assintótica Tempo: O(n) Espaço: O(1)
    def todos_pacientes(self):
        for vizinhos in self.grafo:
            print(vizinhos)
    #Análise Assintótica Tempo: O(n) Espaço: O(n)
    def alocar_fila_de_pioridade(self, pacientes_prioritarios):
        fila = deque([])
        for paciente in pacientes_prioritarios:
            fila.append(paciente)
        
        return fila 
     #Análise Assintótica Tempo: O(n) Espaço: O(n)
    def mostrar_prioritarios(self, fila):
        
        for i in range(len(fila)):
            print(f"Paciente número {i+1}:", fila.popleft()) 
     #Análise Assintótica Tempo: O(n) Espaço: O(n)
    def alocar_dados(self):
        data = []
    
        for key, value in self.grafo.items():
            data.append({"nome": key, "gravidade": value})
    
        return data


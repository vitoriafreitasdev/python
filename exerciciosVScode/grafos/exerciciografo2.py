
from collections import defaultdict

from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices

        self.grafo = defaultdict(list)

        for inicio, fim in self.vertices:
            self.grafo[inicio].append(fim)

    def todos_caminhos(self, inicio, destino):
            todos = []

            def dfs(atual, caminho, visitados):
                 if atual == destino:
                      todos.append(caminho.copy())
                      return
                 
                 for vizinhos in self.grafo.get(atual, []):
                      if vizinhos not in visitados:
                           visitados.add(vizinhos)
                           caminho.append(vizinhos)
                           dfs(vizinhos, caminho, visitados)
                           caminho.pop()
                           visitados.remove(vizinhos)
            dfs(inicio, [inicio], set([inicio]))
            return todos
    
     
    
    def bfs(self, inicio, destino):
        visitados = set([inicio])
        fila = deque([[inicio]])
      
        while fila:
             caminho = fila.popleft()
             print("Caminho ", caminho)
             ultimo = caminho[-1]
             if ultimo == destino:
                  return caminho
             
             for v in self.grafo.get(ultimo, []):
                  if v not in visitados:
                       visitados.add(v)
                       fila.append(caminho + [v])
        return None


vertices = [('R1', 'R2'), ('R1', 'R3'), ('R2', 'R4'), ('R2', 'R5'), ('R3', 'R6'), ('R4', 'R7'), ('R5', 'R7'), ('R5', 'R8'), ('R6', 'R8'), ('R7', 'R9'), ('R8', 'R9')]

grafo = Grafo(vertices)
todos = grafo.todos_caminhos("R1", "R8")
mais_curto = grafo.bfs("R1", "R8")
print(mais_curto)
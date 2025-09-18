from collections import defaultdict

from collections import deque

"""
exercicio o que fazer

cada no representa um roteador e as conexoes entre eles 

criar um grafo nao direcionadoo

"R1" está conectado a "R2" e "R3"

"R2" está conectado a "R4" e "R5"

"R3" está conectado a "R6"

"R4" está conectado a "R7"

"R5" está conectado a "R7" e "R8"

"R6" está conectado a "R8"

"R7" está conectado a "R9"

"R8" está conectado a "R9"

Um algoritmo para encontrar todos os caminhos possíveis entre dois roteadores (DFS)

Um algoritmo para encontrar o caminho mais curto entre dois roteadores (BFS)

Todos os caminhos entre "R1" e "R9"

O caminho mais curto entre "R1" e "R9"

"""

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices

        self.grafo = defaultdict(list)

        for inicio, fim in self.vertices:
            self.grafo[inicio].append(fim)

        print(self.grafo)
    
    def dfs(self, inicio, fim, todos = []):
        pass 

    def bfs(self):
        pass


vertices = [('R1', 'R2'), ('R1', 'R3'), ('R2', 'R4'), ('R2', 'R5'), ('R3', 'R6'), ('R4', 'R7'), ('R5', 'R7'), ('R5', 'R8'), ('R6', 'R8'), ('R7', 'R9'), ('R8', 'R9')]

grafo = Grafo(vertices)

from collections import defaultdict

from collections import deque
# class Grafo:
#     def __init__(self, tamanho, valores):
#         self.tamanho = tamanho
#         self.valores = valores
#         self.grafo = []
#         for i in range(self.tamanho):
#             self.grafo.append([0] * self.tamanho)

#         for v, u in self.valores:
#             self.grafo[v][u] = 1
#             self.grafo[u][v] = 1

#         for i in range(self.tamanho):
#             for j in range(self.tamanho):
#                 print(self.grafo[i][j], end=" ")
#             print()
#         print(self.grafo)
# v = 4
# A = [[0, 1], [1, 2], [1, 3], [2, 3]]
# grafo = Grafo(v, A)


##

class GrafoFlexivel:
    def __init__(self):
        self.vertices = []    # Lista de vértices
        self.mapa = {}        # Mapeamento: vértice -> índice
        self.grafo = []       # Matriz de adjacência
    
    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo"""
        if vertice not in self.mapa:
            indice = len(self.vertices)
            self.mapa[vertice] = indice
            self.vertices.append(vertice)
            
            # Expande a matriz
            for linha in self.grafo:
                linha.append(0)
            self.grafo.append([0] * (indice + 1))
    
    def adicionar_aresta(self, origem, destino):
        """Adiciona aresta entre dois vértices"""
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        i = self.mapa[origem]
        j = self.mapa[destino]
        self.grafo[i][j] = 1
        self.grafo[j][i] = 1
    
    def imprimir_matriz(self):
        """Imprime a matriz de adjacência"""
        if not self.vertices:
            print("Grafo vazio!")
            return
        
        # Para strings, alinha melhor
        max_len = max(len(str(v)) for v in self.vertices)
        formato = f"{max_len}s"
        
        # Cabeçalho
        print(" " * max_len, end=" ")
        for v in self.vertices:
            print(f"{v:{max_len}}", end=" ")
        print()
        
        # Linhas
        for i, v in enumerate(self.vertices):
            print(f"{v:{max_len}}", end=" ")
            for valor in self.grafo[i]:
                print(f"{valor:{max_len}}", end=" ")
            print()

# Exemplo de uso misto
grafo = GrafoFlexivel()

# Podemos misturar strings e números!
grafo.adicionar_aresta("São Paulo", 1)  # String + número
grafo.adicionar_aresta(1, "Rio")        # Número + string
grafo.adicionar_aresta("Rio", "BH")     # String + string
grafo.adicionar_aresta(2, 3)            # Número + número

grafo.imprimir_matriz()
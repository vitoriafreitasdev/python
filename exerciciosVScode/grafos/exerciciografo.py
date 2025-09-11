"""
exercicio o que fazer:

construir um grafo de cidades

mostrar o caminho minimo de uma cidade para outra 

mostrar todos os caminhos possiveis 

"""

from collections import defaultdict

from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices

        self.grafo = defaultdict(list)

        for inicio, fim in self.vertices:
            self.grafo[inicio].append(fim)
            self.grafo[fim].append(inicio)

        
        print(self.grafo)

    def dfs(self, inicio, fim, path=[]):
        path = path + [inicio]

        if inicio == fim:
            return [path]
        
        if inicio not in self.grafo:
            return []
        
        todos_caminhos = []

        for node in self.grafo[inicio]:
            if node not in path:

                caminhos = self.dfs(node, fim, path)

                for caminho in caminhos:
                    todos_caminhos.append(caminho)
            
        return todos_caminhos

    def bfs(self, inicio, fim):
        visitados = set([inicio])
        fila = deque([[inicio]])
        while fila:

            # debug print("fila: ", fila)
            caminho = fila.popleft()
            ultimo = caminho[-1]

            # debug print("caminho: ", caminho)
            # debug print("ultimo: ", ultimo)

            if ultimo == fim:
                return caminho
            #O [] serve como fallback seguro: evita erro e permite que o loop simplesmente não execute se o nó não tiver vizinhos.
            for vizinho in self.grafo.get(ultimo, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(caminho + [vizinho])
                    # debug print("fila: ",fila)
                    # debug print("visitados: ", visitados)
        return None


cidades = [
    ("São Paulo", "Osasco"),
    ("Osasco", "Barueri"),
    ("Barueri", "Alphaville"),
    ("Barueri", "Carapicuiba"),
    ("Carapicuiba", "Itapevi"),
    ("Carapicuiba", "Alphaville"),
    ("Osasco", "Sorocaba"),
]

grafo_cidades = Grafo(cidades)
inicio = "Sorocaba"
fim = "Itapevi"
print(f"Caminho mais curto entre {inicio} e {fim}", grafo_cidades.bfs(inicio, fim))
print(f"Todos caminhos entre {inicio} e {fim}", grafo_cidades.dfs(inicio, fim))
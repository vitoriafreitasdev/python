
"""
exercicio o que fazer:

construir um grafo de paises

mostrar o caminho minimo de um pais para o outro

mostrar todos os caminhos possiveis 

"""

from collections import defaultdict

from collections import deque


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.grafo = defaultdict(list)

        for inicio, fim in vertices:
            self.grafo[inicio].append(fim)
            self.grafo[fim].append(inicio)

    def print_grafo(self):
        for values, keys in self.grafo.items():
            print(f"{values} => {keys}")

    def bfs(self, inicio, destino):
        fila = deque([[inicio]])
        visitados = set([inicio])

        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]

            if ultimo == destino:
                return caminho
            
            for vizinho in self.grafo.get(ultimo, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(caminho + [vizinho])
        return None

    def dfs(self, inicio, destino):
        todos = []

        def dfs_funcao(atual, caminho, visitados):
            if atual == destino:
                todos.append(caminho.copy())
                return
            for vizinhos in self.grafo.get(atual, []):
                if vizinhos not in visitados:
                    visitados.add(vizinhos)
                    caminho.append(vizinhos)
                    dfs_funcao(vizinhos, caminho, visitados)
                    caminho.pop()
                    visitados.remove(vizinhos)
        dfs_funcao(inicio, [inicio], set([inicio]))
        return todos


paises = [
    ("Inglaterra", "França"),
    ("Inglaterra", "País de Gales"),
    ("França", "Italia"),
    ("França", "Alemanha"),
    ("Italia", "Grecia"),
    ("Alemanha", "Noruega"),
    ("Grecia", "Noruega")
]

grafo = Grafo(paises)
grafo.print_grafo()
caminho_mais_curto = grafo.bfs("França", "Noruega")
todos_caminhos = grafo.dfs("França", "Noruega")
print("Caminho mais curto: ", caminho_mais_curto)
print("Todos caminhos: ", todos_caminhos)

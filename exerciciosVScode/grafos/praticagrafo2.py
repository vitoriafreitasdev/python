
from collections import defaultdict

from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = defaultdict(list)

        for v, u in self.vertices:
            self.grafo[v].append(u)

        print(self.grafo)

    def dfs(self, inicio, fim, todos=[]):
        todos = todos + [inicio]

        if inicio == fim:
            return [todos]
        
        if inicio not in self.grafo:
            return []
        
        todos_caminhos = []

        for no in self.grafo[inicio]:
            if no not in todos:
                caminhos = self.dfs(no, fim, todos)
                for c in caminhos:
                    todos_caminhos.append(c) #aqui guarda todos os resultados da resursão.

        return todos_caminhos
    # mais eficiente
    def dfs_pop(self, inicio, destino):
        todos = []

        def dfs_grafo(atual, caminho, visitados):
            if atual == destino:
                todos.append(caminho.copy())
                return
                
            for vizinhos in self.grafo.get(atual, []):
                if vizinhos not in visitados:
                    visitados.add(vizinhos)
                    caminho.append(vizinhos)
                    dfs_grafo(vizinhos, caminho, visitados)
                    caminho.pop()
                    visitados.remove(vizinhos)
        dfs_grafo(inicio, [inicio], set([inicio]))
        return todos
    def bfs(self, inicio, fim):
        visitados = set([inicio])
        fila = deque([[inicio]])

        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]

            if ultimo == fim:
                return caminho
            
            for v in self.grafo.get(ultimo, []):
                if v not in visitados:
                    visitados.add(v)
                    fila.append(caminho + [v])

        return None
    


letras = [
    ("A", "B"),
    ("B", "C"),
    ("B", "D"),
    ("C", "A"),
    ("C", "E"),
    ("D", "E"),
]

grafo = Grafo(letras)
print("\nBfs\n")
print(grafo.bfs("A", "E"))
print("\nDfs\n")
print(grafo.dfs_pop("A", "E"))
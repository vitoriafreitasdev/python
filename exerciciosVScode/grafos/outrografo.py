
from collections import defaultdict
from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = defaultdict(list)

        for v, u in vertices:
            self.grafo[v].append(u)
            self.grafo[u].append(v)

    
    def bfs(self, inicio, destino):
        fila = deque([[inicio]])
        visitados = set([inicio])

        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]

            if ultimo == destino:
                return caminho
            
            for v in self.grafo.get(ultimo, []):
                
                if v not in visitados:
                    visitados.add(v)
                    fila.append(caminho + [v])

        return 
    
    def dfs(self, inicio, fim):
        todos = []

        def dfs_inside(atual, caminho, visitados):
            if atual == fim:
                todos.append(caminho.copy())
                return 

            for v in self.grafo.get(atual, []):
                if v not in visitados:
                    visitados.add(v)
                    caminho.append(v)
                    dfs_inside(v, caminho, visitados)
                    caminho.pop()
                    visitados.remove(v)

        dfs_inside(inicio, [inicio], set([inicio]))
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

todos_caminhos = grafo.dfs("França", "Noruega")

print("Todos caminhos: ", todos_caminhos)


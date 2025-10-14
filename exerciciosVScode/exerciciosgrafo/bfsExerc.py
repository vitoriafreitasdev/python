
from collections import defaultdict
from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.grafo = defaultdict(list)

        for v, u in self.vertices:
            self.grafo[v].append(u)
            self.grafo[u].append(v)

    def bfs(self, inicio, fim):
        fila = deque([[inicio]])
        visitados = set([inicio])
        
        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]

            if ultimo == fim:
                return caminho
            
            for vertice in self.grafo.get(ultimo, []):
                if vertice not in visitados:
                    visitados.add(vertice)
                    fila.append(caminho + [vertice])
        return None
    
    def caminho(self, destino):
        primeiro = list(self.grafo.keys())[0]
        fila = deque([[primeiro]])
        visitados = set([primeiro])

        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]
            if(ultimo == destino):
                return caminho
            
            for v in self.grafo.get(ultimo, []):
                if v not in visitados:
                    visitados.add(v)
                    fila.append(caminho + [v])

        return None

    def dfs(self, inicio, destino):
        todos = []

        def funcao_dfs(atual, caminho, visitados):
            if atual == destino:
                todos.append(caminho.copy())
                return
            for v in self.grafo.get(atual, []):
                if v not in visitados:
                    visitados.add(v)
                    caminho.append(v)
                    funcao_dfs(v, caminho, visitados)
                    caminho.pop()
                    visitados.remove(v)

        funcao_dfs(inicio, [inicio], set([inicio]))
        return todos
    
# testar o dfs
                    

vertices = [
    ("Inglaterra", "Pais de Gales"),
    ("Inglaterra", "Escocia"),
    ("Escocia", "Noruega"),
    ("Pais de Gales", "França"),
    ("Pais de Gales", "Noruega"),
    ("Escocia", "Canada"),
    ("Canada", "Noruega")

]

grafo = Grafo(vertices)
bfs = grafo.bfs("Inglaterra", "Canada")
print(bfs)
caminho = grafo.caminho("França")
print(caminho)
todos = grafo.dfs("Inglaterra", "Noruega")
print(todos)


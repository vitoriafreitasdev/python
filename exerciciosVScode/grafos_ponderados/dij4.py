from collections import defaultdict
import heapq
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = defaultdict(list)

        for v, u, peso in self.vertices:
            self.grafo[v].append((u, peso))

    def dijkstra(self, inicio, fim):
        pilha_minima = [(0, inicio)]
        visitados = set()

        pais = {inicio: None}

        while pilha_minima:
            distancia, no = heapq.heappop(pilha_minima)

            if no in visitados:
                continue

            visitados.add(no)

            if no == fim:
                caminho = []
                while no is not None:
                    caminho.append(no)
                    no = pais[no]
                caminho.reverse()
                return distancia, caminho
            
            for nei, w in self.grafo[no]:
                if nei not in visitados:
                    heapq.heappush(pilha_minima, (distancia + w, nei))

                    if nei not in pais:
                        pais[nei] = no

        return -1
    
    def todos_caminhos(self, inicio, fim):
        todos = []

        def dfs(atual, caminho, visitados):
            if atual == fim:
                todos.append(caminho.copy())
                return
            
            for vizinho, _ in self.grafo.get(atual, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    caminho.append(vizinho)
                    dfs(vizinho, caminho, visitados)
                    visitados.remove(vizinho)
                    caminho.pop()

        dfs(inicio, [inicio], set([inicio]))
        return todos
    

times = [
    ["Paris", "Inglaterra", 30],   # 1 → 2 (2)
    ["Paris", "Italia", 50],   # 1 → 3 (4)
    ["Italia", "Portugal", 70],   # 2 → 4 (7)
    ["Inglaterra", "Grecia", 20],   # 3 → 5 (1)
    ["Grecia", "Portugal", 20]    # 4 → 5 (3)
]
grafo = Grafo(times)
dist, path = grafo.dijkstra("Paris", "Portugal")
todos = grafo.todos_caminhos("Paris", "Portugal")
print("Todos caminhos possíveis: ", todos)
print("Distância mínima:", dist)
print("Caminho:", path)

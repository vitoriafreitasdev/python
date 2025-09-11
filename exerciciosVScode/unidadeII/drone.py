
from collections import deque

class MapaCampus:
    def __init__(self):
        self.grafo = {}  # dicionário: vértice -> lista de vizinhos
    
    def adicionar_aresta(self, origem, destino):
        self.grafo.setdefault(origem, []).append(destino)
        self.grafo.setdefault(destino, []).append(origem)
    
    def bfs_caminho(self, origem, destino):
        visitados = set([origem])
        fila = deque([[origem]])
        while fila:
            caminho = fila.popleft() # aqui sao os que ainda nao foram processados 
            ultimo = caminho[-1]

            if ultimo == destino:
                return caminho 
            for vizinho in self.grafo.get(ultimo, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    
                    fila.append(caminho + [vizinho])
                    print("fila: ",fila)
                    print("visitados: ", visitados)
        return None  # sem rota
    
    def dfs_todos_caminhos(self, origem, destino):
        todos = []
        
        def dfs(atual, caminho, visitados):
            if atual == destino:
                todos.append(caminho.copy())
                return
            for vizinho in self.grafo.get(atual, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    caminho.append(vizinho)
                    dfs(vizinho, caminho, visitados)
                    caminho.pop()
                    visitados.remove(vizinho)
        
        dfs(origem, [origem], set([origem]))
        return todos
    

def principal():
    mapa = MapaCampus()
    corredores = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"),
        ("C", "E"), ("D", "F"), ("E", "F"), ("F", "G")
    ]
    for u, v in corredores:
        mapa.adicionar_aresta(u, v)
    
    partida, destino = "A", "G"
    caminho_minimo = mapa.bfs_caminho(partida, destino)
    print(f"Caminho mínimo entre {partida} e {destino}: {caminho_minimo}")
    
    todos_caminhos = mapa.dfs_todos_caminhos(partida, destino)
    print(f"\nTotal de rotas alternativas encontradas: {len(todos_caminhos)}")
    for rota in todos_caminhos:
        print(rota)

if __name__ == "__main__":
    principal()
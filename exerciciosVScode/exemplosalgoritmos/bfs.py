from collections import deque

def bfs_caminho_minimo(grafo, inicio, objetivo):
    # Fila para a busca
    fila = deque([[inicio]])  # começa com o caminho contendo apenas o nó inicial
    visitados = set([inicio]) # conjunto de nós já visitados

    while fila:
        caminho = fila.popleft()  # pega o primeiro caminho da fila
        nodo = caminho[-1]        # último nó do caminho

        if nodo == objetivo:
            return caminho  # encontramos o caminho mínimo!

        for vizinho in grafo[nodo]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho)   # copia o caminho atual
                novo_caminho.append(vizinho)   # adiciona o vizinho
                fila.append(novo_caminho)

    return None  # se não encontrar caminho

# Exemplo de grafo não ponderado (usando lista de adjacência)
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print("Caminho mínimo de A até F:", bfs_caminho_minimo(grafo, "A", "F"))

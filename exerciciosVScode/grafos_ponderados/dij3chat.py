from collections import defaultdict
import heapq

def shortestPath(times, n, start, dest):
    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append((v, time))

    min_heap = [(0, start)]  # (distância acumulada, nó atual)
    visited = set()
    parent = {start: None}   # para reconstruir o caminho

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        # Se chegamos no destino, reconstruímos o caminho
        if node == dest:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return dist, path

        for nei, w in graph[node]:
            if nei not in visited:
                heapq.heappush(min_heap, (dist + w, nei))
                if nei not in parent:  # só registra o primeiro caminho (menor custo garantido pelo heap)
                    parent[nei] = node

    # Se não encontrou caminho até o destino
    return -1, []


# Exemplo
times = [
    [1, 2, 2],   # 1 → 2 (2)
    [1, 3, 4],   # 1 → 3 (4)
    [2, 4, 7],   # 2 → 4 (7)
    [3, 5, 1],   # 3 → 5 (1)
    [4, 5, 3]    # 4 → 5 (3)
]

dist, path = shortestPath(times, 5, 1, 4)
print("Distância mínima:", dist)
print("Caminho:", path)

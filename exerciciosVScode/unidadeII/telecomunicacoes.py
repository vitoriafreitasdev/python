from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple, Iterable


class Rede:
    def __init__(self):
        self.adj: Dict[str, List[str]] = defaultdict(list)
        self.congestionados: Set[frozenset] = set()

    def adicionar_enlace(self, u: str, v: str):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remover_enlace(self, u: str, v: str):
        self.adj[u] = [n for n in self.adj[u] if n != v]
        self.adj[v] = [n for n in self.adj[v] if n != u]
        self.congestionados.discard(frozenset({u, v}))

    def marcar_congestionado(self, u: str, v: str):
        self.congestionados.add(frozenset({u, v}))

    def bfs_menor_caminho(self, origem: str, destino: str) -> List[str]:
        fila = deque([[origem]])
        visit = {origem}
        while fila:
            caminho = fila.popleft()
            ultimo = caminho[-1]
            if ultimo == destino:
                return caminho
            for viz in self.adj[ultimo]:
                if viz not in visit:
                    visit.add(viz)
                    fila.append(caminho + [viz])
        return []

    def dfs_rotas_limitadas(self, origem: str, destino: str, limite: int) -> Iterable[List[str]]:
        visit = {origem}
        caminho = [origem]

        def dfs(atual: str):
            if len(caminho) - 1 > limite:
                return
            if atual == destino and len(caminho) - 1 == limite:
                yield list(caminho)
                return
            for viz in self.adj[atual]:
                if viz not in visit:
                    visit.add(viz)
                    caminho.append(viz)
                    yield from dfs(viz)
                    caminho.pop()
                    visit.remove(viz)

        yield from dfs(origem)

    def rota_mais_descongestionada(self, rotas: Iterable[List[str]]) -> Tuple[List[str], int]:
        def contar_cong(rota):
            return sum(frozenset({rota[i], rota[i+1]}) in self.congestionados
                       for i in range(len(rota)-1))

        return min(((rota, contar_cong(rota)) for rota in rotas), key=lambda t: t[1])


def principal():
    rede = Rede()
    enlaces = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "E"),
               ("E", "F"), ("F", "D"), ("B", "E"), ("C", "F")]
    
    for u, v in enlaces:
        rede.adicionar_enlace(u, v)

    # marca dois enlaces como congestionados
    rede.marcar_congestionado("B", "C")
    rede.marcar_congestionado("C", "D")

    origem, destino = "A", "D"
    rota_min = rede.bfs_menor_caminho(origem, destino)
    
    if not rota_min:
        print("Não há rota disponível.")
        return

    saltos = len(rota_min) - 1
    rotas_empate = list(rede.dfs_rotas_limitadas(origem, destino, saltos))
    melhor_rota, cong = rede.rota_mais_descongestionada(rotas_empate)

    print(f"Todas as rotas mínimas em saltos ({saltos}):")
    for r in rotas_empate:
        print(r)
    
    print(f"\nRota escolhida (menos enlaces congestionados = {cong}): {melhor_rota}")

    # simula falha em um enlace crítico
    print("\nFalha no enlace B-E")
    rede.remover_enlace("B", "E")
    nova_rota = rede.bfs_menor_caminho(origem, destino)
    print(f"Nova rota em saltos: {nova_rota or 'indisponível'}")


if __name__ == "__main__":
    principal()
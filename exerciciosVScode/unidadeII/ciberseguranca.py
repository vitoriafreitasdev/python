from __future__ import annotations
from collections import defaultdict, Counter, deque
from dataclasses import dataclass
from statistics import median
from typing import Dict, Iterable, List, Set, Generator, Tuple

@dataclass
class GrafoConexoes:
    adjacencia: Dict[str, Set[str]]
    
    @classmethod
    def a_partir_de_arestas(cls, arestas: Iterable[Tuple[str, str]]) -> GrafoConexoes:
        adj: Dict[str, Set[str]] = defaultdict(set)
        for u, v in arestas:
            adj[u].add(v)
            adj[v].add(u)
        return cls(adj)
    
    def graus(self) -> Counter:
        return Counter({no: len(vizinhos) for no, vizinhos in self.adjacencia.items()})
    
    def dfs_componentes(self) -> Generator[Set[str], None, None]:
        visitados: Set[str] = set()
        
        def dfs(no: str, comp: Set[str]):
            comp.add(no)
            for viz in self.adjacencia[no]:
                if viz not in comp:
                    dfs(viz, comp)
        
        for vertice in self.adjacencia:
            if vertice not in visitados:
                componente: Set[str] = set()
                dfs(vertice, componente)
                visitados |= componente
                yield componente
    
    def bfs_distancia(self, origem: str) -> Dict[str, int]:
        niveis: Dict[str, int] = {origem: 0}
        fila: deque[str] = deque([origem])
        
        while fila:
            atual = fila.popleft()
            for viz in self.adjacencia[atual]:
                if viz not in niveis and (n := niveis[atual] + 1) is not None:
                    niveis[viz] = n
                    fila.append(viz)
        return niveis

def principal():
    registros = [
        ("10.0.0.1", "10.0.0.2"), ("10.0.0.2", "10.0.0.3"),
        ("10.0.0.3", "10.0.0.4"), ("10.0.0.4", "10.0.0.5"),
        ("10.0.0.5", "10.0.0.1"), ("10.0.0.6", "10.0.0.7"),
        ("10.0.0.6", "10.0.0.2"), ("192.168.1.10", "10.0.0.4"),
        ("192.168.1.10", "10.0.0.7"), ("192.168.1.10", "10.0.0.6")
    ]
    
    grafo = GrafoConexoes.a_partir_de_arestas(registros)
    graus = grafo.graus()
    limiar = median(graus.values()) * 10
    suspeitos = {n for n, g in graus.items() if g >= limiar}
    print(f"Nos suspeitos por grau anomalo (limiar {limiar:.0f}): {suspeitos}")
    
    servidores_criticos = {"10.0.0.3", "10.0.0.5"}
    
    for comp in grafo.dfs_componentes():
        if servidores_criticos <= comp:
            distancia_min = min(
                grafo.bfs_distancia(s)[t]
                for s in suspeitos 
                for t in servidores_criticos 
                if t in grafo.bfs_distancia(s)
            ) if suspeitos else float('inf')
            
            if distancia_min <= 3:
                print(f"Componente a isolar: {comp}")
                break
    else:
        print("Nenhum componente critico precisa ser isolado.")

if __name__ == "__main__":
    principal()
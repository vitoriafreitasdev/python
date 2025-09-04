

from __future__ import annotations
import csv
import random
import time
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set
import heapq

@dataclass(frozen=True)
class Aresta:
    origem: str
    destino: str
    peso: float

class GrafoServicos:
    def __init__(self):
        self.adj: Dict[str, List[Aresta]] = {}
        self.arestas: List[Aresta] = []
    
    def adicionar_aresta(self, origem: str, destino: str, peso: float):
        ar = Aresta(origem, destino, peso)
        self.arestas.append(ar)
        self.adj.setdefault(origem, []).append(ar)
        self.adj.setdefault(destino, []).append(Aresta(destino, origem, peso))
    
    def carregar_csv(self, caminho: str):
        with open(caminho, newline="") as arq:
            leitor = csv.DictReader(arq)
            for linha in leitor:
                self.adicionar_aresta(linha["origem"], linha["destino"], float(linha["latencia_ms"]))

    # ---------- Kruskal ----------
    def arvore_minima_kruskal(self) -> Tuple[List[Aresta], float]:
        parent: Dict[str, str] = {}
        rank: Dict[str, int] = {}
        
        def achar(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def unir(u, v):
            ru, rv = achar(u), achar(v)
            if ru == rv:
                return False
            if rank[ru] < rank[rv]:
                parent[ru] = rv
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
            else:
                parent[rv] = ru
                rank[ru] += 1
            return True
        
        for no in self.adj:
            parent[no] = no
            rank[no] = 0
        
        arestas_ord = sorted(self.arestas, key=lambda a: a.peso)
        resultado: List[Aresta] = []
        custo = 0.0
        
        for ar in arestas_ord:
            if unir(ar.origem, ar.destino):
                resultado.append(ar)
                custo += ar.peso
        
        return resultado, custo

    # ---------- Prim ----------
    def arvore_minima_prim(self, inicio: str) -> Tuple[List[Aresta], float]:
        visitado: Set[str] = set([inicio])
        heap: List[Tuple[float, str, str]] = []
        resultado: List[Aresta] = []
        custo = 0.0
        
        for ar in self.adj[inicio]:
            heapq.heappush(heap, (ar.peso, ar.origem, ar.destino))
        
        while heap and len(visitado) < len(self.adj):
            peso, u, v = heapq.heappop(heap)
            if v in visitado:
                continue
            
            visitado.add(v)
            resultado.append(Aresta(u, v, peso))
            custo += peso
            
            for ar in self.adj[v]:
                if ar.destino not in visitado:
                    heapq.heappush(heap, (ar.peso, ar.origem, ar.destino))
        
        return resultado, custo
# --------- Gerador de grafo simulado ----------
def gerar_grafo(n_servicos: int, densidade: float) -> GrafoServicos:
    random.seed(11)
    nomes = [f"S{i:02d}" for i in range(n_servicos)]
    g = GrafoServicos()
    
    for i, u in enumerate(nomes):
        for v in nomes[i+1:]:
            if random.random() < densidade:
                lat = random.uniform(1.0, 20.0)
                g.adicionar_aresta(u, v, lat)
    
    return g

# --------- Demonstração ----------
def principal():
    grafo = gerar_grafo(40, 0.35)
    
    t0 = time.perf_counter()
    arv1, custo1 = grafo.arvore_minima_kruskal()
    kr = time.perf_counter() - t0
    
    t1 = time.perf_counter()
    arv2, custo2 = grafo.arvore_minima_prim("S00")
    pr = time.perf_counter() - t1
    
    print(f"Árvore mínima por Kruskal: custo {custo1:.2f} ms, gerada em {kr*1000:.1f} ms")
    print(f"Árvore mínima por Prim: custo {custo2:.2f} ms, gerada em {pr*1000:.1f} ms")
    
    print("\nPrimeiras dez arestas da solução de Kruskal:")
    for ar in arv1[:10]:
        print(f"{ar.origem} ↔ {ar.destino}: {ar.peso:.2f} ms")

if __name__ == "__main__":
    principal()
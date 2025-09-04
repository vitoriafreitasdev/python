from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
import heapq
import random

@dataclass
class Aresta:
    destino: str
    tempo: float  # segundos
    energia: float  # kWh (pode ser negativa em descida)

class Grafo:
    def __init__(self):
        self.adj: Dict[str, List[Aresta]] = {}
    
    def adicionar_aresta(self, origem: str, destino: str, tempo: float, energia: float):
        self.adj.setdefault(origem, []).append(Aresta(destino, tempo, energia))

    # ---------- Dijkstra ----------
    def dijkstra(self, origem: str, alvo: str) -> Tuple[float, float, List[str]]:
        fila: List[Tuple[float, float, str]] = [(0.0, 0.0, origem)]
        visitado: Dict[str, Tuple[float, float]] = {origem: (0.0, 0.0)}
        ante: Dict[str, str] = {}
        
        while fila:
            tempo_atual, energia_atual, no = heapq.heappop(fila)
            
            if no == alvo:
                caminho = [alvo]
                while caminho[-1] != origem:
                    caminho.append(ante[caminho[-1]])
                return tempo_atual, energia_atual, list(reversed(caminho))
            
            for ar in self.adj.get(no, []):
                t = tempo_atual + ar.tempo
                e = energia_atual + ar.energia
                
                if ar.destino not in visitado or t < visitado[ar.destino][0] or (
                    t == visitado[ar.destino][0] and e < visitado[ar.destino][1]
                ):
                    visitado[ar.destino] = (t, e)
                    ante[ar.destino] = no
                    heapq.heappush(fila, (t, e, ar.destino))
        
        raise ValueError("Alvo inalcançável")

    # ---------- BellmanFord ----------
    def bellman_ford(self, origem: str, alvo: str) -> Tuple[float, float, List[str]]:
        # coleta todos os vértices, inclusive os que só aparecem como destino
        vertices = set(self.adj.keys())
        for edges in self.adj.values():
            for ar in edges:
                vertices.add(ar.destino)
        
        dist_tempo: Dict[str, float] = {v: float("inf") for v in vertices}
        dist_energia: Dict[str, float] = {v: float("inf") for v in vertices}
        ante: Dict[str, str] = {}
        
        dist_tempo[origem] = 0.0
        dist_energia[origem] = 0.0
        
        for _ in range(len(vertices) - 1):
            atualizado = False
            for u in vertices:
                for ar in self.adj.get(u, []):
                    if dist_tempo[u] == float("inf"):
                        continue
                    
                    novo_t = dist_tempo[u] + ar.tempo
                    novo_e = dist_energia[u] + ar.energia
                    
                    if novo_t < dist_tempo[ar.destino] or (
                        novo_t == dist_tempo[ar.destino] and novo_e < dist_energia[ar.destino]
                    ):
                        dist_tempo[ar.destino] = novo_t
                        dist_energia[ar.destino] = novo_e
                        ante[ar.destino] = u
                        atualizado = True
            
            if not atualizado:
                break
        
        # verificação de ciclo de energia negativa
        for u in vertices:
            for ar in self.adj.get(u, []):
                if dist_tempo[u] == float("inf"):
                    continue
                if (
                    dist_tempo[u] + ar.tempo == dist_tempo[ar.destino] and
                    dist_energia[u] + ar.energia < dist_energia[ar.destino]
                ):
                    raise ValueError("Ciclo de energia negativa detectado")
        
        if dist_tempo[alvo] == float("inf"):
            raise ValueError("Alvo inalcançável")
        
        caminho = [alvo]
        while caminho[-1] != origem:
            caminho.append(ante[caminho[-1]])
        return dist_tempo[alvo], dist_energia[alvo], list(reversed(caminho))

# ---------- Gerador de malha ----------
def gerar_malha(g: Grafo, n: int, densidade: float):
    random.seed(7)
    pontos = [f"P{i}" for i in range(n)]
    
    for u in pontos:
        for v in pontos:
            if u != v and random.random() < densidade:
                tempo = random.uniform(50, 400)
                energia = random.uniform(0.2, 2.0)
                if random.random() < 0.05:  # descida
                    energia *= -0.3
                g.adicionar_aresta(u, v, tempo, energia)

# ---------- Demonstração ----------
def principal():
    grafo = Grafo()
    gerar_malha(grafo, 15, 0.25)
    origem, destino = "P0", "P10"
    
    tem_negativo = any(ar.energia < 0 for edges in grafo.adj.values() for ar in edges)
    
    try:
        if tem_negativo:
            tempo, energia, caminho = grafo.bellman_ford(origem, destino)
            print("Algoritmo BellmanFord aplicado devido a pesos negativos.")
        else:
            tempo, energia, caminho = grafo.dijkstra(origem, destino)
            print("Algoritmo Dijkstra aplicado (pesos não negativos).")
        
        print("Caminho:", " → ".join(caminho))
        print(f"Tempo total: {tempo:.1f} s, Energia: {energia:.2f} kWh")
    
    except ValueError as e:
        print("Falha no cálculo de rota:", e)

if __name__ == "__main__":
    principal()
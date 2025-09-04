from __future__ import annotations
import heapq
import random
import time
from collections import deque
from dataclasses import dataclass
from typing import Dict, Tuple, List

# -------- Parâmetros de janela e ranking --------
JANELA_SEG = 240  # quatro minutos
TAMANHO_RANKING = 20
INTERVALO_COTACAO_MS = 120

@dataclass
class RegistroHeap:
    variacao: float  # variação percentual
    ts: float  # timestamp da cotação
    ticker: str  # símbolo do ativo
    vivo: bool  # flag para marcação preguiçosa

class RankingMercado:
    def __init__(self):
        self.heap: List[Tuple[float, int, RegistroHeap]] = []
        self.mapa: Dict[str, RegistroHeap] = {}
        self.deque_precos: deque[Tuple[float, str, float]] = deque()
        self.contador = 0

    def _limpar_expirados(self, agora: float):
        while self.deque_precos and agora - self.deque_precos[0][0] > JANELA_SEG:
            _, ticker, _ = self.deque_precos.popleft()
            antigo = self.mapa.get(ticker)
            if antigo:
                antigo.vivo = False

    def _topo_valido(self):
        while self.heap and not self.heap[0][2].vivo:
            heapq.heappop(self.heap)
        return self.heap[0][2] if self.heap else None

    def atualizar_cotacao(self, ticker: str, preco_abertura: float, preco_atual: float):
        agora = time.time()
        self._limpar_expirados(agora)
        
        variacao = (preco_atual - preco_abertura) / preco_abertura * 100
        reg = RegistroHeap(variacao=variacao, ts=agora, ticker=ticker, vivo=True)
        
        self.deque_precos.append((agora, ticker, preco_abertura))
        self.mapa[ticker] = reg
        
        if len(self.heap) < TAMANHO_RANKING:
            heapq.heappush(self.heap, (-variacao, self.contador, reg))
            self.contador += 1
        else:
            topo = self._topo_valido()
            if topo and variacao > topo.variacao:
                heapq.heappush(self.heap, (-variacao, self.contador, reg))
                self.contador += 1
                topo.vivo = False

    def snapshot(self) -> List[Tuple[str, float]]:
        valido = []
        copia = self.heap.copy()
        
        while copia and len(valido) < TAMANHO_RANKING:
            _, _, reg = heapq.heappop(copia)
            if reg.vivo:
                valido.append((reg.ticker, reg.variacao))
        
        valido.sort(key=lambda x: x[1], reverse=True)
        return valido

# --------- Demonstração simplificada ----------
def principal():
    random.seed(3)
    ranking = RankingMercado()
    tickers = [f"ACAO{i:04d}" for i in range(1, 4001)]
    precos_abertura = {t: random.uniform(10, 300) for t in tickers}
    
    inicio = time.time()
    for passo in range(1000):  # mil ciclos de cotações
        t = random.choice(tickers)
        preco_open = precos_abertura[t]
        preco_now = preco_open * random.uniform(0.95, 1.05)
        ranking.atualizar_cotacao(t, preco_open, preco_now)
        
        if passo % 200 == 0:  # imprime a cada 200 atualizações
            top10 = ranking.snapshot()[:10]
            print(f"\nSnapshot passo {passo} (top 10):")
            for sym, var in top10:
                print(f"{sym}: {var:+.2f}%")
        
        time.sleep(INTERVALO_COTACAO_MS / 1000)  # atraso artificial
    
    tempo_exec = time.time() - inicio
    print(f"\nExecução de demonstração concluída em {tempo_exec:.1f}s.")

if __name__ == "__main__":
    principal()
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Musica:
    id: str
    duracao: int  # segundos
    nota: int  # preferência 0-100

def mochila_playlist(musicas: List[Musica], limite_seg: int) -> Tuple[int, List[Musica]]:
    n = len(musicas)
    # matriz de valores: duas linhas para economia de memória
    dp = [[0] * (limite_seg + 1) for _ in range(2)]
    # matriz booleana que marca inclusão da música na solução
    escolha = [[False] * (limite_seg + 1) for _ in range(n)]
    
    for i in range(n):
        atual = i % 2
        prev = (i - 1) % 2
        dur = musicas[i].duracao
        val = musicas[i].nota
        
        for s in range(limite_seg + 1):
            if dur <= s:
                incluir = val + dp[prev][s - dur]
                nao_incluir = dp[prev][s]
                
                if incluir > nao_incluir:
                    dp[atual][s] = incluir
                    escolha[i][s] = True
                else:
                    dp[atual][s] = nao_incluir
            else:
                dp[atual][s] = dp[prev][s]
    
    # reconstrução do conjunto de músicas
    s = limite_seg
    selecionadas: List[Musica] = []
    
    for i in range(n - 1, -1, -1):
        if escolha[i][s]:
            selecionadas.append(musicas[i])
            s -= musicas[i].duracao
    
    selecionadas.reverse()
    return dp[(n - 1) % 2][limite_seg], selecionadas

# -------- Demonstração --------
def principal():
    catalogo = [
        Musica('Faixa1', 210, 85),
        Musica('Faixa2', 180, 92),
        Musica('Faixa3', 200, 75),
        Musica('Faixa4', 240, 60),
        Musica('Faixa5', 300, 95),
        Musica('Faixa6', 150, 80),
        Musica('Faixa7', 190, 70),
        Musica('Faixa8', 230, 88),
        Musica('Faixa9', 260, 77),
        Musica('Faixa10', 215, 90)
    ]
    
    valor, playlist = mochila_playlist(catalogo, 3600)
    tempo_total = sum(m.duracao for m in playlist)
    
    print(f'Nota agregada: {valor}')
    print(f'Tempo total: {tempo_total//60} min {tempo_total%60} s')
    print('\nPlaylist gerada:')
    
    for m in playlist:
        print(f'{m.id} – {m.duracao//60}:{m.duracao%60:02d} | nota {m.nota}')

if __name__ == '__main__':
    principal()
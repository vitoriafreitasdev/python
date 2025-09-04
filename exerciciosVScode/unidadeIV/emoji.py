

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Perfil:
    nome: str
    reacoes: str  # sequência como string de códigos 'R','C','A'

def lcs_quase_linear(a: str, b: str) -> Tuple[int, str]:
    if len(a) < len(b):  # garante que b seja a menor para poupar memória
        a, b = b, a
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(2)]
    caminho: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        linha_atual = i % 2
        linha_ant = (i - 1) % 2
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[linha_atual][j] = dp[linha_ant][j - 1] + 1
                caminho[i][j] = 1  # diagonal
            else:
                if dp[linha_ant][j] >= dp[linha_atual][j - 1]:
                    dp[linha_atual][j] = dp[linha_ant][j]
                    caminho[i][j] = 2  # cima
                else:
                    dp[linha_atual][j] = dp[linha_atual][j - 1]
                    caminho[i][j] = 3  # esquerda
    
    # reconstrução da subsequência
    lcs_lista: List[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if caminho[i][j] == 1:
            lcs_lista.append(a[i - 1])
            i -= 1
            j -= 1
        elif caminho[i][j] == 2:
            i -= 1
        else:
            j -= 1
    
    return dp[m % 2][n], ''.join(reversed(lcs_lista))

def classificar_amistade(tamanho_lcs: int) -> str:
    if tamanho_lcs > 15:
        return 'super amigos'
    if tamanho_lcs >= 10:
        return 'amigos em ascensão'
    return 'apenas conhecidos'

# -------- Demonstração --------
def principal():
    ana = Perfil('Ana', 'RCAARCRACRACARCRAA')
    beto = Perfil('Beto', 'RRACRACRCRAARCRACA')
    
    tam, seq = lcs_quase_linear(ana.reacoes, beto.reacoes)
    grau = classificar_amistade(tam)
    
    print(f'A subsequência comum mais longa tem {tam} emojis.')
    print(f'Sequência compartilhada: {seq}')
    print(f'Diagnóstico de amizade: {grau}')

if __name__ == '__main__':
    principal()
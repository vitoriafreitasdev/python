from __future__ import annotations
import hashlib
import time
from dataclasses import dataclass
from collections import deque
from typing import Dict, Tuple

JANELA_ALERTA_SEG = 900  # quinze minutos
LIMITE_ALERTA = 50  # ocorrências para disparar alerta
TTL_REGISTRO = 3600  # expirar após uma hora
CAPACIDADE_BUCKETS = 131071  # primo próximo a 2^17 para exemplo

@dataclass
class Registro:
    timestamp: float
    ocorrencias: int
    confiavel: bool

class TabelaAssinaturas:
    def __init__(self):
        self.tabela: Dict[str, Registro] = {}
        self.fila_recent: deque[Tuple[str, float]] = deque()
    
    def _hash_indice(self, chave: str) -> int:
        return hash(chave) % CAPACIDADE_BUCKETS
    
    def _limpar_expirados(self, agora: float):
        while self.fila_recent and agora - self.fila_recent[0][1] > JANELA_ALERTA_SEG:
            chave, t = self.fila_recent.popleft()
            reg = self.tabela.get(chave)
            if reg and agora - reg.timestamp > TTL_REGISTRO:
                del self.tabela[chave]
    
    def registrar_anexo(self, conteudo: bytes) -> Tuple[bool, bool]:
        agora = time.time()
        assinatura = hashlib.sha256(conteudo).hexdigest()
        indice = self._hash_indice(assinatura)  # demonstração didática
        
        reg = self.tabela.get(assinatura)
        if reg:
            reg.ocorrencias += 1
            self.fila_recent.append((assinatura, agora))
            alerta = reg.ocorrencias >= LIMITE_ALERTA
            return reg.confiavel, alerta
        
        novo = Registro(timestamp=agora, ocorrencias=1, confiavel=False)
        self.tabela[assinatura] = novo
        self.fila_recent.append((assinatura, agora))
        self._limpar_expirados(agora)
        return False, False  # primeiro contato, não confiável, sem alerta
    
    def marcar_confiavel(self, assinatura: str):
        reg = self.tabela.get(assinatura)
        if reg:
            reg.confiavel = True

# ---------- Demonstração ----------
def principal():
    verificador = TabelaAssinaturas()
    seguro = b"documento_legitimo"
    malicioso = b"macro_malware"
    
    # registra arquivo confiável conhecido
    verificador.marcar_confiavel(hashlib.sha256(seguro).hexdigest())
    
    # simula fluxo de anexos
    for i in range(55):
        conf, alerta = verificador.registrar_anexo(seguro if i == 0 else malicioso)
        if i in (0, 1, 49, 54):  # imprime quatro amostras
            estado = "confiável" if conf else "desconhecido"
            print(f"Iteração {i:02d}: arquivo {estado}, alerta={alerta}")
    
    # imprime estatísticas finais
    total = len(verificador.tabela)
    print(f"\nRegistros na tabela após fluxo: {total}")
    profund = max((time.time() - r.timestamp) for r in verificador.tabela.values())
    print(f"Tempo máximo de permanência (s): {profund:.1f}")

if __name__ == "__main__":
    principal()
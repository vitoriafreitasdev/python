

from __future__ import annotations
import random, time
from dataclasses import dataclass
from typing import Optional, Tuple, Any

# ---------- Nó da árvore AVL ----------
@dataclass
class NoAVL:
    chave: int
    valor: Any
    esquerda: Optional['NoAVL'] = None
    direita: Optional['NoAVL'] = None
    altura: int = 1

# ---------- Classe do índice ----------
class IndiceAVL:
    def __init__(self):
        self.raiz: Optional[NoAVL] = None
        self.rotacoes = 0
        self.buscas = 0
        self.ns_total_busca = 0

    # ----------- Interface pública -----------
    def inserir(self, chave: int, valor: Any) -> None:
        self.raiz, rot = self._inserir(self.raiz, chave, valor)
        self.rotacoes += rot

    def buscar(self, chave: int) -> Optional[Any]:
        inicio = time.perf_counter_ns()
        no = self._buscar(self.raiz, chave)
        self.ns_total_busca += time.perf_counter_ns() - inicio
        self.buscas += 1
        return no.valor if no else None

    def remover(self, chave: int) -> None:
        self.raiz, rot = self._remover(self.raiz, chave)
        self.rotacoes += rot

    # ---------- Estatísticas ----------
    def profundidade(self) -> int:
        return self.raiz.altura if self.raiz else 0

    def media_rotacoes(self) -> float:
        return self.rotacoes / max(1, self.contagem())

    def tempo_medio_busca_ms(self) -> float:
        return (self.ns_total_busca / 1_000_000) / max(1, self.buscas)

    def contagem(self) -> int:
        def contar(no: Optional[NoAVL]) -> int:
            return 0 if not no else 1 + contar(no.esquerda) + contar(no.direita)
        return contar(self.raiz)

    # ---------- Métodos internos ----------
    def _altura(self, no: Optional[NoAVL]) -> int:
        return no.altura if no else 0

    def _balancear(self, no: NoAVL) -> Tuple[NoAVL, int]:
        fator = self._altura(no.esquerda) - self._altura(no.direita)
        rot = 0
        
        # Rotação esquerda
        if fator > 1 and self._altura(no.esquerda.esquerda) >= self._altura(no.esquerda.direita):
            no, rot = self._rot_dir(no), 1
        # Rotação esquerda-direita
        elif fator > 1:
            no.esquerda = self._rot_esq(no.esquerda)
            no, rot = self._rot_dir(no), 2
        # Rotação direita
        elif fator < -1 and self._altura(no.direita.direita) >= self._altura(no.direita.esquerda):
            no, rot = self._rot_esq(no), 1
        # Rotação direita-esquerda
        elif fator < -1:
            no.direita = self._rot_dir(no.direita)
            no, rot = self._rot_esq(no), 2
        return no, rot

    def _atualizar_altura(self, no: NoAVL):
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

    # ---------- Inserção ----------
    def _inserir(self, no: Optional[NoAVL], chave: int, valor: Any) -> Tuple[NoAVL, int]:
        if not no:
            return NoAVL(chave, valor), 0
        
        if chave < no.chave:
            no.esquerda, rot = self._inserir(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita, rot = self._inserir(no.direita, chave, valor)
        else:  # atualiza valor
            no.valor, rot = valor, 0
            return no, rot
        
        self._atualizar_altura(no)
        no, balance_rot = self._balancear(no)
        return no, rot + balance_rot

    # ---------- Busca ----------
    def _buscar(self, no: Optional[NoAVL], chave: int) -> Optional[NoAVL]:
        while no:
            if chave == no.chave:
                return no
            no = no.esquerda if chave < no.chave else no.direita
        return None

    # ---------- Remoção ----------
    def _remover(self, no: Optional[NoAVL], chave: int) -> Tuple[Optional[NoAVL], int]:
        if not no:
            return None, 0
        
        if chave < no.chave:
            no.esquerda, rot = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita, rot = self._remover(no.direita, chave)
        else:  # chave encontrada
            if not no.esquerda or not no.direita:
                return (no.esquerda or no.direita), 0
            sucessor = self._minimo(no.direita)
            no.chave, no.valor = sucessor.chave, sucessor.valor
            no.direita, rot = self._remover(no.direita, sucessor.chave)
        
        if not no:
            return None, rot
        
        self._atualizar_altura(no)
        no, bal_rot = self._balancear(no)
        return no, rot + bal_rot

    def _minimo(self, no: NoAVL) -> NoAVL:
        while no.esquerda:
            no = no.esquerda
        return no

    # ---------- Rotações ----------
    def _rot_esq(self, z: NoAVL) -> NoAVL:
        y, z.direita = z.direita, z.direita.esquerda
        y.esquerda = z
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

    def _rot_dir(self, z: NoAVL) -> NoAVL:
        y, z.esquerda = z.esquerda, z.esquerda.direita
        y.direita = z
        self._atualizar_altura(z)
        self._atualizar_altura(y)
        return y

# ---------- Demonstração ----------
def principal():
    indice = IndiceAVL()
    total = 100_000
    random.seed(1)
    
    # Insere cem mil títulos
    for _ in range(total):
        chave = random.randint(1, 2_000_000_000)
        indice.inserir(chave, f"título_{chave}")
    
    print(f"Profundidade após {total:,} inserções: {indice.profundidade()}")
    print(f"Rotações médias por inserção: {indice.media_rotacoes():.3f}")
    
    # Executa mil buscas
    chaves_busca = random.sample(range(1, 2_000_000_000), 1_000)
    for k in chaves_busca:
        indice.buscar(k)
    
    print(f"Tempo médio de busca: {indice.tempo_medio_busca_ms():.3f} ms")
    
    # Remove mil chaves aleatórias
    for k in chaves_busca[:500]:
        indice.remover(k)
    
    print(f"Profundidade após remoções: {indice.profundidade()}")
    print(f"Total de rotações: {indice.rotacoes}")

if __name__ == "__main__":
    principal()
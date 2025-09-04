from __future__ import annotations
from bisect import bisect_left
from dataclasses import dataclass
import random
import csv, os, time
from typing import List, Tuple, Dict

TAMANHO_QUENTE = 5_000  # cache em memória
TAMANHO_TOTAL = 100_000  # catálogo completo

@dataclass(order=True)
class Produto:
    sku: int
    preco: float

def gerar_catalogo(n: int) -> List[Produto]:
    random.seed(42)
    return [Produto(random.randint(1_000_000, 9_999_999),
                   round(random.uniform(10, 5000), 2))
            for _ in range(n)]

def salvar_ordenado(produtos: List[Produto], caminho: str):
    produtos_ordenados = sorted(produtos)  # ordena por sku
    with open(caminho, "w", newline="") as arq:
        w = csv.writer(arq)
        for p in produtos_ordenados:
            w.writerow([p.sku, p.preco])
    return produtos_ordenados  # devolve lista

def pesquisa_linear(lista: List[Produto], alvo: int) -> Dict:
    comparacoes = 0
    for p in lista:
        comparacoes += 1
        if p.sku == alvo:
            return {"encontrado": True, "preco": p.preco,
                    "comparacoes": comparacoes}
    return {"encontrado": False, "comparacoes": comparacoes}

def pesquisa_binaria(lista_ord: List[Produto], alvo: int) -> Dict:
    comparacoes = 1
    idx = bisect_left(lista_ord, Produto(alvo, 0.0)) # faz a pesquisa binaria 
    if idx < len(lista_ord) and lista_ord[idx].sku == alvo:
        return {"encontrado": True, "preco": lista_ord[idx].preco,
                "comparacoes": comparacoes}
    return {"encontrado": False, "comparacoes": comparacoes}

# com a pesquisa binaria verdadeira, que nao ta no livro texto

def pesquisa_binaria_real(lista_ord: List[Produto], alvo: int) -> Dict:
    comparacoes = 0
    esquerda, direita = 0, len(lista_ord) - 1
    
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        
        if lista_ord[meio].sku == alvo:
            return {"encontrado": True, "preco": lista_ord[meio].preco,
                    "comparacoes": comparacoes}
        elif lista_ord[meio].sku < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return {"encontrado": False, "comparacoes": comparacoes}

def carregar_catalogo_csv(caminho: str) -> List[Produto]:
    with open(caminho, newline="") as arq:
        return [Produto(int(row[0]), float(row[1])) for row in csv.reader(arq)]

def localizar_produto(sku_busca: int,
                     cache: List[Produto],
                     catalogo_ordenado: List[Produto]) -> Dict:
    t0 = time.perf_counter()
    res_cache = pesquisa_linear(cache, sku_busca)
    if res_cache["encontrado"]:
        res_cache["fonte"] = "cache"
        res_cache["tempo_ms"] = (time.perf_counter() - t0) * 1000
        return res_cache
    
    res_full = pesquisa_binaria(catalogo_ordenado, sku_busca)
    res_full["fonte"] = "catálogo"
    res_full["tempo_ms"] = (time.perf_counter() - t0) * 1000
    return res_full

# ---------- Demonstração ----------
def principal():
    # gera catálogo completo e salva em disco simulando banco
    todos = gerar_catalogo(TAMANHO_TOTAL)
    caminho_csv = "catalogo.csv"
    produtos_ordenados = salvar_ordenado(todos, caminho_csv)
    
    # cache quente: simplesmente as primeiras 5 000 posições
    cache_quente = produtos_ordenados[:TAMANHO_QUENTE]
    
    # Escolhe SKUs para teste: um no cache, um fora, um inexistente
    sku_cache = cache_quente[123].sku
    sku_disc = produtos_ordenados[80_000].sku
    sku_inexistente = 999_999_999
    
    for sku in (sku_cache, sku_disc, sku_inexistente):
        resultado = localizar_produto(sku, cache_quente, produtos_ordenados)
        print(f"Busca SKU {sku}: {resultado}")
    
    # limpeza
    os.remove(caminho_csv)

if __name__ == "__main__":
    principal()
from __future__ import annotations
from typing import List, Callable, Generator
from textwrap import indent

# Decorador para contar comparações e trocas
def estatisticas(func: Callable[[List[int]], Generator[tuple[List[int], int, int], None, None]]):
    def wrapper(lista: List[int]) -> List[int]:
        comparacoes = trocas = 0
        for estado, c, t in func(lista.copy()):
            comparacoes += c
            trocas += t
            print(indent(str(estado), " "))
            print(f"Comparações: {comparacoes}, Trocas: {trocas}\n")
        return lista
    return wrapper

@estatisticas
def bubble_sort_passo(lista: List[int]) -> Generator[tuple[List[int], int, int], None, None]:
    n = len(lista)
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            yield lista, 1, 0
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                yield lista, 0, 1
        if not trocou:
            break
    yield lista, 0, 0

@estatisticas
def insertion_sort_passo(lista: List[int]) -> Generator[tuple[List[int], int, int], None, None]:
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            yield lista, 1, 0
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        yield lista, 1, 1  # última comparação e inserção
    yield lista, 0, 0

@estatisticas
def selection_sort_passo(lista: List[int]) -> Generator[tuple[List[int], int, int], None, None]:
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            yield lista, 1, 0
            if lista[j] < lista[min_idx]:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            yield lista, 0, 1
    yield lista, 0, 0

def principal():
    dados_originais = [18, 5, 12, 7, 1, 9, 3, 15]
    print("Bubble Sort:")
    bubble_sort_passo(dados_originais)
    
    dados_parciais = [1, 3, 5, 7, 12, 9, 15, 18]  # quase ordenado
    print("Insertion Sort:")
    insertion_sort_passo(dados_parciais)
    
    dados_auditoria = [9, 4, 16, 2, 11, 6, 3, 14]
    print("Selection Sort:")
    selection_sort_passo(dados_auditoria)

if __name__ == "__main__":
    principal()
from __future__ import annotations
from collections import deque
from typing import List

# -------- Algoritmos de ordenação simples --------
def bubble_sort(arr: List[float]) -> None:
    n = len(arr)
    for i in range(n - 1):
        
        trocou = False
        for j in range(n - 1 - i):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:  # já ordenado
            break

def insertion_sort(arr: List[float]) -> None:
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def selection_sort(arr: List[float]) -> None:
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# -------- Buffer circular e lógica de escolha --------
BUFFER_MAX = 50  # capacidade máxima para auditoria
BUFFER_PADRAO = 10  # tamanho regular de operação
buffer = deque(maxlen=BUFFER_MAX)

def inserir_leitura(valor: float) -> None:
    buffer.append(valor)

def ordenar_e_mostrar() -> None:
    lista = list(buffer)  # snapshot
    n = len(lista)
    if n < BUFFER_PADRAO:
        bubble_sort(lista)
        metodo = "Bubble Sort"
    elif n == BUFFER_PADRAO:
        insertion_sort(lista)
        metodo = "Insertion Sort"
    else:
        selection_sort(lista)
        metodo = "Selection Sort"
    
    mediana = lista[n // 2] if n % 2 else (lista[n // 2 - 1] + lista[n // 2]) / 2
    print(f"Método utilizado: {metodo}")
    print(f"Buffer ordenado: {lista}")
    print(f"Mediana: {mediana:.2f}°C\n")

# ---------- Demonstração ----------
def principal():
    leituras = [23.5, 24.1, 22.9, 23.0, 24.3, 23.8, 24.0,
                23.2, 23.7, 24.4, 25.0, 24.6, 24.8]  # 13 amostras
    
    for temp in leituras:
        inserir_leitura(temp)
    
    ordenar_e_mostrar()
    
    # Simula mais leituras até completar 50 para auditoria
    for temp in [24.1 + i*0.02 for i in range(37)]:
        inserir_leitura(temp)
    
    ordenar_e_mostrar()

if __name__ == "__main__":
    principal()
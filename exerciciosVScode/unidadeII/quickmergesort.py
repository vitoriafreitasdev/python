

from __future__ import annotations
import heapq, os, random, tempfile, time, tracemalloc
from array import array
from typing import List, Iterator

# -------- Geração de dados compactados --------
def gerar_timestamps(qtd: int) -> array:
    ar = array("L")
    bits32 = random.getrandbits
    for _ in range(qtd):
        ar.append(bits32(32))
    return ar

# -------- Quick Sort otimizado --------
def quick_sort(arr: List[int], inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    while inicio < fim:
        if fim - inicio < 32:  # fallback
            #Se a partição é pequena, usa insertion sort e termina o trabalho
            insertion(arr, inicio, fim)
            return
        pivo = mediana_tres(arr, inicio, fim)
        i, j = inicio, fim
        while i <= j:
            while arr[i] < pivo:
                i += 1
            while arr[j] > pivo:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
        # recursão na menor partição para limitar profundidade
        if j - inicio < fim - i:
            quick_sort(arr, inicio, j)
            inicio = i
        else:
            quick_sort(arr, i, fim)
            fim = j

def mediana_tres(a: List[int], i: int, j: int) -> int:
    k = (i + j) // 2
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    if a[k] > a[j]:
        a[k], a[j] = a[j], a[k]
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    return a[k]

def insertion(a: List[int], i: int, j: int):
    for x in range(i + 1, j + 1):
        chave, y = a[x], x - 1
        while y >= i and a[y] > chave:
            a[y + 1] = a[y]
            y -= 1
        a[y + 1] = chave

# -------- Merge Sort externo com heapq.merge --------
CHUNK = 500_000

def escrever_chunks(dados: array) -> List[str]:
    arquivos = []
    for i in range(0, len(dados), CHUNK):
        parte = sorted(dados[i:i + CHUNK])
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(array("L", parte).tobytes())
        tmp.close()
        arquivos.append(tmp.name)
    return arquivos

def ler_chunk(caminho: str) -> Iterator[int]:
    with open(caminho, "rb") as f:
        bloco = array("L")
        bloco.frombytes(f.read())
        for valor in bloco:
            yield valor

def merge_externo(arquivos: List[str], destino: str):
    iteradores = [ler_chunk(p) for p in arquivos]
    with open(destino, "wb") as out:
        for valor in heapq.merge(*iteradores):
            out.write(array("L", [valor]).tobytes())
    for p in arquivos:
        os.remove(p)

# -------- Orquestração e métricas --------
def medir(func, *args, **kwargs):
    tracemalloc.start()
    ini = time.perf_counter()
    resultado = func(*args, **kwargs)
    dur = time.perf_counter() - ini
    pico = tracemalloc.get_traced_memory()[1] / 1_048_576
    tracemalloc.stop()
    return resultado, dur, pico

def principal():
    registros = 10_000_00  # 10 milhões para protótipo
    print(f"Gerando {registros:,} timestamps...")
    dados, t_gen, mem_gen = medir(gerar_timestamps, registros)
    print(f"Geração em {t_gen:.2f}s, pico {mem_gen:.1f} MiB\n")

    # Quick Sort
    lista_quick = list(dados)
    print("Quick Sort (mediana de três)...")
    _, t_qs, mem_qs = medir(quick_sort, lista_quick)
    print(f"Tempo: {t_qs:.2f}s, Pico RAM: {mem_qs:.1f} MiB\n")

    # Merge Sort externo
    print("Merge Sort externo em chunks...")
    arqs, t_split, mem_split = medir(escrever_chunks, dados)
    merge_destino = tempfile.NamedTemporaryFile(delete=False).name
    _, t_merge, mem_merge = medir(merge_externo, arqs, merge_destino)
    tempo_total_merge = t_split + t_merge
    pico_merge = max(mem_split, mem_merge)
    print(f"Tempo total: {tempo_total_merge:.2f}s, Pico RAM: {pico_merge:.1f} MiB")
    print(f"Arquivo mesclado armazenado em {merge_destino}")

if __name__ == "__main__":
    principal()
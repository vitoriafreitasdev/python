from __future__ import annotations
from collections import deque
from typing import List
# hash_table1 = {}
# nomes = ["vitoria", "joao", "marquesa", "juaria"]
# hash_table1["nomes"] = []
# hash_table1["nomes"] += nomes 

# print(hash_table1["nomes"].index("marquesa"))

# mercado_hash = {}
# mercado_hash["abacate"] = 2.12

# print(mercado_hash["abacate"])

# def encontrar_posicao(hash_table, chave, nome):
#     print(hash_table[chave].index(nome))
# encontrar_posicao(hash_table1, "nomes", "joao")
# hash_table = {}
# nomes = ["vitoria", "joao", "marquesa", "juaria"]
# idades = [25, 30, 45, 22]
# alturas = [1.65, 1.80, 1.70, 1.60]
# profissoes = ["engenheira", "medico", "empresaria", "estudante"]

# hash_table["pessoas"] = []
# for i in range(len(nomes)):
#     pessoa = {
#         "nome": nomes[i],
#         "idade": idades[i],
#         "altura": alturas[i],
#         "profissao": profissoes[i]
#     }
#     hash_table["pessoas"].append(pessoa)
# def encontrar_pessoa_por_nome(hash_table, nome_procurado):
#     for pessoa in hash_table["pessoas"]:
#         if pessoa["nome"] == nome_procurado:
#             return pessoa
#     return None
# print(hash_table["pessoas"])
# print(encontrar_pessoa_por_nome(hash_table, "vitoria"))


from typing import List

def bubble_sort(arr: List[float]) -> List[float]:
    n = len(arr)
    
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:  # já ordenado
            break
    
    return arr  # Retorna a lista ordenada

# Teste
lista = [10, 34, 4, 3, 1, 11]
lista_ordenada = bubble_sort(lista)
print(lista_ordenada)  # Output: [1, 3, 4, 10, 11, 34]
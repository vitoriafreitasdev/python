
hash_table1 = {}
nomes = ["vitoria", "joao", "marquesa", "juaria"]
hash_table1["nomes"] = []
hash_table1["nomes"] += nomes 

print(hash_table1["nomes"].index("marquesa"))

mercado_hash = {}
mercado_hash["abacate"] = 2.12

print(mercado_hash["abacate"])

def encontrar_posicao(hash_table, chave, nome):
    print(hash_table[chave].index(nome))
encontrar_posicao(hash_table1, "nomes", "joao")
hash_table = {}
nomes = ["vitoria", "joao", "marquesa", "juaria"]
idades = [25, 30, 45, 22]
alturas = [1.65, 1.80, 1.70, 1.60]
profissoes = ["engenheira", "medico", "empresaria", "estudante"]

hash_table["pessoas"] = []
for i in range(len(nomes)):
    pessoa = {
        "nome": nomes[i],
        "idade": idades[i],
        "altura": alturas[i],
        "profissao": profissoes[i]
    }
    hash_table["pessoas"].append(pessoa)
def encontrar_pessoa_por_nome(hash_table, nome_procurado):
    for pessoa in hash_table["pessoas"]:
        if pessoa["nome"] == nome_procurado:
            return pessoa
    return None
print(hash_table["pessoas"])
print(encontrar_pessoa_por_nome(hash_table, "vitoria"))

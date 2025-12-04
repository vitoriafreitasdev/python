objetos = [
    {
    "nome": "vitoria",
    "idade": 22
    },
    {
    "nome": "joao",
    "idade": 30
    },
    {
    "nome": "letica",
    "idade": 18
    },
]

for objeto in objetos:
    print(objeto["idade"])

objeto2 = {
    1: {
    "nome": "vitoria",
    "idade": 22
    },
    2: {
    "nome": "joao",
    "idade": 30
    },
    3 : {
    "nome": "letica",
    "idade": 18
    }
}



# for i in range(1, len(objeto2) + 1):
#     print(objeto2[i]["nome"])
#     print(objeto2[i]["idade"])

for pessoa in objeto2.values():
    print(pessoa["nome"])
    print(pessoa["idade"])

for chave, pessoa in objeto2.items():
    print(f"ID: {chave}")
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
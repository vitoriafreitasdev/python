from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 3},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 2},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 6},
}



@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_vendas}")
def pegar_vendas(id_vendas: int):
    if id_vendas in vendas:
        return vendas[id_vendas]
    else:
        return {"Erro": "ID venda inexistente"}

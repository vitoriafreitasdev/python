
"""

rama quer trocar o seu livro de pianos em uma piano de verdade, pelo caminho mais barato

livro 5 => lp raro
livro 0 => poster
lp raro 15 => baixo 
lp raro 20 =>  bateria 
poster 35 => bateria
poster 30 => baixo
baixo 20 => piano
bateria 10 => piano 


"""

from collections import defaultdict

class GrafoPonderado:
    def __init__(self, vertices_arestas):
        self.grafo = defaultdict(list)
        for inicio, fim, peso in vertices_arestas:
            self.grafo[inicio].append((fim, peso))



    def print_grafo(self):
        print(self.grafo.keys())
        print(self.grafo.values())
        for keys, values in self.grafo.items():
            print(f"{keys} - {values}")

    def dijkstra(self, inicio, fim):
        # junta todos os nós (origem + destino)
        todos_nos = set(self.grafo.keys())
        print("todos nos: ",todos_nos)
        for vizinhos in self.grafo.values():
            for v, _ in vizinhos:
                todos_nos.add(v)
        print("todos nos: ",todos_nos)
        # inicializa custos
        custos = {no: float("inf") for no in todos_nos}
        custos[inicio] = 0
        print("custos[inicio]: ",custos[inicio])

        pais = {inicio: None}
        print("pais: ",pais)
        processados = set()

        def achar_custo_mais_baixo():
            custo_mais_baixo = float("inf")
            no_custo_mais_baixo = None 
            for no in custos:
                if custos[no] < custo_mais_baixo and no not in processados:
                    custo_mais_baixo = custos[no]
                    no_custo_mais_baixo = no 
            return no_custo_mais_baixo

        no = achar_custo_mais_baixo()
        while no is not None:
            custo = custos[no]
            print(f"\nProcessando nó: {no}, custo atual: {custo}")
            for vizinho, peso in self.grafo[no]:
                novo_custo = custo + peso
                if novo_custo < custos[vizinho]:
                    print(f"  Atualizando custo de {vizinho}: {custos[vizinho]} -> {novo_custo}")
                    custos[vizinho] = novo_custo
                    pais[vizinho] = no
            processados.add(no)
            print("  Custos atuais:", custos)
            no = achar_custo_mais_baixo()

        # reconstruir caminho
        caminho = []
        n = fim

        if custos[fim] == float("inf"):
            return None, float("inf")
        while n is not None:
            caminho.append(n)
            n = pais.get(n)
        caminho.reverse()

        return caminho, custos[fim]


vertices = [
    ("Livro", "LP", 5),           
    ("Livro", "Poster", 0),    
    ("LP", "Baixo", 15),             
    ("LP", "Bateria", 20),             
    ("Poster", "Baixo", 30),             
    ("Poster", "Bateria", 35),   
    ("Baixo", "Piano", 20),             
    ("Bateria", "Piano", 10),             
]

grafo = GrafoPonderado(vertices)
grafo.print_grafo()

caminho, custo = grafo.dijkstra("Livro", "Piano")
print("\nCaminho mais barato:", caminho)
print("Custo total:", custo)

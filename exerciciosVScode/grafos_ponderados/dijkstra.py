"""

rama quer trocar o seu livro de pianos em uma piano de vdd

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
from collections import deque

class GrafoPonderado:
    def __init__(self, vertices_arestas):
        """
        vertices_arestas: lista de tuplas (inicio, fim, peso)
        """
        self.grafo = defaultdict(list)
        
        for inicio, fim, peso in vertices_arestas:
            self.grafo[inicio].append((fim, peso))
            # Para grafos não direcionados, adicione também:
            # self.grafo[fim].append((inicio, peso))
    def adicionar_aresta(self, inicio, fim, peso):
        """Adiciona uma aresta com peso"""
        self.grafo[inicio].append((fim, peso))
        
paises_com_pesos = [
    ("Inglaterra", "França", 344),           # km entre Londres e Paris
    ("Inglaterra", "País de Gales", 212),    # km entre Londres e Cardiff
    ("França", "Itália", 1106),              # km entre Paris e Roma
    ("França", "Alemanha", 878),             # km entre Paris e Berlim
    ("Itália", "Grécia", 1048),              # km entre Roma e Atenas
    ("Alemanha", "Noruega", 1311),           # km entre Berlim e Oslo
    ("Grécia", "Noruega", 2868)              # km entre Atenas e Oslo
]
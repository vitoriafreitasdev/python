class Arvore:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
    
    def __str__(self):
        return str(self.valor)
    

A = Arvore(1)
B = Arvore(2)
C = Arvore(3)
D = Arvore(4)
E = Arvore(5)
F = Arvore(6)
G = Arvore(7)
H = Arvore(8)

A.esquerda = B
A.direita = C
B.esquerda = E 
B.direita = F
C.esquerda = G 
C.direita = H  
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

# dfs 
todos = []

def dfs(node, todo_nos):
    if not node:
        return False
    
    todo_nos.append(node.valor)
    dfs(node.esquerda, todo_nos)
    dfs(node.direita, todo_nos)

dfs(A, todos)
print(todos)

from collections import deque

def bfs(node, alvo):
    if not node:
        return False 
    
    lista = deque([node])
    while lista:
        atual = lista.popleft()
        if atual.valor == alvo:
            return atual.valor 

        if atual.esquerda:
            lista.append(atual.esquerda)   
        
        if atual.direita:
            lista.append(atual.direita)
    return None


print(bfs(A, 2))
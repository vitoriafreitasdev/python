v = 4
A = [[0, 1], [1, 2], [1, 3], [2, 3]]

M = []

print("Grafo com matriz")

for i in range(v):
    M.append([0] * v)


for u, v in A:
    M[u][v] = 1
    M[v][u] = 1

for i in range(4):
    for j in range(4):
        print(M[i][j], end=" ")
    print()


## 
print("Grafo com lista")
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    D[v].append(u)
print(D)

print("DFS")

def dfs(node):
    print(node)
    for node in D[node]:
        if node not in seen:
            seen.add(node)
            dfs(node)
    

node = 0
seen = set()
dfs(node)

print("Iterative dfs")
source = 0
visites = set()
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for node in D[node]:
        if node not in visites:
            visites.add(node)
            stack.append(node)

            
print("bfs")

from collections import deque

queue = deque() 

source = 0
seen = set()
seen.add(source)
queue.append(source)

while queue:
    node = queue.popleft()
    print(node)
    for node in D[node]:
        if node not in seen:
            seen.add(node)
            queue.append(node)

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f'Node({self.value})'
    
    def display(self):
        con = [node.value for node in self.neighbors]
        return f'{self.value} is connect to {con}'
    

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(A.display())
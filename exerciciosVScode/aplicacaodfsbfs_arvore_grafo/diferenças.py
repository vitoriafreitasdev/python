# dfs 
#arvore binaria
def dfs_tree(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return dfs_tree(node.left, target) or dfs_tree(node.right, target)
#grafo
def dfs_graph(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_graph(graph, neighbor, target, visited):
                return True
    return False
#bfs
#arvore binaria
from collections import deque

def bfs_tree(node, target):
    if not node:
        return False
    queue = deque([node])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

# grafo
from collections import deque

def bfs_graph(graph, start, target):
    visited = set([start])
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

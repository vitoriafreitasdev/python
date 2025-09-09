


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

    def __str__(self):
        return str(self.val)
    


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)


A.left = B 
A.right = C 
B.left = D 
B.right = E 
C.left = F

#DFS
print("\nPre-Order\n")

def pre_order(node):

    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

print("\nIn-Order\n")

def in_order(node):
    if not node:
        return

    
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

print("\nPost-Order\n")

def post_order(node):

    if not node:
        return

    
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)


print("\nIterative version:\n")

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)


pre_order_iterative(A)

#bfs
from collections import deque 

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        
        if node.left: q.append(node.left)
        if node.left: q.append(node.left)
    level_order(A)


#check if value exist with dfs, time O(n)

def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True 
    
    return search(node.left, target) or search(node.right, target)


print(search(A, 5))
from collections import deque

def search_bfs(node, target):
    if not node:
        return False
    
    # fila para visitar os nós
    queue = deque([node])
    
    while queue:
        current = queue.popleft()  # retira da frente (FIFO)
        
        if current.val == target:
            return True
        
        # adicionar filhos na fila
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return False


print(search_bfs(A, 5))   # True
print(search_bfs(A, 100)) # False


# binary search tree (BSTs)

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2 
B2.left, B2.right = D2, E2 
C2.left, C2.right = F2, G2 

in_order(A2)

# time: O(log n), space: o(log n)

def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True 
    
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)

print(search_bst(A2, 8))

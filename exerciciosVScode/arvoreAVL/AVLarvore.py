class node:
    def __init__(self, remedio, efeito, colateral, passa):
        # Usar tupla (passa, remedio) como chave
        self.key = (passa, remedio)
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
        self.height = 1
        self.remedio = remedio 
        self.efeito = efeito 
        self.colateral = colateral 
        self.passa = passa


class AVLtree:
    def __init__(self):
        self.root = None

    def insert(self, remedio, efeito, colateral, passa):
        if self.root == None:
            self.root = node(remedio, efeito, colateral, passa)
        else:
            self._insert(remedio, efeito, colateral, passa, self.root)

    def _insert(self, remedio, efeito, colateral, passa, cur_node):
        new_key = (passa, remedio)
        current_key = (cur_node.passa, cur_node.remedio)
        
        if new_key < current_key:
            if cur_node.left_child == None:
                cur_node.left_child = node(remedio, efeito, colateral, passa)
                cur_node.left_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(remedio, efeito, colateral, passa, cur_node.left_child)
        elif new_key > current_key:
            if cur_node.right_child == None:
                cur_node.right_child = node(remedio, efeito, colateral, passa)
                cur_node.right_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(remedio, efeito, colateral, passa, cur_node.right_child)
        else:
            print("Medicamento já existe na árvore!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(f'{cur_node.remedio}: passa={cur_node.passa}, efeito: {cur_node.efeito}, colateral: {cur_node.colateral}, h={cur_node.height}')
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, passa, remedio):
        if self.root != None:
            return self._find((passa, remedio), self.root)
        else:
            return None

    def _find(self, key, cur_node):
        current_key = (cur_node.passa, cur_node.remedio)
        
        if key == current_key:
            return cur_node
        elif key < current_key and cur_node.left_child != None:
            return self._find(key, cur_node.left_child)
        elif key > current_key and cur_node.right_child != None:
            return self._find(key, cur_node.right_child)

    def delete_value(self, passa, remedio):
        return self.delete_node(self.find(passa, remedio))

    def delete_node(self, node):
        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.passa, node.remedio) == None:
            print("Node to be deleted not found in the tree!")
            return None

        # returns the node with min key in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None:
                num_children += 1
            if n.right_child != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # CASE 1 (node has no children)
        if node_children == 0:
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)
            # copy the inorder successor's data to the node formerly
            # holding the data we wished to delete
            node.key = successor.key
            node.passa = successor.passa
            node.remedio = successor.remedio
            node.efeito = successor.efeito
            node.colateral = successor.colateral
            # delete the inorder successor now that its data was
            # copied into the other node
            self.delete_node(successor)
            return

        if node_parent != None:
            # fix the height of the parent of current node
            node_parent.height = 1 + max(
                self.get_height(node_parent.left_child),
                self.get_height(node_parent.right_child),
            )

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    def search(self, passa, remedio):
        if self.root != None:
            return self._search((passa, remedio), self.root)
        else:
            return False

    def _search(self, key, cur_node):
        current_key = (cur_node.passa, cur_node.remedio)
        
        if key == current_key:
            return True
        elif key < current_key and cur_node.left_child != None:
            return self._search(key, cur_node.left_child)
        elif key > current_key and cur_node.right_child != None:
            return self._search(key, cur_node.right_child)
        return False
    
    # AVL functions 
    
    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent == None:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if cur_node == None:
            return

        left_height = self.get_height(cur_node.left_child)
        right_height = self.get_height(cur_node.right_child)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)

        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)

        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)

        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3 != None:
            t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(
            self.get_height(z.left_child),
            self.get_height(z.right_child),
        )
        y.height = 1 + max(
            self.get_height(y.left_child),
            self.get_height(y.right_child),
        )

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2

        if t2 != None:
            t2.parent = z
        y.parent = sub_root
        
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(
            self.get_height(z.left_child),
            self.get_height(z.right_child),
        )
        y.height = 1 + max(
            self.get_height(y.left_child),
            self.get_height(y.right_child),
        )

    def get_height(self, cur_node):
        if cur_node == None:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left_child)
        right = self.get_height(cur_node.right_child)
        return cur_node.left_child if left >= right else cur_node.right_child
    
    ## metodos adicionados pelo deepseak, não pegar
    def find_by_remedio(self, remedio_name):
        """Método adicional para buscar por nome do remédio"""
        if self.root != None:
            return self._find_by_remedio(remedio_name, self.root)
        else:
            return None

    def _find_by_remedio(self, remedio_name, cur_node):
        if cur_node.remedio == remedio_name:
            return cur_node
        result = None
        if cur_node.left_child != None:
            result = self._find_by_remedio(remedio_name, cur_node.left_child)
        if result == None and cur_node.right_child != None:
            result = self._find_by_remedio(remedio_name, cur_node.right_child)
        return result

    def get_all_by_passa(self, passa_value):
        """Retorna todos os nodes com um determinado valor de passa"""
        results = []
        if self.root != None:
            self._get_all_by_passa(passa_value, self.root, results)
        return results

    def _get_all_by_passa(self, passa_value, cur_node, results):
        if cur_node != None:
            if cur_node.passa == passa_value:
                results.append(cur_node)
            self._get_all_by_passa(passa_value, cur_node.left_child, results)
            self._get_all_by_passa(passa_value, cur_node.right_child, results)


# Exemplo de uso
if __name__ == "__main__":
    # Criando a árvore AVL
    avl_tree = AVLtree()

    # Inserindo dados na árvore
    data_to_insert = [
        ('Remedio A', 'eficiente', 'sem colateral', 1),
        ('Remedio B', 'eficiente', 'colateral forte', 0),
        ('Remedio C', 'não eficiente', 'sem colateral', 0),
        ('Remedio D', 'eficiente', 'colateral medio', 1),
    ]

    for remedio, efeito, colateral, passa in data_to_insert:
        avl_tree.insert(remedio, efeito, colateral, passa)

    # Imprimindo a árvore
    print("Árvore AVL completa (ordenada por (passa, remedio)):")
    avl_tree.print_tree()
    print()

    # Buscando valores
    print("Buscando (1, 'Remedio A'):", avl_tree.search(1, 'Remedio A'))
    print("Buscando (0, 'Remedio X'):", avl_tree.search(0, 'Remedio X'))
    print()

    # Encontrando um nó específico por valor
    node = avl_tree.find(0, 'Remedio B')
    if node:
        print(f"Nó encontrado (0, 'Remedio B'): {node.remedio}, {node.efeito}, {node.colateral}")
    print()

    # Buscando por nome do remédio
    remedio_node = avl_tree.find_by_remedio('Remedio A')
    if remedio_node:
        print(f"Remédio encontrado: {remedio_node.remedio}, passa: {remedio_node.passa}")
    print()

    # Buscando todos os remédios com passa=0
    print("Remédios com passa=0:")
    for node in avl_tree.get_all_by_passa(0):
        print(f"  {node.remedio}: {node.efeito}, {node.colateral}")
    print()

    # Testando altura da árvore
    print("Altura da árvore:", avl_tree.height())
    print()

    # Testando deleção
    print("Deletando (0, 'Remedio B')...")
    avl_tree.delete_value(0, 'Remedio B')
    print("Árvore após deleção:")
    avl_tree.print_tree()
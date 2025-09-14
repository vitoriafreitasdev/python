import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split

# vamos começar fazendo a avl tree, vai conter os dados que vão alimentar o ML 
# efetivo = 1 s efetivo, 0 se nao. colateral = 0 se sem colateral, colateral = 1, se tem efeito colateral
# passa = 1, se passa, passa = 0, se nao passa
class No:
    def __init__(self, remedio, efetivo, colateral, passa):
        self.key = (remedio, passa)
        self.remedio = remedio
        self.passa = passa
        self.efetivo = efetivo 
        self.colateral = colateral 
        self.height = 0
        self.parent = None 
        self.left = None 
        self.right = None 

    
class AVLarvore:
    def __init__(self):
        self.root = None 

    def insert(self, remedio, efetivo, colateral, passa):
        if self.root == None:            
            self.root = No(remedio, efetivo, colateral, passa)
        else:
            self._insert(remedio, efetivo, colateral, passa, self.root)
    
    def _insert(self, remedio, efetivo, colateral, passa, no_atual):
        new_key = (passa, remedio)
        current_key = (no_atual.passa, no_atual.remedio)

        if new_key < current_key:
            if no_atual.left == None:
                no_atual.left = No(remedio, efetivo, colateral, passa)
                no_atual.left.parent = no_atual
                self._inspect_insertion(no_atual.left)
            else:
                self._insert(remedio, efetivo, colateral, passa, no_atual.left)
        elif new_key > current_key:
            if new_key > current_key:
                if no_atual.right == None:
                    no_atual.right = No(remedio, efetivo, colateral, passa)
                    no_atual.right.parent = no_atual
                    self._inspect_insertion(no_atual.right)
                else:
                    self._insert(remedio, efetivo, colateral, passa, no_atual.right)
        else:
            print("Medicamentos já existem na arvore.")

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
            return -1
    
    def _height(self, no_atual, altura_atual):
        if no_atual == None:
            return altura_atual
        
        left_height = self._height(no_atual.left, altura_atual + 1)
        right_height = self._height(no_atual.right, altura_atual + 1)
        return max(left_height, right_height)
    
    def _find(self, key, no_atual):
        # fazer aqui
        pass


if __name__ == "__main__":
    # Criando a árvore AVL
    avl_tree = AVLarvore()

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
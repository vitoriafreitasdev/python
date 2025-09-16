
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from collections import deque

"""
focar na parte de estraficação de pacientes
fazer um grafo que vai representar os pacientes que participaram do teste
dividir em => nome, idade, gravidade da doença 
rotinas de aprendizado de máquina para estratificação de pacientes
fazer um analise com aprendizado de maquina para pegar os pacientes que estao em situações mais graves, 1 para grave, 0 para nao grave
pacientes graves seram prioridade => entraram na fila de pioridade

"""


class No:
    def __init__(self, remedio, efetivo, colateral, passa):
        # padronizamos a chave como (passa, remedio) para comparar corretamente
        self.key = (passa, remedio)
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
        if self.root is None:            
            self.root = No(remedio, efetivo, colateral, passa)
        else:
            self._insert(remedio, efetivo, colateral, passa, self.root)
    
    def _insert(self, remedio, efetivo, colateral, passa, no_atual):
        new_key = (passa, remedio)
        current_key = (no_atual.passa, no_atual.remedio)

        if new_key < current_key:
            if no_atual.left is None:
                no_atual.left = No(remedio, efetivo, colateral, passa)
                no_atual.left.parent = no_atual
                self._inspect_insertion(no_atual.left)
            else:
                self._insert(remedio, efetivo, colateral, passa, no_atual.left)
        elif new_key > current_key:
            if no_atual.right is None:
                no_atual.right = No(remedio, efetivo, colateral, passa)
                no_atual.right.parent = no_atual
                self._inspect_insertion(no_atual.right)
            else:
                self._insert(remedio, efetivo, colateral, passa, no_atual.right)
        else:
            print("Medicamentos já existem na arvore.")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(f'{cur_node.remedio}: passa={cur_node.passa}, efeito: {cur_node.efetivo}, colateral: {cur_node.colateral}, h={cur_node.height}')
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return -1
    
    def _height(self, no_atual, altura_atual):
        if no_atual is None:
            return altura_atual
        
        left_height = self._height(no_atual.left, altura_atual + 1)
        right_height = self._height(no_atual.right, altura_atual + 1)
        return max(left_height, right_height)
    
    def find(self, passa, remedio):
        if self.root is not None:
            return self._find((passa, remedio), self.root)
        else:
            return None
        
    def _find(self, key, atual):
        key_atual = (atual.passa, atual.remedio)

        if key == key_atual:
            return atual   # retorna o nó inteiro
        elif key < key_atual and atual.left is not None:
            return self._find(key, atual.left)
        elif key > key_atual and atual.right is not None:
            return self._find(key, atual.right)
        return None
    
    def delete_value(self, passa, remedio):
        return self.delete_node(self.find(passa, remedio))
    
    def delete_node(self, no):
        if no is None or self.find(no.passa, no.remedio) is None:
            print("No não achado na arvore.")
            return None 

        def min_value_node(n):
            atual = n 
            while atual.left is not None:
                atual = atual.left 
            return atual 
        
        def num_children(n):
            nc = 0
            if n.left is not None:
                nc += 1
            if n.right is not None:
                nc += 1
            return nc
        
        no_parent = no.parent
        no_children = num_children(no)

        if no_children == 0:
            if no_parent is not None:
                if no_parent.left == no:
                    no_parent.left = None 
                else:
                    no_parent.right = None 
            else:
                self.root = None 

        elif no_children == 1:
            child = no.left if no.left is not None else no.right

            if no_parent is not None:
                if no_parent.left == no:
                    no_parent.left = child 
                else:
                    no_parent.right = child 
            else: 
                self.root = child 
            
            child.parent = no_parent
        
        else:  # no_children == 2
            sucessor = min_value_node(no.right)

            # copiar dados do sucessor para o nó
            no.key = sucessor.key 
            no.passa = sucessor.passa
            no.remedio = sucessor.remedio 
            no.efetivo = sucessor.efetivo 
            no.colateral = sucessor.colateral

            # remover o sucessor
            self.delete_node(sucessor)
            return
        
        if no_parent is not None:
            no_parent.height = 1 + max(
                self.get_height(no_parent.left),
                self.get_height(no_parent.right)
            )
            self._inspect_deletion(no_parent)

    def search(self, passa, remedio):
        if self.root is not None:
            return self._search((passa, remedio), self.root)
        else:
            return False 
    
    def _search(self, key, no_atual):
        chave_atual = (no_atual.passa, no_atual.remedio)

        if key == chave_atual:
            return True
        elif key < chave_atual and no_atual.left is not None:
            return self._search(key, no_atual.left)
        elif key > chave_atual and no_atual.right is not None:
            return self._search(key, no_atual.right)
        return False 
    
    def _inspect_insertion(self, no_atual):
        if no_atual.parent is None:
            return         

        left_height = self.get_height(no_atual.left)
        right_height = self.get_height(no_atual.right)

        if abs(left_height - right_height) > 1: 
            path = [no_atual.parent, no_atual]
            # garantir que há x (taller child of no_atual)
            y = path[1]
            x = self.taller_child(y)
            self._rebalance_node(path[0], y, x)
            return
        
        new_height = 1 + no_atual.height
        if new_height > no_atual.parent.height:
            no_atual.parent.height = new_height
        
        self._inspect_insertion(no_atual.parent)

    def _inspect_deletion(self, no_atual):
        if no_atual is None:
            return
        
        left_height = self.get_height(no_atual.left)
        right_height = self.get_height(no_atual.right)      

        if abs(left_height - right_height) > 1:
            y = self.taller_child(no_atual)
            x = self.taller_child(y)
            self._rebalance_node(no_atual, y, x)

        self._inspect_deletion(no_atual.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else: 
            raise Exception("Aconteceu um erro ao rebalancear.")
    
    def _right_rotate(self, z):
        sub_root = z.parent 
        y = z.left 
        t3 = y.right 
        y.right = z 
        z.parent = y
        z.left = t3 

        if t3 is not None:
            t3.parent = z 
        y.parent = sub_root 
        if y.parent is None:
            self.root = y 
        else:
            if y.parent.left == z:
                y.parent.left = y 
            else:
                y.parent.right = y 
        
        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )
    
    def _left_rotate(self, z):
        sub_root = z.parent 
        y = z.right
        t2 = y.left 
        y.left = z
        z.parent = y 
        z.right = t2 
        
        if t2 is not None:
            t2.parent = z 
        y.parent = sub_root 
        
        if y.parent is None:
            self.root = y 
        else: 
            if y.parent.left == z:
                y.parent.left = y 
            else:
                y.parent.right = y 
        
        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )
        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

    def get_height(self, no_atual):
        if no_atual is None:
            return 0 
        return no_atual.height

    def taller_child(self, no_atual):
        left = self.get_height(no_atual.left)
        right = self.get_height(no_atual.right)
        return no_atual.left if left >= right else no_atual.right
    
    def transforme_data(self, raiz, data_list):
        if raiz:
            self.transforme_data(raiz.left, data_list)
            data_list.append({
                "remedio": raiz.remedio,
                "efetivo": raiz.efetivo,
                "colateral": raiz.colateral,
                "passa": raiz.passa
            })
            self.transforme_data(raiz.right, data_list)
    
    def bfs_remedios_que_passaram(self, raiz):
        
        if not raiz:
            return False 
        
        fila = deque([raiz])
        passaram = []
        
        while fila:
            atual = fila.popleft()
            
            if atual.passa == 1:
                passaram.append(atual.remedio)

            if atual.left:
                fila.append(atual.left)

            if atual.right:
                fila.append(atual.right)
        
        return passaram


    def dfs_todos_remedios_do_teste(self, raiz, todos_remedios):
        
        if not raiz:
            return 
        
        if raiz.remedio:
            todos_remedios.append(raiz.remedio)
        
        return self.dfs_todos_remedios_do_teste(raiz.left, todos_remedios) or self.dfs_todos_remedios_do_teste(raiz.right, todos_remedios)

if __name__ == "__main__":
    # Criando a árvore AVL
    avl_tree = AVLarvore()
    dados_para_inserir = []

    def menu():
        remedios_quantidade = int(input("Quantos remedios se vai inserir para analise: "))
    
        for i in range(remedios_quantidade):
            # Inserindo dados na árvore
            eficiencia = input("Remedio é eficiente (s/n): ")

            if(eficiencia != "s" and eficiencia != "n"):
                print("Insira os dados corretamente.")
                break
            
            colateral = input("Remedio tem colateral (sem colateral/colateral medio/colateral forte): ")
            
            if(colateral != "sem colateral" and colateral != "colateral medio" and colateral != "colateral forte"):
                print("Insira os dados corretamente.")
                break
            
            if colateral == "sem colateral" or colateral == "colateral medio":
                colateral_aceitavel = True 
            
            if colateral == "colateral forte":
                colateral_aceitavel = False

            if colateral_aceitavel and eficiencia == "s":
                passa = 1
            else:
                passa = 0

            dados_para_inserir.append((f'Remedio {i}', f'{eficiencia}', f'{colateral}', passa))
    
    menu()

    print(dados_para_inserir)
    for remedio, efetivo, colateral, passa in dados_para_inserir:
        avl_tree.insert(remedio, efetivo, colateral, passa)

    data_list = []
    avl_tree.transforme_data(avl_tree.root, data_list)

    df = pd.DataFrame(data_list) 

    inputs = df.drop('passa', axis='columns')
    target = df['passa']

    le_remedio = LabelEncoder()
    le_efetivo = LabelEncoder()
    le_colateral = LabelEncoder()

    inputs["remedio_n"] = le_remedio.fit_transform(inputs['remedio'])
    inputs["efetivo_n"] = le_colateral.fit_transform(inputs['efetivo'])
    inputs["colateral_n"]= le_colateral.fit_transform(inputs['colateral'])

    inputs_n = inputs.drop(['remedio', 'efetivo', 'colateral'], axis="columns")
    
    print("Dados da Árvore AVL:")
    print(df)
    print("\nDados Codificados:")
    print(inputs_n)

    model = tree.DecisionTreeClassifier()
    model.fit(inputs_n, target)
    porcetagem_acerto = model.score(inputs_n, target)
    while True:

        try:
            print("De acordo com a tabela de de dados codificados, coloque abaixo os numeros, dos seguintes dados: remedio, efetivo, colateral.")
            n1 = int(input("Numero do remedio: "))
            n2 = int(input("Numero do efetivo: "))
            n3 = int(input("Numero do colateral: "))
            resultado = model.predict([[n1, n2, n3]])

            if resultado == 1:
                print("Aprovado para fase 2")
            else:
                print("Reporovado, precisa de mais testes e mais reajustes a serem feitos.")

            continuar = input("Deseja continuar (s/n): ")

            if continuar != "s":
                print("Encerrando...")
                break

        except ValueError:
            print("Deu algum erro, tente novamente.")   
            break   
    
    print("\n")
    passaram =  avl_tree.bfs_remedios_que_passaram(avl_tree.root)
    todos_remedios = []
    avl_tree.dfs_todos_remedios_do_teste(avl_tree.root, todos_remedios)

    print("=== Remedios que passaram no teste ===")
    for remedio in passaram:
        print(remedio) 

    print("=== Todos remedios que estão no teste ===")
    for remedio in todos_remedios:
        print(remedio) 

    # print("Árvore AVL completa (ordenada por (passa, remedio)):")
    # avl_tree.print_tree()
   
   



import unittest
from grafo import Grafo 
from avltree import AVLarvore 
from collections import deque


class TestAvl(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.dados = [('A', 's', 'sem colateral', 's', 1)]
        self.avl = AVLarvore()
        for remedio, efetivo, colateral, seguro, passa in self.dados:
            self.avl.insert(remedio, efetivo, colateral, seguro, passa)

    def test_bfs(self):
        # Com apenas 1 elemento, deve retornar apenas ['A']
        self.assertEqual(self.avl.bfs(self.avl.root), ['A'])
    
    def test_dfs(self):
        todos_remedios = []
        self.avl.dfs(self.avl.root, todos_remedios)
        # Com apenas 1 elemento, deve retornar apenas ['A']
        self.assertEqual(todos_remedios, ['A'])
    
    def test_transforme_data(self):
        data_list = []
        self.avl.transforme_data(self.avl.root, data_list)
        self.assertEqual(data_list, [{'remedio': 'A', 'efetivo': 's', 'colateral': 'sem colateral', 'seguro': 's', 'passa': 1}])
    
    def test_search(self):
        self.assertEqual(self.avl.search(1, 'A'), True)

    def test_height(self):
        self.assertAlmostEqual(self.avl.height(), 0)

if __name__ == '__main__':
    unittest.main()
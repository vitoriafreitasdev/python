
import unittest
from grafo import Grafo 
from avltree import AVLarvore 
import io
import sys
from collections import deque

class TestGrafo(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.vertices = [("A", 1), ("B", 0), ("C", 1)]
        self.grafo = Grafo(self.vertices)

    def test_todos_pacientes(self):
        captured = io.StringIO()
        sys.stdout = captured   
        self.grafo.todos_pacientes()
        sys.stdout = sys.__stdout__  

        saida = captured.getvalue().strip().split("\n")
        self.assertEqual(saida, ["A", "B", "C"])

    def test_alocar_fila_de_pioridade(self):
        pacientes_prioritarios = ["A", "B", "C"]
        self.assertEqual(self.grafo.alocar_fila_de_pioridade(pacientes_prioritarios), deque(['A', 'B', 'C']))

    def test_mostrar_prioritarios(self):
        fila = deque(['A', 'B', 'C'])
        captured = io.StringIO()
        sys.stdout = captured   
        self.grafo.mostrar_prioritarios(fila)
        sys.stdout = sys.__stdout__  

        saida = captured.getvalue().strip().split("\n")
        self.assertEqual(saida, [
            "Paciente número 1: A",
            "Paciente número 2: B",
            "Paciente número 3: C"
        ])

    def test_alocar_dados(self):

        self.assertEqual(self.grafo.alocar_dados(), [{'nome': 'A', 'gravidade': [1]}, {'nome': 'B', 'gravidade': [0]}, {'nome': 'C', 'gravidade': [1]}])

if __name__ == '__main__':
    unittest.main()
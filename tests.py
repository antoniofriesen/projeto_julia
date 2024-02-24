import unittest
import functions

class TestFunctions(unittest.TestCase):
    def test_calculate_slope(self):
        tempo = [0, 1, 2, 3, 4]
        porcentagem = [0, 20, 40, 60, 80]
        self.assertEqual(functions.calcular_slope(tempo, porcentagem), 20)

    def test_normalize(self):
        valores = [5, 10, 15, 20]
        self.assertEqual(functions.normalizar(valores), [25.0, 50.0, 75.0, 100.0])

if __name__ == '__main__':
    unittest.main()

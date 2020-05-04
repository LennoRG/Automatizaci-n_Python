import unittest


class test_001(unittest.TestCase):

    def setUp(self):   #SIRVE PARA DEFINIR MIS DATOS DE PRUEBAS
        self.Variable_A = 50
        self.Variable_B = 56


    def test_001(self):
        self.RESULTADO = self.Variable_A + self.Variable_B

    def tearDown(self): #ES EL LUGAR DONDE SE EVALUA O FINALIZA LA PRUEBA
        self.assertTrue(self.RESULTADO == 100, f"El valor no es 100, es {self.RESULTADO}")



if __name__ == '__main__':
    unittest.main()

import unittest

class test_002(unittest.TestCase):
    def setUp(self):
        pass

    def test_002(self):
        self.Variable_A = 50
        self.Variable_B = 50


        self.assertEquals(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def test_003(self):
        self.Variable_A = 50
        self.Variable_B = 40

        self.assertNotEqual(self.Variable_A, self.Variable_B, "Los valores son distintos")

    def test_004(self):
        self.Variable_A = 100

        if self.Variable_A >=10:
            self.Resultado = True

        else:
            self.Resultado = False

        self.assertTrue(self.Variable_A, f"El valor no es verdadero, es: {self.Variable_A}")

    def test_005(self):
        self.Variable_A = "Hola Leno Ramirez"
        self.Variable_B = "Hola Leno"

        self.assertIn(self.Variable_B, self.Variable_A, f"No coinciden")

    def test_006(self):
        self.Variable_A = "Hola Leno Ramirez"
        self.Variable_B = "XXXX"

        self.assertIsNot(self.Variable_B, self.Variable_A, f"No coinciden")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
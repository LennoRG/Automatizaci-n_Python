import time
from src.fuctions.Functions import Functions as Inicio
import unittest

class TestInicio(Inicio, unittest.TestCase):

    def setUp(self):
        Inicio.abrir_navegador(self)


    def testInicio(self):
        nombre = "hola0_1.test@yopmail.com"
        contraseña = "Qa123456$"


        Inicio.get_json_file(self, "inicio")  #CARGA EL JSON CON TODOS SUS VALORES

        Inicio.get_elements(self, "Btn_inicioSesion").click()
        time.sleep(3)
        Inicio.get_elements(self, "P_Correo").click()
        time.sleep(2)

        Inicio.get_elements(self, "Email").send_keys(nombre)
        Inicio.get_elements(self, "Password").send_keys(contraseña)
        Inicio.get_elements(self, "IniciarSesion").click()



    def tearDown(self):
        time.sleep(10)
        Inicio.tearDow(self)



if __name__ == '__main__':
    unittest.main()

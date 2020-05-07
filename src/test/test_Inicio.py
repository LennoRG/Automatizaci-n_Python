import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.fuctions.Functions import Functions as NextCloud


import unittest

class TestInicio(NextCloud, unittest.TestCase):

    def setUp(self):
        NextCloud.abrir_navegador(self)


    def testInicio(self):
        nombre = "hola0_1.test@yopmail.com"
        contraseña = "Qa123456$"

        NextCloud.get_json_file(self, "portal") #CARGA EL JSON CON TODOS SUS VALORES


        NextCloud.get_elements(self, "Btn_inicioSesion").click()
        time.sleep(3)
        NextCloud.get_elements(self, "P_Correo").click()
        time.sleep(2)


        NextCloud.get_elements(self, "Email").send_keys(nombre)
        NextCloud.get_elements(self, "Password").send_keys(contraseña)


        NextCloud.get_elements(self, "IniciarSesion").click()
        time.sleep(5)

        ###################################################
        ######## EMPLIEZA AUTOMATIZACION DEL PORTAL #######
        ###################################################
        NextCloud.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)

        ####### COMPARO LOS TEXTOS DE CADA ACCION #######
        self.TEXTOS_ACCIONES = self.driver.find_elements(By.CLASS_NAME, "menu-item-name")
        self.count = 0

        for self.TEX in self.TEXTOS_ACCIONES:
            RESULTADO_TEXTOS = ['Carpeta nueva', 'Cargar archivo',
                                'Cargar carpeta', 'Nuevo archivo de texto',
                                'Nuevo documento', 'Nueva hoja de cálculo',
                                'Nueva presentación']
            assert RESULTADO_TEXTOS[self.count] == self.TEX.text, "LOS NOMBRES NO COINCIDEN"
            self.count = self.count + 1
        ####### TERMINO DE COMPARAR LOS TEXTOS DE CADA ACCION #######

        NextCloud.get_elements(self, "Crear_Carpeta").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Btn_Crear_Carpeta").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_detalle_Carpeta").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)
        '''NextCloud.get_elements(self, "Cargar_Archivo").click()   #CARGAR ARCHIVOS
        time.sleep(3)
        NextCloud.get_elements(self, "Cargar_Archivo").click()   #CARGAR ARCHIVOS
        time.sleep(3)'''
        NextCloud.get_elements(self, "Nuevo_Archivo_Texto").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Btn_Crear_Archivo_Texto").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Archivo_Texto").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Detalle_Texto").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Nuevo_Documento").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Btn_Crear_Nuevo_Documento").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Nuevo_Documento").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)
        NextCloud.get_elements(self,  "Hoja_Calculo").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Btn_Crear_Hoja_Calculo").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Hoja_Calculo").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Nueva_Presentacion").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Btn_Crear_Presentacion").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Presentacion").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Vista_Cuadricula").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Vista_Lista").click()
        time.sleep(3)

        ######### FUNCIONES DE OPCIONES DE ARCHIVOS ###########
        '''self.NAME_ACCIONES_ARCHIVOS = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/app-menu/ul/li[2]/div[1]/div")
        self.count = 0

        for self.NAM in self.NAME_ACCIONES_ARCHIVOS:
            RESULTADO_NAME = ['Mover a papelera', 'Compartir',
                              'Añadir a favoritos', 'Detalles',
                              'Renombrar', 'Mover o copiar', 'Descargar']
            assert RESULTADO_NAME[self.count] == self.NAM.text, "LOS TEXTOS NOMBRES NO COINCIDEN"
            self.count = self.count + 1'''

        NextCloud.get_elements(self, "Mover_Papelera").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Compartir").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Compartir").click()
        time.sleep(3)

        ####### FUNCION PARA LOCALIZAR UN ELEMENT Y DESPLEGAR SU CONTENIDO #########
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        ####### TERMINA FUNCION PARA LOCALIZAR UN ELEMENT Y DESPLEGAR SU CONTENIDO #########

        NextCloud.get_elements(self, "Favoritiar").click()
        time.sleep(3)

        localizador = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        NextCloud.get_elements(self, "Detalles").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Detalles").click()
        time.sleep(5)

        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        NextCloud.get_elements(self, "Rename").click()
        time.sleep(3)

        NextCloud.get_elements(self, "Mover_Copiar").click()
        time.sleep(3)
        NextCloud.get_elements(self, "Cerrar_Mover_Copiar").click()
        time.sleep(3)

        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        NextCloud.get_elements(self, "Descargar").click()
        time.sleep(3)

        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        NextCloud.get_elements(self, "Favoritiar").click() #DESFAVORITIAR
        time.sleep(3)

        NextCloud.get_elements(self, "Check_Imagen").click()
        time.sleep(3)

        assert NextCloud.get_text(self, "Titulo_Archivos") == "Archivos" #COMPARO EL TEXT ARCHIVOS




        '''Inicio.get_elements(self, "Btn_Actividad").click()
        time.sleep(10)'''


    def tearDown(self):
        time.sleep(10)
        NextCloud.tearDow(self)



if __name__ == '__main__':
    unittest.main()

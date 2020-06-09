# -*- coding: utf-8 -*-
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.fuctions.Functions import Functions as NextCloud
import unittest
import allure

@allure.feature(u"Test Claro drive 02") #Nombre de la prueba para el reporte en allure
@allure.story(u"Segunda prueba con Allure: Captura de Pantalla") #Historia del Tests
@allure.testcase(u"Caso de prueba de Inicio sesion", u"Aqui se pude poner la url para conectar el testCase a Jira")
@allure.severity(allure.severity_level.NORMAL)#Status del test case Error, Critycal etc.
@allure.description(u"""Se realizo la primera prueba para genrar un reporte en allure: </br>
                    La prueba se realizo con exito </br>
                    </br></br>""")


class TestInicio(NextCloud, unittest.TestCase):

    def setUp(self):
        with allure.step(u"Paso 1: Ingresamos a Google"):
            NextCloud.abrir_navegador(self)
            NextCloud.get_json_file(self, "portal")  # CARGA EL JSON CON TODOS SUS VALORES


    def testInicio(self):
        nombre = "hola0_1.test@yopmail.com"
        contraseña = "Qa123456$"

        #NextCloud.get_json_file(self, "portal") #CARGA EL JSON CON TODOS SUS VALORES

        with allure.step(u"Paso 2: Ingresamos a Google y Empieza la Automatizacón"):

             NextCloud.get_elements(self, "Btn_inicioSesion").click()
             time.sleep(3)
             NextCloud.get_elements(self, "P_Correo").click()
             time.sleep(2)

             NextCloud.get_elements(self, "Email").send_keys(nombre)
             NextCloud.get_elements(self, "Password").send_keys(contraseña)

             #NextCloud.esperar_elemento(self, "IniciarSesion") #ESPERAR ELEMTO

             NextCloud.get_elements(self, "IniciarSesion").click()
             time.sleep(5)

             ###################################################
             ######## EMPLIEZA AUTOMATIZACION DEL PORTAL #######
             ###################################################
             NextCloud.captura(self, "Claro Drive") #CAPTURA LA PANTALLA Y LA GUARDA EN EL REPORTE DE ALLURE
             #NextCloud.captura_pantalla(self) #CAPTURA LA PANTALLA

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
             #NextCloud.esperar_elemento(self, "Btn_Crear_Carpeta")  # ESPERAR ELEMTOvvvvvv

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

             NextCloud.get_elements(self, "Check_Imagen").click() #SELECCIONO ARCHIVO
             time.sleep(3)
             NextCloud.get_elements(self, "Check_Imagen").click() #DESELECCIONO ARCHIVO
             time.sleep(3)

             assert NextCloud.get_text(self, "Titulo_Archivos") == "Archivos" #COMPARO EL TEXT ARCHIVOS
             assert NextCloud.get_text(self, "Titulo_Carpeta") == "Carpetas" #COMPARO EL TEXT CARPETA
             assert NextCloud.get_text(self, "Titulo_Archivos_Recientes") == "Archivos recientes"  #COMPARO EL TEXT ARCHIVOS RECIENTES

             NextCloud.get_elements(self, "Check_Carpeta").click()  #SELECCIONO CARPETA
             time.sleep(3)
             NextCloud.get_elements(self, "Check_Carpeta").click()  #DESELECCIONO CARPETA
             time.sleep(3)
             NextCloud.get_elements(self, "Mover_Papelera_Carpeta").click()  #ELIMONO CARPETA
             time.sleep(3)

             #FUNCIONALIDADES HEADER LIST_VIEW
             NextCloud.get_elements(self, "Check_Header_list_view").click()
             time.sleep(3)

             '''self.OPCIONES_HEADER = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-header/div/div[2]")
             self.count = 0
            
             for self.OPC in self.OPCIONES_HEADER:
                 RESULTADO_OPCIONES = ['Mover o copiar', 'Descargar', 'Eliminar']
                 assert RESULTADO_OPCIONES[self.count] == self.OPC.text, "LOS TEXTO NO COINCIDEN"
                 self.count = self.count + 1
             time.sleep(3)'''
             assert NextCloud.get_text(self, "Header_Mover_Copiar") == "Mover o copiar"
             assert NextCloud.get_text(self, "Header_Descargar") == "Descargar"
             assert NextCloud.get_text(self, "Header_Eliminar") == "Eliminar"

             NextCloud.get_elements(self, "Header_Mover_Copiar").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Header_Cerrar_Mover_Copiar").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Header_Descargar").click()
             time.sleep(3)
             #NextCloud.get_elements(self, "Check_Header_list_view").click()
             time.sleep(3)
             #NextCloud.get_elements(self, "Header_Eliminar").click()
             #time.sleep(3)
             #TERMINA FUNCIONALIDADES HEADER LIST_VIEW

             ############### FUNCIONALIDADES DE LA LISTA DE OPCIONES EN IMAGENES EN ARCHIVOS RECIENTES ############
             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)

             assert NextCloud.get_text(self, "Menu_List_Imagenes_Eliminar") == "Mover a papelera"
             assert NextCloud.get_text(self, "Menu_List_Imagenes_Compartir") == "Compartir"
             assert NextCloud.get_text(self, "Menu_List_Imagenes_Favoritiar") == "Añadir a favoritos"
             assert NextCloud.get_text(self, "Menu_List_Texto_Destalles") == "Detalles"
             assert NextCloud.get_text(self, "Menu_List_Imagenes_Renombrar") == "Renombrar"
             assert NextCloud.get_text(self, "Menu_List_Imagenes_MoverCopiar") == "Mover o copiar"
             assert NextCloud.get_text(self, "Menu_List_Imagenes_Descargar") == "Descargar"
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes_Eliminar").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes_Compartir").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Cerrar_Compartir").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Texto_Destalles").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Cerrar_Detalles").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes_Renombrar").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes_MoverCopiar").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Cerrar_Mover_Copiar").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes_Descargar").click()
             time.sleep(3)

             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes_Favoritiar").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Menu_List_Imagenes").click()
             time.sleep(3)
             NextCloud.get_elements(self, "Cerrar_Imagen").click()
             time.sleep(3)

             #########################################################################################
             ############################  ACCIONES DE BTNS FILTROS ##################################
             #########################################################################################
             '''self.TXT_FLTROS = self.driver.find_elements(By.ID, "filters")
             self.count = 0
            
             for self.TXT_ in self.TXT_FLTROS:
                 RESULTADOS_FILTROS = ['Mi unidad', 'Reciente', 'Favoritos',
                                       'Imágenes', 'Videos', 'Contactos', 'Compartidos',
                                       'Te compartieron', 'Compartiste', 'Ligas compartidas'
                                       'Etiquetas', 'Papelera']
                 assert RESULTADOS_FILTROS[self.count] == self.TXT_.text, "LOS TEXTOS FILTROS NO COINCIDEN"
                 self.count = self.count + 1'''
             assert NextCloud.get_text(self, "Filtro_ALL_ARCHIVOS") == "Todos los archivos"
             assert NextCloud.get_text(self, "Filtro_RECIENTE") == "Reciente"
             assert NextCloud.get_text(self, "Filtro_Favoritos") == "Favoritos"
             assert NextCloud.get_text(self, "Filtro_Imagenes") == "Imágenes"
             assert NextCloud.get_text(self, "Filtro_Videos") == "Videos"
             assert NextCloud.get_text(self, "Filtro_Contactos") == "Contactos"
             assert NextCloud.get_text(self, "Filtro_Compartidos") == "Compartidos"
             assert NextCloud.get_text(self, "Filtro_Papelera") == "Papelera"
             assert NextCloud.get_text(self, "Filtro_Etiquetas") == "Etiquetas"
             ############### FUNCIONALIDADES DE LA LISTA DE OPCIONES EN IMAGENES EN ARCHIVOS RECIENTES ############

             '''Inicio.get_elements(self, "Btn_Actividad").click()
             time.sleep(10)'''


             #NextCloud.scroll_to(self,  "Centro de ayuda") #FUNCION SCROLL
             #NextCloud.js_clic(self, "Centro de ayuda") #DA CLIC A UN TEXTO CON JAVASCRIPT


    def tearDown(self):
        with allure.step(u"Paso 3: Cerramos el Driver, Se cierra la Automación"):
            time.sleep(10)
            NextCloud.tearDow(self)



if __name__ == '__main__':
    unittest.main()

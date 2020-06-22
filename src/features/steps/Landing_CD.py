# -*- coding: utf-8 -*-
import time

from behave import *
import pytest
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from fuctions.Functions import Functions as Buzon
from fuctions.Inicializar import Inicializar
from selenium.webdriver.common.by import By

use_step_matcher("re")

class Landing_CD(Buzon):
    @given("Open the application")
    def abrir_navegador(self):
        Buzon.abrir_navegador(self)


    @step("I charge the Json of the App: portal\.json")
    def cargo_Json(self):
        Buzon.get_json_file(self, "portal")


    @step("I click on the button Iniciar Sesion")
    def btn_IniciaSesion(self):
        Buzon.get_elements(self, "Btn_inicioSesion").click()
        time.sleep(2)


    @step("I click Correo")
    def login_Correo(self):
        nombre = "hola0_1.test@yopmail.com"
        contraseña = "Qa123456$"

        Buzon.get_elements(self, "P_Correo").click()
        time.sleep(3)

        Buzon.get_elements(self, "Email").send_keys(nombre)
        Buzon.get_elements(self, "Password").send_keys(contraseña)
        Buzon.get_elements(self, "IniciarSesion").click()
        time.sleep(15)

    @step("I click on the button Btn_Crear\+")
    def step_impl(self):
       Buzon.get_elements(self, "Btn_Crear+").click()
       time.sleep(5)

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


    @step("I click Carpeta")
    def step_impl(self):
        Buzon.get_elements(self, "Crear_Carpeta").click()
        time.sleep(3)

        Buzon.get_elements(self, "Btn_Crear_Carpeta").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_detalle_Carpeta").click()
        time.sleep(3)

    @step("I click Archivo de Texto")
    def step_impl(self):
        Buzon.get_elements(self, "Btn_Crear+").click()
        time.sleep(3)
        Buzon.get_elements(self, "Nuevo_Archivo_Texto").click()
        time.sleep(3)
        Buzon.get_elements(self, "Btn_Crear_Archivo_Texto").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Archivo_Texto").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Detalle_Texto").click()
        time.sleep(3)


    @then("I click Vista Cuadricula")
    def step_impl(self):
        Buzon.get_elements(self, "Vista_Cuadricula").click()
        time.sleep(3)


    @then("I click Vista Lista")
    def step_impl(self):
        Buzon.get_elements(self, "Vista_Lista").click()
        time.sleep(3)


    @then("I click Mover a Papelera")
    def step_impl(self):
        Buzon.get_elements(self, "Mover_Papelera").click()
        time.sleep(3)


    @step("I click Compartir")
    def step_impl(self):
        Buzon.get_elements(self, "Compartir").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Compartir").click()
        time.sleep(3)


    @step("I click Favoritiar")
    def step_impl(self):
        ####### FUNCION PARA LOCALIZAR UN ELEMENT Y DESPLEGAR SU CONTENIDO #########
        localizador = self.driver.find_element(By.XPATH,
                                               "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        ####### TERMINA FUNCION PARA LOCALIZAR UN ELEMENT Y DESPLEGAR SU CONTENIDO #########
        Buzon.get_elements(self, "Favoritiar").click()
        time.sleep(3)


    @step("I click Detalles")
    def step_impl(self):
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        Buzon.get_elements(self, "Detalles").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Detalles").click()
        time.sleep(3)


    @step("I click Renombrar")
    def step_impl(self):
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        Buzon.get_elements(self, "Rename").click()
        time.sleep(3)


    @step("I click Mover Copiar")
    def step_impl(self):
        Buzon.get_elements(self, "Mover_Copiar").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Mover_Copiar").click()
        time.sleep(3)


    @step("I click Descargar")
    def step_impl(self):
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        Buzon.get_elements(self, "Descargar").click()
        time.sleep(3)


    @step("I click Desfavoritiar")
    def step_impl(self):
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/app-amx-files/app-files-content/div/app-list[3]/app-file[1]/div/div[1]/div[3]")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        action.perform()
        time.sleep(3)
        Buzon.get_elements(self, "Favoritiar").click() #DESFAVORITIAR
        time.sleep(3)


    @step("I click Check_Imagen")
    def step_impl(self):
        Buzon.get_elements(self, "Check_Imagen").click()  #SELECCIONO ARCHIVO
        time.sleep(3)
        Buzon.get_elements(self, "Check_Imagen").click()  #DESELECCIONO ARCHIVO
        time.sleep(3)

        assert Buzon.get_text(self, "Titulo_Archivos") == "Archivos"  #COMPARO EL TEXT ARCHIVOS
        assert Buzon.get_text(self, "Titulo_Carpeta") == "Carpetas"  #COMPARO EL TEXT CARPETA
        assert Buzon.get_text(self,"Titulo_Archivos_Recientes") == "Archivos recientes"  #COMPARO EL TEXT ARCHIVOS RECIENTES


    @then("I click Check_Carpeta")
    def step_impl(self):
        Buzon.get_elements(self, "Check_Carpeta").click()  #SELECCIONO CARPETA
        time.sleep(3)
        Buzon.get_elements(self, "Check_Carpeta").click()  #DESELECCIONO CARPETA
        time.sleep(3)


    @step("I click Mover Carpeta a Papelera")
    def step_impl(self):
        Buzon.get_elements(self, "Mover_Papelera_Carpeta").click()  #ELIMINO CARPETA
        time.sleep(20)


    @then("I click Check_Header_list_view")
    def step_impl(self):
        # FUNCIONALIDADES HEADER LIST_VIEW
        Buzon.get_elements(self, "Check_Header_list_view").click()
        time.sleep(3)

        assert Buzon.get_text(self, "Header_Mover_Copiar") == "Mover o copiar"
        assert Buzon.get_text(self, "Header_Descargar") == "Descargar"
        assert Buzon.get_text(self, "Header_Eliminar") == "Eliminar"


    @step("I click Mover_Copiar")
    def step_impl(self):
        Buzon.get_elements(self, "Header_Mover_Copiar").click()
        time.sleep(3)
        Buzon.get_elements(self, "Header_Cerrar_Mover_Copiar").click()
        time.sleep(3)


    @then("I click Header_Descargar")
    def step_impl(self):
        Buzon.get_elements(self, "Header_Descargar").click()
        time.sleep(3)


    @step("I clic Menu_List_Imagenes")
    def step_impl(self):
        ############### FUNCIONALIDADES DE LA LISTA DE OPCIONES EN IMAGENES EN ARCHIVOS RECIENTES ############
        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)

        assert Buzon.get_text(self, "Menu_List_Imagenes_Eliminar") == "Mover a papelera"
        assert Buzon.get_text(self, "Menu_List_Imagenes_Compartir") == "Compartir"
        assert Buzon.get_text(self, "Menu_List_Imagenes_Favoritiar") == "Añadir a favoritos"
        assert Buzon.get_text(self, "Menu_List_Texto_Destalles") == "Detalles"
        assert Buzon.get_text(self, "Menu_List_Imagenes_Renombrar") == "Renombrar"
        assert Buzon.get_text(self, "Menu_List_Imagenes_MoverCopiar") == "Mover o copiar"
        assert Buzon.get_text(self, "Menu_List_Imagenes_Descargar") == "Descargar"
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes_Eliminar").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes_Compartir").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Compartir").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Texto_Destalles").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Detalles").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes_Renombrar").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes_MoverCopiar").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Mover_Copiar").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes_Descargar").click()
        time.sleep(3)

        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes_Favoritiar").click()
        time.sleep(3)
        Buzon.get_elements(self, "Menu_List_Imagenes").click()
        time.sleep(3)
        Buzon.get_elements(self, "Cerrar_Imagen").click()
        time.sleep(3)


    @then("I compare actions of BTNS filters")
    def step_impl(self):
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
        assert Buzon.get_text(self, "Filtro_ALL_ARCHIVOS") == "Todos los archivos"
        assert Buzon.get_text(self, "Filtro_RECIENTE") == "Reciente"
        assert Buzon.get_text(self, "Filtro_Favoritos") == "Favoritos"
        assert Buzon.get_text(self, "Filtro_Imagenes") == "Imágenes"
        assert Buzon.get_text(self, "Filtro_Videos") == "Videos"
        assert Buzon.get_text(self, "Filtro_Contactos") == "Contactos"
        assert Buzon.get_text(self, "Filtro_Compartidos") == "Compartidos"
        assert Buzon.get_text(self, "Filtro_Papelera") == "Papelera"
        assert Buzon.get_text(self, "Filtro_Etiquetas") == "Etiquetas"
        ############### FUNCIONALIDADES DE LA LISTA DE OPCIONES EN IMAGENES EN ARCHIVOS RECIENTES ############

import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from src.fuctions.Inicializar import Inicializar
from selenium.webdriver.chrome.options import Options as OpcionesChrome

import json

class Functions(Inicializar):
    ###### INICIALIZAR DRIVER #####
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print(Inicializar.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("----------------")

        if navegador == ("Chrome"):
            '''caps = DesiredCapabilities.CHROME.copy()
            caps["platform"] = "WINDOWS"
            caps["browserName"] = "Chrome"
            caps["ignoreZoomSetting"] = True
            caps["requireWindowFocus"] = True
            caps["nativeEvents"] = True'''
            options = OpcionesChrome()
            options.add_argument('start-maximized')

            self.driver = webdriver.Chrome(Inicializar.basedir +"\\drivers\\chromedriver.exe")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0] #FUNCION PARA REGRESAR A LA VENTANA PRINCIPAL
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

        if navegador == "Firefox":
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0]  # FUNCION PARA REGRESAR A LA VENTANA PRINCIPAL
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            self.nWindows = 0
            return self.driver

    def tearDow(self):
        print("SE CERRO CON EXITO EL DRIVER")
        time.sleep(5)
        self.driver.quit()

    #################################################################
    ############### FUNCION RUTA DE CARPETA DEL JSON ################
    #################################################################
    '''def __init__(self):
        self.json_GetFieldBy = None  #VALOR QUE CONTINE ESE ATRIBUTO EN EL JSON INCIO
        self.json_ValueToFind = None #VALOR QUE CONTINE ESE ATRIBUTO EN EL JSON INCIO'''

    def get_json_file(self, file):
        json_path = Inicializar.Json + "/" + file + '.json' #Ruta de la carpeta donde esta el JSON, Mencionada en el archivo Inicializar
        try:
            with open(json_path, "r") as read_file:    #Abro el json
                self.json_strings = json.loads(read_file.read())  #CARGO_TODO EL COTENIDO DEL JSON
                print("get_json_file: " + json_path) #Imprimo la ruta del Json
                return self.json_strings
        except FileNotFoundError: #FUNCION SI EL ARCHIVO NO EXISTE
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el archivo " + file)
            Functions.tearDow(self)

    ################################################################################
    ########################### LEO LAS ENTIDADES DEL JSON #########################
    ################################################################################
    def get_entity(self, entity):    # entity ES LAS ENTIDAD DEL JSON QUE QUIERO LEER
        if self.json_strings is False:
            print("Esta Entity No Existe")  #Si la entidad no existe se imprime
        else:                               #SI LA ENTITY EXISTE SE EJECUTA EL ELSE
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"] #VALOR DE LA ENTIDAD EN JSON
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"] #VALOR DE LA ENTIDAD EN JSON
                return True
            except KeyError:
                pytest.skip(u"get_json_file: No se encontro el archivo " + entity)
                Functions.tearDow(self)
                return None


    ########################################################################################################
    ############### COMPORTAMIENTO DE LAS FUNCIONES DEL JSON, PARA QUE SE EJECUTEN EN EL TEST ##############
    ########################################################################################################
    def get_elements(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en JSON Definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements
            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDow(self)
            except TimeoutError:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDow(self)

    #################################################################################################
    ########################## GET TEXT FUNCIONALIDAD PARA COMPARAR TEXTOS ##########################
    #################################################################################################
    def get_text(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements == self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_text: " + self.json_ValueToFind)
                print("Text Value: " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " +self.json_ValueToFind)
                Functions.tearDow(self)
            except TimeoutError:
                print("get_text: No se encontro el elemento: " +self.json_ValueToFind)
                Functions.tearDow(self)









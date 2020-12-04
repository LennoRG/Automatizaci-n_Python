# -*- coding: utf-8 -*-
import time

from behave import *

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from fuctions.Functions import Functions as Register
from fuctions.Inicializar import Inicializar
from selenium.webdriver.common.by import By


use_step_matcher("re")

class Register_CD(Register):
    @given("Open the Applicationn")
    def abrir_navegador(self):
        Register.abrir_navegador(self)


    @when("I charge the Json of the App: registerCorreo\.json")
    def cosumo_json(self):
        Register.get_json_file(self, "registerCorreo")


    @then("I click on the button Registrate")
    def step_impl(self):
        Register.get_elements(self, "BTN_Registrate").click()
        time.sleep(3)


    @step("I click on Correo")
    def step_impl(self):
        Register.get_elements(self, "Correo").click()
        time.sleep(2)


    @then("I enter the Registro data")
    def step_impl(self):
        correoUsuario = "testautomatizado03@getnada.com"
        contraseña = "Qa654321$"

        Register.get_elements(self, "Input_IngresaCorreo").send_keys(correoUsuario)
        Register.get_elements(self,  "Input_Contrasena").send_keys(contraseña)

    @step("I click the button Registrarme")
    def step_impl(self):
        Register.get_elements(self, "BTN_Registrarme").click()
        time.sleep(3)


    @when("You select the TDC plan")
    def step_impl(self):
        Register.get_elements(self, "Plan_PagoTarjeta").click()
        time.sleep(3)


    @then("I click on the 200GB plan")
    def step_impl(self):
        Register.get_elements(self, "Plan_200GB") #ELIJO EL LA OPCION 200GB
        time.sleep(2)


    @step("I click the button Aceptar")
    def step_impl(self):
        Register.get_elements(self, "Plan_BTNAceptar").click()
        time.sleep(3)


    @when("I am in the payment information enter Nombre of the TDC Titular")
    def step_impl(self):
        titularTarjeta = "Test Smoke"

        Register.get_elements(self, "InfoPago_NombreTitular").send_keys(titularTarjeta)
        time.sleep(1)


    @then("Enter the TDC number")
    def step_impl(self):
        numTarjeta = "4523984527360876"

        Register.get_elements(self, "InfoPago_NumeroTarjeta").send_keys(numTarjeta)
        time.sleep(1)

    @then("Income the Mes of the TDC")
    def step_impl(self):
        mesTarjeta = "01"

        Register.get_elements(self, "InfoPago_Mes").send_keys(mesTarjeta)
        time.sleep(1)

    @then("Enter the Anio of the TDC")
    def step_impl(self):
        anioTarjeta = "22"

        Register.get_elements(self, "InfoPago_Anio").send_keys(anioTarjeta)
        time.sleep(1)

    @then("Enter the CVV of the TDC")
    def step_impl(self):
        cvvTarjeta = "698"

        Register.get_elements(self, "InfoPago_CVV").send_keys(cvvTarjeta)
        time.sleep(1)

    @step("I click button Aceptar")
    def step_impl(self):
        Register.get_elements(self, "InfoPago_BTNAceptar").click()
        time.sleep(3)


    @when("I am on the success screen, I click on the IR A MI CLARO DRIVE button")
    def step_impl(self):
        Register.get_elements(self, "Success_BTN").click()
        time.sleep(5)


    @then("Opens the Popup Bienvenida and I click on Google Play")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_GooglePlay").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña principal
        time.sleep(3)


    @then("I click on App Store")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_AppStore").click()
        time.sleep(3)

        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(3)


    @then("I click on Claro drove Desktop")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_Desktop").click()
        time.sleep(3)

        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(3)


    @then("I click on Terminos and Politicas de Privacidad")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_TerminosPolitica").click()
        time.sleep(3)

        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(3)


    @then("I click on 200GB")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_200GB").click()
        time.sleep(3)

        Register.get_elements(self, "Seccion_Archivos").click()
        time.sleep(3)


    @then("I click on 300GB")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_300GB").click()
        time.sleep(3)

        Register.get_elements(self, "Seccion_Archivos").click()
        time.sleep(3)

    @then("I click on 1024GB")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_1024GB").click()
        time.sleep(3)

        Register.get_elements(self, "Seccion_Archivos").click()
        time.sleep(3)


    @step("I click button Cerrar Popup Bienvenida")
    def step_impl(self):
        Register.get_elements(self, "Popup_Bienvenida_Cerrar").click()
        time.sleep(3)


    @when("The Wizard opens I click the Comenzar button")
    def step_impl(self):
        self.Texto_Wizard = self.driver.find_elements(By.XPATH,
                                                       "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Wizard in self.Texto_Wizard:
            RESULTADO_TEXTO = ['Descubre las funciones principales de Claro drive con este tutorial.']
            assert RESULTADO_TEXTO[self.count] == self.Wizard.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1

        Register.get_elements(self, "Wizard_BTN_Comenzar").click()
        time.sleep(2)


    @then("I click on the Siguiente button on CREAR")
    def step_impl(self):
        self.Texto_WizardCrear = self.driver.find_elements(By.XPATH,
                                                           "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Crear in self.Texto_WizardCrear:
            RESULTADO_TEXTO = ['Sube a Claro drive todos tus archivos, fotos y videos.']
            assert RESULTADO_TEXTO[self.count] == self.Crear.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1

        Register.get_elements(self, "Wizard_BTN_Siguiente").click()
        time.sleep(2)


    @then("I click on the Siguiente button on Menu")
    def step_impl(self):
        self.Textos_WizardMenu = self.driver.find_elements(By.XPATH,
                                                           "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Menu in self.Textos_WizardMenu:
            RESULTADO_TEXTO = [
                'Descubre las acciones disponibles como la opción de compartir de tus carpetas y archivos presionando el ícono de los tres puntos.']
            assert RESULTADO_TEXTO[self.count] == self.Menu.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1

        Register.get_elements(self, "Wizard_BTN_Siguiente").click()
        time.sleep(2)


    @then("I click on the Siguiente button on Favoritos")
    def step_impl(self):
        self.Texto_WizardFav = self.driver.find_elements(By.XPATH,
                                                       "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Wizard in self.Texto_WizardFav:
            RESULTADO_TEXTO = ['Encuentra aquí tus archivos o carpetas que hayas marcado como favoritos.']
            assert RESULTADO_TEXTO[self.count] == self.Wizard.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1

        Register.get_elements(self, "Wizard_BTN_Siguiente").click()
        time.sleep(2)


    @step("I click on the Finalizar button on Galeria")
    def step_impl(self):
        self.Texto_WizardGal = self.driver.find_elements(By.XPATH,
                                                       "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Wizard in self.Texto_WizardGal:
            RESULTADO_TEXTO = [
                'Encuentra tus imágenes y videos en la galería de Claro drive que hayas sincronizado previamente.']
            assert RESULTADO_TEXTO[self.count] == self.Wizard.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1

        Register.get_elements(self, "Wizard_BTN_Finalizar").click()
        time.sleep(2)



    @when("I click button Wizard")
    def step_impl(self):
        Register.get_elements(self, "Wizard_BTN").click()
        time.sleep(2)

        self.Texto_WizardBtn = self.driver.find_elements(By.XPATH,
                                                         "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Wizard in self.Texto_WizardBtn:
            RESULTADO_TEXTO = ['Descubre las funciones principales de Claro drive con este tutorial.']
            assert RESULTADO_TEXTO[self.count] == self.Wizard.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(2)


    @then("The Wizard opens I click the Comenzar button")
    def step_impl(self):
        self.Texto_Wizard = self.driver.find_elements(By.XPATH,
                                                      "/html/body/div[3]/div/app-amx-files/app-wizard-popup/div[3]/div/div/div[1]/div/div[2]")
        self.count = 0

        for self.Wizard in self.Texto_Wizard:
            RESULTADO_TEXTO = ['Descubre las funciones principales de Claro drive con este tutorial.']
            assert RESULTADO_TEXTO[self.count] == self.Wizard.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(2)


        Register.get_elements(self, "Wizard_BTN_Comenzar").click()
        time.sleep(2)


    @step("I click button Cerrar Wizard")
    def step_impl(self):
        Register.get_elements(self, "Wizard_BTN_Saltar").click()
        time.sleep(3)


    @step("I click button Saltar Wizard")
    def step_impl(self):
        Register.get_elements(self, "Wizard_BTN_Saltar").click()
        time.sleep(5)
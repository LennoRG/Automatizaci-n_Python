# -*- coding: utf-8 -*-
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestLanding_001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()


    def testLanding_001(self):
        self.driver.get("https://test-portal.clarodrive.com/")
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[1]")\
            .click() #DESCUBRE
        #MENSAJE_01 = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container1/div/div/div[1]/div/div/text()[1]")\
         #   .text
        #print(MENSAJE_01)

        #assert MENSAJE_01 == "Te presentamos el espacio ideal para compartir tu mundo digital entre amigos, familia y compañeros de trabajo. ",\
         #   "EL TEXTO NO COINCIDE"

        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[2]")\
            .click() #COMPARTE
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[3]")\
            .click() #DESCUBRE
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[4]")\
            .click() #DESCARGA
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[5]")\
            .click() #OPCIONES
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[6]")\
            .click() #PLANES
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-nav-bar/div/div/app-menu-navbar/div/div[7]")\
            .click() #NEGOCIO
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/header/div[1]")\
            .click() #LOGOCLARO DRIVE


        #FOOTER LANDING

        MENSAJE_AYUDA = self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[1]/div[1]").text
        print(MENSAJE_AYUDA)
        assert MENSAJE_AYUDA == "Ayuda", "MENSAJE NO COINCIDE"
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[1]/div[2]").click() #CENTRO DE AYUDA
        time.sleep(5)
        #self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0]) #Regreso a la pestaña 0
        time.sleep(3)

        #self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[1]/div[3]").click() #CORREO ELECTRONICO

        MENSAJE_FormaPago = self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/div[1]").text #FORMAS PAGO
        print(MENSAJE_FormaPago)
        assert MENSAJE_FormaPago == "Formas de Pago", "MENSAJE NO COINCIDE"
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/a[1]").click() #TELMEX
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/a[2]").click() #TELCEL
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/a[3]").click() #TDC
        time.sleep(5)

        MENSAJE_LEGALES = self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[3]/div").text  #LEGALES
        print(MENSAJE_LEGALES)
        assert MENSAJE_LEGALES == "Legales", "MENSAJE NO COINCIDE"
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[3]/a[1]").click() #ACERCA DE
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[3]/a[2]").click() #TERMINOS Y CONDICIONES
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[3]/a[3]").click() #POLITICA DE PRIVACIDAD
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        MENSAJE_CERTIFICACIONES = self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/div[2]").text #LEGALES
        print(MENSAJE_CERTIFICACIONES)
        assert MENSAJE_CERTIFICACIONES == "Certificaciones", "MENSAJE NO COINCIDE"
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[2]/div[3]/span").click() #SECURITY STANDARD

        MENSAJE_COPYRIGHT = self.driver.find_element_by_xpath("/html/body/app-copyright/div").text #COPYRIGHT
        print(MENSAJE_COPYRIGHT)
        assert MENSAJE_COPYRIGHT == "Claro drive © 2020 AMX Contenido S.A. de C.V.", "MENSAJE NO COINCIDE"
        time.sleep(3)

        MENSAJE_DESCARGA = self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[4]/div").text #DESCARGA APLICACION
        print(MENSAJE_DESCARGA)
        assert MENSAJE_DESCARGA == "Descarga la aplicación", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[4]/a[1]").click() #GOOGLE PLAY
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0]) #REGRESO A LA PESTAÑA 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[4]/a[2]").click() #APP STORE
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # REGRESO A LA PESTAÑA 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/app-footer-landing/footer/div[4]/a[3]").click() #CLARO DRIVE PARA WINDOWS Y MAC
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # REGRESO A LA PESTAÑA 0

        time.sleep(10)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

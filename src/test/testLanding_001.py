# -*- coding: utf-8 -*-
import unittest

import time
from selenium import webdriver


class TestLanding_001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()


    def testLanding_001(self):
        self.driver.get("https://test-portal.clarodrive.com/")
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container1/div/div/div[1]/div")\
            .click() #DESCUBRE
        #MENSAJE_01 = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container1/div/div/div[1]/div/div/text()[1]")\
         #   .text
        #print(MENSAJE_01)

        #assert MENSAJE_01 == "Te presentamos el espacio ideal para compartir tu mundo digital entre amigos, familia y compañeros de trabajo. ",\
         #   "EL TEXTO NO COINCIDE"

        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[2]")\
            .click() #COMPARTE
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[3]")\
            .click() #DESCUBRE
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[4]")\
            .click() #DESCARGA
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[5]")\
            .click() #OPCIONES
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[6]")\
            .click() #PLANES
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[7]")\
            .click() #NEGOCIO
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/header/div[1]")\
            .click() #LOGOCLARO DRIVE


        #FOOTER LANDING

        MENSAJE_AYUDA = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/div[1]").text
        print(MENSAJE_AYUDA)
        assert MENSAJE_AYUDA == "Ayuda", "MENSAJE NO COINCIDE"

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/div[2]/a").click() #CENTRO DE AYUDA
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/a").click() #CORREO ELECTRONICO

        MENSAJE_FormaPago = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/div[1]").text #FORMAS PAGO
        print(MENSAJE_FormaPago)
        assert MENSAJE_FormaPago == "Formas de Pago", "MENSAJE NO COINCIDE"

        time.sleep(30)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

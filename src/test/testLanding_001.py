# -*- coding: utf-8 -*-
import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLanding_001(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()


    def testLanding_001(self):
        self.driver.get("https://test-portal.clarodrive.com/")
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-logreg/div/a[1]")\
            .click() #REGISTRATE BTN SUPERIOR DERECHA
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-logreg/div/a[2]")\
            .click() #INICIO SESION  SUPERIOR DERECHA
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/app-login/app-telmex-login/app-button-text[2]").click() #BTN CANCELAR
        time.sleep(5)

        #FUNCIONALIDADES DEL BTN 100GB TELCEL O TELMEX
        self.driver.find_element_by_id("free").click() #BTN 100GB TELCEL O TELMEX
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[2]").click() #TELCEL
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[1]").click() #TELMEX

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/app-login/app-telmex-register/app-button-text").click() #BTN CANCELAR
        time.sleep(3)

        #FUNCIONALIDADES DEL BTN REGISTRATE
        self.driver.find_element_by_id("register").click() #BTN REGISTRATE
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[2]").click() #TELCEL
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[3]").click() #CLARO MUSICA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[4]").click() #CLARO VIDEO
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[5]").click() #CORREO
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[1]").click() #TELMEX
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/app-login/app-telmex-register/app-button-text").click()  #BTN CANCELAR
        time.sleep(3)

        #FUNCIONALIDADES BTN INICIA SESION
        self.driver.find_element_by_id("login").click() #BTN LOGIN LANDING
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[2]").click() #TELCEL
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[3]").click() #CLARO MUSICA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[4]").click() #CLARO VIDEO
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[5]").click() #CORREO
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[1]").click() #TELMEX
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/app-login/app-telmex-login/app-button-text[2]").click()  #BTN CANCELAR
        time.sleep(3)



        #FUNCIONALIDADES BARRA DE OPCIONES DE LANDING
        self.OPCIONES_LANDING = self.driver.find_elements(By.CLASS_NAME, "Menu ng-star-inserted")
        self.count = 0

        for self.OPC in self.OPCIONES_LANDING:
            RESULTADO_OPCIONES = ['Descubre', 'Comparte', 'Respalda', 'Descarga',
                                  'Opciones', 'Planes', 'Negocio']
            assert RESULTADO_OPCIONES[self.count] == self.OPC.text, "EL TEXTO OPCIONES NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)



        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[1]")\
            .click() #DESCUBRE

        '''self.TEXTO_DESCUBRE = self.driver.find_elements(By.CLASS_NAME, "wrapper")
        self.count = 0

        for self.TEX in self.TEXTO_DESCUBRE:
            RESULTADO_TEXTO = ['Te presentamos el espacio ideal para compartir tu mundo digital entre amigos, familia y compañeros de trabajo.  Claro drive es la mejor opción para guardar fotos, videos, música, documentos y más, de manera segura.']

            assert RESULTADO_TEXTO[self.count] == self.TEX.text, "EL TEXTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)'''


        ''' MENSAJE_01 = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container1/div/div/div[1]/div/div/text()[1]")\
            .text
        print(MENSAJE_01)

        assert MENSAJE_01 == "Te presentamos el espacio ideal para compartir tu mundo digital entre amigos, familia y compañeros de trabajo. ",\
            "EL TEXTO NO COINCIDE" '''

        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[2]")\
            .click() #COMPARTE
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[3]")\
            .click() #DESPALDA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[4]")\
            .click() #DESCARGA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[5]")\
            .click() #OPCIONES
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[6]")\
            .click() #PLANES
        time.sleep(3)

        ######## COMPARO EL NUMERO DE PLANES DENTRO DE UN FOR ########
        self.PLAN_TELCEL = self.driver.find_elements(By.CLASS_NAME, "Capacity")
        self.count = 0

        for self.PLAN_ in self.PLAN_TELCEL:
            RESULDADO_PLAN = ['100GB', '200GB', '300GB', '1024GB']
            assert RESULDADO_PLAN[self.count] == self.PLAN_.text, "EL NUMERO DE PLANES NO COINCIDEN"
            self.count = self.count + 1
        time.sleep(3)
        ######## TERMINO DE COMPARAR EL NUMERO DE PLANES DENTRO DE UN FOR ########

        ####### COMPARO TEXTO PERIDO DE PLANES #####
        self.PERIODO_TELCEL = self.driver.find_elements(By.CLASS_NAME, "Period")
        self.count = 0

        for self.PER in self.PERIODO_TELCEL:
            PERIODO_RESULTADO = ['SIN COSTO', 'MENSUAL', 'MENSUAL', 'MENSUAL']
            assert PERIODO_RESULTADO[self.count] == self.PER.text, "EL TEXTO PERIODO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)
        ####### TERMINI DE COMPARAR TEXTO PERIDO DE PLANES #####

        ##### COMPARO COSTO POR MES ######
        self.COSTO_TELCEL = self.driver.find_elements(By.CLASS_NAME, "Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
        self.count = 1

        for self.COS in self.COSTO_TELCEL:
            RESULTADO_COSTO = ['$19.00 MXN', '$36.00 MXN', '$169.00 MXN']
            assert RESULTADO_COSTO[self.count] == self.COS.text, "EL TEXTO DEL COSTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)
        ###### TERMINO DE COMPARAR COSTO POR MES ######

        TEXTO_TELCEL = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/div[2]/div[2]/div").text
        print(TEXTO_TELCEL)
        assert TEXTO_TELCEL == "Con tu número Telcel", "TEXTO NO COINCIDE"
        time.sleep(3)

        #### ACCION DE BOTONES CONTRATADO AHORA TELCEL ####
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/a/div")\
            .click() #BTN 100GB
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)") #SCROLL BAJO A LOS PLANES
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[2]/a/div")\
            .click() #BTN 200GB
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[3]/a/div")\
            .click() #BTN 300GB
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[4]/a/div")\
            .click() #BTN 1024GB
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[6]").click() #PLANES
        time.sleep(3)
        #### TERMINA ACCION DE BOTONES CONTRATADO AHORA TELCEL ####


        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/div/div[2]")\
            .click() #PLAN TELMEX
        time.sleep(3)

        ######## COMPARO EL NUMERO DE PLANES DENTRO DE UN FOR ########
        self.PLAN_TELMEX = self.driver.find_elements(By.CLASS_NAME, "Capacity")
        self.count = 0

        for self.PLAN_T in self.PLAN_TELMEX:
            RESUL_PLAN = ['100GB', '200GB', '300GB', '1024GB']
            assert RESUL_PLAN[self.count] == self.PLAN_T.text, "EL NUMERO DE PLAN NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        TEXTO_TELMEX = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/div[2]/div[2]").text
        print(TEXTO_TELMEX)
        assert TEXTO_TELMEX == "Con tu número Telmex", "TEXTO NO COINCIDE"
        time.sleep(3)
        ######## TERMINO DE COMPARAR EL NUMERO DE PLANES DENTRO DE UN FOR ########

        ##### COMPARO COSTO POR MES ######
        self.COSTO_TELMEX = self.driver.find_elements(By.CLASS_NAME, "Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
        self.count = 0

        for self.COST in self.COSTO_TELMEX:
            RESULTADO_COST = ['$19.00 MXN', '$36.00 MXN', '$169.00 MXN']
            assert RESULTADO_COST[self.count] == self.COST.text, "EL TEXTO COSTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)
        ##### TERMINO DE COMPARAR COSTO POR MES ######

        ####### COMPARO PERIDO TELMEX ######
        self.PERIODO_TELMEX = self.driver.find_elements(By.CLASS_NAME, "Period")
        self.count = 0

        for self.PERI in self.PERIODO_TELMEX:
            PERI_RESULTADO = ['SIN COSTO', 'MENSUAL', 'MENSUAL', 'MENSUAL']
            assert PERI_RESULTADO[self.count] == self.PERI.text, "EL TEXTO PERIODO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)
        #### TERMINO DE COMPARAR PERIODO TELMEX ######

        #### ACCION DE BOOTONES CONTRATAR TELMEX ###
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/a/div")\
            .click() #BTN 100GB
        time.sleep(2)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[2]/a/div")\
            .click() #BTN 200GB
        time.sleep(2)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[3]/a/div")\
            .click() #BTN 300GB
        time.sleep(2)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[4]/a/div")\
            .click() #BTN 1024GB
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[6]")\
            .click()  #PLANES
        time.sleep(3)

        #### TERMINA ACCION DE DE BOTONES CONTRATAR TELMX ###



        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/div/div[3]")\
            .click() #PLAN TDC
        time.sleep(3)

        self.PLAN_TDC = self.driver.find_elements(By.CLASS_NAME, "Capacity")
        self.count = 0

        for self.PLAN_C in self.PLAN_TDC:
            RESULT_PLAN = ['200GB', '300GB', '1024GB']
            assert RESULT_PLAN[self.count] == self.PLAN_C.text, "EL NUMERO DE PLAN  NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        self.COSTO_TDC = self.driver.find_elements(By.CLASS_NAME, "Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
        self.count = 0

        for self.COSTO in self.COSTO_TDC:
            RESULTADO_COS = ['$19.00 MXN', '$36.00 MXN', '$169.00 MXN']
            assert RESULTADO_COS[self.count] == self.COSTO.text, "EL TEXTO DEL COSTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        self.PERIODO_TDC = self.driver.find_elements(By.CLASS_NAME, "Period")
        self.count = 0

        for self.PERIO in self.PERIODO_TDC:
            PERIO_RESULTADO = ['MENSUAL', 'MENSUAL', 'MENSUAL']
            assert PERIO_RESULTADO[self.count] == self.PERIO.text, "EL TEXTO PERIODO MENSUAL NO COINCIDEN"
            self.count = self.count + 1
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/a/div")\
            .click() #BTN 200GG CONTRATALO TDC
        time.sleep(2)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[2]/a/div")\
            .click() #BTN 300GB CONTRATALO TDC
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[3]/a/div")\
            .click() #BTN 1024GB CONTRATALO TDC
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[6]")\
            .click() #PLANES
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/div/div[1]")\
            .click()  #REGRESO AL PLAN TELCEL
        time.sleep(3)


        #self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-nav-bar/div/div/app-menu-navbar/div/div[7]")\
         #   .click() #NEGOCIO
        #time.sleep(5)
        #self.driver.find_element_by_xpath("/html/body/div[3]/app-root/app-microsite-wrapper/app-nav-bar/div/div/div[2]").click() #LOGOCLARO DRIVE
        #time.sleep(3)


        #FOOTER LANDING
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        MENSAJE_AYUDA = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/div[1]").text
        print(MENSAJE_AYUDA)
        assert MENSAJE_AYUDA == "Ayuda", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/div[2]").click() #CENTRO DE AYUDA
        time.sleep(3)
        #self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0]) #Regreso a la pestaña 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/a").click() #CORREO ELECTRONICO

        MENSAJE_FormaPago = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/div[1]").text #FORMAS PAGO
        print(MENSAJE_FormaPago)
        assert MENSAJE_FormaPago == "Formas de Pago", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/a[1]").click() #TELMEX
        time.sleep(5)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/a[2]").click() #TELCEL
        time.sleep(5)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/a[3]").click() #TDC
        time.sleep(5)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        MENSAJE_LEGALES = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[3]/div").text  #LEGALES
        print(MENSAJE_LEGALES)
        assert MENSAJE_LEGALES == "Legales", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[3]/a[1]").click() #ACERCA DE
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[3]/a[2]").click() #TERMINOS Y CONDICIONES
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[3]/a[3]").click() #POLITICA DE PRIVACIDAD
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)

        MENSAJE_CERTIFICACIONES = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/div[2]").text #CERTIFICACIONES
        print(MENSAJE_CERTIFICACIONES)
        assert MENSAJE_CERTIFICACIONES == "Certificaciones", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/div[3]").click() #SECURITY STANDARD

        MENSAJE_COPYRIGHT = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-copyright/div").text #COPYRIGHT
        print(MENSAJE_COPYRIGHT)
        assert MENSAJE_COPYRIGHT == "Claro drive © 2020 AMX Contenido S.A. de C.V.", "MENSAJE NO COINCIDE"
        time.sleep(3)

        MENSAJE_DESCARGA = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[4]/div").text #DESCARGA APLICACION
        print(MENSAJE_DESCARGA)
        assert MENSAJE_DESCARGA == "Descarga la aplicación", "MENSAJE NO COINCIDE"
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[4]/a[1]").click() #GOOGLE PLAY
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0]) #REGRESO A LA PESTAÑA 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[4]/a[2]").click() #APP STORE
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  #REGRESO A LA PESTAÑA 0
        time.sleep(3)


        #HEADER
        self.RED_CLARO = self.driver.find_elements(By.CLASS_NAME, "RedClaroSub")
        self.count = 0

        for self.RED_ in self.RED_CLARO:
            RESULTADO_RED = ['Claro video', 'Claro música', 'Claro shop']
            assert RESULTADO_RED[self.count] == self.RED_.text, "LOS TEXTOS NO COINCIDES"
            self.count = self.count + 1
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-elinks/div/div[2]/span[1]").\
            click() #CLARO VIDEO
        self.driver.switch_to.window(self.driver.window_handles[0])  #REGRESO A LA PESTAÑA 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-elinks/div/div[2]/span[3]").\
            click()  #CLARO MUSICA
        self.driver.switch_to.window(self.driver.window_handles[0])  #REGRESO A LA PESTAÑA 0
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-elinks/div/div[2]/div").\
            click() #CLARO SHOP
        self.driver.switch_to.window(self.driver.window_handles[0]) #REGRESO A LA PESTAÑA 0
        time.sleep(3)


        #FUNCIONALIDAD COMBOBOX PAISES
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/div").click()  #COMBOBOX PAISES
        time.sleep(5)

        ######## COMPARO LOS NOMBRE DE LOS PAISES DENTRO DE UN FOR ########
        self.PAISES = self.driver.find_elements(By.CLASS_NAME, "CB-NAME")
        self.count = 1

        for self.PAI in self.PAISES:
            RESULTADO_ESPERADO = ['México', 'Colombia', 'Brasil', 'Guatemala',
                                  'Honduras', 'Nicaragua', 'El Salvador',
                                  'Costa Rica', 'Perú', 'Argentina', 'Panamá', 'Chile',
                                  'Ecuador', 'Puerto Rico', 'República Dominicana', 'Uruguay'
                                  'Paraguay']
            assert RESULTADO_ESPERADO[self.count] == self.PAI.text, "LOS NOMBRES DE PAISES NO COINCIDEN"
            self.count = self.count + 1
        ######## TERMINO DE COMPARAR LOS NOMBRE DE LOS PAISES ########

        #self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/div").click() #COMBOBOX PAISES
        time.sleep(5)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/app-countries/div/app-country-button[2]/div")\
            .click() #COLOMBIA
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)") #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/div").click() #COMBOBOX PAISES
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/app-countries/div/app-country-button[3]/div")\
            .click() #BRASIL
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)") #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/div").click() #COMBOBOX PAISES
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/app-countries/div/app-country-button[4]/div")\
            .click() #GUATEMALA
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)") #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/div").click() #COMBOBOX PAISES
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-top-bar/app-dropdown/app-countries/div/app-country-button[1]/div")\
            .click() #MEXICO
        time.sleep(3)
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)


        #FOOTER
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[4]/a[3]").click()  #CLARO DRIVE PARA WINDOWS Y MAC
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  #REGRESO A LA PESTAÑA 0

        time.sleep(10)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

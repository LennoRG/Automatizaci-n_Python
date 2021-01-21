# -*- coding: utf-8 -*-
import time
from behave import *

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from fuctions.Functions import Functions as Landing
from fuctions.Inicializar import Inicializar
from selenium.webdriver.common.by import By

#comentario


use_step_matcher("re")

class Landing_CD(Landing):
    @given("Open the application Claro drive")
    def abrir_navegador(self):
        Landing.abrir_navegador(self)


    @when("I charge the Json of the App: landing\.json")
    def cargo_Json(self):
        Landing.get_json_file(self, "landing")


    @then("I click Inicio sesion")
    def step_impl(self):
        Landing.get_elements(self, "BTN_IniciaSesion").click()
        time.sleep(5)


    @step("I click in partner Telmex")
    def step_impl(self):
        Landing.get_elements(self, "Partner_Telmex").click()
        time.sleep(5)


    @then("I click in partner Telcel")
    def step_impl(self):
        Landing.get_elements(self, "Partner_Telcel").click()
        time.sleep(3)


    @then("I click in partner Claro musica")
    def step_impl(self):
        Landing.get_elements(self, "Partner_ClaroMusica")
        time.sleep(3)


    @then("I click in partner Claro video")
    def step_impl(self):
        Landing.get_elements(self, "Partner_ClaroVideo").click()
        time.sleep(3)


    @then("I click in Correo")
    def step_impl(self):
        Landing.get_elements(self, "Correo").click()
        time.sleep(3)


    @step("I click Iniciar Sesion")
    def step_impl(self):
        Landing.get_elements(self, "BTN_IniciarSesion").click()
        time.sleep(3)


    @then("I click Olvidaste tu contraseña")
    def step_impl(self):
        Landing.get_elements(self, "OlvidasteContra").click()
        time.sleep(5)


    @then("I click Cancelar")
    def step_impl(self):
        Landing.get_elements(self, "Cancelar").click()
        time.sleep(5)


    @when("The window will open click ENVIAR")
    def step_impl(self):
        Landing.get_elements(self, "Enviar_Contra").click()
        time.sleep(3)


    @then("I click Volver a inicio")
    def step_impl(self):
        Landing.get_elements(self, "VolverInicio").click()
        time.sleep(5)

    @when("I click Registrarme")
    def step_impl(self):
        Landing.get_elements(self, "Registrarme").click()
        time.sleep(3)


    @step("I click in Terminos y condiciones")
    def step_impl(self):
        Landing.get_elements(self, "TerminosCond").click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña principal
        time.sleep(5)


    @then("I click in Politicas privacidad")
    def step_impl(self):
        Landing.get_elements(self, "PoliticaPrivacidad").click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)


    @then("I click button Registrame")
    def step_impl(self):
        Landing.get_elements(self, "BTN_Registrarme").click()
        time.sleep(3)


    @then("In click in button Cancelar")
    def step_impl(self):
        Landing.get_elements(self, "BTN_Cancelar").click()
        time.sleep(3)

        # FUNCIONALIDADES BARRA DE OPCIONES DE LANDING
        self.OPCIONES_LANDING = self.driver.find_elements(By.CLASS_NAME, "Menu ng-star-inserted")
        self.count = 0

        for self.OPC in self.OPCIONES_LANDING:
            RESULTADO_OPCIONES = ['Descubre', 'Comparte', 'Respalda', 'Descarga',
                                  'Opciones', 'Planes', 'Negocio']
            assert RESULTADO_OPCIONES[self.count] == self.OPC.text, "EL TEXTO OPCIONES NO COINCIDE"
            print(RESULTADO_OPCIONES)
            self.count = self.count + 1
        time.sleep(3)

    @then("I click Descubre")
    def step_impl(self):
        Landing.get_elements(self, "Descubre").click()
        time.sleep(3)


    @then("I click Comparte")
    def step_impl(self):
        Landing.get_elements(self, "Comparte").click()
        time.sleep(3)

        self.Texto_Comparte = self.driver.find_elements(By.XPATH,
                                                        "/html/body/div[4]/app-root/app-landing-wrapper/app-container2/div/div/div/div[1]/div[1]")
        self.count = 0

        for self.Comparte in self.Texto_Comparte:
            RESULTADO_TEXTO = [
                'Claro drive contigo']
            assert RESULTADO_TEXTO[self.count] == self.Comparte.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(2)

        self.Texto_ComparteText = self.driver.find_elements(By.XPATH,
                                                        "/html/body/div[4]/app-root/app-landing-wrapper/app-container2/div/div/div/div[1]/div[2]")
        self.count = 0

        for self.ComparteText in self.Texto_ComparteText:
            RESULTADO_TEXTO = [
                'Claro drive te regala 100GB de almacenamiento para empezar a compartir tu contenido a donde sea que vayas y desde cualquier dispositivo.']
            assert RESULTADO_TEXTO[self.count] == self.ComparteText.text, "EL TEXTO NO COINCIDE (Segundo Texto)"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)


    @then("I click Respalda")
    def step_impl(self):
        Landing.get_elements(self, "Respalda").click()
        time.sleep(3)

        self.Texto_Respalda = self.driver.find_elements(By.XPATH,
                                                            "/html/body/div[4]/app-root/app-landing-wrapper/app-container3/div/div/div[1]/div[1]")
        self.count = 0

        for self.Respalda in self.Texto_Respalda:
            RESULTADO_TEXTO = [
                'No pierdas tus fotos']
            assert RESULTADO_TEXTO[self.count] == self.Respalda.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)

        self.Texto_RespaldaText = self.driver.find_elements(By.XPATH,
                                                            "/html/body/div[4]/app-root/app-landing-wrapper/app-container3/div/div/div[1]/div[2]")
        self.count = 0

        for self.RespaldaText in self.Texto_RespaldaText:
            RESULTADO_TEXTO = [
                'En Claro drive es muy sencillo crear tu álbum, compartirlo y organizarlo. Puedes buscar fotos por fecha o evento, y respaldarlas en tu dispositivo móvil.']
            assert RESULTADO_TEXTO[self.count] == self.RespaldaText.text, "EL TEXTO NO COINCIDE (Segundo Texto)"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)


    @when("I click Descarga")
    def step_impl(self):
        Landing.get_elements(self, "Descarga").click()
        time.sleep(3)

        self.Texto_Descarga = self.driver.find_elements(By.XPATH,
                                                        "/html/body/div[4]/app-root/app-landing-wrapper/app-container4/div/div/div[1]/div[1]")
        self.count = 0

        for self.Descarga in self.Texto_Descarga:
            RESULTADO_TEXTO = ['Claro drive para todos']
            assert RESULTADO_TEXTO[self.count] == self.Descarga.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)

        self.Texto_DescargaText = self.driver.find_elements(By.XPATH,
                                                            "/html/body/div[4]/app-root/app-landing-wrapper/app-container4/div/div/div[1]/div[2]")
        self.count = 0

        for self.DescargaText in self.Texto_DescargaText:
            RESULTADO_TEXTO = ['Disponible en Google Play, iOS']
            assert RESULTADO_TEXTO[self.count] == self.DescargaText.text, "EL TEXTO NO COINCIDE (Segundo Texto)"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)


    @then("I click Google play")
    def step_impl(self):
        Landing.get_elements(self, "Descarga_GooglePlay").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña principal
        time.sleep(5)


    @then("I click App Store")
    def step_impl(self):
        Landing.get_elements(self, "Descarga_AppStore").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)


    '''@then("I click Claro drive")
    def step_impl(self):
        Landing.get_elements(self, "Descarga_ClaroDrive").click()
        time.sleep(5)
        Landing.get_elements(self, "Descarga_ClaroDrive_Imagen").click()
        time.sleep(5)'''


    @when("I click Opciones")
    def step_impl(self):
        Landing.get_elements(self, "Opciones").click()
        time.sleep(3)

        self.Texto_Opciones = self.driver.find_elements(By.XPATH,
                                                        "/html/body/div[4]/app-root/app-landing-wrapper/app-container5/div/div/div[1]/div[1]")
        self.count = 0

        for self.Opciones in self.Texto_Opciones:
            RESULTADO_TEXTO = ['¡Comienza ahora!']
            assert RESULTADO_TEXTO[self.count] == self.Opciones.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)

        self.Texto_OpcionesText = self.driver.find_elements(By.XPATH,
                                                            "/html/body/div[4]/app-root/app-landing-wrapper/app-container5/div/div/div[1]/div[2]")
        self.count = 0

        for self.OpcionesText in self.Texto_OpcionesText:
            RESULTADO_TEXTO = ['Elige una opción para registrarte']
            assert RESULTADO_TEXTO[self.count] == self.OpcionesText.text, "EL TEXTO NO COINCIDE (Segundo Texto)"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)


    @then("I click option Telmex")
    def step_impl(self):
        Landing.get_elements(self, "Opciones_Telmex").click()
        time.sleep(3)


    @then("I click option Telcel")
    def step_impl(self):
        Landing.get_elements(self, "Opciones_Telcel").click()
        time.sleep(3)


    @then("I click option Claro musica")
    def step_impl(self):
        Landing.get_elements(self, "Opciones_CM").click()
        time.sleep(3)


    @then("I click option Claro video")
    def step_impl(self):
        Landing.get_elements(self, "Opciones_CV").click()
        time.sleep(3)


    @then("I click option Correo")
    def step_impl(self):
        Landing.get_elements(self, "Opciones_Correo").click()
        time.sleep(3)


    @when("I click Planes")
    def step_impl(self):
        Landing.get_elements(self, "Planes").click()
        time.sleep(3)

        self.Texto_Planes = self.driver.find_elements(By.XPATH,
                                                       "/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/div/div[1]")
        self.count = 0

        for self.Planes in self.Texto_Planes:
            RESULTADO_TEXTO = ['¿Necesitas más espacio?']
            assert RESULTADO_TEXTO[self.count] == self.Planes.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)

        self.Texto_PlanesText = self.driver.find_elements(By.XPATH,
                                                            "/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/div/div[2]")
        self.count = 0

        for self.PlanesText in self.Texto_PlanesText:
            RESULTADO_TEXTO = [
                'Para llevar tus archivos a donde quieras, es probable que necesites un plan a tu medida. Por ello te ofrecemos planes flexibles en los que instantáneamente obtendrás una mayor capacidad de almacenamiento en la nube.']
            assert RESULTADO_TEXTO[self.count] == self.PlanesText.text, "EL TEXTO NO COINCIDE (Segundo Texto)"
            print(RESULTADO_TEXTO)
            # self.count = self.count + 1
        time.sleep(3)


    @then("I click plan TDC")
    def step_impl(self):
        Landing.get_elements(self, "Planes_Correo").click()
        time.sleep(3)

        self.PLAN_TDC = self.driver.find_elements(By.CLASS_NAME, "Capacity")
        self.count = 0

        for self.PLAN_C in self.PLAN_TDC:
            RESULT_PLAN = ['200GB', '300GB', '1024GB']
            assert RESULT_PLAN[self.count] == self.PLAN_C.text, "EL NUMERO DE PLAN  NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        self.COSTO_TDC = self.driver.find_elements(By.CLASS_NAME,
                                                   "Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
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


    @then("I click plan Telmex")
    def step_impl(self):
        Landing.get_elements(self, "Planes_Telmex").click()
        time.sleep(3)

        ######## COMPARO EL NUMERO DE PLANES DENTRO DE UN FOR ########
        self.PLAN_TELMEX = self.driver.find_elements(By.CLASS_NAME, "Capacity")
        self.count = 0

        for self.PLAN_T in self.PLAN_TELMEX:
            RESUL_PLAN = ['100GB', '200GB', '300GB', '1024GB']
            assert RESUL_PLAN[self.count] == self.PLAN_T.text, "EL NUMERO DE PLAN NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        TEXTO_TELMEX = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/div[2]/div[2]").text
        print(TEXTO_TELMEX)
        assert TEXTO_TELMEX == "Con tu número Telmex", "TEXTO NO COINCIDE"
        time.sleep(3)
        ######## TERMINO DE COMPARAR EL NUMERO DE PLANES DENTRO DE UN FOR ########

        ##### COMPARO COSTO POR MES ######
        self.COSTO_TELMEX = self.driver.find_elements(By.CLASS_NAME,"Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
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

    @then("I click plan Telcel")
    def step_impl(self):
        Landing.get_elements(self, "Planes_Telcel").click()
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
        self.COSTO_TELCEL = self.driver.find_elements(By.CLASS_NAME,"Offers ng-tns-c22-1 ng-trigger ng-trigger-togglePlans ng-star-inserted")
        self.count = 1

        for self.COS in self.COSTO_TELCEL:
            RESULTADO_COSTO = ['$19.00 MXN', '$36.00 MXN', '$169.00 MXN']
            assert RESULTADO_COSTO[self.count] == self.COS.text, "EL TEXTO DEL COSTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)
        ###### TERMINO DE COMPARAR COSTO POR MES ######
        TEXTO_TELCEL = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/div[2]/div[2]/div").text
        print(TEXTO_TELCEL)
        assert TEXTO_TELCEL == "Con tu número Telcel", "TEXTO NO COINCIDE"
        time.sleep(3)

        '''TEXTO_TELCEL25 = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-container6/div/div/app-offer/div/app-payment-methods/app-plans/div[1]/div[2]/div[2]/div").text
        print(TEXTO_TELCEL25)
        assert TEXTO_TELCEL25 == "Con tu número Telcel", "TEXTO NO COINCIDE"
        time.sleep(3)'''


    @when("I click Negocio")
    def step_impl(self):
        Landing.get_elements(self, "Negocio").click()
        time.sleep(5)


    @then("I click negocio Caracteristicas")
    def step_impl(self):
        Landing.get_elements(self, "Negocio_Caracteristicas").click()
        time.sleep(3)


    @then("I click negocio Descarga")
    def step_impl(self):
        Landing.get_elements(self, "Negocio_Descarga").click()
        time.sleep(3)


    @then("I click negocio Planes")
    def step_impl(self):
        Landing.get_elements(self, "Negocio_Planes").click()
        time.sleep(3)



    @then("I click Claro dirve personal")
    def step_impl(self):
        Landing.get_elements(self, "Negocio_ClaroDrive").click()
        time.sleep(10)


    @then("I click Link footer Centro de ayuda")
    def step_impl(self):
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")  # SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_AYUDA = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[1]/div[1]").text
        print(TEXTO_AYUDA)
        assert TEXTO_AYUDA == "Ayuda", "MENSAJE NO COINCIDE"
        time.sleep(2)

        TEXTO_CentroAyuda = Landing.get_elements(self, "Footer_CentroAyuda").text
        print(TEXTO_CentroAyuda)
        assert TEXTO_CentroAyuda == "Centro de ayuda", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_CentroAyuda").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)


    @then("I click Link footer Correo electronico")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_COPYRIGHT = self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/app-copyright/div/div").text  # COPYRIGHT
        print(TEXTO_COPYRIGHT)
        assert TEXTO_COPYRIGHT == "Claro drive © 2020 AMX Contenido S.A. de C.V.", "MENSAJE NO COINCIDE"
        time.sleep(3)

        TEXTO_Correo = Landing.get_elements(self, "Footer_CorreoElectronico").text  #FORMAS PAGO
        print(TEXTO_Correo)
        assert TEXTO_Correo == "Correo electrónico", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_CorreoElectronico").click()
        time.sleep(10)



    @then("I click Link footer Forma de pago Telmex")
    def step_impl(self):
        TEXTO_FormaPago = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[2]/div[1]").text  #FORMAS PAGO
        print(TEXTO_FormaPago)
        assert TEXTO_FormaPago == "Formas de Pago", "MENSAJE NO COINCIDE"
        time.sleep(3)

        TEXTO_Telmex = Landing.get_elements(self, "Footer_Telmex").text  #FORMAS PAGO
        print(TEXTO_Telmex)
        assert TEXTO_Telmex == "Telmex", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_Telmex").click()
        time.sleep(3)


    @then("I click Link footer Forma de pago Telcel")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_Telcel = Landing.get_elements(self, "Footer_Telcel").text  # FORMAS PAGO
        print(TEXTO_Telcel)
        assert TEXTO_Telcel == "Telcel", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_Telcel").click()
        time.sleep(3)


    @then("I click Link footer Forma de pago TDC")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_TDC = Landing.get_elements(self, "Footer_TDC").text  #FORMAS PAGO
        print(TEXTO_TDC)
        assert TEXTO_TDC == "Tarjeta de crédito", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_TDC").click()
        time.sleep(3)


    @then("I click Link footer Acerca de")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_LEGALES = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[3]/div").text  # LEGALES
        print(TEXTO_LEGALES)
        assert TEXTO_LEGALES == "Legales", "MENSAJE NO COINCIDE"
        time.sleep(2)

        TEXTO_AcercaDe = Landing.get_elements(self, "Footer_Acercade").text  #FORMAS PAGO
        print(TEXTO_AcercaDe)
        assert TEXTO_AcercaDe == "Acerca de", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_Acercade").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)


    @then("I click Link footer Terminos y Condicones")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_TerminosCondi = Landing.get_elements(self, "Footer_TerminosCondiciones").text  #FORMAS PAGO
        print(TEXTO_TerminosCondi)
        assert TEXTO_TerminosCondi == "Términos y condiciones", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_TerminosCondiciones").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)


    @then("I click Link footer Politicas de privacidad")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_PoliticasPriv = Landing.get_elements(self, "Footer_PoliticaPrivacidad").text  #FORMAS PAGO
        print(TEXTO_PoliticasPriv)
        assert TEXTO_PoliticasPriv == "Política de privacidad", "MENSAJE NO COINCIDE"
        time.sleep(2)

        Landing.get_elements(self, "Footer_PoliticaPrivacidad").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)


    @then("I click Footer Google play")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  #SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        TEXTO_DESCARGAAPP = self.driver.find_element_by_xpath(
            "/html/body/div[4]/app-root/app-landing-wrapper/app-footer-landing/footer/div[4]/div").text  #DESCARGA APLICACION
        print(TEXTO_DESCARGAAPP)
        assert TEXTO_DESCARGAAPP == "Descarga la aplicación", "MENSAJE NO COINCIDE"
        time.sleep(3)

        Landing.get_elements(self, "Footer_GooglePlay").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)



    @then("I click Footer App Store")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  # SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        Landing.get_elements(self, "Footer_AppStore").click()
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[0])  # Regreso a la pestaña 0
        time.sleep(3)


    @then("I click Footer Desktop Mac Windows")
    def step_impl(self):
        self.driver.execute_script(
            "window.scroll(0,document.body.scrollHeight)")  # SCROLL DOW BAJA AL FINAL DE LA PAGINA
        time.sleep(3)

        Landing.get_elements(self, "Footer_DesktopWindMac").click()
        time.sleep(3)

        Landing.get_elements(self, "Logo_ClaroDrive").click()
        time.sleep(3)



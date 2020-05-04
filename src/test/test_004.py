import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_004(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15) #TIEMPO DE ESPERA DE UN ELEMENTO
        self.driver.maximize_window() #MAXIMIZA LA VENTANA DE WINDOWS

        #VARIABLES GLOBALES DE REGISTRO TDC
        self.NombreTitularTDC = "Automatizacion"
        self.NumTDC = "4523984527360876"
        self.MM = "01"
        self.AA = "22"
        self.CVV = "698"



    def test_004(self):

        nombre = "hola0_1.test@yopmail.com"
        contraseña = "Qa123456$"

        #LANDING
        self.driver.get("https://test-portal.clarodrive.com/")
        self.driver.find_element_by_id("register").click()
        time.sleep(5)

        #PANTALLA REGISTRP
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/div/div[5]").click()
        self.driver.find_element_by_class_name("InputEmail").send_keys(nombre)
        self.driver.find_element_by_class_name("InputPassword").send_keys(contraseña)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[3]/app-partner/app-login/app-mail-register/app-form-simple/form/div[1]/div[2]/app-input-password/p")\
            .click()
        self.driver.find_element_by_class_name("Btn").click()
        self.driver.find_element_by_class_name("Button").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[2]/app-plans/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[2]/app-plans/div/div[1]").click() #PLAN 200GB
        self.driver.find_element_by_class_name("Button").click()
        time.sleep(5)

        #PANTALLA REGISTRO TDC
        self.driver.find_element_by_class_name("InputText").send_keys(self.NombreTitularTDC)
        self.driver.find_element_by_class_name("InputNumber").send_keys(self.NumTDC)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[2]/app-card-request/form/div[1]/div[3]/app-input-credit-card-exp-month/input")\
            .send_keys(self.MM)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[2]/app-card-request/form/div[1]/div[4]/app-input-credit-card-exp-year/input")\
            .send_keys(self.AA)
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div[2]/app-card-request/form/div[1]/div[5]/app-input-credit-card-code/input")\
            .send_keys(self.CVV)
        self.driver.find_element_by_class_name("Button").click()
        time.sleep(5)

        #PANTALLA POPUP MENSAJE DE LISTO
        self.driver.find_element_by_xpath("/html/body/div[4]/app-root/app-landing-wrapper/div/app-onboarding/div/app-success-redirect/div[4]")\
            .click()
        time.sleep(5)

        #Buzon POPUP DE BIENVENIDA BTN PLANES
        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[5]/div[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/header/div[1]/a/div").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[5]/div[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/header/div[1]/a/div").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[5]/div[3]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/header/div[1]/a/div").click()
        time.sleep(3)
        #TERMINA Buzon POPUP DE BIENVENIDA BTN PLANES


        #VALIDAR TEXTO PRINCIPAL CLARO DRIVE (POPUP DE BIENVENIDA)
        self.TXT_PRINCIPAL = self.driver.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div")
        self.count = 0

        for self.TXT_ in self.TXT_PRINCIPAL:
            RESULTADO_ESPERADO = ['Tus archivos contigo, siempre.']
            assert RESULTADO_ESPERADO[self.count] == self.TXT_.text, "EL TEXTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        #TERMINO DE VALIDAR TEXTO PRINCIPAL CLARO DRIVE (POPUP DE BIENVENIDA)

        self.TXT_APP = self.driver.find_elements(By.XPATH, "//TXT[@id='popup']/div[2]")
        self.count = 0

        for self.TXT in self.TXT_APP:
            RESULTADO_APP = ['Descarga la app']
            assert RESULTADO_APP[self.count] == self.TXT.text, "EL TEXTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)

        #FUNCIONALIDAD DE BOTONES CON LOGO#
        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[3]/a[1]")\
            .click() #GOOGLE PLAY
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[3]/a[2]")\
            .click() #APP STORE
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[3]/a[3]")\
            .click() #PARA WINDOWS Y MAC
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])  #Regreso a la pestaña 0
        time.sleep(3)

        #TERMINA FUNCIONALIDAD DE BOTONES CON LOGO#

        #VALIDO ENLACE TERMINOS Y CONDICIONES
        '''self.ENLACE_TERMINOS = self.driver.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[4]")
        self.count = 0

        for self.ENLA in self.ENLACE_TERMINOS:
            RESULTADO_ENLACE = ['Términos y política de privacidad']
            assert RESULTADO_ENLACE[self.count] == self.ENLA.txt, "EL TEXTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(3)'''

        self.driver.find_element_by_link_text("/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[4]")\
            .click() #ENLACE TTERMINOS Y CONDICIONES
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0]) #REGRESO A LA PESTAÑA 0
        time.sleep(2)
        #VALIDO ENLACE TERMINOS Y CONDICIONES

        #VALIDO TEXTO POPUP
        self.TEXT_ALMACENAMIENTO = self.driver.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/text()[1]")
        self.count = 0

        for self.TEXT_A in self.TEXT_ALMACENAMIENTO:
            RESULTADO_TEXT =['¿Necesitas más almacenamiento?']
            assert RESULTADO_TEXT[self.count] == self.TEXT_A.text, "EL TEXTO NO COINCIDE"
            self.count = self.count + 1
        time.sleep(2)

        self.TXT_PLANES = self.driver.find_elements(By.XPATH, "/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/text()[2]")
        self.count = 0

        for self.TXT_P in self.TXT_PLANES:
            RESULTADO_PLANES = ['Estos son nuestros planes:']
            assert RESULTADO_PLANES[self.count] == self.TXT_P.text, "EL TEXTO NO COINCIDE"
            self.count = self.count = 1
        time.sleep(5)

        #TERMINO DE VALIDAR TEXTO POPUP

        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/button[4]")\
            .click() #BTN CERRAR POPUP
        time.sleep(15)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

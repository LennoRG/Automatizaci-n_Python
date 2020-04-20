import unittest
import time
from selenium import webdriver


class Test_004(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15) #TIEMPO DE ESPERA DE UN ELEMENTO
        self.driver.maximize_window() #MAXIMIZA LA VENTANA DE WINDOWS

        #VARIABLES GLOBALES DE REGISTRO TDC
        self.NombreTitularTDC = "Automatizacion Python"
        self.NumTDC = "4523984527360876"
        self.MM = "01"
        self.AA = "22"
        self.CVV = "698"



    def test_004(self):

        nombre = "hola1.test@yopmail.com"
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

        #Buzon POPUP DE BIENVENIDA
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
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/div[2]/button[4]").click()

        time.sleep(30)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

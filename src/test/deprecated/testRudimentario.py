from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys

#INICIALIZO EL DRIVER
driver = webdriver.Chrome()
#VOY AL HOST DE LA APLICACION
driver.get("http://www.python.org")
#SE VERIFICA QUE EL TITULO DE LA APLICACION
assert "Python" in driver.title
time.sleep(20)
#ALMACENO EN UNA VARIABLE EL OBJETO CON QUIEN VOY A INTERACTUAR
elem = driver.find_element_by_id("id-search-field")
#LIMPIO LA CAJA TXT
elem.clear()
#ESCRIBO EN LA CAJA TXT pycon
elem.send_keys("pycon")
time.sleep(10)

#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

#CIERRO EL DRIVER
driver.close()

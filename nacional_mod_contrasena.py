import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Justo hoy la pagina tiene problemas para validar cuentas, por lo que le pedi a un amigo que me prestara la suya. 
# Debido a esto cambiare la contraseña por la misma, si quisiera cambiarla por otra podria cambiar las variables psw2 y psw3 
# que son la nueva contraseña y la verificacion de esta misma. Además si quisiera hacer esto muchas veces podria encerrarlo todo en un ciclo

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
driver.get('https://www.solotodo.cl/account/login?next=%2F')
time.sleep(12)

#el xpath es copiado de la misma pagina con las herramientas de desarrollador
user = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
u = "flydlerlegueoflegends@gmail.com"
user.send_keys(u)
psw = driver.find_element_by_xpath('//*[@id="password"]')
p = "2qa1ws..**"
psw.send_keys(p)
driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[3]/div/form/input').submit()    

time.sleep(4)
driver.get('https://www.solotodo.cl/account/password_change')
time.sleep(4)

psw1 = driver.find_element_by_xpath('//*[@id="inputOldPassword"]')
psw2 = driver.find_element_by_xpath('//*[@id="inputPassword1"]')
psw3 = driver.find_element_by_xpath('//*[@id="inputPassword2"]')
_psw1 = p
_psw2 = "2qa1ws..**"
_psw3 = "2qa1ws..**"
psw1.send_keys(_psw1)
psw2.send_keys(_psw2)
psw3.send_keys(_psw3)

driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[3]/div/form/input').submit()    
time.sleep(4)

import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
driver.get('https://www.solotodo.cl/account/password_reset')
time.sleep(7)

#el xpath es copiado de la misma pagina con las herramientas de desarrollador
email = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
psw_nueva="nicolasestebanc@hotmail.es"
email.send_keys(psw_nueva)

driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[3]/div/form/input').submit()    
time.sleep(3)

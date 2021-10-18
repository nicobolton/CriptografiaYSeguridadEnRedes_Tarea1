
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")

for i in range(30):
    driver.get('https://www.solotodo.cl/account/signup')
    time.sleep(4)
    #el xpath es copiado de la misma pagina con las herramientas de desarrollador
    email = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    e = "nico"+str(i)+"@gmail.com"
    email.send_keys(e)

    psw = driver.find_element_by_xpath('//*[@id="inputPassword1"]')
    psw2 = driver.find_element_by_xpath('//*[@id="inputPassword2"]')
    p = "Nn12345678"
    psw.send_keys(p)
    psw2.send_keys(p)
 
    driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[3]/div/form/input').submit()    
    time.sleep(4)





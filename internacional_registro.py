
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
for i in range(4):
    #i=i+2
    driver.get('https://usuarios.eldiario.es/registro')
    time.sleep(2)
    
    #el xpath es copiado de la misma pagina con las herramientas de desarrollador
    _email = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[1]/label/div/input[@value]')
    email = "nicola"+str(i)+"@hotmail.es"
    print(email)
    _email.send_keys(email)

    clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[2]/button').submit()    

# -------
    time.sleep(5)
    # valores
    name = "nicolas"
    lastName = "correa"
    psw = "aA12345678"

    _name = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[1]/label/div/input[@value]')
    _psw = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[4]/label/div/input[@value]')
    _lastName = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[2]/label/div/input[@value]')
    _name.send_keys(name)
    _lastName.send_keys(lastName)
    _psw.send_keys(psw)

    time.sleep(2)
    __clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[5]/button').submit()    
    ___clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[2]/form/div/div[5]/button').click()    
    time.sleep(8)




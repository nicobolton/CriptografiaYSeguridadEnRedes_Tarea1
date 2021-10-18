import string
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")

email =["nn@hotmail.com","nn2@hotmail.com"]
for i in email:

    driver.get('https://usuarios.eldiario.es/recuperar')
    time.sleep(2)
    #el xpath es copiado de la misma pagina con las herramientas de desarrollador
    _email = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div/div[3]/form/div[1]/label/div/input[@value]')
    _email.send_keys(i)
    clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div/div[3]/form/div[2]/button').submit()    
    time.sleep(4)
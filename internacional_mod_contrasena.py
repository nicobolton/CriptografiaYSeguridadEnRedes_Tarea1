
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver de chrome, luego "driver" es la variable para interactuar con la pagina
driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
driver.get('https://usuarios.eldiario.es/iniciar-sesion/')
time.sleep(3)

#el xpath es copiado de la misma pagina con las herramientas de desarrollador
usr = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[1]/label/div/input[@value]')
usr.send_keys("nicolasestebanc@hotmail.es")
psw = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[2]/label/div/input[@value]')
_str = "111111"
psw.send_keys(_str)
clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[4]/button').submit()    


time.sleep(4)
driver.get('https://usuarios.eldiario.es/perfil/cuenta/')
time.sleep(4)
clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[5]/div/div[1]/form/div[2]/div/div/span').click()    
time.sleep(4)
_psw = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[5]/div/div[1]/form/div[2]/div/div[2]/div/div[2]/label/div/input[@value]')
__psw = _str
_psw.send_keys(__psw)
psw_nueva = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[5]/div/div[1]/form/div[2]/div/div[2]/div/div[3]/label/div/input[@value]')
_psw_nueva = "222222"
psw_nueva.send_keys(_psw_nueva)
time.sleep(4)
clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/div[5]/div/div[1]/form/div[7]/button[1]').submit()    


time.sleep(1)
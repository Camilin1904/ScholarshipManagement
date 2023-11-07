from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SignInTest(LiveServerTestCase):
    
    def testSignIn(self):
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/')

        username = driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('correoprueba@gmail.com')
       
        name = driver.find_element(by=By.ID,value='id_name')
        name.click()
        name.clear()
        name.send_keys('Usuario de Prueba')

        password1 = driver.find_element(by=By.ID,value='id_password1')
        password2 = driver.find_element(by=By.ID,value='id_password2')

        password1.click()
        password1.clear()
        password1.send_keys('prueba9170')

        password2.click()
        password2.clear()
        password2.send_keys('prueba9170')

        submit = driver.find_element(by=By.ID,value='signin')
        submit.send_keys(Keys.RETURN)

        assert 'Home' in driver.title





    
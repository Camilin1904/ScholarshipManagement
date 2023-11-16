from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testErrorSignIn(LiveServerTestCase):

    def testError(self):
        driver = webdriver.Edge()

        driver.get('http://127.0.0.1:3000/')

        username = driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('admin@gmail.com')

        name = driver.find_element(by=By.ID,value='id_name')
        name.click()
        name.clear()
        name.send_keys('Admin')

        password = driver.find_element(by=By.ID,value='id_password1')
        password.click()
        password.clear()
        password.send_keys('prueba')

        password2 = driver.find_element(by=By.ID,value='id_password2')
        password2.click()
        password2.clear()
        password2.send_keys('pruebaMal')


        signin = driver.find_element(by=By.ID,value='signin')
        signin.click()  

        driver.implicitly_wait(10)

        alert = driver.find_element(by=By.CLASS_NAME,value='alert')

        assert alert.is_displayed()

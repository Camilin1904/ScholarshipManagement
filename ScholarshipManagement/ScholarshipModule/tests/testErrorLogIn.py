from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testErrorLogIn(LiveServerTestCase):

    def testError(self):
        driver = webdriver.Edge()

        driver.get('http://127.0.0.1:3000/')

        login = driver.find_element(by=By.ID,value='login')
        login.click()

        driver.implicitly_wait(10)

        username = driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('admin@gmail.com')

        password = driver.find_element(by=By.ID,value='id_password')
        password.click()
        password.clear()
        password.send_keys('prueba')

        submit = driver.find_element(by=By.ID,value='signin')
        submit.click()

        alert = driver.find_element(by=By.CLASS_NAME,value='alert')

        assert alert.is_displayed()

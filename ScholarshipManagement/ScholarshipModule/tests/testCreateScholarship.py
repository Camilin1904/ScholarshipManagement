from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testCreateScholarship(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

        self.driver.get('http://127.0.0.1:3000/') 

    def logIn(self):
        login = self.driver.find_element(by=By.ID,value='login')
        login.click()

        self.driver.implicitly_wait(10)

        username = self.driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('correo_admin@gmail.com')

        password = self.driver.find_element(by=By.ID,value='id_password')
        password.click()
        password.clear()
        password.send_keys('administrador12')

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.send_keys(Keys.RETURN)

        assert 'Home' in self.driver.title

    def testEnterScholarshipManagement(self):

        self.logIn()

        btnScholarship = self.driver.find_element(by=By.XPATH,value="//a[@href= '/scholarship']")
        btnScholarship.click()

        self.driver.implicitly_wait(10)

        title = self.driver.find_element(by=By.ID,value='title')

        assert 'Programa de Becas' in title


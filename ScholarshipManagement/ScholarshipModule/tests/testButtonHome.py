from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testCreateApplicant(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

        self.driver.fullscreen_window()

        self.driver.get('http://127.0.0.1:3000/') 

    def logIn(self):
        login = self.driver.find_element(by=By.ID,value='login')
        login.click()

        self.driver.implicitly_wait(10)

        username = self.driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('financial@gmail.com')

        password = self.driver.find_element(by=By.ID,value='id_password')
        password.click()
        password.clear()
        password.send_keys('FINANCIAL')

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(20)

        assert 'Home' in self.driver.title

    def enterRegisterApplicant(self):

        register = self.driver.find_element(by=By.ID,value='register')
        register.click()

        self.driver.implicitly_wait(20)

        assert 'Creación Aplicante' in self.driver.title

    def returnHome(self):
        
        home = self.driver.find_element(by=By.XPATH,value='/html/body/header/div/ul/li[1]/a') 
        home.click()

        self.driver.implicitly_wait(20)

        assert 'Home' in self.driver.title

    def enterSearchApplicant(self):

        management = self.driver.find_element(by=By.ID,value='management')
        management.click()

        self.driver.implicitly_wait(20)

        assert 'Buscar estudiante' in self.driver.title

    def testButtonHome(self):

        self.logIn()
        self.enterRegisterApplicant()
        self.returnHome()
        self.enterSearchApplicant()
        self.returnHome()

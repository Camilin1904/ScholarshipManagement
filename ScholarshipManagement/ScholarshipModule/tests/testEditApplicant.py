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
    
    def enterSeeMore(self):
        seeMore = self.driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div/nav/form[1]/div/button')
        seeMore.click()

        self.driver.implicitly_wait(20)

        assert 'Información de aplicante' in self.driver.title

    def enterEditAppli(self):
        editButton = self.driver.find_element(by=By.ID,value='edit')
        editButton.click()

        self.driver.implicitly_wait(20)

        assert 'Edición de Aplicante' in self.driver.title

        name = self.driver.find_element(by=By.ID,value='id_name')
        lastName = self.driver.find_element(by=By.ID,value='id_lastName')

        name.clear()
        lastName.clear()
        name.send_keys('Fercho')
        lastName.send_keys('Alto')

        saveButton = self.driver.find_element(by=By.ID,value='save')
        saveButton.click()

        self.driver.implicitly_wait(20)

        assert 'Información de aplicante' in self.driver.title
        assert 'Fercho' in self.driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div/ul/li/p[1]').text
        assert 'Alto' in self.driver.find_element(by=By.XPATH,value='/html/body/div/div[2]/div/ul/li/p[2]').text
    def testButtonHome(self):

        self.logIn()
        self.enterSearchApplicant()
        self.enterSeeMore()
        self.enterEditAppli()

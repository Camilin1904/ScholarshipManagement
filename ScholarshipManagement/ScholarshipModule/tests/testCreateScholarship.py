from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ScholarshipModule.models import *

class testCreateScholarship(LiveServerTestCase):

    databases = {'default': 'test'}

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
        username.send_keys('correo_admin@gmail.com')

        password = self.driver.find_element(by=By.ID,value='id_password')
        password.click()
        password.clear()
        password.send_keys('administrador12')

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(20)

        assert 'Home' in self.driver.title

    def enterScholarshipManagement(self):

        self.driver.implicitly_wait(20)

        btnScholarship = self.driver.find_element(by=By.ID,value='scholarship_btn')
        btnScholarship.click()

        self.driver.implicitly_wait(20)

    def createScholarshipManagement(self):

        goToCreate = self.driver.find_element(by=By.ID,value='CreateButton')
        goToCreate.click()

        self.driver.implicitly_wait(20)
        assert 'Crear programa de becas' in self.driver.title

    
    def fillFirstForm(self):

        self.driver.implicitly_wait(20)

        id = self.driver.find_element(by=By.ID,value='id_ID')
        id.clear()
        id.send_keys('1')

        name = self.driver.find_element(by=By.ID,value='id_name')
        name.clear()
        name.send_keys('Beca de prueba')

        description = self.driver.find_element(by=By.ID,value='id_description')
        description.clear()
        description.send_keys('Un texto de prueba')

        requirements = self.driver.find_element(by=By.ID,value='id_requirements')
        requirements.clear()
        requirements.send_keys('Un texto de prueba de requerimientos')

        btnSubmit = self.driver.find_element(by=By.CLASS_NAME,value='standardButton')
        btnSubmit.click()

        assert 'Seleccion de donante' in self.driver.title

    def selectDonor(self):

        donor = self.driver.find_element(by=By.XPATH,value="//button[@value='1']")
        donor.click()

        assert 'Configuracion de coverturas' in self.driver.title

    def fillTypes(self):

        value = self.driver.find_element(by=By.ID,value='id_value')
        value.clear()
        value.send_keys('100')

        type = self.driver.find_element(by=By.ID,value='id_type')
        type.clear()
        type.send_keys('Alimenticia')

        save = self.driver.find_element(by=By.ID,value='save')
        save.click()

        self.driver.implicitly_wait(20)

        assert 'Resumen de beca' in self.driver.title

    def testCheck(self):

        self.logIn()
        self.enterScholarshipManagement()
        self.createScholarshipManagement()
        self.fillFirstForm()
        self.selectDonor()
        self.fillTypes()

        self.driver.implicitly_wait(20)
        
        btnSubmit = self.driver.find_element(by=By.ID,value='save')
        btnSubmit.click()

        self.driver.implicitly_wait(20)

        assert 'Programa de becas' in self.driver.title

    def tearDown(self):
        self.driver.close()

        

        

    
    



    


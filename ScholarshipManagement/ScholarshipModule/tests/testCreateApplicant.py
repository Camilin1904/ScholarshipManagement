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

    def fillFirstForm(self):

        name = self.driver.find_element(by=By.ID,value='id_name')
        lastName = self.driver.find_element(by=By.ID,value='id_lastName')
        email = self.driver.find_element(by=By.ID,value='id_email')
        phone = self.driver.find_element(by=By.ID,value='id_phone')

        name.send_keys('Prueba')
        lastName.send_keys('Pruebin')

        email.send_keys('prueba@gmail.com')
        phone.send_keys('1234567890')

        submit = self.driver.find_element(by=By.ID,value='nextButton')
        submit.click()

        self.driver.implicitly_wait(20)


        assert self.driver.find_element(by=By.ID,value='academicInformation').is_displayed()

    def fillSecondForm(self):

        code = self.driver.find_element(by=By.ID,value='id_studentCode')
        faculty = self.driver.find_element(by=By.ID,value='id_faculty')
        major = self.driver.find_element(by=By.ID,value='id_major')

        code.clear()
        code.send_keys('A00123456')

        faculty.click()
        opFaculty = self.driver.find_element(by=By.XPATH,value="//option[@value='Ingeniería, Diseño y Ciencias Aplicadas']")

        opFaculty.click()
        
        major.click()
        opMajor= self.driver.find_element(by=By.XPATH,value="//option[@value='Ingeniería de Sistemas']")

        opMajor.click()

        submit = self.driver.find_element(by=By.ID,value='save')
        submit.click()

        self.driver.implicitly_wait(20)

        assert self.driver.find_element(by=By.ID,value='deletable').is_displayed()

    def testCreateWithAnnouncement(self):

        self.logIn()
        self.enterRegisterApplicant()
        self.fillFirstForm()
        self.fillSecondForm()

        announcement = self.driver.find_element(by=By.XPATH,value="//button[@value='1']")
        announcement.click()

        assert 'Home' in self.driver.title
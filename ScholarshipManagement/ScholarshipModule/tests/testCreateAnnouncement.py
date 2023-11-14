from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testCreateAnnouncement(LiveServerTestCase):

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

    def enterAnnouncementManagement(self):

        enter = self.driver.find_element(by=By.ID,value='announcement_btn')
        enter.click()

        self.driver.implicitly_wait(20)

        assert 'Busqueda de convocatoria' in self.driver.title

    def enterCreateAnnouncement(self):

        createBtn = self.driver.find_element(by=By.ID,value='newScholarshipBttn')
        createBtn.click()

        self.driver.implicitly_wait(20)

        assert 'Creación convocatoria' in self.driver.title

    def fillForm(self):

        type = self.driver.find_element(by=By.ID,value='id_announcementForm-type')
        type.click()

        opType = self.driver.find_element(by=By.XPATH,value="//option[@value = '2']")
        opType.click()

        
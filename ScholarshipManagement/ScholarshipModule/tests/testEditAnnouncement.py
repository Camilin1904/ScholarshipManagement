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
        username.send_keys('admin@gmail.com')

        password = self.driver.find_element(by=By.ID,value='id_password')
        password.click()
        password.clear()
        password.send_keys('ADMIN')

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(20)

        assert 'Home' in self.driver.title

    def enterAnnouncementManagement(self):

        enter = self.driver.find_element(by=By.ID,value='announcement_btn')
        enter.click()

        self.driver.implicitly_wait(20)

        assert 'Busqueda convocatoria' in self.driver.title
    
    def enterMoreInfoAnnouncement(self):

        moreInfo = self.driver.find_element(by=By.XPATH,value="//button[@value= '2']")
        moreInfo.click()

        assert 'Información convocatoria' in self.driver.title

    def enterEditAnnouncement(self):

        editBtn = self.driver.find_element(by=By.ID,value='editBttn')
        editBtn.click()

    

    def editInfo(self):

        fieldToChange = self.driver.find_element(by=By.ID,value='id_announcementEventFormPublication-endDate')
        fieldToChange.clear()
        fieldToChange.send_keys('04122023')

        submit = self.driver.find_element(by=By.ID,value='saveBttn')
        submit.click()

    def testEdit(self):

        self.logIn()
        self.enterAnnouncementManagement()
        self.enterMoreInfoAnnouncement()
        self.enterEditAnnouncement()
        self.editInfo()

        assert 'Información convocatoria' in self.driver.title
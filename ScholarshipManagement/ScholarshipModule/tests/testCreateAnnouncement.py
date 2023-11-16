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

        scholarship = self.driver.find_element(by=By.ID,value='select2-id_scholarshipAnnouncementForm-scholarshipId-container')
        scholarship.click()

        textField = self.driver.find_element(by=By.XPATH,value="//input[@class='select2-search__field']")
        textField.clear()
        textField.send_keys('Beca de ciudadania')
        textField.send_keys(Keys.ENTER)

        inscriptionDateStart = self.driver.find_element(by=By.ID,value='id_announcementEventFormInscription-startingDate')
        inscriptionDateStart.send_keys('04122023')

        inscriptionDateFinal = self.driver.find_element(by=By.ID,value='id_announcementEventFormInscription-endDate')
        inscriptionDateFinal.send_keys('08122023')

        interviewDateStart = self.driver.find_element(by=By.ID,value='id_announcementEventFormInterview-startingDate')
        interviewDateStart.send_keys('11122023')

        interviewDateFinal = self.driver.find_element(by=By.ID,value='id_announcementEventFormInterview-endDate')
        interviewDateFinal.send_keys('16122023')

        selectDateStart = self.driver.find_element(by=By.ID,value='id_announcementEventFormSelection-startingDate')
        selectDateStart.send_keys('19122023')

        selectDateFinal = self.driver.find_element(by=By.ID,value='id_announcementEventFormSelection-endDate')
        selectDateFinal.send_keys('21122023')

        publicationDateStart = self.driver.find_element(by=By.ID,value='id_announcementEventFormPublication-startingDate')
        publicationDateStart.send_keys('25122023')

        publicationDateFinal = self.driver.find_element(by=By.ID,value='id_announcementEventFormPublication-endDate')
        publicationDateFinal.send_keys('26122023')

        submit = self.driver.find_element(by=By.ID,value='saveBttn')
        submit.click()

    def testCreateAnnouncement(self):

        self.logIn()
        self.enterAnnouncementManagement()
        self.enterCreateAnnouncement()
        self.fillForm()


        assert 'Busqueda convocatoria' in self.driver.title

    def tearDown(self):
        self.driver.close() 


    
        


        
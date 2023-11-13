from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testRoleAssignment(LiveServerTestCase):

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
        submit.click()

        self.driver.implicitly_wait(10)

        assert 'Home' in self.driver.title
    
    def enterRoleAssignment(self):

        rol = self.driver.find_element(by=By.ID,value='rol_btn')
        rol.click()

        self.driver.implicitly_wait(10)

    def searchUser(self):
        
        select = self.driver.find_element(by=By.XPATH,value="//select[@name= 'username']")
        select.click()

        option = self.driver.find_element(by=By.XPATH,value="//option[@value= '3']")
        option.click()

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.click()

    def testAssignRole(self):

        self.logIn()
        self.enterRoleAssignment()
        self.searchUser()

        select = self.driver.find_element(by=By.XPATH,value="//select[@id= 'id_role']")
        select.click()

        option = self.driver.find_element(by=By.XPATH,value="//option[@value= '2']")
        option.click()

        submit = self.driver.find_element(by=By.ID,value='signin')
        submit.click()

        assert self.driver.find_element(by=By.CLASS_NAME,value='alert').is_displayed()



    

        





        

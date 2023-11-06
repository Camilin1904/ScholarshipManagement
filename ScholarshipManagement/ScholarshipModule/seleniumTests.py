
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriver
from selenium.webdriver.common.by import By

class SignInTest():

    def __init__(self):
        self.driver = webdriver.Edge('./msedgedriver')
    
    #Add implicit wait for element to be found
    def applyWait(self):
        self.driver.implicitly_wait(10)
    
    #Open SignUp page
    def openSignInPage(self):
        self.driver.get('http://127.0.0.1:3000/')
        assert self.driver.title=='Signin'
    
    #Fill username as correoprueba@gmail.com
    def fillUsername(self):
        username = self.driver.find_element(by=By.ID,value='id_username')
        username.click()
        username.clear()
        username.send_keys('correoprueba@gmail.com')
    
    #Fill name as Usuario de Prueba
    def fillName(self):
        name = self.driver.find_element(by=By.ID,value='id_name')
        name.click()
        name.clear()
        name.send_keys('Usuario de Prueba')
    
    #Fill password as prueba9170
    def fillPasswords(self):
        password1 = self.driver.find_element(by=By.ID,value='id_password1')
        password2 = self.driver.find_element(by=By.ID,value='id_password2')

        password1.click()
        password1.clear()
        password1.send_keys('prueba9170')

        password2.click()
        password2.clear()
        password2.send_keys('prueba9170')
    
    def submitForm(self):

        registerBtn = self.driver.find_element(by=By.ID,value='signin')
        registerBtn.click()
    
    def check(self):
        title = self.driver.title

        assert title == 'Home'

        self.driver.close()



bot = SignInTest()

bot.openSignInPage()

bot.applyWait()

bot.fillUsername()

bot.fillName()

bot.fillPasswords()

bot.submitForm()

bot.check()
    


        
    

    





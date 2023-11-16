import os
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class testFilteredReportScholarship(LiveServerTestCase):

    def setUp(self):
        op = webdriver.EdgeOptions()
        
        p = {'download.default_directory': 'C:\\Users\\Downloads'}
        #add options to browser
        op.add_experimental_option('prefs', p)
        
        self.driver = webdriver.Edge(options=op)

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
    
    
    def enterReportScreen(self):
        
        repBtn = self.driver.find_element(by=By.ID,value='report_btn')
        repBtn.click()
        
        assert 'Report Generator' in self.driver.title


    def enterScholarshipScreen(self):
        
        appBtn = self.driver.find_element(by=By.ID,value='sch_btn')
        appBtn.click()
        
        assert '/typeOfReport/' in self.driver.current_url
        
    
    def enterFltScreen(self):
    
        fltBtn = self.driver.find_element(by=By.ID,value='flt_btn')
        fltBtn.click()
        
        
        assert '/filterOfReport/' in self.driver.current_url
        
    
    def enterSumScreen(self):
        
        allBtn = self.driver.find_element(by=By.ID,value='flt_btn')
        allBtn.click()
        
        
        assert '/reportResume/' in self.driver.current_url
    
    
    

    def testFilteredReportApplicant(self):

        self.logIn()
        self.enterReportScreen()
        self.enterScholarshipScreen()
        self.enterFltScreen()
        self.enterSumScreen()
        downBtn = self.driver.find_element(by=By.ID, value='down_btn')
        downBtn.click()
        alert = self.driver.switch_to.alert
        alert.accept()
         
    
    def tearDown(self):
        self.driver.close()



        





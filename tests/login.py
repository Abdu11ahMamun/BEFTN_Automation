from selenium import webdriver
import time
import unittest
import sys
sys.path.append('D:/BEFTN_Automation') 

from beftn.loginPage import loginPage
from beftn.homePage import homePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver
        driver.get("http://192.168.1.154:8080/beftn/faces/login.xhtml")
        time.sleep(2)
        login = loginPage(driver)
        login.enter_username('mamun')
        login.enter_password('b')
        login.click_login()
        time.sleep(2)
        homePage = homePage(driver)
        homePage.click_logout()
        time.sleep(2)


        # self.driver.find_element('xpath', '//*[@id="j_idt13"]/table[2]/tbody/tr[2]/td/input').send_keys("mamun")
        # self.driver.find_element('xpath', '//*[@id="j_idt13:masked-password"]').send_keys("b")
        # self.driver.find_element('xpath', '//*[@id="j_idt13"]/table[2]/tfoot/tr/td/input').click()
        # time.sleep(2)
        # self.driver.find_element('xpath','//*[@id="topControl"]/table/tbody/tr/td[5]/div/a').click()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test finished")

if __name__ == '__main__':
    unittest.main()











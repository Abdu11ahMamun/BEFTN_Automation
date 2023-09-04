from selenium import webdriver
import time
import unittest
import datetime  # Import the datetime module
import sys
sys.path.append('D:/BEFTN_Automation') 

from beftn.loginPage import LoginPage
from beftn.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver
        driver.get("http://192.168.1.154:8080/beftn/faces/login.xhtml")
        time.sleep(2)
        
        login = LoginPage(driver)
        
        login.enter_username('mamun')
        login.enter_password('b')
        login.click_login()
        time.sleep(2)
        homePage = HomePage(driver)
        homePage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finished")

if __name__ == '__main__':
    # Generate a timestamp for the report filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"D:/BEFTN_Automation/report/report_{current_time}.html"

    # Use the timestamped filename for the report
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output=report_filename)
    )

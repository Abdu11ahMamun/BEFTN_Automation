from selenium import webdriver
import time
import unittest
import datetime  
import sys
sys.path.append('D:/BEFTN_Automation') 
from location.location import Locators
from selenium.webdriver.common.by import By

from beftn.loginPage import LoginPage
from beftn.homePage import HomePage
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        time.sleep(2)
        driver.get('http://192.168.1.154:8080/beftn/faces/outbound/txn/cieppdedit.xhtml')
        time.sleep(2)

        account_Id = driver.find_element(By.ID ,"txnEntryForm:originatorAccount")
        balance_Id = driver.find_element(By.ID ,"txnEntryForm:originatorBalance")
        #msg_id = driver.find_element(By.XPATH, "//span[@class='rf-msgs-sum']")
        msg_id = None
        # actions = ActionChains(driver)
        # actions.key_down(Keys.CONTROL).key_down(Keys.CONTROL)
        # Perform the actions
        # actions.perform()
        account_Id.click()
        account_Id.send_keys('0191120008388')
        account_Id.send_keys(Keys.ENTER)

        
        time.sleep(2)
        wait = WebDriverWait(driver, 10)
        
      



        
        time.sleep(1)
        wait = WebDriverWait(driver, 10)
        try:
            msg_id = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='rf-msgs-sum']")))
        except Exception as e:
            # Handle any exceptions or timeouts here
            print(f"Exception: {e}")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finished")

# if __name__ == '__main__':
#     # Generate a timestamp for the report filename
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     report_filename = f"D:/BEFTN_Automation/report/report_{current_time}.html"

#     # Use the timestamped filename for the report
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output=report_filename)
#     )
if __name__ == '__main__':
    unittest.main()

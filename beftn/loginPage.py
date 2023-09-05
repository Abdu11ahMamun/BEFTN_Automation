import sys
sys.path.append('D:/BEFTN_Automation') 
from location.location import Locators
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        
        self.username_xpath = Locators.username_xpath
        self.password_xpath = Locators.password_xpath 
        self.login_button_xpath = Locators.login_button_xpath

    def enter_username(self, username):
        username_element = self.driver.find_element(By.XPATH, self.username_xpath)
        username_element.click()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.driver.find_element(By.XPATH, self.password_xpath)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_button_element = self.driver.find_element(By.XPATH, self.login_button_xpath)
        login_button_element.click()
        
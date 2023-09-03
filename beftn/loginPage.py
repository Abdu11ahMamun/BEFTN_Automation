class loginPage:

    def __init__(self, driver):
        self.driver = driver
        

        self.username_xpath = '//*[@id="j_idt13"]/table[2]/tbody/tr[2]/td/input'
        self.password_xpath = '//*[@id="j_idt13:masked-password"]'  # Added a missing closing bracket here
        self.login_button_xpath = '//*[@id="j_idt13"]/table[2]/tfoot/tr/td/input'

    def enter_username(self, username):
        username_element = self.driver.find_element_by_xpath(self.username_xpath)
        username_element.click()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.driver.find_element_by_xpath(self.password_xpath)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_button_element = self.driver.find_element_by_xpath(self.login_button_xpath)
        login_button_element.click()

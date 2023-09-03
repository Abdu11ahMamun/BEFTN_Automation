class homePage:

    def __init__(self, driver):
        self.driver = driver

        # Define the XPath constants
        self.logout_xpath = '//*[@id="topControl"]/table/tbody/tr/td[5]/div/a'

    def click_logout(self):
        logout_element = self.driver.find_element_by_xpath(self.logout_xpath)
        logout_element.click()

from selenium.webdriver.common.by import By


class Dashboard(object):

    def __init__(self, driver):
        self.driver = driver
        self.new_btn = driver.find_element(By.LINK_TEXT, "New")

    # home page locators defining
    def to_new_repo(self):
        self.new_btn.click()

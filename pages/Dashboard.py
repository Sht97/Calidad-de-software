from selenium.webdriver.common.by import By


class Dashboard(object):

    def __init__(self, driver):
        self.driver = driver
        self.btn_new = driver.find_element(By.LINK_TEXT, "New")
        self.title=self.driver.title
    # home page locators defining
    def to_new_repo(self):
        self.btn_new.click()

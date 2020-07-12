from selenium.webdriver.common.by import By
class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.sigin_button = driver.find_element(By.LINK_TEXT, "Sign in")

# home page locators defining

    def to_login(self):
        self.sigin_button.click()


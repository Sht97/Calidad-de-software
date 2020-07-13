from selenium.webdriver.common.by import By

class Sigin(object):

    def __init__(self, driver):
        self.driver = driver
        self.input_user = self.driver.find_element(By.ID, "login_field")
        self.input_password = self.driver.find_element(By.ID, "password")
        self.btn_send = self.driver.find_element(By.XPATH, "/html/body/div[3]/main/div/form/div[4]/input[9]")

    def write_user(self,user):
        self.input_user.clear()
        self.input_user.send_keys(user)

    def write_pass(self,password):
        self.input_password.clear()
        self.input_password.send_keys(password)

    def login(self):
        self.btn_send.click()


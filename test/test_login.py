from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Home import Home
from pages.Sign_in import Sigin

class Github_login():

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_github(self,mail,password):
        driver = self.driver
        driver.get("http://www.github.com")
        self.driver.set_window_size(1920, 1080)
        home = Home(driver)
        home.to_login()
        login=Sigin(driver)
        login.write_mail(mail)
        login.write_pass(password)
        login.login()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    prueba=Github_login()
    prueba.setUp()
    prueba.test_login_github('Danielf.r97@gmail.com','Fe63b4366c140')
    prueba.tearDown()

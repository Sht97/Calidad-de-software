from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Home import Home
from pages.Sign_in import Sigin
from pages.Dashboard import Dashboard
from pages.Repository import Repository
import time


class Github_repository_test():

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.user= 'selenium-POM'
        self.password='PruebaSelenium.'
        self.name_repo='Calidad software'
        self.description='Selenium'
        self.root_url='http://www.github.com'
        self.driver.maximize_window()
        self.driver.get(self.root_url)

    def test_login(self):
        driver=self.driver
        home = Home(driver)
        home.to_login()
        login=Sigin(driver)
        login.write_user(self.user)
        login.write_pass(self.password)
        login.login()
        if driver.title == "GitHub":
            print("SignIn github successfully")
        else:
            print("SignIn failed")

    def test_create_repository(self):
        driver=self.driver
        dashboard=Dashboard(driver)
        dashboard.to_new_repo()

        repository=Repository(driver)
        repository.fill_name(self.name_repo)
        repository.fill_description(self.description)
        time.sleep(3)
        repository.create_repo()
        if self.name_repo.replace(' ','-') in self.driver.current_url:
            print("Sucess")
        else:
            print("Fail")

    def exit(self):
        self.driver.close()

if __name__ == "__main__":
    test=Github_repository_test()
    test.test_login()
    test.test_create_repository()
    # test.exit()

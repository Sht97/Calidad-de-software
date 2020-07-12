from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestUntitled():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get("https://github.com/")
        self.driver.set_window_size(960, 1053)
        self.driver.find_element(By.CSS_SELECTOR, ".octicon-three-bars").click()
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.ID, "login_field").send_keys("danielf.r97@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Fe63b4366c140")
        self.driver.find_element(By.NAME, "commit").click()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#dashboard-repos-container > #repos-container .public:nth-child(3) .css-truncate:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "New").click()
        self.driver.find_element(By.ID, "repository_name").click()
        self.driver.find_element(By.ID, "repository_name").send_keys("jeje")
        print('holii')
a=TestUntitled()
a.setup_method(print(''))
a.test_untitled()
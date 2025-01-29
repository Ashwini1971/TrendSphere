from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.RegisterPage import RegisterPage
from selenium.webdriver.chrome.webdriver import WebDriver

class TestRegister(RegisterPage):
    base_url = 'https://www.shopclues.com/'
    email_id = 'sashwini.2021@gmail.com'
    mobile_num = '7795361971'
    password = 'self@1ove'

    def test_title(self):
        self.driver = WebDriver()
        self.driver.get(self.base_url)
        excepted_title = 'Online Shopping Site India - Shop Online for men, women and kids fashion, home, kitchen, health, sports and more products at ShopClues'
        WebDriverWait(self.driver, 10).until(EC.title_is(excepted_title))
        actual_title = self.driver.title
        if actual_title == excepted_title:
            assert True
        else:
            assert False









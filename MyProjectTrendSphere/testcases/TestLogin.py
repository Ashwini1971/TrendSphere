from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
from utilities.customer_logging import LogMaker



headers = 'u_email, u_pwd'
datas = [('sashwini.alpha@gmail.com', 'Achu@123')]

class TestLogin:
    logger = LogMaker.log_gen()
    @mark.parametrize(headers, datas)
    def test_user_login(self, driver_, pages, u_email, u_pwd):
        self.driver = driver_
        wait = WebDriverWait(self.driver, 10)
        accept_button = wait.until(
            EC.element_to_be_clickable(pages.register_page.accept_all_cookies)
        )
        accept_button.click()
        print("Cookies accepted!")
        self.logger.info('--------test_user_login------------')
        pages.home_page.click_signin()
        self.logger.info('--------click sign-in------------')
        pages.login_page.user_login_(u_email='sashwini.alpha@gmail.com', u_pwd='Achu@123')
        self.logger.info('--------Sign - in clicked------------')
        assert "dashboard" in self.driver.current_url, f'Login failed for {u_email}'



































import time
from Lib.Generic_functions import Wrapper
from Pages.UserLoginPage import LoginPage
from Pages.SearchProductPage import SearchProductPage
from utilities.read_properies import ReadConfig
from utilities.custom_logger import LogMarker


class TestUserLogin:
    base_url = ReadConfig.get_page_url()
    email_address = ReadConfig.get_email_address()
    password = ReadConfig.get_password()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogMarker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info('---test_title_verification verified---')
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        excepted_title = 'Shopping | Signi-in | Signup'

        if actual_title == excepted_title:
            assert True
        else:
            assert False

    def test_valid_login_user(self, setup):
        self.logger.info('---test_valid_login_user started---')
        self.driver = setup
        self.generic_method = Wrapper(self.driver)
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchProductPage(self.driver)
        time.sleep(4)
        self.generic_method.enter_text(self.login_page.email_address_textbox, value=self.email_address)
        self.generic_method.enter_text(self.login_page.password_textbox, value=self.password)
        self.generic_method.click_element(self.login_page.login_button)
        time.sleep(2)
        actual_title = self.driver.title
        excepted_title = 'My Cart'

        if actual_title == excepted_title:
            self.logger.info('---Screenshot captured---')
            self.driver.save_screenshot(r'C:\Users\User\PycharmProjects\SwagLabs\screenshot\shot1.png')
            assert True

        else:
            assert False

        # self.generic_method.click_element(self.search_page.search_product())
        self.generic_method.click_element(self.search_page.product_button)
        self.generic_method.click_element(self.search_page.sub_product_button)
        self.generic_method.page_down_()
        time.sleep(1)
        self.generic_method.click_element(self.search_page.add_to_cart)
        time.sleep(2)
















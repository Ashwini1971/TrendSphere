from time import sleep
from utilities import excel_utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lib.Generic_functions import Wrapper as G_methods
from POM.loginPage import LoginPage
from utilities.read_properies import ReadConfig
from utilities.custom_logger import LogMaker


class TestLogin:
    base_url = ReadConfig.get_url()
    user_name = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogMaker.log_gen()
    path = r'C:\Users\User\PycharmProjects\POMbasedProject\test_data\nopecommerce_login.xlsx'
    status_list = []

    def test_title(self, setup):
        self.logger.info('*****************test_title started****************')
        self.driver = setup
        WebDriverWait(self.driver, 10).until(EC.title_is('Your store. Login'))
        actual_title = self.driver.title
        excepted_title = 'Your store. Login'
        if actual_title == excepted_title:
            self.logger.info('*****************test_title matched****************')
            assert True
        else:
            self.logger.info('*****************test_title not matching****************')
            assert False

    def test_valid_login_data_driven(self, setup):
        self.logger.info('*****************test_valid_login_data_driven started****************')
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.generic_methods = G_methods(self.driver)
        self.login_page = LoginPage(self.driver)

        self.rows = excel_utils.get_row_count(self.path, 'Sheet1')
        print('No of rows:', self.rows)


        for r in range(2, self.rows+1):
            self.user_name = excel_utils.read_data(file=self.path, row_num=r, col_num=1, sheet_name='sheet1')
            self.password = excel_utils.read_data(self.path, r, 2, 'sheet1')
            self.exp_login = excel_utils.read_data(self.path, r, 3, 'sheet1')

            self.generic_methods.enter_text(self.login_page.text_box_email, self.user_name)
            self.generic_methods.enter_text(self.login_page.text_box_password, self.password)
            self.generic_methods.click_element(self.login_page.button_login)
            self.driver.save_screenshot(r'C:\Users\User\PycharmProjects\POMbasedProject\screenshot\shot2.png')
            actual_title = self.driver.title
            expected_title = 'Dashboard / nopCommerce administration'
            sleep(10)


            if actual_title == expected_title:
                if self.exp_login == 'YES':
                    self.logger.info('test data passed')
                    self.status_list.append('Pass')
                    self.generic_methods.click_element(self.login_page.button_logout)


                elif self.exp_login == 'NO':
                    self.logger.info('test data failed')
                    self.status_list.append('Fail')
                    self.generic_methods.click_element(self.login_page.button_logout)


            elif actual_title != expected_title:
                if self.exp_login == 'YES':
                    self.logger.info('test data failed')
                    self.status_list.append('Fail')


                elif self.exp_login == 'NO':
                    self.logger.info('test data passed')
                    self.status_list.append('Pass')
            else:
                print('not working')
            print(f'Status list is : {self.status_list}')

            if 'Fail' in self.status_list:
                self.logger.info('The admin data driven test case is Failed')
                assert True
            else:
                self.logger.info('The admin data driven test case is Passed')
                assert False





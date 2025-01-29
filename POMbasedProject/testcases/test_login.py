# from time import sleep
#
# import pytest
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from Lib.Generic_functions import Wrapper as G_methods
# from POM.loginPage import LoginPage
# from utilities.read_properies import ReadConfig
# from utilities.custom_logger import LogMaker
#
#
# class TestLogin:
#     base_url = ReadConfig.get_url()
#     user_name = ReadConfig.get_username()
#     password = ReadConfig.get_password()
#     logger = LogMaker.log_gen()
#
#     # @pytest.mark.sanity
#     def test_title(self, setup):
#         self.logger.info('*****************test_title started****************')
#         self.driver = setup
#         WebDriverWait(self.driver, 10).until(EC.title_is('Your store. Login'))
#         actual_title = self.driver.title
#         excepted_title = 'Your store. Login'
#         if actual_title == excepted_title:
#             self.logger.info('*****************test_title matched****************')
#             assert True
#         else:
#             self.logger.info('*****************test_title not matching****************')
#             self.driver.save_screenshot(r'C:\Users\User\PycharmProjects\POMbasedProject\screenshot\shot1.png')
#             assert False
#
#     @pytest.mark.sanity
#     @pytest.mark.regression
#     def test_valid_login(self, setup):
#         self.logger.info('*****************test_valid_login started****************')
#         self.drive = setup
#         generic_methods = G_methods(self.drive)
#         login_page = LoginPage(self.drive)
#         generic_methods.enter_text(login_page.text_box_email, self.user_name)
#         generic_methods.enter_text(login_page.text_box_password, self.password)
#         generic_methods.click_element(login_page.check_box_rm)
#         generic_methods.click_element(login_page.button_login)
#         sleep(4)
#         actual_title = 'Dashboard'
#         if actual_title == 'Dashboard':
#             self.logger.info('*****************test_title matched****************')
#             self.drive.save_screenshot(r'C:\Users\User\PycharmProjects\POMbasedProject\screenshot\shot1.png')
#             assert True
#         else:
#             self.logger.info('*****************test_title not matching****************')
#             self.drive.save_screenshot(r'C:\Users\User\PycharmProjects\POMbasedProject\screenshot\shot2.png')
#             assert False





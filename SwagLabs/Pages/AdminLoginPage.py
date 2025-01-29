from Lib.Generic_functions import Wrapper

class AdminLoginPage:
    PATH = 'xpath'
    user_name_textbox = (PATH, '//input[@id="inputEmail"]')
    password_textbox = (PATH, '//input[@id="inputPassword"]')
    login_button = (PATH, "//button[.='Login']")
    admin_login_link = (PATH, '//a[@href="admin"]')

    def __init__(self, driver):
        self.driver = driver

    def AdminLogin_(self, *, user_name, password):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.click_element(self.admin_login_link)
        wrapper.enter_text(self.user_name_textbox, value=user_name)
        wrapper.enter_text(self.password_textbox, value=password)
        wrapper.click_element(self.login_button)










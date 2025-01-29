from Lib.Generic_functions import Wrapper

class LoginPage:
    PATH = 'xpath'
    email_address_textbox = (PATH, '//input[@name="email"]')
    password_textbox = (PATH, '//input[@id="exampleInputPassword1"]')
    login_button = (PATH, '//a[@href="login.php"]')
    logout_button = (PATH, '//a[@href="logout.php"]')

    def __init__(self, driver):
        self.driver = driver

    def Login_(self):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.enter_text(self.email_address_textbox)
        wrapper.enter_text(self.password_textbox)
        wrapper.click_element(self.login_button)










from Lib.Generic_functions import Wrapper

class RegisterPage:
    PATH = 'xpath'
    full_name_textbox = (PATH, '//input[@name="fullname"]')
    email_address_textbox = (PATH, '//input[@name="emailid"]')
    contact_no_textbox = (PATH, '//input[@name="contactno"]')
    password_textbox = (PATH, '//input[@id="password"]')
    conf_password_textbox = (PATH, '//input[@id="confirmpassword"]')
    sign_up_button = (PATH, '//button[@id="submit"]')

    login_link = (PATH, '//a[@href="login.php"]')

    def __init__(self, driver):
        self.driver = driver

    def Login_(self, *, full_name, email, contact_no, password, conf_pwd):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.enter_text(self.full_name_textbox, value=full_name)
        wrapper.enter_text(self.email_address_textbox, value=email)
        wrapper.enter_text(self.contact_no_textbox, value=contact_no)
        wrapper.enter_text(self.password_textbox, value=password)
        wrapper.enter_text(self.conf_password_textbox, value=conf_pwd)
        wrapper.click_element(self.sign_up_button)









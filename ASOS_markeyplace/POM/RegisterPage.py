from Lib.Generic_functions import Wrapper
class RegisterPage(Wrapper):
    email_text_box = ('xpath', '//input[@name="email"]')
    mobile_num_text_box = ('xpath', '//input[@name="phone"]')
    register_button = ('xpath', '//a[@name="register"]')
    register_checkbox_pwd = ('xpath', '//input[@id="register_with_password"]')
    password = ('xpath', '(//input[@tabindex="4"])[1]')

    def __init__(self, driver, driver_):
        super().__init__(driver_)
        self.driver = driver


    def registration(self, email, mobile_num, password):
        Wrapper.enter_text(self.email_text_box, value=email)
        Wrapper.enter_text(self.mobile_num_text_box, value=mobile_num)
        Wrapper.click_element(self.register_checkbox_pwd)
        Wrapper.enter_text(self.password, value=password)
        Wrapper.click_element(self.register_button)












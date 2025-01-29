from Lib.Generic_functions import Wrapper
class LoginPage:
     PATH_ = 'xpath'
     text_box_email = (PATH_, '//input[@id="Email"]')
     text_box_password = (PATH_, '//input[@id="Password"]')
     check_box_rm = (PATH_, '//input[@id="RememberMe"]')
     button_login = (PATH_, '//button[.="Log in"]')
     button_logout = (PATH_, '//a[@href="/logout"]')

     def __init__(self, driver):
         self.driver = driver

     def Login_(self, *, username, password):
         wrapper = Wrapper(self.driver)
         wrapper.maximize_browser()
         wrapper.enter_text(self.text_box_email, value=username)
         wrapper.enter_text(self.text_box_password, value=password)

         wrapper.click_element(self.check_box_rm)
         wrapper.click_element(self.button_login)
         wrapper.click_element(self.button_logout)





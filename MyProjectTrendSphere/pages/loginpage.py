import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from library.GF import Wrapper
from pages.homepage import HomePage

class LoginPage(HomePage):
    accept_all_cookies = ('xpath', "//button[.='Accept all cookies']")
    email_textbox = ('xpath', '//input[@name="email"]')
    password_textbox = ('xpath','//input[@id="password"]')
    remember_checkbox = ('xpath','//input[@name="rememberMe"]')
    signin_button = ('xpath', '//button[@data-testid="submitButton"]')

    def user_login_(self, *, u_email, u_pwd):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.email_textbox, value=u_email)
        wrapper.enter_text(self.password_textbox, value=u_pwd)
        if self.remember_checkbox:
            wrapper.click_element(self.remember_checkbox)
        time.sleep(5)
        wait = WebDriverWait(self.driver, 20)  # Increased wait time
        sign_in_button = wait.until(
            EC.element_to_be_clickable(self.signin_button)
        )
        wrapper.click_element(sign_in_button)


        







from Lib.genericfunction import Wrapper

class Login(Wrapper):
    username_textfield = ('xpath', '//input[@name="username"]')
    password_textfield = ('xpath', '//input[@name="password"]')
    login_button = ('xpath', '//button[@type="submit"]')
    logout_button = ('xpath', '//a[@href="/logout"]')


    def login_heroku_app(self, u, p):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.username_textfield, u)
        wrapper.enter_text(self.password_textfield, p)
        wrapper.click_element(self.login_button)
        wrapper.click_element(self.logout_button)








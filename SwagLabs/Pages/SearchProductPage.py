from Lib.Generic_functions import Wrapper
from Pages.UserLoginPage import LoginPage

class SearchProductPage:
    PATH = 'xpath'
    email_address_textbox = (PATH, '//input[@name="email"]')
    password_textbox = (PATH, '//input[@id="exampleInputPassword1"]')
    login_button = (PATH, "//button[.='Login']")
    product_button = (PATH, '//a[@href="category.php?cid=3"]')
    sub_product_button = (PATH, '//a[@href="sub-category.php?scid=8"]')
    add_to_cart = (PATH, '//a[.="The Wimpy Kid Do -It- Yourself Book"]/../../..//button[.="Add to cart"]')

    def __init__(self, driver):
        self.wrapper = None
        self.driver = driver

    def search_product(self):
        self.wrapper = Wrapper(self.driver)
        self.wrapper.maximize_browser()
        self.wrapper.enter_text(self.email_address_textbox)
        self.wrapper.enter_text(self.password_textbox)
        self.wrapper.click_element(self.login_button)
        self.wrapper.enter_text(self.product_button)
        self.wrapper.click_element(self.sub_product_button)
        self.wrapper.click_element(self.product_button)
        self.wrapper.page_down_()
        self.wrapper.click_element(self.add_to_cart)


    # def alert_popup_ok(self):
    #     print('popup name : ', self.wrapper.alert_popup_ok().text)
    #     self.wrapper.alert_popup_ok()

















from Lib.Generic_functions import Wrapper
from Pages.SearchProductPage import SearchProductPage

class AddToCartPage:
    PATH = 'xpath'
    my_cart_button = (PATH, "//a[.='My Cart']")
    product_checkbox = (PATH, '//input[@value="15"]')
    Billing_Address_textbox = (PATH, '//textarea[@name="billingaddress"]')
    Billing_State_textbox = (PATH, '//input[@id="bilingstate"]')
    Billing_City_textbox = (PATH, '//input[@id="billingcity"]')
    Billing_Pincode_textbox = (PATH, '//input[@id="billingpincode"]')
    update_button1 = (PATH, '//button[@name="update"]')

    Shipping_Address_textbox = (PATH, '//textarea[@name="shippingaddress"]')
    Shipping_State_textbox = (PATH, '//input[@id="shippingstate"]')
    Shipping_City_textbox = (PATH, '//input[@id="shippingcity"]')
    Shipping_Pincode_textbox = (PATH, '//input[@id="shippingpincode"]')
    update_button2 = (PATH, '//button[@name="shipupdate"]')

    proceed_to_checkout_button3 = (PATH, "//button[.='PROCCED TO CHEKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.click_element(self.update_button1)
        search_product_ = SearchProductPage(self.driver)
        search_product_.search_product()
        wrapper.click_element(self.my_cart_button)























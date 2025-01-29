import time

from Lib.Generic_functions import Wrapper
from utilities.read_properies import ReadConfig

class InsertPage:
    PATH = 'xpath'
    user_name_textbox = (PATH, '//input[@id="inputEmail"]')
    password_textbox = (PATH, '//input[@id="inputPassword"]')
    login_button = (PATH, "//button[.='Login']")

    admin_login_link = (PATH, '//a[@href="admin"]')
    insert_product_link = (PATH, '//a[@href="insert-product.php"]')

    Category_drop_down = (PATH, '//select[@name="category"]')
    Sub_Category_drop_down = (PATH, '//select[@id="subcategory"]')
    Product_Name_textbox = (PATH, '//input[@name="productName"]')
    Product_Company_textbox = (PATH, '//input[@name="productCompany"]')

    Product_Price_Before_Discount_textbox = (PATH, '//input[@name="productpricebd"]')
    Product_Price_After_Discount_textbox = (PATH, '//input[@name="productprice"]')
    Product_Description_textbox = (PATH, "//div[@class='controls']/textarea[@name='productDescription']")
    Product_Shipping_Charge_textbox = (PATH, '//input[@name="productShippingcharge"]')
    Product_Availability_textbox = (PATH, '//select[@id="productAvailability"]')

    Product_Image1 = (PATH, '//input[@name="productimage1"]')
    Product_Image2 = (PATH, '//input[@name="productimage2"]')
    Product_Image3 = (PATH, '//input[@name="productimage3"]')
    insert_button = (PATH, '//button[@type="submit"]')

    def __init__(self, driver):
        self.driver = driver

    def insert_product(self):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.click_element(self.admin_login_link)
        wrapper.enter_text(self.user_name_textbox, value=ReadConfig.get_admin_username())
        wrapper.enter_text(self.password_textbox, value=ReadConfig.get_admin_password())
        wrapper.click_element(self.login_button)

        wrapper.click_element(self.insert_product_link)
        wrapper.drop_down(self.Category_drop_down)
        wrapper.drop_down(self.Sub_Category_drop_down)
        wrapper.enter_text(self.Product_Name_textbox)
        wrapper.enter_text(self.Product_Company_textbox)
        wrapper.enter_text(self.Product_Price_Before_Discount_textbox)
        wrapper.enter_text(self.Product_Price_After_Discount_textbox)
        time.sleep(3)
        wrapper.enter_text(self.Product_Description_textbox)
        wrapper.enter_text(self.Product_Shipping_Charge_textbox)
        wrapper.enter_text(self.Product_Availability_textbox)
        wrapper.enter_text(self.Product_Image1)
        wrapper.enter_text(self.Product_Image2)
        wrapper.enter_text(self.Product_Image3)
        wrapper.click_element(self.insert_button)
        time.sleep(3)











































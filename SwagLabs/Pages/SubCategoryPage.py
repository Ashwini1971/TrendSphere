from Lib.Generic_functions import Wrapper
from utilities.read_properies import ReadConfig

class CreateSubCategoryPage:
    PATH = 'xpath'
    user_name_textbox = (PATH, '//input[@id="inputEmail"]')
    password_textbox = (PATH, '//input[@id="inputPassword"]')
    login_button = (PATH, "//button[.='Login']")

    admin_login_link = (PATH, '//a[@href="admin"]')
    create_subcategory_link = (PATH, '//a[@href="subcategory.php"]')

    category_name_dropdown = (PATH, '//select[@name="category"]')
    subcategory_name_textbox = (PATH, '//input[@name="subcategory"]')
    create_button = (PATH, "//button[.='Create']")


    def __init__(self, driver):
        self.driver = driver

    def manage_product(self):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.click_element(self.admin_login_link)
        wrapper.enter_text(self.user_name_textbox, value=ReadConfig.get_admin_username())
        wrapper.enter_text(self.password_textbox, value=ReadConfig.get_admin_password())
        wrapper.click_element(self.login_button)

        wrapper.click_element(self.create_subcategory_link)
        wrapper.drop_down(self.category_name_dropdown)
        wrapper.enter_text(self.subcategory_name_textbox)
















































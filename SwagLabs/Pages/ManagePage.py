
from Lib.Generic_functions import Wrapper
from utilities.read_properies import ReadConfig

class ManagePage:
    PATH = 'xpath'
    user_name_textbox = (PATH, '//input[@id="inputEmail"]')
    password_textbox = (PATH, '//input[@id="inputPassword"]')
    login_button = (PATH, "//button[.='Login']")

    admin_login_link = (PATH, '//a[@href="admin"]')
    manage_product_link = (PATH, '//a[@href="manage-products.php"]')

    show_count_dropdown = (PATH, '//select[@name="DataTables_Table_0_length"]')
    search_textbox = (PATH, '//input[@type="text"]')


    def __init__(self, driver):
        self.driver = driver

    def manage_product(self):
        wrapper = Wrapper(self.driver)
        wrapper.maximize_browser()
        wrapper.click_element(self.admin_login_link)
        wrapper.enter_text(self.user_name_textbox, value=ReadConfig.get_admin_username())
        wrapper.enter_text(self.password_textbox, value=ReadConfig.get_admin_password())
        wrapper.click_element(self.login_button)

        wrapper.click_element(self.manage_product_link)
        wrapper.drop_down(self.show_count_dropdown)
        wrapper.enter_text(self.search_textbox)
















































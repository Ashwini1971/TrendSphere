from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
# headers = 'r_email,r_pwd,day,month,year,first_name,last_name,gender,postcode'
# datas = [('sashwini.2021@gmail.com', 'Aswini@123', '03', '09', '1999', 'aswini', 'sasi', '562125', 'female')]

class TestRegistration:

    def test_title_verification(self, driver_):
        self.drive = driver_
        excepted_title = self.drive.title
        actual_title = 'H&M | Online Fashion, Homeware & Kids Clothes | H&M IN'
        if excepted_title == actual_title:
            assert True
        else:
            assert False
    # @mark.parametrize(headers, datas)
    def test_registration(self, driver_, pages):
        self.drive = driver_
        wait = WebDriverWait(self.drive, 10)
        accept_button = wait.until(
            EC.element_to_be_clickable(pages.register_page.accept_all_cookies)
        )
        accept_button.click()

        print("Cookies accepted!")
        pages.home_page.click_signin()
        pages.register_page.user_register_(r_email='sashwini.2021@gmail.com',
                                           r_pwd='Aswini@123',
                                           day='03',
                                           month='09',
                                           year='1999',
                                           first_name='aswini',
                                           last_name='sasi',
                                           postcode='562125',
                                           gender='female')

































    
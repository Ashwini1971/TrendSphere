from library.GF import Wrapper
from pages.homepage import HomePage

class RegisterPage(HomePage):
    accept_all_cookies = ('xpath', "//button[.='Accept all cookies']")
    become_a_member_button = ('xpath', "//button[.='Become a member']")
    register_email_textbox = ('xpath','//input[@class="psxM onAo"]')
    register_password_textbox = ('xpath','//input[@class="psxM onAo"]')

    day_textbox = ('xpath', '//input[@id="dateOfBirth"]')
    month_textbox = ('xpath', '//input[@name="month"]')
    year_textbox = ('xpath', '//input[@name="year"]')
    add_more_dropdown = ('xpath', '//span[@class="x_nB F88Q"]')
    customer_first_textbox = ('xpath', '//input[@id="firstName"]')
    customer_last_textbox = ('xpath', '//input[@id="lastName"]')
    customer_gender_dropdown = ('xpath', '//select[@id="gender"]')
    customer_postcode_dropdown = ('xpath', '//input[@id="postalCode"]')
    email_me_updates_checkbox = ('xpath', '//input[@id="hmNewsSubscription"]')
    new_member_button = ('xpath', "//span[.='Become an H&M member']")

    def user_register_(self, *, r_email, r_pwd, day, month, year, first_name, last_name, gender, postcode):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.become_a_member_button)
        wrapper.enter_text(self.register_email_textbox, value=r_email)
        wrapper.enter_text(self.register_password_textbox, value=r_pwd)
        wrapper.enter_text(self.day_textbox, value=day)
        wrapper.enter_text(self.month_textbox, value=month)
        wrapper.enter_text(self.year_textbox, value=year)
        wrapper.click_element(self.add_more_dropdown)
        wrapper.enter_text(self.customer_first_textbox, value=first_name)
        wrapper.enter_text(self.customer_last_textbox, value=last_name)
        wrapper.drop_down(self.customer_gender_dropdown, value=gender)
        wrapper.enter_text(self.customer_postcode_dropdown, value=postcode)
        wrapper.click_element(self.email_me_updates_checkbox)
        wrapper.click_element(self.new_member_button)







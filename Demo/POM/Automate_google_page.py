from Lib.genericfunction import Wrapper

class AutomateGoogle(Wrapper):
    search_textfield = ('xpath', '//input[@class="lst"]')
    sign_out_button = ('xpath', '//button[@class="M6CB1c rr4y5c"]')
    google_search_button = ('xpath', '//input[@value="Google Search"]')

    def enter_search_data(self, search_data):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.search_textfield, value=search_data)
        wrapper.click_element(self.sign_out_button)
        wrapper.click_element(self.google_search_button)








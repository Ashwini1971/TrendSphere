from library.GF import Wrapper

class HomePage(Wrapper):
    signin_link = ('xpath', '//button[@class="CGae mYRh vEfo __5DXf k0Zy"]')
    favourite_link = ('xpath', '//span[@class="Gxpv"]')
    shopping_bag_link = ('xpath', '//span[@class="DU5j"]')
    search_textbox = ('xpath', '(//input[@class="psxM XAI6"])[1]')


    def click_signin(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.signin_link)

    def click_favourite(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.favourite_link)

    def click_shopping_bag(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.shopping_bag_link)

    def click_search(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.search_textbox)






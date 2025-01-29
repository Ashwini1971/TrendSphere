
class TestGoogleSearch:

    def test_title_verification(self, driver_):
        self.drive = driver_
        excepted_title = self.drive.title
        actual_title = 'Google'
        if excepted_title == actual_title:
            assert True
        else:
            assert False

    def test_google(self, driver_, pages):
        self.drive = driver_
        pages.automate_google_page.enter_search_data('Selenium Python documentation')



































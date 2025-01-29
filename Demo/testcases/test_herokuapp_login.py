from utilitiesfiles.config import ReadConfig
class TestGoogleSearch:

    def test_title_verification(self, driver_):
        self.drive = driver_
        excepted_title = self.drive.title
        actual_title = 'The Internet'
        if excepted_title == actual_title:
            assert True
        else:
            assert False

    def test_heroku_app(self, driver_, pages):
        self.drive = driver_
        pages.login_auto.login_heroku_app(ReadConfig.user_name(),
                                          ReadConfig.password_())



































import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as chr_
from POM.Automate_google_page import AutomateGoogle
from POM.login_automation import Login

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help='specify the browser: chrome or firefox or edge')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def driver_(browser):
    driver = chr_()
    driver.get('https://the-internet.herokuapp.com/login')
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def pages(driver_):
    class pages:
        automate_google_page = AutomateGoogle(driver_)
        login_auto = Login(driver_)
    return pages()




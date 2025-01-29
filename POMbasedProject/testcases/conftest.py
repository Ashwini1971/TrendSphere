from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from utilities.read_properies import ReadConfig
import pytest

#To get command line option for the browsers
def pytest_addoption(parser):
     parser.addoption('--browser', action='store', default='firefox',
                      help='specify the browser: chrome or firefox or edge')

# To obtain values of browser
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def setup(browser):
    # global driver_
    if browser == 'chrome':
        driver_ = Chrome()
    elif browser == 'firefox':
        driver_ = Firefox()
    elif browser == 'edge':
        driver_ = Edge()
    else:
        raise ValueError('unsupported browser')
    driver_.get(ReadConfig.get_url())
    yield driver_
    driver_.close()


# @fixture()
# def pages(driver):
#     class pages:
#         login1 = LoginPage(driver)
#     return pages()



# Hook to adding environment info in html reports
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce project, nopcommerce'
    config.stash[metadata_key]['Test module name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester name'] = 'Aswini'

# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop("plugins", None)
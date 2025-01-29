import pytest
from selenium.webdriver.chrome.webdriver import WebDriver as chr_
from pages.registerpage import RegisterPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from  utilities.config import ReadConfig

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                     help='specify the browser: chrome or firefox or edge')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def driver_(browser):
    driver = chr_()
    driver.get(ReadConfig.get_url())
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture()
def pages(driver_):
    class pages:
        home_page = HomePage(driver_)
        register_page = RegisterPage(driver_)
        login_page = LoginPage(driver_)
    return pages()

# import csv
#
# with open(r'C:\Users\User\PycharmProjects\MyProjectTrendSphere\stu1.csv') as file1:
#     with open(r'C:\Users\User\PycharmProjects\MyProjectTrendSphere\stu2.csv') as file2:
#         read_1 = csv.reader(file1)
#         read_2 = csv.reader(file2)
#         header1, header2 = next(read_1), next(read_2)
#         for data1, data2 in zip(read_1, read_2):
#             print(data1, data2)

# with open(r'C:\Users\User\PycharmProjects\MyProjectTrendSphere\stu2.csv') as file2:
#     read_2 = csv.reader(file2)
#     header = next(read_2)
#     for data in read_2:
#         print(data)



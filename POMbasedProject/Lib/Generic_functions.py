from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait



def wait_(func):
    def wrapper_(*args, **kwargs):
        driver_instance_self = args[0] # self
        locator_ = args[1] #
        wait = WebDriverWait(driver_instance_self.driver, 30)
        wait.until(EC.visibility_of_element_located(locator_))
        return func(*args, **kwargs)
    return wrapper_


class Wrapper:

    def __init__(self, driver_):
        self.driver = driver_

    def refresh_page(self):
        self.driver.refresh()

    def maximize_browser(self):
        self.driver.maximize_window()

    def minimize_browser(self):
        self.driver.minimize_window()

    @wait_
    def webpage_title(self):
        return self.driver.title

    @wait_
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait_
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def page_up_(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()

    def page_down_(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    def Arrow_down_(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()

    def Arrow_up_(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_UP).perform()

    @wait_
    def context_click(self, locator):
        actions = ActionChains(self.driver)
        desktop = self.driver.find_element(*locator)
        actions.context_click(desktop).perform()

    @wait_
    def double_click(self, locator):
        actions = ActionChains(self.driver)
        desktop = self.driver.find_element(*locator)
        actions.double_click(desktop).perform()


    @wait_
    def drag_drop(self, locator1, locator2):

        source_element = self.driver.find_element(*locator1)
        destination_element = self.driver.find_element(*locator2)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, destination_element).perform()

    @wait_
    def drop_down(self, locator, value):
        dropdown_data = self.driver.find_element(*locator)
        drop_select_ = Select(dropdown_data)
        drop_select_.select_by_visible_text(value)






















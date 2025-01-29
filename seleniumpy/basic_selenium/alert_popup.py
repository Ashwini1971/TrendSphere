import time

from selenium.webdriver.chrome.webdriver import WebDriver as driver

chrome_ = driver()
chrome_.implicitly_wait(10)
chrome_.get('https://testautomationpractice.blogspot.com/')
'To click on OKAY'
chrome_.find_element('xpath', "//button[.='Simple Alert']").click()
'alert and popup'
my_alert = chrome_.switch_to.alert
print(my_alert.text)
my_alert.accept()
time.sleep(3)

'To click on ok or cancel'
chrome_.find_element('xpath', '//button[@id="confirmBtn"]').click()
print(my_alert.text)
my_alert.dismiss()
time.sleep(3)

'To press a data'
chrome_.find_element('xpath', '//button[@id="promptBtn"]').click()
print(my_alert.text)
my_alert.send_keys('test-automation')
my_alert.accept()
# my_alert.dismiss()
time.sleep(5)
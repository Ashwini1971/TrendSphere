import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from csv import DictReader, reader, writer

from urllib3.filepost import writer

'--------end to end scenario of demo_webshop--------'
# chrome_ = WebDriver()
# chrome_.get('https://demowebshop.tricentis.com/')
# chrome_.implicitly_wait(5)
# chrome_.maximize_window()
'---------------------Register----------------------------------'
# chrome_.find_element('xpath', "//a[.='Register']").click()
#
# # gender_input = input('Choose the gender : ')
# # if gender_input == 'female':
# chrome_.find_element('xpath', '//input[@id="gender-female"]').click()
#
# # elif gender_input == 'male':
# #     chrome_.find_element('xpath', '//input[@id="gender-male"]').click()
#
# webelements_details1 = chrome_.find_elements('xpath',
#                                     '//input[@class="text-box single-line"]')
# details_datas = ['aswini', 'sasidharan', 'sashwini.2021@gmail.com']
# for web_holder, element in zip(webelements_details1, details_datas):
#     time.sleep(1)
#     web_holder.send_keys(element)
#
#
# webelements_password2 = chrome_.find_elements('xpath', '//input[@class="text-box single-line password"]')
# password_ = 'aswini@123'
# for web_holder in webelements_password2:
#     time.sleep(1)
#     web_holder.send_keys(password_)
#
# submit_button = chrome_.find_element('xpath', '//input[@id="register-button"]')
# submit_button.click()

'---------------------------login---------------------------------------'

# chrome_.find_element('xpath', "//a[.='Log in']").click()
# login_customer = chrome_.find_elements('xpath', '//div[@class="inputs"]//input')
# login_credentials = ["sashwini.alpha@gmail.com", 'Achu@123']
#
# for web_ele, data in zip(login_customer, login_credentials):
#     web_ele.send_keys(data)
#
# chrome_.find_element('xpath', '//input[@id="RememberMe"]').click()
# chrome_.find_element('xpath', '//input[@class="button-1 login-button"]').click()
#
# "//span[.='1800.00']"
# "//span[.='24.00']/../..//input[@value='Add to cart']"
# '------------search-----------------'
# chrome_.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('computer')
# chrome_.find_element('xpath', '//input[@type="submit"]').click()
#
#
# actions = ActionChains(chrome_)
# actions.send_keys(Keys.ARROW_DOWN)
# time.sleep(4)
# chrome_.find_element('xpath', "//span[.='1800.00']//../..//input[@value='Add to cart']").click()
# chrome_.find_element('xpath', '//input[@id="add-to-cart-button-74"]').click()
# chrome_.find_element('xpath', "//span[.='Shopping cart']").click()
# time.sleep(2)
#
'-----------checkout-------------'
# countries1 = chrome_.find_element('xpath', '//select[@id="CountryId"]')
# select_1 = Select(countries1)
# select_1.select_by_visible_text('India')
# chrome_.find_element('xpath', '//input[@name="estimateshipping"]').click()
# chrome_.find_element('xpath', '//input[@id="termsofservice"]').click()
# chrome_.find_element('xpath', '//button[@name="checkout"]').click()
# time.sleep(2)
#
'--------------billing_address----------'
# billing_address_textbox = chrome_.find_element('xpath', '//select[@name="billing_address_id"]')
# select_3 = Select(billing_address_textbox)
# select_3.select_by_visible_text('aswini sasidharan, sarjapur, bangalore 562125, India')



# billing_address_details = ['aswini', 'sasidharan', 'sashwini.alpha@gmail.com', 'TYSS', 'bangalore',
#                    'sarjapur', '', '562125', '7795361971', '']
# for text_box, data  in zip(billing_address_textbox, billing_address_details):
#     text_box.clear()
#     time.sleep(1)
#     text_box.send_keys(data)

# countries2 = chrome_.find_element('xpath', '//select[@id="BillingNewAddress_CountryId"]')
# select_2 = Select(countries2)
# select_2.select_by_visible_text('India')
# time.sleep(3)
# chrome_.find_element('xpath', '(//input[@title="Continue"])[1]').click()
# time.sleep(2)
'--------------shipping_address----------'

# chrome_.find_element('xpath', '//input[@type="checkbox"]').click()
# chrome_.find_element('xpath', '(//input[@class="button-1 new-address-next-step-button"])[2]').click()
# chrome_.find_element('xpath', '//input[@id="paymentmethod_0"]').click()
# chrome_.find_element('xpath', '//input[@class="button-1 payment-method-next-step-button"]').click()
# chrome_.find_element('xpath', '//input[@class="button-1 payment-info-next-step-button"]').click()
# chrome_.find_element('xpath', '//input[@value="Confirm"]').click()
# time.sleep(2)
# chrome_.find_element('xpath', '//input[@value="Continue"]').click()
# time.sleep(2)

def duplicate_data(file_1, file_2, output_file):
    with open(file_1) as file1:
        header1 = next(file1)
        line1 = file1.readlines()
        print(line1)

    with open(file_2) as file2:
        header2 = next(file2)
        line2 = file2.readlines()

    combined_lines = line1 + line2
    unique_lines = set(line for line in combined_lines)

    with open(output_file, 'w') as file3:
        for line in unique_lines:
            file3.write(line)



file_1 = 'csvfiles/stu1.csv'
file_2 = 'csvfiles/stu2.csv'
output_file = 'csvfiles/non-dul1.csv'
print(duplicate_data(file_1, file_2, output_file))

























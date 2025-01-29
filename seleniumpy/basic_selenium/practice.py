import time
from selenium.webdriver.chrome.webdriver import WebDriver as chr_
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from time import sleep
driver = chr_()

# driver.get('https://demoqa.com/select-menu')
# driver.maximize_window()

# list_box = driver.find_element('xpath', '//select[@id="oldSelectMenu"]')
# select = Select(list_box)
'Write a program to select an option from a dropdown by visible text.'
# select.select_by_visible_text('Blue')
# time.sleep(3)
'''
Write a program to select an option from a dropdown using the value attribute.
'''
# select.select_by_value('2')
# time.sleep(3)
'Create a Selenium script to print all the options available in a dropdown.'
# list_box = driver.find_elements('xpath', '//select[@id="oldSelectMenu"]')
# for l_b in list_box:
#     print(l_b.text)
'How can you check if a dropdown supports multiple selections? Write a program to demonstrate it'
'Write a program to select the last option in a dropdown by index.'

# multiple_dropdown = driver.find_element('xpath', '//select[@name="cars"]')
# dropdown = Select(multiple_dropdown)
# dropdown.select_by_visible_text('Volvo')
# dropdown.select_by_visible_text('Audi')
# time.sleep(2)
# if dropdown.is_multiple:
#     print(True)
'Write a program to select the last option in a dropdown by index.'
# data = driver.find_elements('xpath', '//select[@name="cars"]')
#
# for d in data:
#    print(d.text.replace('\n', ' ').split()[-1])

'''
Create a script to select all options in a multi-select 
dropdown one by one and then deselect all options.
'''
# multiple_dropdown = driver.find_element('xpath', '//select[@name="cars"]')
# dropdown = Select(multiple_dropdown)
# all_options = dropdown.options
#
# if dropdown.is_multiple:
#     print(True)
#
# for car in all_options:
#     print('Selecting all options')
#     sleep(1)
#     dropdown.select_by_visible_text(car.text)
#
#
# print('Deselecting all options')
# dropdown.deselect_all()
# sleep(1)

'''
Write a program to verify if a specific option exists in a dropdown. 
If it does, select it.

'''
# multiple_options = driver.find_element('xpath', '//select[@name="cars"]')
# select = Select(multiple_options)
# all_options = select.options
#
# for option in all_options:
#     if option.text == 'Saab':
#         select.select_by_visible_text(option.text)
#         sleep(2)
'''
Write a Selenium script to handle nested dropdowns 
(a dropdown within another dropdown menu).
'''


'''
Write a script to verify that the default selected option 
in a dropdown is correct.
'''
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# driver.maximize_window()
#
# time.sleep(3)
# driver.find_element('xpath', '//input[@id="phone"]').send_keys('7795361971')
# dr_ = driver.find_element('xpath', '//select[@id="select1"]')
# select_country = Select(dr_)
# default_selected = select_country.first_selected_option
# print(default_selected.text)
# time.sleep(2)
# assert '+91' == default_selected.text, 'Equal'
'''
Create a program to count the number of options in a dropdown 
and assert if it matches an expected count.
'''
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# driver.maximize_window()
# time.sleep(3)
# drop_down = driver.find_element('xpath', '//select[@id="select1"]')
# select_options = Select(drop_down)
# options = select_options.options
# print('Count of country_code : ', len(options))
'''
Automate a scenario where the dropdown options are dynamically 
loaded after clicking a button. Select the third option 
after the dropdown is populated.
'''
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# driver.maximize_window()
# time.sleep(3)
# drop_down = driver.find_element('xpath', '//select[@id="select1"]')
# select_options = Select(drop_down)
# select_options.select_by_index(3)

'''
Write a script to handle a dropdown where the options are not enclosed in a 
<select> tag but instead implemented using <div> or <ul> elements.
'''
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# driver.maximize_window()
# time.sleep(3)
# drop_down = driver.find_element('xpath', '//select[@id="select1"]')
# select_options = Select(drop_down)
# select_options.select_by_index(3)
'''
Write a program to validate whether selecting different options from a 
dropdown triggers the expected changes in other elements of the webpage 
(e.g., a table, graph, or text).

Automate a test case to select an option in a dropdown, submit the form, 
and verify the result on the next page.

Create a script to interact with a multi-select dropdown and ensure 
specific options are selected while others remain unselected.

'''
'''
Scenario-Based Practice:
On an e-commerce website:
Select a product category from a dropdown.
Verify that the displayed products belong to the selected category.
'''
# driver.get('https://demoapps.qspiders.com/ui/dropdown?sublist=0')
# driver.maximize_window()
# time.sleep(3)
# d = driver.find_element('xpath', '(//div[contains(@class, " css-19bb58m")])[3]')
# select_ = Select(d)
# all_otp = select_.options
# for otp in all_otp:
#     print(otp.text)
# select_.select_by_visible_text('Germany')

'''
On a travel website:
Select a departure city and destination city from two dropdowns.
Verify that the chosen cities are reflected in the search results.


On a registration form:
Select your country from a dropdown.
Verify that the corresponding state/province dropdown is updated correctly.


On a job portal:
Select a job role from a dropdown.
Validate that only relevant job postings are displayed after 
clicking the search button.

On a banking website:
Select an account type (e.g., savings, current) from a dropdown.
Verify that the interest rates or features displayed are specific 
to the selected account type.
'''


















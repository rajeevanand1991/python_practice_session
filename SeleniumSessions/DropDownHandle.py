from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/hr-software-sign-up/")


# Suppose if we have n number of dropdown in the webpage, every time we need to create object reference for select class.
# To avoid this, we can create a custom method on that.

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


# generic method without using select class:
def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))  # 233
    for ele in dropDownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

country_options = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')
select_values_from_dropdown(country_options, 'China')

ele_country = driver.find_element(By.ID, 'Form_getForm_Country')
select = Select(ele_country)
# select.select_by_visible_text('Argentina') #This is inside the tag: <option>Argentina</option>
# select.select_by_index(4)
select.select_by_value('United Arab Emirates')  # This is <option value="United Arab Emirates">

print(select.is_multiple)  # Prints None

# simply we can call this method, to avoid above lines of code repititive
select_values(ele_country, 'United Arab Emirates')

# To collect all the options values in the select dropdown:
select = Select(ele_country)
cou_list = select.options

for ele in cou_list:  # Iterate over the for loop
    print(ele.text)
    if (ele.text == 'South Africa'):
        ele.click()
        break

# Famous Interview question: select a dropdown value without using Select class
country_options = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')
print(len(country_options))  # 233
for ele in country_options:
    print(ele.text)
    if ele.text == 'Australia':
        ele.click()
        break
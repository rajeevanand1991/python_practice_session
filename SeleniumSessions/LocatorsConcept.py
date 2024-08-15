#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/30-day-free-trial/")
driver.maximize_window()

print(driver.title) #30-Day Advanced Free Trial | OrangeHRM

#we can use the variable(username_url) like WebElement in Java like below:
username_url = driver.find_element(By.ID,'Form_getForm_subdomain')
full_name = driver.find_element(By.ID,'Form_getForm_Name')
email = driver.find_element(By.ID,'Form_getForm_Email')
phone_number = driver.find_element(By.ID,'Form_getForm_Contact')
solutions_link = driver.find_element(By.LINK_TEXT,'Solutions')

username_url.send_keys("rajeevautomationlabs")
full_name.send_keys("Rajeev Anand K.R")
email.send_keys("rajeevanand1991@gmail.com")
phone_number.send_keys("9940939678")
solutions_link.click()

time.sleep(5)
driver.quit()
#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/login.cfm")
driver.maximize_window()

username = driver.find_element(By.NAME,'username')
password = driver.find_element(By.NAME,'password')
login_button = driver.find_element(By.XPATH,"//input[@value='Login']")

username.send_keys("batchautomation")
password.send_keys("Test@12345")
login_button.click()

print(driver.title) #Free CRM software for customer relationship management, sales, and support.
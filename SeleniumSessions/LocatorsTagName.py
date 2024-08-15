#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com/")
driver.maximize_window()

header_element = driver.find_element(By.TAG_NAME,'h1')
print(header_element.text) #Same easy software. New AI superpowers.

time.sleep(5)
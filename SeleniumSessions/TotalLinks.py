#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

linksList = driver.find_elements(By.TAG_NAME,'a')
print(len(linksList)) #371

for ele in linksList:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

imageList = driver.find_elements(By.TAG_NAME,'img')
print(len(imageList)) #224

for ele in imageList:
    print(ele.get_attribute('src'))
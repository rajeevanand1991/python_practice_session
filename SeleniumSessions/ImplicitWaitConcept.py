from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(20)
#time out = 10
#dynamic wait
#imp wait will be applied for all the web elements
#global wait
#find_element
#find_elements
#only for web elements
#not gor non web elements: title, url, alerts

driver.get("https://app.hubspot.com/login")

print(driver.title)

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")

#driver.implicitly_wait(5) #we are overriding now to maintain 5 seconds from now, the disadvantage is like follow 5 seconds for all web elements if element not loading

driver.find_element(By.ID, 'password').send_keys("test@12345")

#driver.implicitly_wait(0) #nullify of imp wait

#e3
#e4

#e5
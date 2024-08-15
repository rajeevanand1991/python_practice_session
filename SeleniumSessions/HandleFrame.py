from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://www.londonfreelance.org/courses/frames/index.html")

#driver.switch_to.frame(2) #just count the number of index (start from 0-n) frame in F12 Dev Tools
#driver.switch_to.frame('main') #RECOMMENDED!! This is frame name we are using.
# we can use this below approach as well like frame element:
frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(headerValue)

driver.switch_to.default_content() #To come back completely from the whole frames
driver.switch_to.parent_frame() #it wil go one level to the parent frame alone

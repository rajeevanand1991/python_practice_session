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

driver.get("https://amazon.in")
driver.find_element(By.Link_Text, 'Best Sellers').click()
time.sleep(2)

driver.back() #it will go back from Best sellers page to amazon.in main page
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()

driver.quit()
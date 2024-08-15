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

driver.get("https://www.reddit.com/")
print(driver.get_cookies())

#or we can follow below way as well:

cookies = driver.get_cookies() #it will return one dictionary

for cook in cookies:
	print(cook)

driver.add_cookie({"name":"rajeevpython", "domain": "reddit.com", "value":"python"})
print(driver.get_cookies())
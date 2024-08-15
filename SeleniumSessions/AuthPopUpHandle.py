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

#This is the real webpage url below:
#driver.get("https://the-internet.herokuapp.com/basic_auth")

#For handling Authentication pop up: username and password: admin we are passing in the url with : separator
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

#This is for chrome
#options = webdriver.ChromeOptions()
#options.headless = True #way 1: we can set True to enable and False to disable
#options.add_argument('--headless') #way 2: To run it in the headless mode, by skipping above line
#options.add_argument('--incognito')
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#This is for firefox
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(GeckoDriverManager().install(), options=options)
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options) #use this code if above line not works

driver.implicity_wait(10)

driver.get("https://amazon.com/")
print(driver.title)
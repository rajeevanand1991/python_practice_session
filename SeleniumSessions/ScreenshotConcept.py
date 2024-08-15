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

#options = webdriver.ChromeOptions()
#options.headless = True #way 1: we can set True to enable and False to disable
#options.add_argument('--headless') #way 2: To run it in the headless mode, by skipping above line
#options.add_argument('--incognito')
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.reddit.com/")
#driver.get_screenshot_as_file('reddit_1.png') #way 1 to take screenshot

'''full screenshot'''
#make sure that you are running in headless mode

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')
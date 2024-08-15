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

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
time.sleep(3)

'''This is drag and drop example'''
source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")

act_chains = ActionChains(driver)
#act_chains.drag_and_drop(source,target).perform() #one way

#Interview question, For DragAndDrop, what are the different actions you can perform? other than drag_and_drop() direct method.
act_chains.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(3)
driver.quit()
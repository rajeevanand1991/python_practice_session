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

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(3)

'''This is right/context click example'''
right_click_ele = driver.find_element(By.XPATH,"//span[text()='right click me']")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR,"li.context-menu-item span")
for ele in right_click_options:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break

time.sleep(3)
driver.quit()
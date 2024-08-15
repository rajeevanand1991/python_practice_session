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

driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(3)
'''move to element''' #This is comment by using triple quotes '''
addon_ele = driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n']/div/div/div[text()='Add-ons']")
act_chains = ActionChains(driver)
act_chains.move_to_element(addon_ele).perform()

senior_ctzn_disc_ele = driver.find_element(By.XPATH,"//a[@rel='noopener noreferrer']/div/div[text()='Senior Citizen Discount']")
senior_ctzn_disc_ele.click()

time.sleep(3)
driver.quit()
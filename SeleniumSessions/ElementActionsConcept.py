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

driver.get("https://app.hubspot.com/login")
driver.maximize_window()
time.sleep(3)

'''This is Element Actions Concept example'''

username_ele = driver.find_element(By.ID,'username')
password_ele = driver.find_element(By.ID,'password')
login_button_ele = driver.find_element(By.ID,'loginBtn')
#The below locator used for login button in the classiccrmpro.com
#login_button_ele = driver.find_element(By.XPATH,"//input[@type='submit']")

act_chains = ActionChains(driver)
#act_chains.send_keys_to_element(username_ele,'batchautomation@gmail.com').perform() ==> sometimes this .perform() will type multiple times in the UI screen, during that time, we can AVOID this .perform() method
act_chains.send_keys_to_element(username_ele,'batchautomation@gmail.com').perform()
act_chains.send_keys_to_element(password_ele,'Test@12345').perform()
act_chains.click(login_button_ele).perform()

time.sleep(3)
driver.quit()
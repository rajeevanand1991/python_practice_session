from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://app.hubspot.com/login")

#Explicit wait added below:
wait = WebDriverWait(driver, 10)
#wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains('HubSpot'))

print(driver.title)

#wait.until(expected_conditions())
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('test@gmail.com')

driver.find_element(By.ID, 'password').send_keys("test@123")
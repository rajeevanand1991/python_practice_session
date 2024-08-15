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

wait = WebDriverWait(driver, 10)
signup_link = wait.until(ec.element_to_be_clickable((By.Link_Text, 'Sign up')))
print(signup_link.text)
signup_link.click()

#visibility_of_element_located ==> will check not only in DOM, also in the page as well
first_name = wait.until(ec.visibility_of_element_located((By.ID, 'uid-firstName-5')))
first_name.send_keys('rajeev')
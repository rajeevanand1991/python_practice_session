from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME, 'proceed').click()

wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
driver.close()
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
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
alert.accept() #accept it, click on OK button simply
alert.dismiss() #cancel the pop up

#If suppose do you need to pass/write some values in the alert, use below method:
#alert.send_keys('hi')

driver.switch_to.default_content() #This will come back from alert to webdriver UI screen

time.sleep(3)
driver.quit()

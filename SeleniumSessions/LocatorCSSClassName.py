#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
driver.maximize_window()

#username1 = driver.find_element(By.CSS_SELECTOR,'#username')
#The below are presence on the Inspect of chrome on class name field element
#class="form-control private-form__control login-email"
#class="form-control private-form__control login-password m-bottom-3"
#username2 = driver.find_element(By.CLASS_NAME,'login-email')
#username3 = driver.find_element(By.CSS_SELECTOR,'input.form-control.private-form__control.login-email')
username4 = driver.find_element(By.XPATH,"//input[@class='form-control private-form__control login-email']")
password = driver.find_element(By.CLASS_NAME,'login-password')
login_button = driver.find_element(By.CLASS_NAME,'login-submit')

#username1.send_keys("rajeev30@gmail.com")
#username1.clear()
#username2.send_keys("updatedrajeev30@gmail.com")
#username3.send_keys("testCSSSelector@gmail.com")
username4.send_keys("testXPATH@gmail.com")
password.send_keys("Test@12345")
login_button.click()

print(driver.title) #HubSpot Login and Sign in

#driver.find_element(By.LINK_TEXT,'Get started free').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'free').click()

time.sleep(5)
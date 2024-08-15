from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].click();" ,best_sellers) #To make click

title = driver.execute_script("return document.title;") #To return the title of the page
print(title)

driver.execute_script("history.go(0);") #To refresh the page

#To generate an alert explicitly
driver.execute_script("alert('hello Selenium');")

#To view what all are the elements present in the webpage:
inner_text = driver.execute_script("return document.documentElement.innerText;")
print(inner_text)

driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)

#To highlight webelement on the complete form:
#driver.get("https://app.hubspot.com/login")
#form = driver.find_element(By.ID, 'hs-login')
#driver.execute_script("arguments[0].style.border = '3px solid red'",form)

#To scroll down bottom of the webpage completely:
#driver.get("https://classic.freecrm.com/")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

#To scroll down the webpage until the particular specified webelement alone
#forgot_pwd = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
#driver.execute_script("arguments[0].scrollIntoView(true);", forgot_pwd)
#driver.get("https://www.amazon.in/")
#sports_header = driver.find_element(By.XPATH, "//span[text()='Best Sellers in Sports, Fitness & Outdoors']")
#driver.execute_script("arguments[0].scrollIntoView(true);", sports_header)

#To show what browser, user is currently using:
print(driver.execute_script("return navigator.userAgent;"))

#To scroll up top of the webpage completely:
#driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

#Type value in textbox:
#driver.get("https://app.hubspot.com/login")
#driver.execute_script("document.getElementById('username').value='rajeev@gmail.com';")
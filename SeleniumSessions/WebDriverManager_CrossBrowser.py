#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "chrome"

if browserName == "chrome":
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    #driver = webdriver.Chrome(ChromeDriverManager().install()) ==> #Getting Traceback (most recent call last) error
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #TypeError: 'module' object is not callable
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print('please pass the correct browser name: '+browserName)
    raise Exception('driver is not found')#This will Throw an exception explicitly by not executing driver lines of code unnecessarily

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
driver.find_element(By.ID,'username').send_keys("rajeevanand1991@gmail.com")
driver.find_element(By.ID,'password').send_keys("Test@12345")
driver.find_element(By.ID,'loginBtn').click()

print(driver.title) #HubSpot Login and Sign in

time.sleep(4)
driver.quit()
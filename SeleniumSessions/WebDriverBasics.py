#importing selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Rajeev") #Rajeev
#TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path'
#driver = webdriver.Chrome(executable_path="C:\\Users\\Anand\\PycharmProjects\\PythonSeleniumSessions\\drivers\\chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com")
title=driver.title
print(title) #Google

driver.find_element(By.NAME,'q').send_keys("naveen automationlabs")
optionsList = driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li span')
print(len(optionsList)) #50

for ele in optionsList:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

time.sleep(5) #same as like Thread.sleep() method in Java
driver.close()

driver = webdriver.Chrome()
#driver = webdriver.Chrome("C:\\Users\\Anand\\PycharmProjects\\PythonSeleniumSessions\\drivers\\chromedriver")
driver.get("https://www.freecrm.com")
title=driver.title
print(title) #1 Free CRM Power Up your Entire Business Free Forever customer relationship management
driver.close()

driver = webdriver.Chrome()

driver.get("https://ui.cogmento.com/")

title=driver.title

print(title) #Cogmento CRM

#assert "Cogmento CRM" in title

userName = driver.find_element(By.NAME,"email")
userName.send_keys("naveenk")
password = driver.find_element(By.NAME, "password")
password.send_keys("test@123")
driver.quit()
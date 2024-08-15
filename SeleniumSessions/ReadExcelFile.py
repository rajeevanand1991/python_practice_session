import xlrd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/30-day-free-trial/")

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
comp_name = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
contact = driver.find_element(By.ID, 'Form_submitForm_Contact')
total_emp = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
country = driver.find_element(By.ID, 'Form_submitForm_Country')

workbook = xlrd.open_workbook("DataFile.xlsx")
#for sheet1 we used login
#sheet = workbook.sheet_by_name("login")

#for sheet2 we used registration
sheet = workbook.sheet_by_name("registration")

#get total number of rows:
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount) #prints 3
print(colCount) #prints 2

for curr_row in range(1, rowCount):
    #for sheet 1 login we use this:
    #user_name = sheet.cell_value(curr_row, 0)
    #password = sheet.cell_value(curr_row, 1)

    #print(user_name + " " + password)

     urlValue = sheet.cell_value(curr_row, 0)
     firstName = sheet.cell_value(curr_row, 1)
     lastName = sheet.cell_value(curr_row, 2)
     emailID = sheet.cell_value(curr_row, 3)
     jobTitle = sheet.cell_value(curr_row, 4)
     company = sheet.cell_value(curr_row, 5)
     phoneNumber = sheet.cell_value(curr_row, 6)
     totalEmp = sheet.cell_value(curr_row, 7)
     industry_name = sheet.cell_value(curr_row, 8)
     countryName = sheet.cell_value(curr_row, 9)

     print(url + firstName + lastName)

     url.clear()
     url.send_keys(urlValue)
     first_name.clear()
     first_name.send_keys(firstName)
     last_name.clear()
     last_name.send_keys(lastName)
     email.clear()
     email.send_keys(emailID)
     job_title.clear()
     job_title.send_keys(jobTitle)
     comp_name.clear()
     comp_name.send_keys(company)
     contact.clear()
     contact.send_keys(phoneNumber)
     total_emp.clear()
     total_emp.send_keys(totalEmp)
     industry.clear()
     industry.send_keys(industry_name)
     country.clear()
     country.send_keys(countryName)

     time.sleep(4)
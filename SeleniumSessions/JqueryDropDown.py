from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

def select_values(options_list, value):
    if not value[0] == 'all':
        for ele in drop_list:
            print(ele.text)
            #Suppose if we have many values to select, use this for loop concept to iterate over list
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try: # using try except block as like in Java try/catch block to handle the ElementNotInteractableException
             # because out of 45 elements, only 15 elements we can click in the UI screen
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)

        #This exisiting code not required
        #if ele.text == value:
         #   ele.click()
         #   break

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(3)

drop_list = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
#values_list = ['choice 2', 'choice 3', 'choice 6 2 1'] #passing some specific values
#values_list = ['choice 7'] #passing single value
values_list = ['all'] #This is for selecting all values in the dropdown

select_values(drop_list, values_list)

# Tedious job if we have multiple value to call the below function every time
#select_values(drop_list, 'choice 2')
#select_values(drop_list, 'choice 3')
#select_values(drop_list, 'choice 6 2 1')

time.sleep(2)
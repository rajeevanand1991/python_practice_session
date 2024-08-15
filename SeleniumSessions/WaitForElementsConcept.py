from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.freshworks.com/")

wait = WebDriverWait(driver, 10)
#both these also we can use as well: visibility_of_all_elements_located and visibility_of_any_elements_located
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for ele in footer_links:
	print(ele.text)

#For Frame, we can use this
wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID, 'test')))

#Dropdown values and Checkbox value, we can use this
wait.until(ec.element_located_to_be_selected('checkbox'))

#For url, we can use this as well: url_changes, url_matches, url_to_be
wait.until(ec.url_contains('freshworks'))
from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("----------------setup---------------------")
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.co.in")

    yield #This will execute after all the test case at the end
    print("----------------tear down---------------------")
    driver.quit()

#way2:
#@pytest.mark.usefixtures("init_driver")
#def test_google_title():
#@pytest.mark.usefixtures("init_driver")
#def test_google_url():

#way 1: def test_google_title(init_driver):
def test_google_title(init_driver):
    assert driver.title == "Google11"

def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.co.in/"
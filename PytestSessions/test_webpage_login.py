from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

def test_google():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.co.in")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_insta():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://mail.google.com/mail/")
    assert driver.title == "Gmail"
    driver.quit()

def test_rediff():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://m.rediff.com/")
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()
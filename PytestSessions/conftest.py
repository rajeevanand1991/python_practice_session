import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains #will use it for to perform all the actions like move to elements, drag & drop, Right click and user actions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time
import pytest
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture(params=["chrome", "firefox"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        web_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.fixture
def input_total():
    total = 100
    return total
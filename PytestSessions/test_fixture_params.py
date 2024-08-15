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

#we have commented that, conftest.py file added for this replacement of code taken from that place
# @pytest.fixture(params=["chrome", "firefox"],scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = Chrome(service=Service(ChromeDriverManager().install()))
#     if request.param == "firefox":
#         web_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.get("https://www.google.co.in")
        assert self.driver.title == "Google"


    def test_google_url(self):
        self.driver.get("https://www.google.co.in")
        assert self.driver.current_url == "https://www.google.co.in/"
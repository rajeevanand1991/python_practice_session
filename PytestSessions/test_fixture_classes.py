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


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):

    def test_google_title_chrome(self):
        self.driver.get("https://www.google.co.in")
        assert self.driver.title == "Google"
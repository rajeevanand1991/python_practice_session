from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
                                "username, password",
                                [
                                    ("admin@gmail.com", "admin@123"),
                                    ("rajeev@gmail.com","rajeev123")
                                ]
                            )

    def test_login(self, username, password):
        """ #This is the documentation to understand the logic
        This method is used to login to hub spot application
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(3)
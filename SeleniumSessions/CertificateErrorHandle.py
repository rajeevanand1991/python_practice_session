from selenium import webdriver
from selenium.webdriver import Chrome, DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import time

#WAY 1: Chrome browser will work
#options = Options()
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')

#WAY 2: Chrome browser will work
#desired_capabilities = DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCerts'] = True

#WAY 3: Chrome browser will work
options = Options()
options.set_capability('acceptInsecureCerts', True)

#WAY 1:
#driver = Chrome(service=Service(ChromeDriverManager().install(), options = options))

#WAY 2:
driver = Chrome(service=Service(ChromeDriverManager().install(), desired_capabilities = options))

#WAY 3:
driver = Chrome(service=Service(ChromeDriverManager().install(), chrome_options = options))

#WAY 4: Firefox browser will work
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True

#WAY 5: Firefox browser will work
desired_capabilities = DesiredCapabilities.FIREFOX.copy()
desired_capabilities['acceptInsecureCerts'] = True

#WAY 4:
#driver = webdriver.Firefox(executable_path = GeckoDriverManager().install(), firefox_profile = profile)

#WAY 5:
driver = webdriver.Firefox(executable_path = GeckoDriverManager().install(), capabilities = desired_capabilities)

driver.implicitly_wait(10)

driver.get("https://expired.badsssl.com/")

print(driver.find_element((By.TAG_NAME, 'h1')).text)
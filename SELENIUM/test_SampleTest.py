import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import pytest_html

class firstSeleniumtest():
    options = webdriver.ChromeOptions()

    path = os.getcwd()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://google.com')
    driver.quit()
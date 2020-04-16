import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import pytest_html

class firstSeleniumtest():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='C:\\chromedriver_win32 (6)\\chromedriver.exe')
        self.driver.maximize_window()

    def test_openBrowser(self , setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        try:
            element = WDW(self.driver,10).until(EC.presence_of_element_located((By.ID,'txtUsername')))

        finally:
            print('webpage is loaded')
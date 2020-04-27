from selenium import webdriver as wd
from selenium.webdriver import DesiredCapabilities


# setup grid in local, refrence :

hubUrl = 'http://169.254.166.115:4444/wd/hub'
capability = DesiredCapabilities.CHROME.copy()
firefoxCaps = DesiredCapabilities.FIREFOX.copy()

ChromeRemoteOPtions = wd.ChromeOptions()
FFopts = wd.FirefoxOptions()
ffdriver = wd.Remote(command_executor=hubUrl,desired_capabilities=firefoxCaps,options=FFopts)
ffdriver.get("http://freecrm.com")
print(ffdriver.title)
ffdriver.quit()
# driver = wd.Remote(command_executor=hubUrl, desired_capabilities=capability, options=ChromeRemoteOPtions)
#
# driver.get("https://freecrm.com")
# print(driver.title)
# driver.quit()

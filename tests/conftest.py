import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

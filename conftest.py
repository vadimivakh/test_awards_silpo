import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

hostname = 'http://awards.silpo.iir.fozzy.lan/'


@pytest.yield_fixture(scope='function')
def chromedriver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    _driver.get(hostname)
    yield _driver
    _driver.quit()


@pytest.yield_fixture(scope='function')
def geckodriver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://awards.silpo.iir.fozzy.lan/')
    yield driver
    driver.quit()

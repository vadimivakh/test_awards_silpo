import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

hostname = 'https://google.com/'


@pytest.yield_fixture(scope='session')
def chromedriver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    _driver.get('http://awards.silpo.iir.fozzy.lan/')
    yield _driver
    _driver.quit()


@pytest.yield_fixture(scope='session')
def geckodriver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://awards.silpo.iir.fozzy.lan/')
    yield driver
    driver.quit()
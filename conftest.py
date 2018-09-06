import pytest
from selenium import webdriver


hostname = 'http://awards.silpo.iir.fozzy.lan/'


# @pytest.yield_fixture(scope='function')
# def web_driver():
#     _driver = webdriver.Chrome()
#     _driver.maximize_window()
#     _driver.get(hostname)
#     yield _driver
#     _driver.quit()
#
#
# @pytest.yield_fixture(scope='function')
# def geckodriver():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get('http://awards.silpo.iir.fozzy.lan/')
#     yield driver
#     driver.quit()
#
#
# def pytest_report_header(config):
#     return " -== Awards functioning testing =- "


""" allows lunch tests using params from cli """


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: opera, chrome, firefox")


@pytest.yield_fixture(scope="function", autouse=True)
def web_driver(request):
    driver = None
    browser_name = request.config.getoption("--browser")
    if browser_name == 'opera':
        driver = webdriver.Opera()
    elif browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    driver.get(hostname)
    yield driver
    driver.quit()

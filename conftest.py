import pytest
from selenium import webdriver

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


def pytest_report_header(config):
    return " -== Awards functioning testing =- "


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


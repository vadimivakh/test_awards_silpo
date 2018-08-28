from selenium.webdriver.support.wait import WebDriverWait


class BaseWebPage(object):
    wait = WebDriverWait(driver, 5)
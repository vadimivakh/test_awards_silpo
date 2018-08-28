from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def page_content(self, driver):
        return self.driver.page_source

    def test_login_button_is_active(self, chromedriver):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "button[tabindex='0']")))

        return

    def login_with(self, driver, card_number):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number)
        sleep(2)
        return self


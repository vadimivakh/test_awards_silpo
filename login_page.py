from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def top_menu_is_exists(self, driver):
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return True
        except TimeoutException:
            return False

    def page_content(self, driver):
        return self.driver.page_source

    def input_field_is_exists(self, driver):
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "// input")))
        except TimeoutException:
            return False
        return True

    def login_button_is_exists(self, driver):
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "// button")))
        except TimeoutException:
            return False
        return True

    def login_with_valid_card(self, driver, card_number):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number)
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]"))).click()
        return self

    def submit_button_is_active(self, driver):
        submit_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]")))
        return submit_button.is_enabled()

    def login_with_invalid_card(self, driver, card_number):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number)
        button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]")))
        return button.is_enabled()


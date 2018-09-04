from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from my_choise_page import MyChoisePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://awards.silpo.iir.fozzy.lan/login")

        # submit_button = WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "//span[contains(text(),'увійти')]")))

        self.xpath_locator_for_validation_message = "//div[@class='validation-message']"

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
        return MyChoisePage(driver)

    def submit_button_is_active(self, driver):
        # submit_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]")))
        return WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]"))).is_enabled

    def login_with_invalid_card(self, driver, card_number):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number)
        button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'увійти')]")))
        return button.is_enabled()

    def login_with_empty_field(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys('', Keys.TAB)
        return self

    def title_text_size(self, driver):
        try:
            title_text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p[class='title-text']")))
            return title_text.value_of_css_property('font-size')
        except TimeoutException:
            return False

    def title_text_margin_bottom(self, driver):
        try:
            title_text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p[class='title-text']")))
            return title_text.value_of_css_property('margin-bottom')
        except TimeoutException:
            return False

    def get_validation_message(self, driver):

        """Returns a text of a validation message if it is existed"""
        try:
            validation_text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_locator_for_validation_message)))
            return validation_text.text
        except TimeoutException:
            return False

    def login_with_not_full_card_number(self, driver, card_number):

        """Loginisation with not full card number. Card has less than 13 symbols"""
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number, Keys.TAB)
        return self

    def fill_the_card_number_field(self, driver, card_number):

        """Login with entered card number without clicking the 'увійти' button"""
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "number"))).send_keys(card_number, Keys.TAB)
        return self


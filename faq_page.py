from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from my_choise_page import MyChoisePage


class FaqPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://awards.silpo.iir.fozzy.lan/login")

        """"xpath locators for self.page objects"""
        self.xpath_locator_for_content_block = "// div[@class='faq-page-content']"


    def top_menu_is_exists(self, driver):
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return True
        except TimeoutException:
            return False

    def page_content(self, driver):
        return self.driver.page_source

    def content_block_is_enabled(self, driver):
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_locator_for_content_block)))
            return True
        except TimeoutException:
            return False

    def number_of_question(self, driver):

        """ Returns quantity of the questions on the page """
        sleep(2)
        question_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p[class$='title']")))
        # count = 0
        # for el in question_list:
        #     count += 1
        return len(question_list)

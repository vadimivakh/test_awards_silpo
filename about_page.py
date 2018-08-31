# -*- coding: utf-8 -*-

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from voting_page import VotingPage
from my_choise_page import MyChoisePage


class AboutProjectPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def top_menu_is_exists(self, driver):
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return True
        except TimeoutException:
            return False

    def title_text(self, driver):
        return driver.title

    def page_content(self, driver):
        return self.driver.page_source

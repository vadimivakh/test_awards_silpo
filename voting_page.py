# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VotingPage:

    def __init__(self, driver):
        self.driver = driver

    def page_content(self, driver):
        return self.driver.page_source

    def left_menu_is_enable(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[class='menu']"))).click()
        except TimeoutException:
            return False
        return True

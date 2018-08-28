# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from voting_page import VotingPage


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def click_voting_button(self, driver):
        button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//span[@class='jss64']")))
        button.click()
        return VotingPage(driver)

    def title_text(self, driver):
        return driver.title

    def click_to_voting_topmenu_item(self):
        pass

    def click_to_about_project_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='topMenu-item'][2]"))).click()
        return self

    def click_to_rules_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='topMenu-item'][3]"))).click()
        return self

    def click_to_fag_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='topMenu-item'][4]"))).click()
        return self

    def click_to_my_choice_topmenu_item(self):
        pass

    def click_to_login_section(self, driver):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='exit-icon-wrapper topMenu-item']"))).click()
        return LoginPage(driver)

    def page_content(self, driver):
        return self.driver.page_source

# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from voting_page import VotingPage
from my_choise_page import MyChoisePage

class MainPage:

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

    def click_voting_button(self, driver):
        vote_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'ГОЛОСУВАТИ')]")))
        vote_button.click()
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

    def click_to_my_choice_topmenu_item(self, driver):

        return MyChoisePage(driver)

    def click_to_login_section(self, driver):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='exit-icon-wrapper topMenu-item']"))).click()
        return LoginPage(driver)

    def page_content(self, driver):
        return self.driver.page_source

    def vote_button_is_displayed_on_the_page(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'ГОЛОСУВАТИ')]"))).is_displayed()

    def vote_button_is_enabled(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'ГОЛОСУВАТИ')]"))).is_enabled()

    def elephant_menu_is_displayed(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='jss36 jss38 jss37 tool-bar']"))).is_enabled()

    def elephant_img_is_enabled(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[class='elephant-image-background-slon-big']"))).is_displayed()

    def counter_is_enabled(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='countdown']"))).is_displayed()
# -*- coding: utf-8 -*-

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from voting_page import VotingPage
from my_choise_page import MyChoisePage
from about_page import AboutProjectPage


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

        """XPATH locators"""
        self.xpath_locator_vote_button = "//span[contains(text(),'ГОЛОСУВАТИ')]"
        self.xpath_locator_about_project_topmenu_item = "//div[@class='topMenu-item'][2]"
        self.xpath_locator_rules_topmenu_item = "//div[@class='topMenu-item'][3]"
        self.xpath_locator_faq_topmenu_item = "//div[@class='topMenu-item'][4]"
        self.xpath_locator_topmenu = "// div[@class ='topMenu']"
        self.xpath_locator_my_choise_topmenu_item = "//span[contains(text(),'Мій вибір')]"
        self.xpath_locator_login_button_topmenu_item = "a[class='exit-icon-wrapper topMenu-item']"

    def top_menu_is_exists(self, driver):

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return True
        except TimeoutException:
            return False

    def click_voting_button(self, driver):

        vote_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_vote_button)))
        vote_button.click()
        return VotingPage(driver)

    def title_text(self, driver):
        return driver.title

    def click_to_voting_topmenu_item(self):
        pass

    def click_to_about_project_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_about_project_topmenu_item))).click()
        return AboutProjectPage(driver)

    def click_to_rules_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_rules_topmenu_item))).click()
        return self

    def click_to_fag_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_faq_topmenu_item))).click()
        return self

    def click_to_my_choice_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_my_choise_topmenu_item))).click()
        return MyChoisePage(driver)

    def click_to_login_button(self, driver):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.xpath_locator_login_button_topmenu_item))).click()
        return LoginPage(driver)

    def page_content(self, driver):
        return self.driver.page_source

    def vote_button_is_displayed_on_the_page(self, driver):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_locator_vote_button))).is_displayed()

    def vote_button_is_enabled(self, driver):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_locator_vote_button))).is_enabled()

    def elephant_menu_is_displayed(self, driver):
        return self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='jss36 jss38 jss37 tool-bar']"))).is_enabled()

    def elephant_img_is_enabled(self, driver):
        return self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "img[class='elephant-image-background-slon-big']"))).is_displayed()

    def counter_is_enabled(self, driver):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='countdown']"))).is_displayed()

    def click_to_logo_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[class='topMenu-silpoElephant topMenu-item']"))).click()
        return self

    def vote_button_text_equals_to(self, driver, button_text):
        try:
            button = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'ГОЛОСУВАТИ')]")))
            return button.text == button_text
        except TimeoutException:
            return False

    def topmenu_height(self, driver):
        try:
            topmenu = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.xpath_locator_topmenu)))
            return topmenu.value_of_css_property('height')
        except TimeoutException:
            return False

    def topmenu_items_fontsize(self, driver):
        try:
            topmenu = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return topmenu.value_of_css_property('font-size')
        except TimeoutException:
            return False

    def topmenu_button_clicked_color(self, driver):
        try:
            topmenu = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Голосувати')]")))
            topmenu.click()
            return topmenu.value_of_css_property('color')
        except TimeoutException:
            return False

    def topmenu_font_family(self, driver):
        try:
            topmenu = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='topMenu']")))
            return topmenu.value_of_css_property('font-family')
        except TimeoutException:
            return False

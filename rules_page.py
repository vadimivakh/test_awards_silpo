# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from about_page import AboutProjectPage
from faq_page import FaqPage
from login_page import LoginPage
from my_choise_page import MyChoisePage


class RulesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        """ xpath selectors for page objects """
        self.xpath_locator_elephant_image = "// img[@class='elephant-image-background-slon-big']"
        self.xpath_locator_block_content = "// div[@class='rules-page-content']"
        self.xpath_selector_rules_page_content = "// div[@class='rules-page-content']"
        self.xpath_selector_title_of_page_content = "// h2[@class='block-title']"
        self.xpath_locator_about_project_topmenu_item = "//div[@class='topMenu-item'][2]"
        self.xpath_locator_rules_topmenu_item = "//div[@class='topMenu-item'][3]"
        self.xpath_locator_faq_topmenu_item = "//div[@class='topMenu-item'][4]"
        self.xpath_locator_topmenu = "// div[@class ='topMenu']"
        self.xpath_locator_my_choise_topmenu_item = "//span[contains(text(),'Мій вибір')]"
        self.xpath_locator_login_button_topmenu_item = "a[class='exit-icon-wrapper topMenu-item']"

    def page_content(self, driver):
        return driver.page_source

    def top_menu_is_exists(self, driver):

        """ Return boolean value about top-menu existing """
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, self.xpath_locator_topmenu)))
            return True
        except TimeoutException:
            return False

    def title_text(self, driver):
        return driver.title

    def click_to_about_project_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_about_project_topmenu_item))).click()
        return AboutProjectPage(driver)

    def click_to_rules_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_rules_topmenu_item))).click()
        return self

    def click_to_faq_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_faq_topmenu_item))).click()
        return FaqPage(driver)

    def click_to_my_choice_topmenu_item(self, driver):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_my_choise_topmenu_item))).click()
        return MyChoisePage(driver)

    def click_to_login_button(self, driver):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.xpath_locator_login_button_topmenu_item))).click()
        return LoginPage(driver)

    def block_content_is_enabled(self, driver):

        """ Check if the block of content is enabled"""
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_locator_block_content)))
        return self.driver

    def title_font_size(self, driver):

        """ Returns int-type value of the title's fontsize """
        try:
            content_title = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_selector_title_of_page_content)))
            return content_title.value_of_css_property('font-size')
        except TimeoutException:
            return False

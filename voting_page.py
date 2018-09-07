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

    def category_by_index(self, driver, category_index):

        """" Activating transferred category on menu """
        xpath_locator_for_category = "//ul/a[{}]".format(category_index)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_locator_for_category))).click()
        except TimeoutException:
            return False
        return self

    def sub_category_by_index(self, driver, subcategory_index):

        """" Activating transferred subcategory on menu """
        xpath_locator_for_subcategory = "//li[@class='sub-menu-item'] [2]".format(subcategory_index)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_locator_for_subcategory))).click()
        except TimeoutException:
            return False
        return self

    def rest_of_the_product_are_disabled_after_voting(self, driver):

        """ Returns boolean value True if rest of the products on the page are disabled after voting """
        product_list = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "//*[@id='root']//li/div")))

        for product in product_list:
            if product.get_attribute('class') != 'item-container unActive':     #css_selector *[class$='vote-button']
                return False
        return True

    def vote_for_product_with_index(self, driver, product_index):

        """ Returns product name that was voted """
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//*[@id='root']//li/div")))


    def voted_product_falls_into_mychoise(self, driver, voted_product):


        """Check if the voted product falls into 'My choise' page after voting"""


    def get_current_url(self, driver):

        """Returns current ulr as str value"""
        return driver.current_url
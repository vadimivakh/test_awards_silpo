# -*- coding: utf-8 -*-

import pytest
from time import sleep
from mainpage import MainPage


# def test_awards_main_title(chromedriver):
#     homepage = MainPage(chromedriver)
#     awards_title = homepage.title_text(chromedriver)
#     assert awards_title == "Голосуйте за улюбленні товари"
#
#
# def test_awards_title(chromedriver):
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_section(chromedriver)
#     assert 'Вхід до голосування' in loginpage.page_content(chromedriver)
#
#
# def test_awards_title_two(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_login_section(chromedriver)
#     assert "Голосуйте" in homepage.title_text(chromedriver)
#
#
# def test_click_to_faq(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_fag_topmenu_item(chromedriver)
#     assert 'Питання та відповіді' in homepage.page_content(chromedriver)
#
#
# def test_click_to_rules(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_rules_topmenu_item(chromedriver)
#     assert 'ПРАВИЛА ПРОВЕДЕННЯ' in homepage.page_content(chromedriver)


# def test_click_to_voting_button(chromedriver):
#     homepage = MainPage(chromedriver)
#     vote_page = homepage.click_voting_button(chromedriver)
#     assert vote_page.left_menu_is_not_present(chromedriver) is not False


def test_valid_login(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    login_page.login_with(chromedriver, card_number='0291077164447')
    assert 'МІЙ ВИБІР' in login_page.page_content(chromedriver)





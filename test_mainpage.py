# -*- coding: utf-8 -*-

import pytest
from time import sleep
from mainpage import MainPage

"""
                                                MAINPAGE AWARDS
"""

# # tc_1
# def test_awards_main_title(chromedriver):
#     homepage = MainPage(chromedriver)
#     awards_title = homepage.title_text(chromedriver)
#     assert awards_title == "Голосуйте за улюбленні товари"
#
#
# # tc_2
# def test_mainpage_topmenu_is_exists(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.top_menu_is_exists(chromedriver)
#
#
# # tc_3
# def test_button_is_displayed_on_main_page(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.vote_button_is_displayed_on_the_page(chromedriver)
#
#
# # tc_4
# def test_click_on_login_button_from_mainpage(chromedriver):
#     homepage = MainPage(chromedriver)
#     login_page = homepage.click_to_login_button(chromedriver)
#     assert "Вхід до голосування" in login_page.page_content(chromedriver)
#
#
# # tc_5
# def test_click_on_my_choise_from_mainpage_unlogined(chromedriver):
#     homepage = MainPage(chromedriver)
#     my_choise_page = homepage.click_to_my_choice_topmenu_item()
#     assert 'Вхід до голосування' in my_choise_page.content(chromedriver)
#
#
# # tc_6
# def test_click_on_mychoise_button_from_mainpage_logined(chromedriver):
#     homepage = MainPage(chromedriver)
#     login_page = homepage.click_to_login_button(chromedriver)
#     my_choise_page = login_page.login_with_valid_card(chromedriver, card_number='0291077164447')
#     assert "Мій вибір" in my_choise_page.page_content(chromedriver)
#
#
# # tc_7
# def test_click_to_faq_from_mainpage(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_fag_topmenu_item(chromedriver)
#     assert 'Питання та відповіді' in homepage.page_content(chromedriver)
#
#
# # tc_8
# def test_click_to_rules_from_mainpage(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_rules_topmenu_item(chromedriver)
#     assert 'ПРАВИЛА ПРОВЕДЕННЯ' in homepage.page_content(chromedriver)
#
#
# # tc_9 network
# def test_click_to_about_button_from_topmenu(chromedriver):
#     homepage = MainPage(chromedriver)
#     about_page = homepage.click_to_about_project_topmenu_item(chromedriver)
#     assert 'ЛЕГЕНДА' in about_page.page_content(chromedriver)
#
#
# # tc_10
# @pytest.mark.acceptance
# def test_awards_title_two(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_login_section(chromedriver)
#     assert "Голосуйте" in homepage.title_text(chromedriver)
#
# # tc_11
# def test_click_to_logo_topmenu_item(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_my_choice_topmenu_item(chromedriver)
#     homepage.click_to_logo_topmenu_item(chromedriver)
#     assert homepage.vote_button_is_enabled(chromedriver)
#
#
# # tc_12
# def test_click_to_voting_button(chromedriver):
#     homepage = MainPage(chromedriver)
#     vote_page = homepage.click_voting_button(chromedriver)
#     assert vote_page.left_menu_is_enable(chromedriver) is True
#
#
# # without_id
# def test_elephant_img_is_displayed(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.elephant_img_is_enabled(driver=chromedriver)
#
#
# # without_id
# def test_timer_is_displayed(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.counter_is_enabled(driver=chromedriver)
#
#
# # without_id
# def test_url_match_mainpage(chromedriver):
#     must_be_url = 'http://awards.silpo.iir.fozzy.lan/'
#     homepage = MainPage(chromedriver)
#     current_url = homepage.current_url
#     assert must_be_url == current_url
#
#
# # without_id
# def test_matching_button_value(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.vote_button_value_equals_to(driver=chromedriver, button_text='ГОЛОСУВАТИ')
#
#
# # without_id
# def test_topmenu_height(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_height(chromedriver) == '70px'
#
#
# # without_id
# def test_topmenu_items_fontsize(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_items_fontsize(chromedriver) == '16px'
#
# # without_id
# def test_topmenu_background_color(chromedriver):
#     pass
#
#
# # without_id
# def test_topmenu_button_clicked_color(chromedriver):
#     homepage = MainPage(chromedriver)
#     homepage.click_to_voting_topmenu_item()
#     assert homepage.topmenu_button_clicked_color(chromedriver) == 'rgba(238, 117, 1, 1)'


# # without_id
# def test_topmenu_font_family(chromedriver):
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_font_family(chromedriver) == 'sans-serif'


"""
                                               LOGINPAGE AWARDS
"""

# without_id
def test_title_text_size(chromedriver):
    homepage = MainPage(chromedriver)
    loginpage = homepage.click_to_login_button(chromedriver)
    assert loginpage.title_text_size() ==


# осталось посмотреть tc_9  и зафейленные 4 теста

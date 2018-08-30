# -*- coding: utf-8 -*-

import pytest
from time import sleep
from mainpage import MainPage

# tc_1
def test_awards_main_title(chromedriver):
    homepage = MainPage(chromedriver)
    awards_title = homepage.title_text(chromedriver)
    assert awards_title == "Голосуйте за улюбленні товари"








# tc_2
def test_awards_title(chromedriver):
    homepage = MainPage(chromedriver)
    loginpage = homepage.click_to_login_section(chromedriver)
    assert 'Вхід до голосування' in loginpage.page_content(chromedriver)


# tc_3
@pytest.mark.acceptance
def test_awards_title_two(chromedriver):
    homepage = MainPage(chromedriver)
    homepage.click_to_login_section(chromedriver)
    assert "Голосуйте" in homepage.title_text(chromedriver)


# tc_4
def test_click_to_faq(chromedriver):
    homepage = MainPage(chromedriver)
    homepage.click_to_fag_topmenu_item(chromedriver)
    assert 'Питання та відповіді' in homepage.page_content(chromedriver)


def test_click_to_rules(chromedriver):
    homepage = MainPage(chromedriver)
    homepage.click_to_rules_topmenu_item(chromedriver)
    assert 'ПРАВИЛА ПРОВЕДЕННЯ' in homepage.page_content(chromedriver)


def test_click_to_voting_button(chromedriver):
    homepage = MainPage(chromedriver)
    vote_page = homepage.click_voting_button(chromedriver)
    assert vote_page.left_menu_is_not_present(chromedriver) is not False


def test_valid_login(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    login_page.login_with_valid_card(chromedriver, card_number='0291077164447')
    sleep(2)
    assert 'МІЙ ВИБІР' in login_page.page_content(chromedriver)


def test_login_button_exists(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    assert login_page.login_button_is_exists(chromedriver)


def test_input_field_is_exists(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    assert login_page.input_field_is_exists(chromedriver)


def test_mainpage_topmenu_is_exists(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.top_menu_is_exists(chromedriver)


def test_loginpage_topmenu_is_exists(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    assert login_page.top_menu_is_exists(chromedriver)


def test_login_with_valid_card_number(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver).login_with_valid_card(chromedriver, card_number='0291077164447')
    assert login_page.submit_button_is_active(chromedriver) is True


def test_login_with_invalid_card_number(chromedriver):
    homepage = MainPage(chromedriver)
    login_page = homepage.click_to_login_section(chromedriver)
    login_status = login_page.login_with_invalid_card(chromedriver, card_number='1234567891234')
    print('login_status = ', login_status)
    assert login_status is not True


def test_button_is_displayed_on_pyrtthe_main_page(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.vote_button_is_displayed_on_the_page(chromedriver)


def test_button_is_displayed_on_main_page(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.vote_button_is_enabled(chromedriver)


def test_elephant_topmenu_is_diplayed(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.elephant_menu_is_displayed(driver=chromedriver)


def test_elephant_img_is_displayed(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.elephant_img_is_enabled(driver=chromedriver)


def test_timer_is_displayed(chromedriver):
    homepage = MainPage(chromedriver)
    assert homepage.counter_is_enabled(driver=chromedriver)


def test_click_on_my_choise_from_mainpage_unllined(chromedriver):
    homepage = MainPage(chromedriver)
    my_choise_page = homepage.click_to_my_choice_topmenu_item()
    assert 'Вхід до голосування' in my_choise_page.content(chromedriver)



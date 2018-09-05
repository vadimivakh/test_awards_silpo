# -*- coding: utf-8 -*-

import pytest
from time import sleep
from mainpage import MainPage
from faq_page import FaqPage
from rules_page import RulesPage

# """
#                                                 MAINPAGE AWARDS
# """
#
# @pytest.mark.done
# def test_awards_main_title(chromedriver):
#
#     """Check title of mainpage"""
#     homepage = MainPage(chromedriver)
#     awards_title = homepage.title_text(chromedriver)
#     assert awards_title == "Голосуйте за улюбленні товари"
#
#
# @pytest.mark.done
# def test_mainpage_topmenu_is_exists(chromedriver):
#
#     """Check if topmenu on mainpage is exists"""
#     homepage = MainPage(chromedriver)
#     assert homepage.top_menu_is_exists(chromedriver)
#
#
# @pytest.mark.done
# def test_button_is_displayed_on_main_page(chromedriver):
#
#     """Check if 'ГОЛОСУВАТИ' button is displayed in mainpage"""
#     homepage = MainPage(chromedriver)
#     assert homepage.vote_button_is_displayed_on_the_page(chromedriver)
#
#
# @pytest.mark.done
# def test_click_on_login_button_from_mainpage(chromedriver):
#
#     """Check action of the button 'Увійти'"""
#     homepage = MainPage(chromedriver)
#     login_page = homepage.click_to_login_button(chromedriver)
#     assert "Вхід до голосування" in login_page.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_click_on_my_choise_from_mainpage_unlogined(chromedriver):
#
#     """Check if the action of 'МІЙ ВИБІР' button is correct - unlogined user"""
#     homepage = MainPage(chromedriver)
#     my_choise_page = homepage.click_to_my_choice_topmenu_item()
#     assert 'Вхід до голосування' in my_choise_page.content(chromedriver)
#
#
# @pytest.mark.done
# def test_click_on_mychoise_button_from_mainpage_logined(chromedriver):
#
#     """Check if the action of 'МІЙ ВИБІР' button is correct - logined user"""
#     homepage = MainPage(chromedriver)
#     login_page = homepage.click_to_login_button(chromedriver)
#     my_choise_page = login_page.login_with_valid_card(chromedriver, card_number='0291077164447')
#     assert "Мій вибір" in my_choise_page.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_click_to_faq_from_mainpage(chromedriver):
#
#     """Check if the action of 'ПИТАННЯ ТА ВІДПОВІДІ' button on Top-Menu is correct"""
#     homepage = MainPage(chromedriver)
#     homepage.click_to_faq_topmenu_item(chromedriver)
#     assert 'Питання та відповіді' in homepage.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_click_to_rules_from_mainpage(chromedriver):
#
#     """Check if the action of 'ЯКОГО СЛОНА ОБРАТИ?' on Top-Menu button is correct"""
#     homepage = MainPage(chromedriver)
#     homepage.click_to_rules_topmenu_item(chromedriver)
#     assert 'ПРАВИЛА ПРОВЕДЕННЯ' in homepage.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_click_to_about_button_from_topmenu(chromedriver):
#
#     """Check if the action of 'ПРОЕКТ «СЛОН' on Top-Menu button is correct"""
#     homepage = MainPage(chromedriver)
#     about_page = homepage.click_to_about_project_topmenu_item(chromedriver)
#     assert 'ЛЕГЕНДА' in about_page.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_awards_title_two(chromedriver):
#
#     """Check if the title of 'Вхід до голосування' page is correct"""
#     homepage = MainPage(chromedriver)
#     homepage.click_to_login_button(chromedriver)
#     assert "Голосуйте" in homepage.title_text(chromedriver)
#
# @pytest.mark.done
# def test_click_to_logo_topmenu_item(chromedriver):
#
#     """Check if the action of the 'Elefant' logo is correct"""
#     homepage = MainPage(chromedriver)
#     homepage.click_to_my_choice_topmenu_item(chromedriver)
#     homepage.click_to_logo_topmenu_item(chromedriver)
#     assert homepage.vote_button_is_enabled(chromedriver)
#
#
# @pytest.mark.done
# def test_click_to_voting_button(chromedriver):
#
#     """Check if the action of the 'Голосувати' button on the mainpage is correct"""
#     homepage = MainPage(chromedriver)
#     vote_page = homepage.click_voting_button(chromedriver)
#     assert vote_page.left_menu_is_enable(chromedriver) is True
#
#
# @pytest.mark.done
# def test_elephant_img_is_displayed(chromedriver):
#
#     """Check if the elephant image is displayed on the mainpage"""
#     homepage = MainPage(chromedriver)
#     assert homepage.elephant_img_is_enabled(driver=chromedriver)
#
#
# @pytest.mark.done
# def test_timer_is_displayed(chromedriver):
#
#     """Check if the timer is enabled on the mainpage"""
#     homepage = MainPage(chromedriver)
#     assert homepage.counter_is_enabled(driver=chromedriver)
#
#
# @pytest.mark.done
# def test_url_match_mainpage(chromedriver):
#
#     """Check if the url of the mainpage is equals to required url"""
#     must_be_url = 'http://awards.silpo.iir.fozzy.lan/'
#     homepage = MainPage(chromedriver)
#     current_url = homepage.current_url
#     assert must_be_url == current_url
#
#
# @pytest.mark.done
# def test_matching_button_value(chromedriver):
#
#     """Check if the text of the 'ГОЛОСУВАТИ' button is equals to 'ГОЛОСУВАТИ'"""
#     homepage = MainPage(chromedriver)
#     assert homepage.vote_button_text_equals_to(driver=chromedriver, button_text='ГОЛОСУВАТИ')
#
#
# @pytest.mark.done
# def test_topmenu_height(chromedriver):
#
#     """Check the height of the Top-Menu"""
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_height(chromedriver) == '70px'
#
#
# @pytest.mark.done
# def test_topmenu_items_fontsize(chromedriver):
#
#     """Check the size of the Top-Menu text"""
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_items_fontsize(chromedriver) == '16px'
#
# @pytest.mark.done
# def test_topmenu_background_color(chromedriver):
#
#     """Check the colour of the background"""
#     pass
#
#
# @pytest.mark.done
# def test_topmenu_button_clicked_color(chromedriver):
#
#     """Check the colour of the 'ГОЛОСУВАТИ' button when it is clicked"""
#     homepage = MainPage(chromedriver)
#     homepage.click_to_voting_topmenu_item()
#     assert homepage.topmenu_button_clicked_color(chromedriver) == 'rgba(238, 117, 1, 1)'
#
#
# @pytest.mark.done
# def test_topmenu_font_family(chromedriver):
#
#     """Check the family of the fonts on the mainpage"""
#     homepage = MainPage(chromedriver)
#     assert homepage.topmenu_font_family(chromedriver) == 'sans-serif'
#
#
# """
#                                                LOGINPAGE AWARDS
# """
#
#
# @pytest.mark.done
# def test_title_text_size(chromedriver):
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     assert loginpage.title_text_size(chromedriver) == '32px'
#
#
# @pytest.mark.done
# def test_title_text_margin_bottom(chromedriver):
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     title_text_margin_bottom = loginpage.title_text_margin_bottom(driver=chromedriver)
#     assert title_text_margin_bottom == '40px'
#
#
# @pytest.mark.done
# def test_login_button_font_size(chromedriver):
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     status = loginpage
#
#
# @pytest.mark.done
# def test_login_with_correct_card_number(chromedriver):
#
#     """Check if the loginisation has correct functioning with valid card numder (029 0226351066). Cardnumber contains one space"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     my_choise_page = loginpage.login_with_valid_card(driver=chromedriver, card_number='029 0226351066')
#     search_word = 'Мій вибір'
#     assert search_word in my_choise_page.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_validation_message_caused_by_sending_empty_field(chromedriver):
#
#     """Check if the validation message 'Поле обов'зкове для заповнення' has correct function with empty input field"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.login_with_empty_field(chromedriver)
#     validation_message_text = loginpage.validation_message(chromedriver)
#     assert validation_message_text == 'Поле обов\'зкове для заповнення'
#
#
# @pytest.mark.done
# def test_validation_message_caused_by_sending_short_card_numder_12_symbols(chromedriver):
#
#     """Check if the validation message 'Номер має містити 13 цифр' has correct function with notfull card numder - 029107716444"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.login_with_not_full_card_number(driver=chromedriver, card_number='029107716444')
#     validation_text_message = loginpage.validation_message(chromedriver)
#     assert validation_text_message == 'Номер має містити 13 цифр'
#
#
# @pytest.mark.done
# def test_validation_message_caused_by_sending_short_card_number_5_symbols(chromedriver):
#
#     """Check if the validation message 'Номер має містити 13 цифр' has correct function with notfull card numder - 02910"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.login_with_not_full_card_number(driver=chromedriver, card_number='02910')
#     validation_text_message = loginpage.validation_message(chromedriver)
#     assert validation_text_message == 'Номер має містити 13 цифр'
#
#
# @pytest.mark.done
# def test_validation_message_caused_by_invalid_card_number_1_symbol(chromedriver):
#
#     """Check if the validation message 'Номер має містити 13 цифр' has correct function with invalid card numder - 0"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.login_with_not_full_card_number(driver=chromedriver, card_number='0')
#     validation_text_message = loginpage.get_validation_message(chromedriver)
#     assert validation_text_message.lower() == 'номер має містити 13 цифр'
#
#
# @pytest.mark.done
# def test_validation_message_caused_by_invalid_card_number(chromedriver):
#
#     """Check if the validation message 'Невірний номер карти' has correct function with invalid card numder - 1111111111111"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.login_with_not_full_card_number(driver=chromedriver, card_number='1111111111111')
#     validation_text_message = loginpage.validation_message(chromedriver)
#     assert validation_text_message == 'Невірний номер карти'
#
#
# @pytest.mark.done
# def test_error_message_does_not_exists_with_valid_card_number(chromedriver):
#
#     """Check if the validation message does not exists after entering the valid card number - 0291077164447"""
#     homepage = MainPage(chromedriver)
#     loginpage = homepage.click_to_login_button(chromedriver)
#     loginpage.fill_the_card_number_field(driver=chromedriver, card_number='0291077164447')
#     error_message = loginpage.get_validation_message(chromedriver)
#     assert len(error_message) == 0
#
#
# """
#                                                FAQ PAGE AWARDS
# """
#
# @pytest.mark.done
# def test_title_of_the_faq_page(chromedriver):
#
#     """ Checking the title of the page 'Питання та відповіді' """
#     homepage = MainPage(chromedriver)
#     faq_page = homepage.click_to_faq_topmenu_item(chromedriver)
#     assert 'Питання та відповіді' in faq_page.page_content(chromedriver)
#
#
# @pytest.mark.done
# def test_content_contains_10_questions(chromedriver):
#
#     """ Check if the content block is enabled on the FAQ page """
#     homepage = MainPage(chromedriver)
#     faq_page = homepage.click_to_faq_topmenu_item(chromedriver)
#     assert faq_page.number_of_question(chromedriver) == 10
#
#
# """
#                                                RULES PAGE AWARDS
# """
#
# @pytest.mark.done
# def test_title_of_the_current_page(chromedriver):
#
#     """ Check if the title is appropriate """
#     homepage = MainPage(chromedriver)
#     rules_pages = homepage.click_to_rules_topmenu_item(chromedriver)
#     assert rules_pages.title_text(chromedriver) == "Голосуйте за улюбленні товари"
#
# @pytest.mark.done
# def test_existing_elephant_image(chromedriver):
#
#     """ Check if the elephant image is enable on the page """
#     homepage = MainPage(chromedriver)
#     rules_pages = homepage.click_to_rules_topmenu_item(chromedriver)
#     assert rules_pages.elephant_img_is_enabled(chromedriver)
#
# @pytest.mark.done
# def test_block_content_is_enabled(chromedriver):
#
#     """ Check if the text content is enabled on the page"""
#     homepage = MainPage(chromedriver)
#     rules_pages = homepage.click_to_rules_topmenu_item(chromedriver)
#     assert rules_pages.block_content_is_enabled(chromedriver)
#
# @pytest.mark.done
# def test_title_font_size(chromedriver):
#
#     """ Check if font size of the title of the content is 32px """
#     homepage = MainPage(chromedriver)
#     rules_pages = homepage.click_to_rules_topmenu_item(chromedriver)
#     assert rules_pages.title_font_size(chromedriver) == '32px'
#
# @pytest.mark.done
# def test_title_font_family(chromedriver):
#
#     """ Check if the font family of the block content is 'sans-serif' """
#     homepage = MainPage(chromedriver)
#     rules_pages = homepage.click_to_rules_topmenu_item(chromedriver)
#     assert rules_pages.title_font_family(chromedriver) == 'sans-serif'
#
#
@pytest.mark.opt
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("type_1, default")
    elif cmdopt == "type2":
        print("second")
    assert 0


# def test_probe(cmdopt):
#     homepage = MainPage(cmdopt)
#     assert 0

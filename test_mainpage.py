# -*- coding: utf-8 -*-

import pytest
from time import sleep
from mainpage import MainPage
from faq_page import FaqPage
from rules_page import RulesPage

"""
                                                MAINPAGE AWARDS
"""

@pytest.mark.done
def test_awards_main_title(web_driver):

    """Check title of mainpage"""
    homepage = MainPage(web_driver)
    awards_title = homepage.title_text(web_driver)
    assert awards_title == "Голосуйте за улюбленні товари"


@pytest.mark.done
def test_mainpage_topmenu_is_exists(web_driver):

    """Check if topmenu on mainpage is exists"""
    homepage = MainPage(web_driver)
    assert homepage.top_menu_is_exists(web_driver)


@pytest.mark.done
def test_button_is_displayed_on_main_page(web_driver):

    """Check if 'ГОЛОСУВАТИ' button is displayed in mainpage"""
    homepage = MainPage(web_driver)
    assert homepage.vote_button_is_displayed_on_the_page(web_driver)


@pytest.mark.done
def test_click_on_login_button_from_mainpage(web_driver):

    """Check action of the button 'Увійти'"""
    homepage = MainPage(web_driver)
    login_page = homepage.click_to_login_button(web_driver)
    assert "Вхід до голосування" in login_page.page_content(web_driver)


@pytest.mark.done
def test_click_on_my_choise_from_mainpage_unlogined(web_driver):

    """Check if the action of 'МІЙ ВИБІР' button is correct - unlogined user"""
    homepage = MainPage(web_driver)
    my_choise_page = homepage.click_to_my_choice_topmenu_item()
    assert 'Вхід до голосування' in my_choise_page.content(web_driver)


@pytest.mark.done
def test_click_on_mychoise_button_from_mainpage_logined(web_driver):

    """Check if the action of 'МІЙ ВИБІР' button is correct - logined user"""
    homepage = MainPage(web_driver)
    login_page = homepage.click_to_login_button(web_driver)
    my_choise_page = login_page.login_with_valid_card(web_driver, card_number='0291077164447')
    assert "Мій вибір" in my_choise_page.page_content(web_driver)


@pytest.mark.done
def test_click_to_faq_from_mainpage(web_driver):

    """Check if the action of 'ПИТАННЯ ТА ВІДПОВІДІ' button on Top-Menu is correct"""
    homepage = MainPage(web_driver)
    homepage.click_to_faq_topmenu_item(web_driver)
    assert 'Питання та відповіді' in homepage.page_content(web_driver)


@pytest.mark.done
def test_click_to_rules_from_mainpage(web_driver):

    """Check if the action of 'ЯКОГО СЛОНА ОБРАТИ?' on Top-Menu button is correct"""
    homepage = MainPage(web_driver)
    homepage.click_to_rules_topmenu_item(web_driver)
    assert 'ПРАВИЛА ПРОВЕДЕННЯ' in homepage.page_content(web_driver)


@pytest.mark.done
def test_click_to_about_button_from_topmenu(web_driver):

    """Check if the action of 'ПРОЕКТ «СЛОН' on Top-Menu button is correct"""
    homepage = MainPage(web_driver)
    about_page = homepage.click_to_about_project_topmenu_item(web_driver)
    assert 'ЛЕГЕНДА' in about_page.page_content(web_driver)


@pytest.mark.done
def test_awards_title_two(web_driver):

    """Check if the title of 'Вхід до голосування' page is correct"""
    homepage = MainPage(web_driver)
    homepage.click_to_login_button(web_driver)
    assert "Голосуйте" in homepage.title_text(web_driver)

@pytest.mark.done
def test_click_to_logo_topmenu_item(web_driver):

    """Check if the action of the 'Elefant' logo is correct"""
    homepage = MainPage(web_driver)
    homepage.click_to_my_choice_topmenu_item(web_driver)
    homepage.click_to_logo_topmenu_item(web_driver)
    assert homepage.vote_button_is_enabled(web_driver)


@pytest.mark.done
def test_click_to_voting_button(web_driver):

    """Check if the action of the 'Голосувати' button on the mainpage is correct"""
    homepage = MainPage(web_driver)
    vote_page = homepage.click_voting_button(web_driver)
    assert vote_page.left_menu_is_enable(web_driver) is True


@pytest.mark.done
def test_elephant_img_is_displayed(web_driver):

    """Check if the elephant image is displayed on the mainpage"""
    homepage = MainPage(web_driver)
    assert homepage.elephant_img_is_enabled(driver=web_driver)


@pytest.mark.done
def test_timer_is_displayed(web_driver):

    """Check if the timer is enabled on the mainpage"""
    homepage = MainPage(web_driver)
    assert homepage.counter_is_enabled(driver=web_driver)


@pytest.mark.done
def test_url_match_mainpage(web_driver):

    """Check if the url of the mainpage is equals to required url"""
    must_be_url = 'http://awards.silpo.iir.fozzy.lan/'
    homepage = MainPage(web_driver)
    current_url = homepage.current_url
    assert must_be_url == current_url


@pytest.mark.done
def test_matching_button_value(web_driver):

    """Check if the text of the 'ГОЛОСУВАТИ' button is equals to 'ГОЛОСУВАТИ'"""
    homepage = MainPage(web_driver)
    assert homepage.vote_button_text_equals_to(driver=web_driver, button_text='ГОЛОСУВАТИ')


@pytest.mark.done
def test_topmenu_height(web_driver):

    """Check the height of the Top-Menu"""
    homepage = MainPage(web_driver)
    assert homepage.topmenu_height(web_driver) == '70px'


@pytest.mark.done
def test_topmenu_items_fontsize(web_driver):

    """Check the size of the Top-Menu text"""
    homepage = MainPage(web_driver)
    assert homepage.topmenu_items_fontsize(web_driver) == '16px'

@pytest.mark.done
def test_topmenu_background_color(web_driver):

    """Check the colour of the background"""
    pass


@pytest.mark.done
def test_topmenu_button_clicked_color(web_driver):

    """Check the colour of the 'ГОЛОСУВАТИ' button when it is clicked"""
    homepage = MainPage(web_driver)
    homepage.click_to_voting_topmenu_item()
    assert homepage.topmenu_button_clicked_color(web_driver) == 'rgba(238, 117, 1, 1)'


@pytest.mark.done
def test_topmenu_font_family(web_driver):

    """Check the family of the fonts on the mainpage"""
    homepage = MainPage(web_driver)
    assert homepage.topmenu_font_family(web_driver) == 'sans-serif'


"""
                                               LOGINPAGE AWARDS
"""


@pytest.mark.done
def test_title_text_size(web_driver):
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    assert loginpage.title_text_size(web_driver) == '32px'


@pytest.mark.done
def test_title_text_margin_bottom(web_driver):
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    title_text_margin_bottom = loginpage.title_text_margin_bottom(driver=web_driver)
    assert title_text_margin_bottom == '40px'


@pytest.mark.done
def test_login_button_font_size(web_driver):
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    status = loginpage


@pytest.mark.done
def test_login_with_correct_card_number(web_driver):

    """Check if the loginisation has correct functioning with valid card numder (029 0226351066). Cardnumber contains one space"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    my_choise_page = loginpage.login_with_valid_card(driver=web_driver, card_number='029 0226351066')
    search_word = 'Мій вибір'
    assert search_word in my_choise_page.page_content(web_driver)


@pytest.mark.done
def test_validation_message_caused_by_sending_empty_field(web_driver):

    """Check if the validation message 'Поле обов'зкове для заповнення' has correct function with empty input field"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.login_with_empty_fieldweb_driver
    validation_message_text = loginpage.validation_message(web_driver)
    assert validation_message_text == 'Поле обов\'зкове для заповнення'


@pytest.mark.done
def test_validation_message_caused_by_sending_short_card_numder_12_symbols(web_driver):

    """Check if the validation message 'Номер має містити 13 цифр' has correct function with notfull card numder - 029107716444"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.login_with_not_full_card_number(driver=web_driver, card_number='029107716444')
    validation_text_message = loginpage.validation_message(web_driver)
    assert validation_text_message == 'Номер має містити 13 цифр'


@pytest.mark.done
def test_validation_message_caused_by_sending_short_card_number_5_symbols(web_driver):

    """Check if the validation message 'Номер має містити 13 цифр' has correct function with notfull card numder - 02910"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.login_with_not_full_card_number(driver=web_driver, card_number='02910')
    validation_text_message = loginpage.validation_message(web_driver)
    assert validation_text_message == 'Номер має містити 13 цифр'


@pytest.mark.done
def test_validation_message_caused_by_invalid_card_number_1_symbol(web_driver):

    """Check if the validation message 'Номер має містити 13 цифр' has correct function with invalid card numder - 0"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.login_with_not_full_card_number(driver=web_driver, card_number='0')
    validation_text_message = loginpage.get_validation_message(web_driver)
    assert validation_text_message.lower() == 'номер має містити 13 цифр'


@pytest.mark.done
def test_validation_message_caused_by_invalid_card_number(web_driver):

    """Check if the validation message 'Невірний номер карти' has correct function with invalid card numder - 1111111111111"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.login_with_not_full_card_number(driver=web_driver, card_number='1111111111111')
    validation_text_message = loginpage.validation_message(web_driver)
    assert validation_text_message == 'Невірний номер карти'


@pytest.mark.done
def test_error_message_does_not_exists_with_valid_card_number(web_driver):

    """Check if the validation message does not exists after entering the valid card number - 0291077164447"""
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    loginpage.fill_the_card_number_field(driver=web_driver, card_number='0291077164447')
    error_message = loginpage.get_validation_message(web_driver)
    assert len(error_message) == 0


def test_is_button_disabled(web_driver):
    homepage = MainPage(web_driver)
    loginpage = homepage.click_to_login_button(web_driver)
    assert loginpage.submit_button_is_active(web_driver), 'submit button is not active'



"""
                                               FAQ PAGE AWARDS
"""

@pytest.mark.done
def test_title_of_the_faq_page(web_driver):

    """ Checking the title of the page 'Питання та відповіді' """
    homepage = MainPage(web_driver)
    faq_page = homepage.click_to_faq_topmenu_item(web_driver)
    assert 'Питання та відповіді' in faq_page.page_content(web_driver)


@pytest.mark.done
def test_content_contains_10_questions(web_driver):

    """ Check if the content block is enabled on the FAQ page """
    homepage = MainPage(web_driver)
    faq_page = homepage.click_to_faq_topmenu_item(web_driver)
    assert faq_page.number_of_question(web_driver) == 10


"""
                                               RULES PAGE AWARDS
"""

@pytest.mark.done
def test_title_of_the_current_page(web_driver):

    """ Check if the title is appropriate """
    homepage = MainPage(web_driver)
    rules_pages = homepage.click_to_rules_topmenu_item(web_driver)
    assert rules_pages.title_text(web_driver) == "Голосуйте за улюбленні товари"

@pytest.mark.done
def test_existing_elephant_image(web_driver):

    """ Check if the elephant image is enable on the page """
    homepage = MainPage(web_driver)
    rules_pages = homepage.click_to_rules_topmenu_item(web_driver)
    assert rules_pages.elephant_img_is_enabled(web_driver)

@pytest.mark.done
def test_block_content_is_enabled(web_driver):

    """ Check if the text content is enabled on the page"""
    homepage = MainPage(web_driver)
    rules_pages = homepage.click_to_rules_topmenu_item(web_driver)
    assert rules_pages.block_content_is_enabled(web_driver)

@pytest.mark.done
def test_title_font_size(web_driver):

    """ Check if font size of the title of the content is 32px """
    homepage = MainPage(web_driver)
    rules_pages = homepage.click_to_rules_topmenu_item(web_driver)
    assert rules_pages.title_font_size(web_driver) == '32px'


@pytest.mark.done
def test_title_font_family(web_driver):

    """ Check if the font family of the block content is 'sans-serif' """
    homepage = MainPage(web_driver)
    rules_pages = homepage.click_to_rules_topmenu_item(web_driver)
    assert rules_pages.title_font_family(web_driver) == 'Segoe, Frutiger, "Frutiger Linotype", "Dejavu Sans", "Helvetica Neue", Arial, sans-serif'


"""
                                               RULES PAGE AWARDS
"""


@pytest.mark.in_progress
def test_voting_if_user_is_unlogined(web_driver):

    """ Checks if the voting by unlogined user is impossible """
    homepage = MainPage(web_driver)
    vote_page = homepage.click_voting_button(web_driver)
    login_page =  vote_page.choose_category('').with_subcategory('').first_product(web_driver).click()
    assert "Вхід до голосування" in login_page(web_driver)


@pytest.mark.in_progress
def test_voting_if_user_is_logined(web_driver):

    """ Checks if the voting by logined user is possible """
    pass

#
# """
#                                                VOTING PAGE AWARDS
# """
#
#
# @pytest.mark.in_progress
# def test_checking_disabled_status_of_the_voted_products(web_driver):
#
#     """ Check if the rest of voted products have appropriate disabled status """
#     vote_page.category_by_index(category_index=1).sub_category_by_index('1').get_product_by_index(subcategory_index=1).vote(web_driver)
#     assert vote_page.rest_of_the_product_are_disabled(web_driver)
#
#
# @pytest.mark.done
# def test_click_to_vote_button(web_driver):
#
#     """ Checks if the transition to the voting page is correct """
#     homepage = MainPage(web_driver)
#     voting_page = homepage.click_voting_button(web_driver)
#     assert voting_page.get_current_url(web_driver) == 'http://awards.silpo.iir.fozzy.lan/vote'
#
#
# @pytest.mark.parametrize(subcategory_index, [2, 3])
# def test_voting(web_driver, ):
#
#     """ Checks if voted product falls into the 'My choise' page """
#     homepage = MainPage(web_driver)
#     voting_page = homepage.click_voting_button(web_driver)
#     voted_product =  voting_page.category_by_index(category_index).sub_category_by_index(subcategory_index).get_product_by_index(
#         subcategory_index=1).vote(web_driver)
#     assert voting_page.voted_product_falls_into_mychoise(voted_product)





# проверка незалогинившись голосовать
#
# проверка залогинивщись голосовать
#
# проверка моего выбора


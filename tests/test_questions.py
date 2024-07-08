import pytest

from selenium import webdriver
from pages.main_page import MainPageQaScooter as MpQaS
from locators.main_page_locators import MainPageQaScooterLocators as MpLoc
from test_data import TestData as Td


# class TestQuestionsQaScooter:
#     @pytest.mark.parametrize(
#         "question, answer_locator, answer_text", Td.questions
#     )
#     def test_click_on_question(self, driver, question, answer_locator, answer_text):
#         main_page = MpQaS(driver)
#         main_page.get_main_page()
#         main_page.click_on_question(question, answer_locator)
#         assert driver.find_element(*answer_locator).text == answer_text

class TestQuestionsQaScooter:
    @pytest.mark.parametrize(
        "question, answer_locator, answer_text", Td.questions
    )
    def test_click_on_question(self, driver, question, answer_locator, answer_text):
        main_page = MpQaS(driver)
        main_page.get_main_page()
        main_page.click_on_question(question, answer_locator)
        assert driver.find_element(*answer_locator).text == answer_text



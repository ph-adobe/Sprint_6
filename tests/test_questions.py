import allure
import pytest

from pages.main_page import MainPageQaScooter as MpQaS
from test_data import TestData as Td


class TestQuestionsQaScooter:

    @pytest.mark.parametrize(
        "question, answer_locator, answer_text",
        Td.questions
    )
    @allure.title("Test questions on the main page")
    def test_click_on_question(self, driver, question, answer_locator, answer_text):
        main_page = MpQaS(driver)
        main_page.get_main_page()
        main_page.click_on_question(question, answer_locator)
        assert main_page.check_text_of_answer(answer_locator, answer_text)

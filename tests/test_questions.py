import pytest

from pages.main_page import MainPageQaScooter as MpQaS
from test_data import TestData as Td


class TestQuestionsQaScooter:
    @pytest.mark.parametrize(
        "question, answer_locator, answer_text",
        [pytest.param(faq[0], faq[1], faq[2], id=f"Question {count}") for count, faq in
         enumerate(Td.questions, start=1)]
    )
    def test_click_on_question(self, driver, question, answer_locator, answer_text):
        main_page = MpQaS(driver)
        main_page.get_main_page()
        main_page.click_on_question(question, answer_locator)
        assert driver.find_element(*answer_locator).text == answer_text

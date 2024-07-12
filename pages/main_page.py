import allure
from locators.main_page_locators import MainPageQaScooterLocators as Mpl
from pages.base_page import BasePage
from test_data import TestData as Td


class MainPageQaScooter(BasePage):
    def wait_for_loading_main_page(self):
        self.wait_for_loading(Mpl.home_header)

    @allure.step("Open main page")
    def get_main_page(self):
        self.get_url(Td.MAIN_PAGE_URL)
        self.wait_for_loading(Mpl.home_header)
        self.confirm_cookie_usage()

    @allure.step("Click on question")
    def click_on_question(self, question, answer):
        self.click_on_element(question)
        self.wait_for_loading(answer)

    @allure.step("Check answer")
    def check_text_of_answer(self, answer_locator, answer_text):
        element = self.check_presence_of_element(answer_locator)
        return element.text == answer_text

    @allure.step("Click on order button")
    def click_on_order_button(self, button):
        if button == "button at the top of the page":
            self.click_on_element(Mpl.head_page_order_button)
        elif button == "button in the middle of the page":
            self.click_on_element(Mpl.bottom_page_order_button)




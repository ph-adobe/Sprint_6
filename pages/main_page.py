from locators.main_page_locators import MainPageQaScooterLocators as Mpl
from pages.base_page import BasePage
from test_data import TestData as Td


class MainPageQaScooter(BasePage):

    def get_main_page(self):
        self.driver.get(Td.MAIN_PAGE_URL)
        self.wait_for_loading(Mpl.home_header)
        self.confirm_cookie_usage()

    def click_on_question(self, question, answer):
        self.click_on_element(question)
        self.wait_for_loading(answer)

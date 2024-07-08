from locators.main_page_locators import MainPageQaScooterLocators as Mp
from pages.base_page import BasePage
from locators.main_page_locators import MainPageQaScooterLocators as Mpl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageQaScooter(BasePage):
    url = "https://qa-scooter.praktikum-services.ru/"

    def get_main_page(self):
        self.driver.get(self.url)
        self.wait_for_loading(Mpl.scooter_header)
        self.confirm_cookie_usage()

    def scroll_to_question(self, question):
        element = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question))

    def click_on_question(self, question, answer):
        self.scroll_to_question(question)
        self.driver.find_element(*question).click()
        self.wait_for_loading(answer)

    def click_on_head_order_button(self):
        self.driver.find_element(*Mp.head_page_order_button).click()

    def click_on_bottom_button(self):
        self.driver.find_element(*Mp.bottom_page_order_button).click()



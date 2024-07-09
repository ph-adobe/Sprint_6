from locators.main_page_locators import MainPageQaScooterLocators as Mpl
from locators.order_page_locators import OrderPageQaScooterLocators as Op
from pages.order_page import OrderPageQaScooter
from test_data import TestData as Td


class TestTransitions:
    def test_go_to_main_page(self, driver):
        order_page = OrderPageQaScooter(driver)
        order_page.get_order_page()
        order_page.click_on_element(Op.scooter_logo)
        order_page.wait_for_loading(Mpl.home_header)
        assert Td.MAIN_PAGE_URL in driver.current_url

    def test_go_to_dzen(self, driver):
        order_page = OrderPageQaScooter(driver)
        order_page.get_order_page()
        order_page.click_on_element(Op.yandex_logo)
        order_page.switch_to_next_window()
        assert Td.DZEN_LINK in driver.current_url

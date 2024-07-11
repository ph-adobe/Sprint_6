import allure
from pages.order_page import OrderPageQaScooter
from test_data import TestData as Td


class TestTransitions:
    @allure.title("Test switching to main page when click on scooter logo")
    def test_go_to_main_page(self, driver):
        order_page = OrderPageQaScooter(driver)
        order_page.get_order_page()
        order_page.click_on_scooter_logo()
        assert Td.MAIN_PAGE_URL in driver.current_url

    @allure.title("Test switching to dzen page when click on yandex logo")
    def test_go_to_dzen(self, driver):
        order_page = OrderPageQaScooter(driver)
        order_page.get_order_page()
        order_page.click_on_yandex_logo()
        assert Td.DZEN_LINK in driver.current_url

import pytest

from locators.order_page_locators import OrderPageQaScooterLocators as Op
from locators.about_rent_page_locators import AboutRentPageLocators as Arp

from pages.about_rent_page import AboutRentPage
from pages.main_page import MainPageQaScooter
from pages.order_page import OrderPageQaScooter

from test_data import TestData as Td


class TestOrderQaScooter:
    @pytest.mark.parametrize(
        "button_locator, name, surname, address, station, phone_number, rental_period, scooter_color",
        [
            pytest.param(*Td.data_set_to_make_order_1, id="Order button at the top of the page"),
            pytest.param(*Td.data_set_to_make_order_2, id="Order button in the middle of the page")
        ]
    )
    def test_make_order(self, driver, button_locator, name, surname, address, station, phone_number, rental_period,
                        scooter_color):
        order_page = OrderPageQaScooter(driver)
        main_page = MainPageQaScooter(driver)
        about_rent = AboutRentPage(driver)

        main_page.get_main_page()
        main_page.click_on_element(button_locator)
        order_page.wait_for_loading(Op.order_header)
        order_page.set_personal_data(name, surname, address, station, phone_number)
        order_page.wait_for_loading(Arp.about_rent_header)
        about_rent.sent_rent_data(rental_period, scooter_color)

        assert about_rent.check_presence_of_element(Arp.order_is_processed)

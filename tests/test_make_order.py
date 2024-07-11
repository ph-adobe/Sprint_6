import allure
import pytest

from pages.about_rent_page import AboutRentPage
from pages.main_page import MainPageQaScooter
from pages.order_page import OrderPageQaScooter

from test_data import TestData as Td


class TestOrderQaScooter:

    @pytest.mark.parametrize(
        "button, name, surname, address, station, phone_number, rental_period, scooter_color",
        [
           Td.data_set_to_make_order_1,
           Td.data_set_to_make_order_2,
        ]
    )
    def test_make_order(self, driver, button, name, surname, address, station, phone_number, rental_period,
                        scooter_color):
        allure.dynamic.title(f"Test making order [{button}]")
        order_page = OrderPageQaScooter(driver)
        main_page = MainPageQaScooter(driver)
        about_rent = AboutRentPage(driver)

        main_page.get_main_page()
        main_page.click_on_order_button(button)
        order_page.set_personal_data(name, surname, address, station, phone_number)
        about_rent.sent_rent_data(rental_period, scooter_color)

        assert about_rent.check_order_processed()

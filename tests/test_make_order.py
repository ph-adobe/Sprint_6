import pytest

from pages.order_page import OrderPageQaScooter
from pages.about_rent_page import AboutRentPage
from test_data import TestData as Td
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from locators.order_page_locators import OrderPageQaScooterLocators as OpLoc
from pages.main_page import MainPageQaScooter

from locators.main_page_locators import MainPageQaScooterLocators as MpLoc


class TestOrderQaScooter:
    @pytest.mark.parametrize(
        "name, surname, address, station, phone_number, rental_period, scooter_color",
        [
            Td.data_set_to_make_order_1,
            Td.data_set_to_make_order_2
        ]
    )
    def test_make_order(self, driver, name, surname, address, station, phone_number, rental_period, scooter_color):
        order_page = OrderPageQaScooter(driver)
        main_page = MainPageQaScooter(driver)
        about_rent = AboutRentPage(driver)

        main_page.get_main_page()
        main_page.confirm_cookie_usage()
        main_page.click_on_head_order_button()
        order_page.check_order_page_loaded()
        order_page.set_personal_data(name, surname, address, station, phone_number)
        about_rent.sent_rent_data(rental_period, scooter_color)
        # assert self.driver.find_element(*OpLoc.order_rent_header)


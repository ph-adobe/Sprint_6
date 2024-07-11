import allure
from locators.main_page_locators import MainPageQaScooterLocators as Mpl
from locators.order_page_locators import OrderPageQaScooterLocators as Op
from pages.base_page import BasePage
from test_data import TestData as Td


class OrderPageQaScooter(BasePage):

    @allure.step("Open order page")
    def get_order_page(self):
        self.get_url(Td.ORDER_PAGE_URL)
        self.wait_for_loading(Op.order_header)
        self.confirm_cookie_usage()

    @allure.step("Input name")
    def set_name(self, name):
        self.input_data(Op.name_input_field, name)

    @allure.step("Input surname")
    def set_surname(self, surname):
        self.input_data(Op.surname_input_field, surname)

    @allure.step("Input address")
    def set_address(self, address):
        self.input_data(Op.address_input_field, address)

    @allure.step("Choose station")
    def set_station(self, station):
        self.choose_element_from_drop_down_list(Op.station_field, station)

    @allure.step("Input phone number")
    def set_phone_number(self, phone_number):
        self.input_data(Op.phone_number_field, phone_number)

    @allure.step("Send personal data: name, surname, address, station, phone number.")
    def set_personal_data(self, name, surname, address, station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone_number(phone_number)
        self.click_on_element(Op.next_button)
        self.wait_for_loading(Op.order_rent_header)

    @allure.step("Click on scooter logo")
    def click_on_scooter_logo(self):
        self.click_on_element(Op.scooter_logo)
        self.wait_for_loading(Mpl.home_header)

    @allure.step("Click on yandex logo")
    def click_on_yandex_logo(self):
        self.click_on_element(Op.yandex_logo)
        self.switch_to_next_window(self.dzen_search)



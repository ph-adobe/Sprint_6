from locators.order_page_locators import OrderPageQaScooterLocators as Op
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from test_data import TestData as Td


class OrderPageQaScooter(BasePage):

    def get_order_page(self):
        self.driver.get(Td.ORDER_PAGE_URL)
        self.wait_for_loading(Op.order_header)
        self.confirm_cookie_usage()

    def set_name(self, name):
        self.driver.find_element(*Op.name_input_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*Op.surname_input_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*Op.address_input_field).send_keys(address)

    def set_station(self, station):
        element = self.driver.find_element(*Op.station_field)
        actions = ActionChains(self.driver)
        actions.click(element).send_keys(station, Keys.ARROW_DOWN, Keys.ENTER).perform()

    def set_phone_number(self, phone_number):
        element = self.driver.find_element(*Op.phone_number_field)
        element.click()
        element.send_keys(phone_number)

    def set_personal_data(self, name, surname, address, station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone_number(phone_number)
        self.click_on_element(Op.next_button)
        self.wait_for_loading(Op.order_rent_header)



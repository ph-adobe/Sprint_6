from locators.order_page_locators import OrderPageQaScooterLocators as Op
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class OrderPageQaScooter:

    order_page_link = "https://qa-scooter.praktikum-services.ru/order"
    dzen_link_redirect = "https://dzen.ru/?yredirect=true"

    def __init__(self, driver):
        self.driver = driver

    def check_order_page_loaded(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(Op.order_header))

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

    def click_next_button(self):
        self.driver.find_element(*Op.next_button).click()

    def click_on_yandex_logo(self):
        self.driver.find_element(*Op.yandex_logo).click()

    def click_scooter_logo(self):
        self.driver.find_element(*Op.scooter_logo).click()

    def wait_for_loading_rent_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(Op.order_rent_header))

    def set_personal_data(self, name, surname, address, station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone_number(phone_number)
        self.click_next_button()
        self.wait_for_loading_rent_page()



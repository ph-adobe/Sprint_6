from locators.about_rent_page_locators import AboutRentPageLocators as Arp
from datetime import date, timedelta
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class AboutRentPage:
    def __init__(self, driver):
        self.driver = driver

    def set_rental_data(self):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        self.driver.find_element(*Arp.rent_data_field).click()
        self.driver.find_element(*Arp.rent_data_field).send_keys(tomorrow.strftime("%d.%m.%Y"), Keys.ENTER)

    def set_rental_period(self, period):
        self.driver.find_element(*Arp.rental_period).click()
        if period == "сутки":
            self.driver.find_element(*Arp.rental_period_day).click()
        elif period == "двое суток":
            self.driver.find_element(*Arp.rental_period_two_days).click()

    def set_scooter_color(self, color):
        if color == "черный":
            self.driver.find_element(*Arp.scooter_black_color).click()
        elif color == "серый":
            self.driver.find_element(*Arp.scooter_grey_color).click()

    def click_make_order(self):
        self.driver.find_element(*Arp.make_order_button).click()

    def wait_for_loading(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(Arp.about_rent_header))

    def sent_rent_data(self, period, color):
        self.wait_for_loading()
        self.set_rental_data()
        self.set_rental_period(period)
        self.set_scooter_color(color)
        self.click_make_order()



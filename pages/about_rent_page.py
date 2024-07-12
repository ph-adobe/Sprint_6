import allure
from datetime import date, timedelta
from locators.about_rent_page_locators import AboutRentPageLocators as Arp
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class AboutRentPage(BasePage):
    @allure.step("Choose when to deliver")
    def set_rental_data(self):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        self.input_data(Arp.rent_data_field, tomorrow.strftime("%d.%m.%Y"), Keys.ENTER)

    @allure.step("Choose rental period")
    def set_rental_period(self, period):
        self.click_on_element(Arp.rental_period)
        if period == "сутки":
            self.click_on_element(Arp.rental_period_day)
        elif period == "двое суток":
            self.click_on_element(Arp.rental_period_two_days)

    @allure.step("Choose color of the scooter")
    def set_scooter_color(self, color):
        if color == "черный":
            self.click_on_element(Arp.scooter_black_color)
        elif color == "серый":
            self.click_on_element(Arp.scooter_grey_color)

    @allure.step("Send rental data: data, period, color of the scooter")
    def sent_rent_data(self, period, color):
        self.set_rental_data()
        self.set_rental_period(period)
        self.set_scooter_color(color)
        self.click_on_element(Arp.make_order_button)
        self.wait_for_loading(Arp.popup_question_header)
        self.click_on_element(Arp.yes_button)

    @allure.step("Check if order is processed")
    def check_order_processed(self):
        return self.check_presence_of_element(Arp.order_is_processed)




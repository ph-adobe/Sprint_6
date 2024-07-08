from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    cookie_message = [By.CLASS_NAME, "App_CookieConsent__1yUIN"]
    confirm_cookie_button = [By.XPATH, "//*[@id='rcc-confirm-button']"]

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_loading(self, locator, time=3):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_all_elements_presented(self, locator, time=3):
        WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator))

    def confirm_cookie_usage(self):
        cookie = self.driver.find_element(*self.cookie_message)
        if cookie:
            self.driver.find_element(*self.confirm_cookie_button).click()


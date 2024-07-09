from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BasePage:
    cookie_message = [By.CLASS_NAME, "App_CookieConsent__1yUIN"]
    confirm_cookie_button = [By.XPATH, "//*[@id='rcc-confirm-button']"]
    timeout = 7

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_loading(self, locator, time=timeout):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def confirm_cookie_usage(self):
        cookie = self.driver.find_element(*self.cookie_message)
        if cookie:
            self.driver.find_element(*self.confirm_cookie_button).click()

    def check_presence_of_element(self, element_locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located(element_locator),
            message=f"Not found: {element_locator}",
        )
        return element

    def scroll_to_element(self, element_locator):
        element = self.check_presence_of_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element_locator))

    def click_on_element(self, element_locator):
        self.scroll_to_element(element_locator)
        self.check_presence_of_element(element_locator).click()

    def switch_to_next_window(self):
        current_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break
            sleep(3)

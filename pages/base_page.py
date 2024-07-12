from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    cookie_message = [By.CLASS_NAME, "App_CookieConsent__1yUIN"]
    confirm_cookie_button = [By.XPATH, "//*[@id='rcc-confirm-button']"]
    dzen_search = [By.ID, "ya-search-container-uri0hf"]
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

    def input_data(self, element_locator, *args):
        self.check_presence_of_element(element_locator).click()
        self.check_presence_of_element(element_locator).send_keys(*args)

    def choose_element_from_drop_down_list(self, element_locator, element_to_choose):
        element = self.check_presence_of_element(element_locator)
        actions = ActionChains(self.driver)
        actions.click(element).send_keys(element_to_choose, Keys.ARROW_DOWN, Keys.ENTER).perform()

    def switch_to_next_window(self, element_locator):
        current_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                self.check_presence_of_element(element_locator)
                break


from selenium.webdriver.common.by import By


class BaseLocators:
    cookie_message = [By.CLASS_NAME, "App_CookieConsent__1yUIN"]
    confirm_cookie_button = [By.XPATH, "//*[@id='rcc-confirm-button']"]
    dzen_search = [By.ID, "ya-search-container-uri0hf"]
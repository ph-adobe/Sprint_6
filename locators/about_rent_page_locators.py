from selenium.webdriver.common.by import By


class AboutRentPageLocators:
    about_rent_header = [By.CLASS_NAME, "Order_Header__BZXOb"]

    rent_data_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period = [By.XPATH, "//div[text()='* Срок аренды']"]
    rental_period_menu = [By.CLASS_NAME, "Dropdown-menu"]
    rental_period_day = [By.XPATH, "//div[text()='сутки']"]
    rental_period_two_days = [By.XPATH, "//div[text()='двое суток']"]
    scooter_black_color = [By.ID, "black"]
    scooter_grey_color = [By.ID, "grey"]

    make_order_button = [By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')][text()='Заказать']"]

    popup_question_header = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    yes_button = [By.XPATH, "//button[text()='Да']"]
    order_is_processed = [By.XPATH, "//div[text()='Заказ оформлен']"]

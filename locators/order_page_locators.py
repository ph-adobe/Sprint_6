from selenium.webdriver.common.by import By


class OrderPageQaScooterLocators:
    order_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][text()='Для кого самокат']"]
    order_rent_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][text()='Про аренду']"]

    name_input_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_input_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, "//button[text()='Далее']"]

    yandex_logo = [By.XPATH, "//a[@href='//yandex.ru']"]
    scooter_logo = [By.XPATH, "//a[@href='/']"]




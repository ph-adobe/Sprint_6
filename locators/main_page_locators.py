from selenium.webdriver.common.by import By


class MainPageQaScooterLocators:
    home_header = [By.CLASS_NAME, "Home_Header__iJKdX"]
    head_page_order_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    bottom_page_order_button = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]

    payment_question = [By.ID, "accordion__heading-0"]
    payment_answer = [By.XPATH, "//*[@id='accordion__panel-0']/p"]

    scooter_number_question = [By.XPATH, "//*[@id='accordion__heading-1']"]
    scooter_number_answer = [By.XPATH, "//*[@id='accordion__panel-1']/p"]

    rent_time_calculation_question = [By.XPATH, "//*[@id='accordion__heading-2']"]
    rent_time_calculation_answer = [By.XPATH, "//*[@id='accordion__panel-2']/p"]

    rent_today_question = [By.XPATH, "//*[@id='accordion__heading-3']"]
    rent_today_answer = [By.XPATH, "//*[@id='accordion__panel-3']/p"]

    change_rent_period_question = [By.XPATH, "//*[@id='accordion__heading-4']"]
    change_rent_period_answer = [By.XPATH, "//*[@id='accordion__panel-4']/p"]

    charger_question = [By.XPATH, "//*[@id='accordion__heading-5']"]
    charger_answer = [By.XPATH, "//*[@id='accordion__panel-5']/p"]

    cancellation_question = [By.XPATH, "//*[@id='accordion__heading-6']"]
    cancellation_answer = [By.XPATH, "//*[@id='accordion__panel-6']/p"]

    distance_question = [By.XPATH, "//*[@id='accordion__heading-7']"]
    distance_answer = [By.XPATH, "//*[@id='accordion__panel-7']/p"]



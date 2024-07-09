from selenium.webdriver.common.by import By


class MainPageQaScooterLocators:
    home_header = [By.CLASS_NAME, "Home_Header__iJKdX"]
    head_page_order_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    bottom_page_order_button = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]

    payment_question = [By.ID, "accordion__heading-0"]
    payment_answer = [By.XPATH, "//*[@id='accordion__panel-0']/p"]
    payment_answer_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    scooter_number_question = [By.XPATH, "//*[@id='accordion__heading-1']"]
    scooter_number_answer = [By.XPATH, "//*[@id='accordion__panel-1']/p"]
    scooter_number_answer_text = ("Пока что у нас так: один заказ — один самокат. "
                                  "Если хотите покататься с друзьями, можете просто "
                                  "сделать несколько заказов — один за другим.")

    rent_time_calculation_question = [By.XPATH, "//*[@id='accordion__heading-2']"]
    rent_time_calculation_answer = [By.XPATH, "//*[@id='accordion__panel-2']/p"]
    rent_time_calculation_answer_text = (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    )

    rent_today_question = [By.XPATH, "//*[@id='accordion__heading-3']"]
    rent_today_answer = [By.XPATH, "//*[@id='accordion__panel-3']/p"]
    rent_today_answer_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    change_rent_period_question = [By.XPATH, "//*[@id='accordion__heading-4']"]
    change_rent_period_answer = [By.XPATH, "//*[@id='accordion__panel-4']/p"]
    change_rent_period_answer_text = (
        "Пока что нет! Но если что-то срочное — всегда "
        "можно позвонить в поддержку по красивому номеру 1010.")

    charger_question = [By.XPATH, "//*[@id='accordion__heading-5']"]
    charger_answer = [By.XPATH, "//*[@id='accordion__panel-5']/p"]
    charger_answer_text = (
        "Самокат приезжает к вам с полной зарядкой. "
        "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
        "Зарядка не понадобится.")

    cancellation_question = [By.XPATH, "//*[@id='accordion__heading-6']"]
    cancellation_answer = [By.XPATH, "//*[@id='accordion__panel-6']/p"]
    cancellation_answer_text = ("Да, пока самокат не привезли. "
                                "Штрафа не будет, объяснительной записки тоже не попросим. "
                                "Все же свои.")

    distance_question = [By.XPATH, "//*[@id='accordion__heading-7']"]
    distance_answer = [By.XPATH, "//*[@id='accordion__panel-7']/p"]
    distance_answer_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


from locators.main_page_locators import MainPageQaScooterLocators as Mpl


class TestData:
    MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_PAGE_URL = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_LINK = "https://dzen.ru/?yredirect=true"

    data_set_to_make_order_1 = [
        Mpl.head_page_order_button, "Иван", "Иванов", "ул. Садовая, д.22 кв.100", "Преображенская площадь",
        "81234567890", "сутки", "черный"
    ]

    data_set_to_make_order_2 = [
        Mpl.bottom_page_order_button, "Любовь", "Козлова", "ул. Лесная, д.777 кв.5", "Лихоборы", "+71234567890",
        "двое суток", "серый"
    ]

    questions = [
        [Mpl.payment_question, Mpl.payment_answer, Mpl.payment_answer_text],
        [Mpl.scooter_number_question, Mpl.scooter_number_answer, Mpl.scooter_number_answer_text],
        [Mpl.rent_time_calculation_question, Mpl.rent_time_calculation_answer, Mpl.rent_time_calculation_answer_text],
        [Mpl.rent_today_question, Mpl.rent_today_answer, Mpl.rent_today_answer_text],
        [Mpl.change_rent_period_question, Mpl.change_rent_period_answer, Mpl.change_rent_period_answer_text],
        [Mpl.charger_question, Mpl.charger_answer, Mpl.charger_answer_text],
        [Mpl.cancellation_question, Mpl.cancellation_answer, Mpl.cancellation_answer_text],
        [Mpl.distance_question, Mpl.distance_answer, Mpl.distance_answer_text]
    ]

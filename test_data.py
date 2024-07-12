from locators.main_page_locators import MainPageQaScooterLocators as Mpl


class TestData:
    MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_PAGE_URL = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_LINK = "https://dzen.ru/?yredirect=true"

    data_set_to_make_order_1 = [
        "button at the top of the page", "Иван", "Иванов", "ул. Садовая, д.22 кв.100", "Преображенская площадь",
        "81234567890", "сутки", "черный"
    ]

    data_set_to_make_order_2 = [
        "button in the middle of the page", "Любовь", "Козлова", "ул. Лесная, д.777 кв.5", "Лихоборы", "+71234567890",
        "двое суток", "серый"
    ]

    payment_answer_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    rent_time_calculation_answer_text = (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    )
    scooter_number_answer_text = ("Пока что у нас так: один заказ — один самокат. "
                                  "Если хотите покататься с друзьями, можете просто "
                                  "сделать несколько заказов — один за другим.")
    rent_today_answer_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    change_rent_period_answer_text = ("Пока что нет! Но если что-то срочное — всегда "
                                      "можно позвонить в поддержку по красивому номеру 1010.")
    charger_answer_text = ("Самокат приезжает к вам с полной зарядкой. "
                           "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
                           "Зарядка не понадобится.")
    cancellation_answer_text = ("Да, пока самокат не привезли. "
                                "Штрафа не будет, объяснительной записки тоже не попросим. "
                                "Все же свои.")
    distance_answer_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    questions = [
        [Mpl.payment_question, Mpl.payment_answer, payment_answer_text],
        [Mpl.scooter_number_question, Mpl.scooter_number_answer, scooter_number_answer_text],
        [Mpl.rent_time_calculation_question, Mpl.rent_time_calculation_answer, rent_time_calculation_answer_text],
        [Mpl.rent_today_question, Mpl.rent_today_answer, rent_today_answer_text],
        [Mpl.change_rent_period_question, Mpl.change_rent_period_answer, change_rent_period_answer_text],
        [Mpl.charger_question, Mpl.charger_answer, charger_answer_text],
        [Mpl.cancellation_question, Mpl.cancellation_answer, cancellation_answer_text],
        [Mpl.distance_question, Mpl.distance_answer, distance_answer_text]
    ]

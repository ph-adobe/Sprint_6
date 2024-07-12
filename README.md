# Sprint_6
Проект содержит UI-тесты для приложения [Yandex Scooter](https://qa-scooter.praktikum-services.ru/)

1. Установить зависимости

```bazaar
pip install -r requirements.txt
```
2. Запустить тесты
```bazaar
pytest -v
```

3. Сгенерировать отчет в allure
```bazaar
pytest tests --alluredir=allure_results
```
4. Сформировать отчёт в формате веб-страницы
```bazaar
allure serve allure_results
```
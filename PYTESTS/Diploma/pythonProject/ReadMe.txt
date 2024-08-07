 Технологический стек

Проект использует разнообразные библиотеки и инструменты для автоматизации тестирования веб-приложений,
 генерации данных, обработки изображений и взаимодействия с веб-службами. Ниже приведены основные компоненты стека:

Стандартная библиотека Python

- `os`: Работа с операционной системой, управление путями или системными командами.
- `random`: Генерация случайных данных.
- `re`: Работа с регулярными выражениями, валидация и поиск шаблонов в строках.
- `string`: Доступ к строковым константам и операциям.
- `time`: Работа с временем и задержками.

Внешние библиотеки

- `requests`: Отправка HTTP-запросов для API тестирования или взаимодействия с веб-сервисами.
- `Pillow (PIL)`: Работа с изображениями, их обработка и анализ.
- `pytesseract`: OCR (распознавание текста на изображениях), используется вместе с Pillow для извлечения текста
из изображений.
- `pytest`: Основной тестовый фреймворк.
- `faker`: Генерация фейковых данных (имена, адреса, email и т.д.), `faker.providers.internet` добавляет
 генерацию данных, специфичных для интернета (IP-адреса, домены).

Selenium

- `selenium.webdriver`: Основной модуль для взаимодействия с веб-браузерами.
- `selenium.webdriver.chrome.service.Service`: Управление ChromeDriver.
- `selenium.webdriver.chrome.options.Options`: Настройка опций для Chrome.
- `webdriver_manager.chrome`: Автоматическое управление ChromeDriver.
- `selenium.webdriver.common.by.By`: Удобные селекторы для поиска элементов на странице.
- `selenium.webdriver.support.ui.WebDriverWait`: Ожидание элементов на странице.
- `selenium.webdriver.support.expected_conditions as EC`: Ожидание различных условий на странице (видимость элемента).
- `selenium.common.exceptions.TimeoutException`: Обработка исключений, связанных с ожиданием.

Фикстуры

- Генерация данных:
  - `generate_phone_number`
  - `generate_password`
  - `generate_cyrillic_name`
  - и другие.

- Настройка браузера:
  - `browser`: Инициализация Chrome браузера с помощью `webdriver_manager`.
  - `open_auth_page`: Навигация к странице авторизации.
  - `open_password_recovery_page`: Навигация к странице восстановления пароля.

Проверка тестовых сценариев

Тестовые сценарии проверяют следующие аспекты веб-приложения:

- Аутентификация:
  - Вход по телефону
  - Вход по электронной почте
  - Валидация полей ввода (пустые поля, неверные данные)
  - Проверка граничных значений

- Регистрация:
  - Регистрация по телефону
  - Регистрация по электронной почте
  - Валидация полей ввода (пустые поля, неверные данные)
  - Проверка граничных значений
  - Негативные тесты (недопустимые символы, неправильные данные)

Команды для запуска тестов

Для запуска всех тестов используйте команду:

pytest


Для запуска тестов из определенного файла используйте:

pytest tests/test_auth.py
pytest tests/test_registration.py
pytest tests/test_disable_cookies.py


Для запуска тестов с использованием маркеров используйте:

pytest -m phone
pytest -m email
pytest -m login
pytest -m negative

Для запуска тестов с отображением подробной информации (verbose mode):

pytest -v

Для запуска тестов и создания отчета

pytest --html=report.html

Заключение

Проект использует стек технологий для обеспечения качественного автоматизированного тестирования,
 генерации данных и взаимодействия с веб-сервисами, что позволяет поддерживать высокий уровень надежности
  и функциональности веб-приложения.

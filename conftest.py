"""
Файлик конфигурации для тестов проекта Степик.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Поддержка выбора браузера из командной  строки
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # Поддержка параметра языка из командной  строки
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем имя браузера введенное в командной строке
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Создаем объект класса опций Хрома
        options = Options()
        # Получаем язык введенный в командной строке
        user_language = request.config.getoption("language")
        # Передаем в опции введенный язык
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # Запускаем браузер с опциями
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # Создаем объект класса файрфокс профиля
        fp = webdriver.FirefoxProfile()
        # Получаем язык введенный в командной строке
        user_language = request.config.getoption("language")
        # Передаем в профиль введенный язык
        fp.set_preference("intl.accept_languages", user_language)
        # Запускаем браузер с настроенным профилем
        browser = webdriver.Firefox(firefox_profile=fp)

    yield browser

    print("\nquit browser..")
    browser.quit()

"""
Сценарии тестов для страниц с товарами
"""
import pytest
import time
import random

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    """
    Пробный класс для прохождения сценария создания пользователя перед тестами.
    Цитата со степика: ВАЖНО! Вообще говоря манипулировать браузером в сетапе и уж тем более что-то там проверять —
    это плохая практика, лучше так не делать без особой необходимости. Здесь этот пример исключительно в учебных
    целях, чтобы вы попробовали писать сетапы для тестов. В реальной жизни мы реализовали бы все эти манипуляции с
    помощью API или напрямую через базу данных.
    """

    @pytest.fixture(scope="function", autouse=True)  # для каждого теста, запускается без вызова
    def setup(self, browser):
        # генерируем рандомные мейл и пароль
        email = str(random.randint(750000, 4500000)) + "@fakemail.org"
        password = str(time.time())
        # регистрируем пользователя и проверяем что он зарегистрирован
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        Проверяем что зарегистрированный пользователь
        не видит сообщения о добавлении в корзину перейдя на страницу товара.
        :param browser:
        :return:
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Проверяем что зарегистрированный пользователь
        может успещно добавить товар в корзину
        :param browser:
        :return:
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_prod_to_basket()
        page.should_be_correct_name()
        page.should_be_correct_price()


# нашли и пометили xfail ссылку на страницу с багом
@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                          ]
                         )
def test_guest_can_add_product_to_basket(browser, link):
    """
    Проверяем что на каждой странице из списка для получени ссылки нужно ввести код и корректность добавленых товаров
    :param browser: fixture from conftest.py
    :param link: from parametrize fixture
    :return:
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_prod_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()

    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Проверяем наличие ссылки на логин со страницы товара для гостя
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Проверяем что гость не видит товара
    и видит текст что корзина пуста перейдя в [пустую]корзину со страницы товара
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_items_in_basket()
    basket_page.should_be_text_about_empty_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Проверяем что гость не видит сообщения об успешном добавлении товара после добавления товара
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_prod_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Проверяем что гость не видит сообщения об успешном добавлении товара (не добаляя товар)
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Проверяем что гость видит кнопку ведущую на страницу логина со страницы товара
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Проверяем что сообщение об успешном добавлении исчезает со страницы товара после добавления товара в корзину
    :param browser: fixture from conftest.py
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/" \
           "coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_prod_to_basket()
    page.should_be_disappeared()

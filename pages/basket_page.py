from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    """
    Класс с методами проверки корзины - http://selenium1py.pythonanywhere.com/basket/
    """
    def should_be_text_about_empty_basket(self):
        """
        Проверяем есть ли текст о пустой корзине
        :return:
        """
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY)

    def should_be_not_items_in_basket(self):
        """
        Проверяем что в корзине НЕТ товаров
        :return:
        """
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

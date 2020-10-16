from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage:
    """
    Базовый класс от которого наследуются все классы страниц в Степике
    """

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # неявное ожидание отключено для корректной работы функций с проверкой отсутствия
        # self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        """
        переход в корзину
        :return:
        """
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        """
        переход на страницу логина (и регистарции)
        :return: None
        """
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_element_present(self, how, what):
        """
        проверяем наличие элемента на странице
        :param how: By.*something* from selenium.webdriver.common.by
        :param what: selector
        :return: boolean
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяем что элемента нет на странице и он не появляется в течение timeout
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяем что элемента нет на странице, с частотой 1(третий аргуемнт WebDriverWait),
        в течение timeout, то есть что элемент исчезает со временем
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        """
        проверяем авторизован ли юзер проверкой наличия юзерпика
        :return:
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        """
        Проверяем что на странице есть ссылка на страницу логина
        :return:
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link isn`t presented"

    def solve_quiz_and_get_code(self):
        """
        Метод для решения магической задачи от создаталей курса
        :return:
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
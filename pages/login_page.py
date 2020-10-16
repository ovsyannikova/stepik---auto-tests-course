from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Класс с методами проверки логина и регистрации - http://selenium1py.pythonanywhere.com/accounts/login/
    """
    def should_be_login_page(self):
        """
        Проверка страницы пометодам описанным в классе
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверка что текущий URL это URL страницы логина
        """
        assert LoginPageLocators.LOGIN_TAG_IN_URL in self.browser.current_url, "URL is incorrect!"

    def should_be_login_form(self):
        """
        Проверка что на странце есть форма логина
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn`t presented"

    def should_be_register_form(self):
        """
        Проверка что на странце есть форма регистрации
        """
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Reg form isn`t presented"

    def register_new_user(self, email, password):
        """
        Авторегистрация нового пользователя
        :param email: str
        :param password: str
        :return: None
        """
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT_CONF).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()
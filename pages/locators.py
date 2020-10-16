from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[href=\"/ru/basket/\"]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_TAG_IN_URL = "/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_INPUT_CONF = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_FROM_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_PRICE_FROM_ALERT = (By.CSS_SELECTOR, "#messages .alert-info strong")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    TEXT_ABOUT_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket-items")

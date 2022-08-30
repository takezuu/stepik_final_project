from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    CART = (By.CSS_SELECTOR, '.page_inner > div > div:nth-child(2) > span > a')
    EMPTY_CART = (By.CSS_SELECTOR, '#content_inner > p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    MESSAGE = (By.CSS_SELECTOR, '#messages > div > div')
    CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p')
    CHECK_PRODUCT_MESSAGE = (By.CSS_SELECTOR, '#content_inner > article > div > div:nth-child(2) > h1')
    CHECK_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner > article > div > div:nth-child(2) > p')
    LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'


class MainPageLocators():
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REG = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PW = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PW_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

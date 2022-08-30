from Pages.MainPage import MainPage
from Pages.locators import MainPageLocators, BasePageLocators, LoginPageLocators
from Pages.LoginPage import LoginPage
from Pages.BasketPage import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        MainPage(browser).open_link(MainPageLocators.MAIN_LINK)
        MainPage(browser).go_to_login_page(BasePageLocators.LOGIN_LINK)

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        LoginPage(browser).open_link(MainPageLocators.MAIN_LINK)
        LoginPage(browser).open_cart(BasePageLocators.CART)
        BasketPage(browser).check_empty_cart(BasePageLocators.EMPTY_CART)


def test_login_url_check(browser):
    LoginPage(browser).open_link(LoginPageLocators.LOGIN_URL)
    LoginPage(browser).should_be_login_url()


def test_login_form_check(browser):
    LoginPage(browser).open_link(LoginPageLocators.LOGIN_URL)
    LoginPage(browser).should_be_login_form(LoginPageLocators.LOGIN_FORM)


def test_registration_form_check(browser):
    LoginPage(browser).open_link(LoginPageLocators.LOGIN_URL)
    LoginPage(browser).should_be_login_form(LoginPageLocators.LOGIN_REG)

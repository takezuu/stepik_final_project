from Pages.BasketPage import BasketPage
from Pages.ProductPage import ProductPage
from Pages.locators import ProductPageLocators, BasePageLocators, LoginPageLocators
from Pages.LoginPage import LoginPage
import pytest


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        LoginPage(browser).open_link(LoginPageLocators.LOGIN_URL)
        LoginPage(browser).register_new_user(LoginPageLocators.REG_EMAIL, LoginPageLocators.REG_PW,
                                             LoginPageLocators.REG_PW_2, LoginPageLocators.REG_BTN)
        LoginPage(browser).should_be_authorized_user(BasePageLocators.USER_ICON)

    def test_user_cant_see_success_message(self, browser):
        ProductPage(browser).open_link(ProductPageLocators.LINK)
        ProductPage(browser).should_not_be_success_message_2(ProductPageLocators.CHECK_PRODUCT_MESSAGE)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        ProductPage(browser).open_link(ProductPageLocators.LINK)
        ProductPage(browser).add_to_cart(ProductPageLocators.BUTTON)
        ProductPage(browser).check_message(ProductPageLocators.MESSAGE, ProductPageLocators.CHECK_PRODUCT_MESSAGE)
        ProductPage(browser).check_cart(ProductPageLocators.CART_MESSAGE, ProductPageLocators.CHECK_CART_MESSAGE)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    ProductPage(browser).open_link(ProductPageLocators.LINK)
    ProductPage(browser).add_to_cart(ProductPageLocators.BUTTON)
    ProductPage(browser).should_not_be_success_message(ProductPageLocators.CHECK_PRODUCT_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    ProductPage(browser).open_link(ProductPageLocators.LINK)
    ProductPage(browser).add_to_cart(ProductPageLocators.BUTTON)
    ProductPage(browser).success_message_should_disappear(ProductPageLocators.CHECK_PRODUCT_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    ProductPage(browser).open_link(BasePageLocators.SEE_LOGIN_LINK)
    ProductPage(browser).should_be_login_link(BasePageLocators.LOGIN_LINK)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    ProductPage(browser).open_link(ProductPageLocators.LINK)
    ProductPage(browser).should_be_login_link(BasePageLocators.LOGIN_LINK)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    ProductPage(browser).open_link(ProductPageLocators.LINK)
    ProductPage(browser).open_cart(BasePageLocators.CART)
    BasketPage(browser).check_empty_cart(BasePageLocators.EMPTY_CART)


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    ProductPage(browser).open_link(ProductPageLocators.LINK)
    ProductPage(browser).add_to_cart(ProductPageLocators.BUTTON)
    ProductPage(browser).check_message(ProductPageLocators.MESSAGE, ProductPageLocators.CHECK_PRODUCT_MESSAGE)
    ProductPage(browser).check_cart(ProductPageLocators.CART_MESSAGE, ProductPageLocators.CHECK_CART_MESSAGE)

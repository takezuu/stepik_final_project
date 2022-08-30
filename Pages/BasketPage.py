from Pages.BasePage import BasePage


class BasketPage(BasePage):

    def check_empty_cart(self, cart_message):
        text = self.browser.find_element(*cart_message).text
        assert text == f"{text}", 'Text doesn\'t match'

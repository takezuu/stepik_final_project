from Pages.BasePage import BasePage


class ProductPage(BasePage):

    def add_to_cart(self, button):
        self.browser.find_element(*button).click()
        self.solve_quiz_and_get_code()

    def check_message(self, message, check_product_message):
        check_text = self.browser.find_element(*check_product_message).text
        text = self.browser.find_element(*message).text
        assert text == f"{check_text} был добавлен в вашу корзину.", 'Text doesn\'t match'

    def check_cart(self, cart_message, check_cart_message):
        check_text = self.browser.find_element(*check_cart_message).text
        text = self.browser.find_element(*cart_message).text
        assert text == f"Стоимость корзины теперь составляет {check_text}", 'Text doesn\'t match'

    def should_not_be_success_message(self, element):
        assert self.is_not_element_present(element), "Success message is presented, but should not be"

    def should_not_be_success_message_2(self, element):
        assert not self.is_not_element_present(element), "Success message is presented, but should not be"

    def success_message_should_disappear(self, element):
        assert self.is_disappeared(element), "Success message is not presented, but should be"

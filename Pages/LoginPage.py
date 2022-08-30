from Pages.BasePage import BasePage
import uuid


class LoginPage(BasePage):
    PASSWORD = 'Qwerty223'

    def reg_email(self):
        EMAIL = str(uuid.uuid4()) + '2123hasdf@yand.ru'
        return EMAIL

    def should_be_login_url(self):
        url_login_page = self.browser.current_url
        assert 'login' in url_login_page, 'Sub-string not founded'

    def should_be_login_form(self, element):
        assert self.browser.find_element(*element), 'There isn\'t login form'

    def should_be_register_form(self, element):
        assert self.browser.find_element(*element), 'There isn\'t register form'

    def register_new_user(self, email, password, password2, btn):
        self.browser.find_element(*email).send_keys(LoginPage.reg_email(self))
        self.browser.find_element(*password).send_keys(LoginPage.PASSWORD)
        self.browser.find_element(*password2).send_keys(LoginPage.PASSWORD)
        self.browser.find_element(*btn).click()

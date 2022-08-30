from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import math
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser):
        self.browser = browser

    def solve_quiz_and_get_code(self):
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

    def is_element_present(self, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(element))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(element))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located(element))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self, element):
        self.browser.find_element(*element).click()

    def should_be_login_link(self, element):
        assert self.is_element_present(element), "Login link is not presented"

    def open_link(self, link):
        self.browser.get(link)

    def open_cart(self, element):
        self.browser.find_element(*element).click()

    def should_be_authorized_user(self, element):
        assert self.is_element_present(element), "User icon is not presented, probably unauthorised user"

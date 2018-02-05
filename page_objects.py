from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from time import sleep


class BasePageObject(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.500)

    def find_element(self, by):
        return self.driver.find_element(by=by[0], value=by[1])

    def wait_and_find_element(self, by):
        self.wait.until(ec.presence_of_element_located(by))
        return self.find_element(by)

    @staticmethod
    def fill_element(element, keys):
        element.send_keys(keys)


class HomePage(BasePageObject):
    LOGIN_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, 'body > div._container > header > div > nav > ul > li.academylogin > ul > li > a')

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.MENU_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'body > div._container > header > div > nav > a')
        self.driver.get('http://www.mindvalley.com')
        self.check()

    def check(self):
        pass

    def click_login_button(self):
        menu_button = self.find_element(self.MENU_BUTTON_LOCATOR)
        menu_button.click()
        self.wait.until(ec.presence_of_element_located(self.LOGIN_BUTTON_LOCATOR))
        login_button = self.find_element(self.LOGIN_BUTTON_LOCATOR)
        login_button.click()
        return LoginPage(self.driver)


class LoginPage(BasePageObject):
    EMAIL_FIELD_LOCATOR = (By.NAME, 'email')
    PASSWORD_FIELD_LOCATOR = (By.NAME, 'password')
    LOGIN_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '#a0-onestep > div.a0-mode-container > div > form > div.bottom-content > div > button')
    ERROR_MESSAGE_BOX_LOCATOR = (By.CSS_SELECTOR, '#a0-onestep > div.a0-header.a0-top-header > h2.a0-error')
    FORGOT_PASSWORD_LINK_LOCATOR = (By.LINK_TEXT, 'Forgot your password? Recover password')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.email_field = self.find_element(self.EMAIL_FIELD_LOCATOR)
        self.password_field = self.find_element(self.PASSWORD_FIELD_LOCATOR)
        self.login_button = self.find_element(self.LOGIN_BUTTON_LOCATOR)
        self.forgot_password_link = self.find_element(self.FORGOT_PASSWORD_LINK_LOCATOR)

    def fill_email_field(self, login):
        self.fill_element(self.email_field, login)

    def fill_password_field(self, password):
        self.fill_element(self.password_field, password)

    def click_on_login_button(self):
        self.login_button.click()
        sleep(2)

    def click_on_forgot_password(self):
        self.forgot_password_link.click()
        return RecoverPasswordPage(self.driver)

    def get_error_message(self):
        self.wait.until(ec.visibility_of_element_located(self.ERROR_MESSAGE_BOX_LOCATOR),
                        "Failed waiting for error message to be visible.")
        error_message_box = self.find_element(self.ERROR_MESSAGE_BOX_LOCATOR)
        return error_message_box.text


class RecoverPasswordPage(BasePageObject):
    EMAIL_FIELD_LOCATOR = (By.NAME, 'email')
    SEND_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#a0-change_password > div.bottom-content > div > button')

    def __init__(self, driver):
        super(RecoverPasswordPage, self).__init__(driver)
        self.email_field = self.wait_and_find_element(self.EMAIL_FIELD_LOCATOR)
        self.send_button = self.wait_and_find_element(self.SEND_BUTTON_LOCATOR)


class LibraryPage(BasePageObject):
    MAIN_MENU_LOCATOR = (By.ID, 'main-menu')

    def __init__(self, driver):
        super(LibraryPage, self).__init__(driver)

    def is_main_menu_visible(self):
        self.wait.until(ec.visibility_of_element_located(self.MAIN_MENU_LOCATOR))

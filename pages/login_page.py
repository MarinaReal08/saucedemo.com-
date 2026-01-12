from playwright.sync_api import expect
from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"
    LOGO = ".login_logo"

    def open_login(self):
        self.open(self.URL)

    def login(self, username: str, password: str):
        self.element(self.USERNAME).fill(username)
        self.element(self.PASSWORD).fill(password)
        self.element(self.LOGIN_BTN).click()

    def should_be_loaded(self):
        expect(self.element(self.LOGO)).to_be_visible()
        self.should_have_url_contains(self.URL)

    def should_see_error_contains(self, text_part: str):
        expect(self.element(self.ERROR_MSG)).to_contain_text(text_part)

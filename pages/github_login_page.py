from selenium.webdriver.common.by import By
from conftest import LOGIN
from pages.BasePage import BasePage


class GithubLoginPage(BasePage):
    username_textbox = {"by": By.CSS_SELECTOR, "value": "#login_field"}
    password_textbox = {"by": By.CSS_SELECTOR, "value": "#password"}
    submit_button = {"by": By.CSS_SELECTOR, "value": "input[name='commit']"}

    def _init_(self, driver):
        self.driver = driver

    def login(self, url, username, password):
        self._visit(url['githubBaseURL'] + LOGIN)
        self._type(self.username_textbox, username)
        self._type(self.password_textbox, password)
        self._click(self.submit_button)

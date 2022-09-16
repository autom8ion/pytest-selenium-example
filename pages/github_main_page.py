from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class GithubMainPage(BasePage):
    new_Button = {"by": By.CSS_SELECTOR, "value": "a[class*='btn btn-sm btn-primary'][href*='/new']"}
    find_repository_textfield = {"by": By.CSS_SELECTOR, "value": "input[data-query-name='q']"}

    def _init_(self, driver):
        self.driver = driver

    def select_new_repo_button(self):
        self._is_displayed(self.new_Button, 15)
        self._click(self.new_Button)


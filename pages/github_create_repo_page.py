from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class GithubCreateRepoPage(BasePage):
    repository_name_textbox = {"by": By.CSS_SELECTOR, "value": "#repository_name"}
    description_textbox = {"by": By.CSS_SELECTOR, "value": "#repository_description"}
    create_repository_button = {"by": By.CSS_SELECTOR, "value": "btn-primary btn"}

    def _init_(self, driver):
        self.driver = driver

    def create_repository(self, repository_name):
        self._type(self.repository_name_textbox, repository_name)
        self._click(self.create_repository_button)
        

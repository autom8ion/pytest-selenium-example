import pytest
from pages.github_login_page import GithubLoginPage
from conftest import USERNAME, PASSWORD

@pytest.mark.usefixtures("driver_init")
class TestGithubLogin:

    def test_github_login(self, url):
        login_page = GithubLoginPage(self.driver)
        login_page.login(url, USERNAME, PASSWORD)


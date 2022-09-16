import pytest
from conftest import USERNAME, PASSWORD
from pages.github_login_page import GithubLoginPage
from pages.github_main_page import GithubMainPage
from pages.github_create_repo_page import GithubCreateRepoPage
import uuid

@pytest.mark.usefixtures("driver_init")
class TestGithubRepositories:

    def test_create_repository(self, url):
        login_page = GithubLoginPage(self.driver)
        login_page.login(url, USERNAME, PASSWORD)
        main_page = GithubMainPage(self.driver)
        main_page.select_new_repo_button()
        repo_page = GithubCreateRepoPage(self.driver)
        repo_name = "some_repo_" + uuid.uuid4().hex
        repo_page.create_repository(repo_name)

# pytest-selenium-example
Example Selenium/Pytest starter project

# Getting Started

1. Create pipenv virtual environment in pytest-selenium-example directory by running the 'pipenv install' command in the terminal/powershell/bash.
2. Get into the pipenv shell to execute the tests by utilizing the 'pipenv shell' command
3. Test Executions:

# run all tests
pytest

# filter tests by test module

pytest ./test/test_create_github_repository.py
pytest ./test/test_github_login.py

# run with pytest-html report

pytest --html=report.html --self-contained-html

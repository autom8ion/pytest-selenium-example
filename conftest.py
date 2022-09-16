import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


# Constants
LOGIN = '/login'
USERNAME = 'KTJ-DEMO'
PASSWORD = 'Dog.Bone1'


# Enable tests to run across multiple environments and browsers

def pytest_addoption(parser):
    parser.addoption("--environment", action="store", default="test",
                     help="environment to run the selenium tests against")
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests against")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser").lower()


@pytest.fixture(scope="class")
def url(pytestconfig):
    env = pytestconfig.getoption("environment").lower()

    if env == 'dev':
        url = {
            "githubBaseURL": "https://dev.github.com"
        }
        return url
    elif env == 'test':
        url = {
            "githubBaseURL": "https://github.com"
        }
        return url
    elif env == 'stage':
        url = {
            "githubBaseURL": "https://stage.github.com"
        }
        return url
    elif env == 'prod':
        url = {
            "githubBaseURL": "https://github.com"
        }
        return url
    else:
        raise ValueError('Unknown environment: ' + env)


@pytest.fixture(params=["chrome", "chrome_headless", "edge", "edge_headless"], scope="class")
# @pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.headless = False
        options.page_load_strategy = 'normal'
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
    if request.param == "chrome_headless":
        options = ChromeOptions()
        options.headless = True
        options.page_load_strategy = 'normal'
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
    if request.param == "edge":
        options = EdgeOptions()
        options.headless = False
        options.page_load_strategy = "normal"
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.implicitly_wait(10)
    if request.param == "edge_headless":
        options = EdgeOptions()
        options.headless = True
        options.page_load_strategy = "normal"
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.implicitly_wait(10)
    if request.param == "firefox":
        options = FirefoxOptions()
        options.headless = False
        options.page_load_strategy = "normal"
        options.add_argument('--no-sandbox')
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()

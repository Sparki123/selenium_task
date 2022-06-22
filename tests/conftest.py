import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['GH_TOKEN'] = "your_token_for_ff"


@pytest.fixture(autouse=True)
def setup(request, set_browser):
    set_browser = 'chrome'
    if set_browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif set_browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception(f'"{set_browser}" is not a supported browser')

    if request.cls is not None:
        request.cls.driver = driver
    driver.get("https://useinsider.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'wt-cli-accept-all-btn').click()

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope="class", autouse=True)
def set_browser(request):
    return request.config.getoption("--browser")

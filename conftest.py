import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Google Chrome"""
    browser: webdriver = webdriver.Chrome()
    yield browser
    browser.quit()

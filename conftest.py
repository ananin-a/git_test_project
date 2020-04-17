import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    browser: webdriver = webdriver.Chrome()
    browser.get("https://github.com/")
    print("\nБраузер запущен, начало тестирования...")
    yield browser
    browser.quit()
    print("\nБраузер закрыт, тестирование остановлено.")

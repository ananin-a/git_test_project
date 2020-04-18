from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовый класс."""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открыть страницу."""
        self.browser.get(self.url)

    def element_search(self, locator: str, timeout: int = 3):
        """
        Поиск элемента с явным ожиданием.

        :param locator: локатор
        :param timeout: время ожидания элемента
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(
                locator), message=f">>> Невозможно найти элемент по данному локатору: {locator}")

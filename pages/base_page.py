from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://github.com/"

    def open(self):
        """Открыть главнцю странцу"""
        self.browser.get(self.url)

    def element_search(self, locator: str, timeout: int = 3):
        """
        Поиск элемента на странице с явным ожиданием.

        :param locator: локатор.
        :param timeout: время ожидания элемента.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator), message=f">>> Элемент не найден по локатору {locator}")

    def elements_search(self, locator: str, timeout: int = 3):
        """
        Поиск элементов на странице с явным ожиданием.

        :param locator: передаем локатор.
        :param timeout: вркмя ожидания элемента.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator), message=f">>> Элемент не найден по локатору {locator}")

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .sign_up_page import SignUpPage


class MainPage(BasePage):
    """Главная страница."""

    def click_sing_in(self, browser):
        """
        Переход на страницу авторизации.

        :return: LoginPage
        """
        self.element_search(MainPageLocators.BUTTON_SIGN_IN).click()
        return LoginPage(browser, browser.current_url)

    def click_sing_up(self, browser):
        """
        Переход на стрпницу регистрации.

        :return: SignUpPage
        """
        self.element_search(MainPageLocators.BUTTON_SIGN_UP).click()
        return SignUpPage(browser, browser.current_url)

    def registration(self, browser, name: str, mail: str, password: str):
        """
        Регистрация нового пользователя.

        :param name: имя нового пользователя
        :param mail: электронный адрес нового пользователя
        :param password: пароль нового пользоваьеля
        :return: SignUpPage
        """
        self.entry_new_user_name(name)
        self.entry_new_user_email(mail)
        self.entry_new_user_password(password)
        self.element_search(MainPageLocators.BUTTON_SIGN_UP_FOR).click()
        return SignUpPage(browser, browser.current_url)

    def entry_new_user_name(self, name: str):
        """Ввод имени нового пользователя."""
        self.element_search(MainPageLocators.FIELD_NAME).send_keys(name)

    def entry_new_user_email(self, mail: str):
        """Ввод электронного адреса нового пользователя."""
        self.element_search(MainPageLocators.FIELD_EMAIL).send_keys(mail)

    def entry_new_user_password(self, password: str):
        """Ввести пароль нового пользователя."""
        self.element_search(MainPageLocators.FIELD_PASSWORD).send_keys(password)

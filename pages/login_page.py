from .base_page import BasePage
from .locators import LoginPageLocators
from .sign_up_page import SignUpPage


class LoginPage(BasePage):
    """Страница авторизации."""

    def should_de_a_page_title(self):
        """Должен быть заголовок"""
        return self.element_search(LoginPageLocators.TITLE_PAGE).text

    def should_be_a_message_about_incorrectly_filled_fields(self):
        """Должно быть сообщение о неправильно заполненных полях."""
        return self.element_search(LoginPageLocators.INCORRECT_MASSAGE).text

    def log_in(self, name: str, password: str):
        """
        Заполнение формы авторизации пользователя.

        :param name: имя пользователя
        :param password: пароль
        """
        self.entry_user_name(name)
        self.entry_password(password)
        self.element_search(LoginPageLocators.BUTTON_SIGN_IN).click()

    def entry_user_name(self, name: str):
        """Ввести имя пользователя."""
        return self.element_search(LoginPageLocators.FIELD_USER_NAME).send_keys(name)

    def entry_password(self, password: str):
        """Ввести пароль пользователя."""
        return self.element_search(LoginPageLocators.FIELD_PASSWORD).send_keys(password)

    def tap_button_create_an_account(self, browser):
        """
        Нажать на кнопку завести новый аккаунт.

        :return: SingUpPage
        """
        self.element_search(LoginPageLocators.CREATE_AN_ACCOUNT).click()
        return SignUpPage(browser, browser.current_url)

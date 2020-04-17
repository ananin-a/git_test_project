from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_de_a_page_title(self):
        """Должен быть заголовок 'Sign in to GitHub'."""
        title_name = self.element_search(LoginPageLocators.TITLE_PAGE).text
        print(f"\nЗаголовок {title_name}")
        assert title_name == "Sign in to GitHub", \
            ">>> Неверный заголовок страницы."

    def should_be_incorrect_message(self):
        """Должно быть сообщение о невернои имени или пароля пользователя."""
        incorrect_message = self.element_search(LoginPageLocators.INCORRECT_MASSAGE).text
        print(f"\nСообщение об ошибке {incorrect_message}")
        assert incorrect_message == "Incorrect username or password.", \
            ">>> Нет сообщения о неверном имени или пароле."

    def invalid_log_in(self, name: str, password: str):
        """
        Негативный сценарий.

        :param name: неверное имя пользователя.
        :param password: неверный пароль.
        """
        self.type_user_name(name)
        self.type_password(password)
        self.element_search(LoginPageLocators.BUTTON_SIGN_IN).click()

    def type_user_name(self, name: str):
        """Ввод имени существующего пользователя"""
        return self.element_search(LoginPageLocators.FIELD_USER_NAME).send_keys(name)

    def type_password(self, password: str):
        """Ввод пароля существующего пользователя"""
        return self.element_search(LoginPageLocators.FIELD_PASSWORD).send_keys(password)

    def create_an_account(self):
        """Нажать на кнопку завести новый аккаунт"""
        return self.element_search(LoginPageLocators.CREATE_AN_ACCOUNT).click()

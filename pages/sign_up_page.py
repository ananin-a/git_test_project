from .base_page import BasePage
from .locators import SignUpPageLocators


class SignUpPage(BasePage):
    """Страница регистрации."""

    def should_de_a_page_title(self):
        """Должен быть заголовок страницы."""
        return self.element_search(SignUpPageLocators.TITLE_PAGE).text

    def should_be_message_problems_create_account(self):
        """Ошибка: При стоздании аккаунта возникла проблема."""
        return self.element_search(SignUpPageLocators.PROBLEM_MESSAGE).text

    def should_be_a_error_name_message(self):
        """Получеть текст ошибки от поля Имя."""
        return self.element_search(SignUpPageLocators.NAME_ERROR).text

    def should_be_a_error_name_username_message(self):
        """Получеть текст ошибки от поля Имя."""
        return self.element_search(SignUpPageLocators.NAME_USERNAME).text

    def should_be_a_error_mail_message(self):
        """Получить текст ошибки от поля электронного адреса."""
        return self.element_search(SignUpPageLocators.EMAIL_ERROR).text

    def should_be_a_error_password_message(self):
        """Получить текст ошибки от поля пароля"""
        return self.element_search(SignUpPageLocators.PASSWORD_ERROR).text

    def registration_new_user(self, name: str, email: str, password: str):
        """
        Регистрация нового пользователя.

        :param name: иня нового пользователя
        :param email: електронный адресс нового пользователя
        :param password: пароль нового пользователя
        """
        self.entry_user_name(name)
        self.entry_email_address(email)
        self.entry_password(password)
        self.element_search(SignUpPageLocators.BUTTON_CREATE_ACCOUNT).click()

    def entry_user_name(self, name: str):
        """Ввод имени нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_USER_NAME).send_keys(name)

    def entry_email_address(self, email: str):
        """Ввод електронного адреса нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_EMAIL).send_keys(email)

    def entry_password(self, password: str):
        """Ввод пароль нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_PASSWORD).send_keys(password)

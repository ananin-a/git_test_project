from .base_page import BasePage
from .locators import SignUpPageLocators


class SignUpPage(BasePage):
    def should_de_a_page_title(self):
        """Должен быть заголовок страницы"""
        title_name: str = self.element_search(SignUpPageLocators.TITLE_PAGE).text
        assert title_name == "Create your account", \
            ">>> Неверный заголовок страницы."

    def should_be_message_problems_create_account(self):
        """При стоздании аккаунта возникла проблема"""
        message: str = self.element_search(SignUpPageLocators.PROBLEM_MESSAGE).text
        assert message == "There were problems creating your account.", \
            ">>> Нет сообщения о проблеме создания аккаунта"

    def should_be_a_error_name_message(self):
        """Поле имя не может быть пустым"""
        error_message: str = self.element_search(SignUpPageLocators.NAME_ERROR).text
        assert error_message == "Username can't be blank", \
            ">>> Нет сообщения о пустом имени пользователя."

    def should_be_a_error_mail_message(self):
        """Поле электронного адреса не может быть пустым"""
        error_message: str = self.element_search(SignUpPageLocators.EMAIL_ERROR).text
        assert error_message == "Email can't be blank", \
            ">>> Нет сообщения о пустом поле электронный адрес."

    def should_be_a_error_password_message(self):
        """Поле пароля не может быть пустыи"""
        error_message: str = self.element_search(SignUpPageLocators.PASSWORD_ERROR).text
        assert error_message == "Password can't be blank", \
            ">>> Нет сообщения о пустм поле пароля."

    def registration_new_user(self, name: str, email: str, password: str):
        """
        Регистрация нового пользователя.

        :param name: иня нового пользователя.
        :param email: електронный адресс нового пользователя.
        :param password: пароль нового пользователя.
        """
        self.type_user_name(name)
        self.type_email_address(email)
        self.type_password(password)
        self.element_search(SignUpPageLocators.BUTTON_CREATE_ACCOUNT).click()

    def type_user_name(self, name: str):
        """Ввод имени нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_USER_NAME).send_keys(name)

    def type_email_address(self, email: str):
        """Ввод електронного адреса нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_EMAIL).send_keys(email)

    def type_password(self, password: str):
        """Ввод пароль нового пользователя."""
        return self.element_search(SignUpPageLocators.FIELD_PASSWORD).send_keys(password)

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def click_sing_in(self):
        """Переход на страницу авторизации"""
        return self.element_search(MainPageLocators.BUTTON_SIGN_IN).click()

    def click_sing_up(self):
        """Переход на стрпницу регистрации"""
        return self.element_search(MainPageLocators.BUTTON_SIGN_UP).click()

    def registration(self, name: str, mail: str, password: str):
        """
        Регистрация нового пользователя

        :param name: имя нового пользователя.
        :param mail: электронный адрес нового пользователя.
        :param password: пароль нового пользоваьеля.
        """
        self.type_user_name(name)
        self.type_user_mail(mail)
        self.type_user_password(password)
        self.element_search(MainPageLocators.BUTTON_SIGN_UP_FOR).click()

    def type_user_name(self, name: str):
        """Ввод имени нового пользователя"""
        return self.element_search(MainPageLocators.FIELD_NAME).send_keys(name)

    def type_user_mail(self, mail: str):
        """Ввод электронного адреса нового пользователя"""
        return self.element_search(MainPageLocators.FIELD_EMAIL).send_keys(mail)

    def type_user_password(self, password: str):
        """Ввести пароль нового пользователя"""
        return self.element_search(MainPageLocators.FIELD_PASSWORD).send_keys(password)

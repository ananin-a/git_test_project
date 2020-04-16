from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def click_sing_in(self):
        return self.element_search(MainPageLocators.BUTTON_SIGN_IN).click()

    def click_sing_up(self):
        return self.element_search(MainPageLocators.BUTTON_SIGN_UP).click()

    def registration(self, name: str, mail: str, password: str):
        self.type_user_name(name)
        self.type_user_mail(mail)
        self.type_user_password(password)
        self.click_sing_up_for_git_hub()

    def type_user_name(self, name: str):
        return self.element_search(MainPageLocators.FIELD_NAME).send_keys(name)

    def type_user_mail(self, mail: str):
        return self.element_search(MainPageLocators.FIELD_EMAIL).send_keys(mail)

    def type_user_password(self, password: str):
        return self.element_search(MainPageLocators.FIELD_PASSWORD).send_keys(password)

    def click_sing_up_for_git_hub(self):
        return self.element_search(MainPageLocators.BUTTON_SIGN_UP_FOR).click()

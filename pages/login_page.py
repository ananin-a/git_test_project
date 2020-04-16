from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def check_title_page(self):
        title_name = self.element_search(LoginPageLocators.TITLE_PAGE).text
        assert title_name == "Sign in to GitHub", \
            ">>> "

    def should_be_incorrect_message(self):
        incorrect_message = self.element_search(LoginPageLocators.INCORRECT_MASSAGE).text
        assert incorrect_message == "Incorrect username or password", \
            ">>> "

    def invalid_log_in(self, name: str, password: str):
        self.type_user_name(name)
        self.type_password(password)
        self.click_button_sing_in()

    def type_user_name(self, name: str):
        return self.element_search(LoginPageLocators.FIELD_USER_NAME).send_keys(name)

    def type_password(self, password: str):
        return self.element_search(LoginPageLocators.FIELD_PASSWORD).send_keys(password)

    def click_button_sing_in(self):
        return self.element_search(LoginPageLocators.BUTTON_SIGN_IN).click()

    def create_an_account(self):
        return self.element_search(LoginPageLocators.CREATE_AN_ACCOUNT).click()

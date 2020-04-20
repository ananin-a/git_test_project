from .pages.login_page import LoginPage

url = "https://github.com/login"


def test_login_empty_data(browser):
    """Получение ошибки из за пустого поля логина"""
    name = ""
    password = "cb8q3475b03bf045902"

    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.log_in(name, password)
    error_message = login_page.should_be_a_message_about_incorrectly_filled_fields()
    assert error_message == "Incorrect username or password."


def test_password_empty_data(browser):
    """Получение ошиби из за пустого поля пароля."""
    name = "alex"
    password = ""

    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.log_in(name, password)
    error_message = login_page.should_be_a_message_about_incorrectly_filled_fields()
    assert error_message == "Incorrect username or password."


def test_create_an_account(browser):
    """Переход на страницу создания нового аккаунта."""
    login_page = LoginPage(browser, url)
    login_page.open()
    sign_up_page = login_page.tap_button_create_an_account(browser)
    title_message = sign_up_page.should_de_a_page_title()
    assert title_message == "Create your account"

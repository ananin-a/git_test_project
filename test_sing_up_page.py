from .pages.sign_up_page import SignUpPage

url = "https://github.com/join?source=header"


def test_title_sign_up_page(browser):
    """Проверка заголовка страницы."""
    sign_up_page = SignUpPage(browser, url)
    sign_up_page.open()
    title_test = sign_up_page.should_de_a_page_title()
    assert title_test == "Create your account"


def test_name_is_already_taken(browser):
    """Регистрация пользователя с зарезервированным именем."""
    sign_up_page = SignUpPage(browser, url)
    sign_up_page.open()
    sign_up_page.entry_user_name("username")
    error_message = sign_up_page.should_be_a_error_name_username_message()
    assert error_message == "Username 'username' is unavailable."


def test_login_busy(browser):
    """Регистрация пользователя с занятым именем."""
    sign_up_page = SignUpPage(browser, url)
    sign_up_page.open()
    sign_up_page.entry_user_name("user")
    error_message = sign_up_page.should_be_a_error_name_username_message()
    assert error_message == "Username user is not available."

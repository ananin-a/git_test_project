from .pages.main_page import MainPage

url = "https://github.com/"


def test_sign_in(browser):
    """Проверка наличия заголовка страницы регистрации."""
    main_page = MainPage(browser, url)
    main_page.open()
    login_page = main_page.click_sing_in(browser)
    page_title = login_page.should_de_a_page_title()
    assert page_title == "Sign in to GitHub"


def test_registration_fail(browser):
    """Регистация с невалидными данными нового пользователя."""
    name = "al"
    email = "al@bk.com"
    password = "112233asd"

    main_page = MainPage(browser, url)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    page_title = sign_up_page.should_de_a_page_title()
    assert page_title == "Create your account"
    error_message = sign_up_page.should_be_message_problems_create_account()
    assert error_message == "There were problems creating your account."


def test_sing_up_empty_user_name(browser):
    """Регистрация пользователя с пустым полем логина."""
    name = ""
    email = "al@bk.com"
    password = "112233asd"

    main_page = MainPage(browser, url)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    error_message = sign_up_page.should_be_a_error_name_message()
    assert error_message == "Username can't be blank"


def test_sing_up_invalid_mail(browser):
    """Регисрация пользователя с невалидным полем Email."""
    name = "al"
    email = "123"
    password = 'df7ysd87gs7'

    main_page = MainPage(browser, url)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    error_message = sign_up_page.should_be_a_error_mail_message()
    assert error_message == "Email is invalid or already taken"


def test_sign_up_wint_easy_password(browser):
    """Ввод пароля не соответствующего минимальным  требовани"""
    name = ""
    email = ""
    password = "a2345678"

    main_page = MainPage(browser, url)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    error_message = sign_up_page.should_be_a_error_password_message()
    assert error_message == "Password is weak and can be easily guessed"

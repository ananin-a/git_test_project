from .pages.main_page import MainPage


def test_sign_in(browser):
    main_page = MainPage(browser)
    main_page.open()
    login_page = main_page.click_sing_in(browser)
    page_title = login_page.should_de_a_page_title()
    assert page_title == "Sign in to GitHub"


def test_registration_fail(browser):
    name: str = "al"
    email: str = "al@bk.com"
    password: str = "112233asd"

    main_page = MainPage(browser)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    page_title = sign_up_page.should_de_a_page_title()
    assert page_title == "Create your account"
    error_message = sign_up_page.should_be_message_problems_create_account()
    assert error_message == "There were problems creating your account."


def test_sing_up_empty_user_name(browser):
    name: str = ""
    email: str = "al@bk.com"
    password: str = "112233asd"

    main_page = MainPage(browser)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    error_message = sign_up_page.should_be_a_error_name_message()
    assert error_message == "Username can't be blank"


def test_sing_up_invalid_mail(browser):
    name: str = "al"
    email: str = "123"
    password: str = '123'

    main_page = MainPage(browser)
    main_page.open()
    sign_up_page = main_page.registration(browser, name, email, password)
    error_message = sign_up_page.should_be_a_error_mail_message()
    assert error_message == "Email is invalid or already taken"

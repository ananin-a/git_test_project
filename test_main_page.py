from .pages.main_page import MainPage


def test_sign_in(browser):
    main_page = MainPage(browser)
    main_page.click_sing_in()

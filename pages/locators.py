from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    BUTTON_SIGN_IN = (By.XPATH, "//a[@href='/login']")
    BUTTON_SIGN_UP = (By.XPATH, "//a[@href='/login']/following-sibling::a")
    FIELD_NAME = (By.XPATH, "//input[@name='user[login]']")
    FIELD_EMAIL = (By.XPATH, "//input[@name='user[email]']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='user[password]']")
    BUTTON_SIGN_UP_FOR = (By.XPATH, "//button[text()='Sign up for GitHub']")


class LoginPageLocators:
    """Локаторы страницы авторизации"""
    TITLE_PAGE = (By.XPATH, "//div[@class]/h1")
    FIELD_USER_NAME = (By.XPATH, "//input[@id='login_field']")
    FIELD_PASSWORD = (By.XPATH, "//input[@id='password']")
    BUTTON_SIGN_IN = (By.XPATH, "//input[@value='Sign in']")
    INCORRECT_MASSAGE = (By.XPATH, "//div[@id='js-flash-container']")
    CREATE_AN_ACCOUNT = (By.XPATH, "//a[text()='Create an account']")


class SignUpPageLocators:
    """Локаторы страницы регистрации"""
    TITLE_PAGE = (By.XPATH, "//div[@class]/h1")
    PROBLEM_MESSAGE = (By.XPATH, "//div[@class='flash flash-error my-3']")
    NAME_ERROR = (By.XPATH, "//input[@name='user[login]']/../../following-sibling::dd")
    NAME_USERNAME = (By.XPATH, "//div[@class='mb-1 ']")
    EMAIL_ERROR = (By.XPATH, "//input[@name='user[email]']/../../following-sibling::dd")
    PASSWORD_ERROR = (By.XPATH, "//input[@name='user[password]']/../../following-sibling::dd")
    FIELD_USER_NAME = (By.XPATH, "//input[@name='user[login]']")
    FIELD_EMAIL = (By.XPATH, "//input[@name='user[email]']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='user[password]']")
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//button[@id='signup_button']")

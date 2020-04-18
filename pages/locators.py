from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    BUTTON_SIGN_IN: str = (By.XPATH, "//a[@href='/login']")
    BUTTON_SIGN_UP: str = (By.XPATH, "//a[@href='/login']/following-sibling::a")
    FIELD_NAME: str = (By.XPATH, "//input[@name='user[login]']")
    FIELD_EMAIL: str = (By.XPATH, "//input[@name='user[email]']")
    FIELD_PASSWORD: str = (By.XPATH, "//input[@name='user[password]']")
    BUTTON_SIGN_UP_FOR: str = (By.XPATH, "//button[text()='Sign up for GitHub']")


class LoginPageLocators:
    """Локаторы страницы авторизации"""
    TITLE_PAGE: str = (By.XPATH, "//div[@class]/h1")
    FIELD_USER_NAME: str = (By.XPATH, "//input[@id='login_field']")
    FIELD_PASSWORD: str = (By.XPATH, "//input[@id='password']")
    BUTTON_SIGN_IN: str = (By.XPATH, "//input[@value='Sign in']")
    INCORRECT_MASSAGE: str = (By.XPATH, "//div[@id='js-flash-container']")
    CREATE_AN_ACCOUNT: str = (By.XPATH, "//a[text()='Create an account']")


class SignUpPageLocators:
    """Локаторы страницы регистрации"""
    TITLE_PAGE: str = (By.XPATH, "//div[@class]/h1")
    PROBLEM_MESSAGE: str = (By.XPATH, "//div[@class='flash flash-error my-3']")
    NAME_ERROR: str = (By.XPATH, "//input[@name='user[login]']/../../following-sibling::dd")
    NAME_USERNAME: str = (By.XPATH, "//div[@class='mb-1 ']")
    EMAIL_ERROR: str = (By.XPATH, "//input[@name='user[email]']/../../following-sibling::dd")
    PASSWORD_ERROR: str = (By.XPATH, "//input[@name='user[password]']/../../following-sibling::dd")
    FIELD_USER_NAME: str = (By.XPATH, "//input[@name='user[login]']")
    FIELD_EMAIL: str = (By.XPATH, "//input[@name='user[email]']")
    FIELD_PASSWORD: str = (By.XPATH, "//input[@name='user[password]']")
    BUTTON_CREATE_ACCOUNT: str = (By.XPATH, "//button[@id='signup_button']")

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы страницы приветствия"""
    BUTTON_SIGN_IN: By = (By.XPATH, "//a[@href='/login']")
    BUTTON_SIGN_UP: By = (By.XPATH, "//a[@href='/login']/following-sibling::a")
    FIELD_NAME: By = (By.XPATH, "//input[@name='user[login]']")
    FIELD_EMAIL: By = (By.XPATH, "//input[@name='user[email]']")
    FIELD_PASSWORD: By = (By.XPATH, "//input[@name='user[password]']")
    BUTTON_SIGN_UP_FOR: By = (By.XPATH, "//button[text()='Sign up for GitHub']")


class LoginPageLocators:
    TITLE_PAGE: By = (By.XPATH, "//h1")
    FIELD_USER_NAME: By = (By.XPATH, "//input[@id='login_field']")
    FIELD_PASSWORD: By = (By.XPATH, "//input[@id='password']")
    BUTTON_SIGN_IN: By = (By.XPATH, "//input[@value='Sign in']")
    INCORRECT_MASSAGE: By = (By.XPATH, "//div[@id='js-flash-container']//button")
    CREATE_AN_ACCOUNT: By = (By.XPATH, "//a[text()='Create an account']")
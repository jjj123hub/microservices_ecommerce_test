from pages.base_page import BasePage
from config.settings import Config, Locators

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page.goto(Config.BASE_URL)
        
    def enter_username(self, username):
        self.fill(Locators.USERNAME_INPUT, username)
        
    def enter_password(self, password):
        self.fill(Locators.PASSWORD_INPUT, password)
        
    def click_login(self):
        self.click(Locators.LOGIN_BTN)
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def is_login_successful(self):
        return self.is_visible(Locators.PRODUCTS_TITLE)

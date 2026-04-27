import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    BASE_URL = "https://www.saucedemo.com"
    
    USER_SERVICE_URL = "http://localhost:8001"
    ORDER_SERVICE_URL = "http://localhost:8002"
    PRODUCT_SERVICE_URL = "http://localhost:8003"
    
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_USER = "root"
    DB_PASSWORD = "jlf341124"
    DB_NAME = "ecommerce"
    
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    
    PACT_MOCK_PORT = 1234
    PACT_PROVIDER_URL = "http://localhost:8001"
    
    SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")
    REPORT_DIR = os.path.join(BASE_DIR, "reports")
    PACT_DIR = os.path.join(BASE_DIR, "pacts")
    
    TEST_USERS = {
        "standard": {"username": "standard_user", "password": "secret_sauce"},
        "locked": {"username": "locked_out_user", "password": "secret_sauce"},
        "problem": {"username": "problem_user", "password": "secret_sauce"},
    }

class Locators:
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BTN = "[data-test='login-button']"
    
    PRODUCTS_TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BTN = "[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    
    CART_ITEMS = ".cart_item"
    CHECKOUT_BTN = "[data-test='checkout']"
    
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BTN = "[data-test='continue']"
    
    FINISH_BTN = "[data-test='finish']"
    COMPLETE_HEADER = ".complete-header"

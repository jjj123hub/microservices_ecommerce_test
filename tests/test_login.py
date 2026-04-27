import pytest
import allure
from config.settings import Config

@allure.feature("登录功能")
class TestLogin:
    
    @allure.story("标准用户登录")
    @allure.title("测试标准用户成功登录")
    def test_standard_user_login(self, login_page):
        user = Config.TEST_USERS["standard"]
        login_page.login(user["username"], user["password"])
        assert login_page.is_login_successful()
    
    @allure.story("锁定用户登录")
    @allure.title("测试锁定用户无法登录")
    def test_locked_user_login(self, login_page):
        user = Config.TEST_USERS["locked"]
        login_page.login(user["username"], user["password"])
        assert not login_page.is_login_successful()

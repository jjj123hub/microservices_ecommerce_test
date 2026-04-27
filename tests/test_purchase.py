import pytest
import allure
from config.settings import Config

@allure.feature("购买流程")
class TestPurchase:
    
    @allure.story("完整购买流程")
    @allure.title("测试从登录到完成购买的完整流程")
    def test_complete_purchase_flow(self, login_page, product_page, checkout_page):
        user = Config.TEST_USERS["standard"]
        
        with allure.step("登录系统"):
            login_page.login(user["username"], user["password"])
            assert login_page.is_login_successful()
        
        with allure.step("验证商品列表"):
            assert product_page.get_product_count() > 0
        
        with allure.step("添加商品到购物车"):
            product_page.add_product_to_cart(0)
            assert product_page.get_cart_badge_count() == 1
        
        with allure.step("进入购物车"):
            product_page.go_to_cart()
        
        with allure.step("验证购物车商品"):
            assert checkout_page.get_cart_item_count() == 1
        
        with allure.step("完成结账"):
            assert checkout_page.complete_checkout()

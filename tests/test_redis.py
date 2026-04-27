import pytest
import allure

@allure.feature("Redis性能优化")
class TestRedis:
    
    @allure.story("Hot Key检测")
    @allure.title("测试检测Redis热点Key")
    def test_detect_hot_keys(self, redis_helper):
        hot_keys = redis_helper.get_hot_keys()
        assert isinstance(hot_keys, list)
        for key_info in hot_keys:
            assert "key" in key_info
            assert "ttl" in key_info
    
    @allure.story("缓存操作")
    @allure.title("测试Redis读写操作")
    def test_cache_operations(self, redis_helper):
        test_key = "test:product:1"
        test_value = '{"id": 1, "name": "Test Product", "price": 99.99}'
        
        redis_helper.set(test_key, test_value, ex=3600)
        result = redis_helper.get(test_key)
        
        assert result == test_value
        
        redis_helper.delete(test_key)
        assert redis_helper.get(test_key) is None

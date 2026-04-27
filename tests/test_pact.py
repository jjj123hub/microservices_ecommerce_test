import pytest
import allure
import requests

@allure.feature("契约测试")
class TestContract:
    
    @allure.story("用户服务契约")
    @allure.title("测试用户服务API契约")
    def test_user_service_contract(self, pact_consumer):
        expected = {
            "username": "testuser",
            "email": "test@example.com",
            "id": 123
        }
        
        (pact_consumer
         .given("a user with id 123 exists")
         .upon_receiving("a request for user 123")
         .with_request(method="GET", path="/users/123")
         .will_respond_with(
             status=200,
             headers={"Content-Type": "application/json"},
             body=expected
         ))
        
        with pact_consumer:
            response = requests.get(f"{pact_consumer.uri}/users/123")
            assert response.status_code == 200
            assert response.json() == expected

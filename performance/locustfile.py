from locust import HttpUser, task, between, constant
import random

class EcommerceUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.client.post("/login", json={
            "username": "standard_user",
            "password": "secret_sauce"
        })
    
    @task(3)
    def view_products(self):
        self.client.get("/products")
    
    @task(2)
    def add_to_cart(self):
        product_id = random.randint(1, 6)
        self.client.post(f"/cart/add/{product_id}")
    
    @task(1)
    def checkout(self):
        self.client.post("/checkout", json={
            "firstName": "Test",
            "lastName": "User",
            "postalCode": "12345"
        })

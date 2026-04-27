from pages.base_page import BasePage
from config.settings import Locators
from faker import Faker

fake = Faker()

class CheckoutPage(BasePage):
    def get_cart_item_count(self):
        return self.page.locator(Locators.CART_ITEMS).count()
        
    def click_checkout(self):
        self.click(Locators.CHECKOUT_BTN)
        
    def fill_shipping_info(self, first_name=None, last_name=None, postal_code=None):
        self.fill(Locators.FIRST_NAME_INPUT, first_name or fake.first_name())
        self.fill(Locators.LAST_NAME_INPUT, last_name or fake.last_name())
        self.fill(Locators.POSTAL_CODE_INPUT, postal_code or fake.zipcode())
        
    def click_continue(self):
        self.click(Locators.CONTINUE_BTN)
        
    def click_finish(self):
        self.click(Locators.FINISH_BTN)
        
    def is_order_complete(self):
        return self.is_visible(Locators.COMPLETE_HEADER)
        
    def complete_checkout(self):
        self.click_checkout()
        self.fill_shipping_info()
        self.click_continue()
        self.click_finish()
        return self.is_order_complete()

from pages.base_page import BasePage
from config.settings import Locators

class ProductPage(BasePage):
    def get_product_count(self):
        return self.page.locator(Locators.INVENTORY_ITEM).count()
        
    def add_product_to_cart(self, index=0):
        add_buttons = self.page.locator(Locators.ADD_TO_CART_BTN)
        add_buttons.nth(index).click()
        
    def get_cart_badge_count(self):
        if self.is_visible(Locators.CART_BADGE):
            return int(self.get_text(Locators.CART_BADGE))
        return 0
        
    def go_to_cart(self):
        self.click(Locators.CART_LINK)

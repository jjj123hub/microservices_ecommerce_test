from playwright.sync_api import Page, expect
from config.settings import Config
import os
import time

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate(self, url):
        self.page.goto(url)
        
    def fill(self, locator, value):
        self.page.fill(locator, value)
        
    def click(self, locator):
        self.page.click(locator)
        
    def get_text(self, locator):
        return self.page.inner_text(locator)
        
    def is_visible(self, locator):
        return self.page.is_visible(locator)
        
    def wait_for_visible(self, locator, timeout=10000):
        self.page.wait_for_selector(locator, timeout=timeout)
        
    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(Config.SCREENSHOT_DIR, f"{name}_{timestamp}.png")
        os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
        self.page.screenshot(path=screenshot_path)
        return screenshot_path
        
    def expect_element_to_be_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()
        
    def expect_text_to_contain(self, locator, text):
        expect(self.page.locator(locator)).to_contain_text(text)

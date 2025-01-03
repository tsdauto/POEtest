# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
import os

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 60)

    def take_screenshot(self, name):
        """Take screenshot for debugging"""
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(f"screenshots/{name}.png")
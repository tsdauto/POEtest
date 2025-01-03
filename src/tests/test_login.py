# tests/test_login.py
from cgitb import reset
from datetime import datetime

import allure


def generate_screenshot_name(context):
    """Generate unique screenshot filename"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"login_{context}_{timestamp}"


@allure.title("Login")
class TestLogin:
    def test_open_page(self, login_page):
        result = login_page.open()

        assert "DGS" in result, "Login Error"

    def test_switch_to_main_frame(self, login_page):
        result = login_page.switch_to_main_frame()

        assert result == True, "failed to switch to main frame"

    def test_valid_login(self, login_page):
        result = login_page.login("admin", "password")

        assert result == True, "failed to login"

    def test_login_check(self, login_page):
        result = login_page.is_login_successful()

        assert result == True, "failed to check login information"

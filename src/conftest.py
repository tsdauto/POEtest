# conftest.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope="session")
def config():
    """Global test configuration"""
    return {
        "base_url": os.getenv("TEST_BASE_URL", "http://10.90.90.90"),
        "implicit_wait": 40,
        "screenshot_dir": "screenshots"
    }

@pytest.fixture(scope="class")
def driver(config):
    """WebDriver fixture for browser automation"""

    # printing information to console

    print("\n\n initializing webdriver")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        options=chrome_options
    )
    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    # printing tear down information to console

    print("\n\n tearing down webdriver")

    driver.quit()

@pytest.fixture(scope="function")
def login_page(driver, config):
    """Login page fixture"""
    from pages.login_page import LoginPage
    return LoginPage(driver, config["base_url"])
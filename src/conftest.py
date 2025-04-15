# conftest.py
import sys
from dotenv import load_dotenv
import os

load_dotenv('Settings.env')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope="session")
def config():
    """Global test configuration"""
    return {
        "base_url": os.getenv("TEST_BASE_URL", "http://10.90.90.90"),
        "implicit_wait": 40,
        "screenshot_dir": "screenshots",
        "model_name": "DGS-1210-10XS",
        "screen_width": "1920",
        "screen_height": "1080",
        "device_information": {
            "device_type": {
                "type": "string",
                "title": "Device Type",
                "expected_value": "DGS-1210-10XS/ME Management Switch"
            },
            "system_time": {
                "type": "regexp",
                "title": "System Time",
                "expected_value": r"(\d{2}):(\d{2}):(\d{2}) (\d{2}) (\d{2}) (\d{4})"
            },
            "system_name": {
                "type": "string",
                "title": "System Name",
                "expected_value": "DGS-1210-10XS/ME"
            },
            "system_up_time": {
                "type": "regexp",
                "title": "System Up Time",
                "expected_value": r"^(\d+)\s*days,\s*(\d{0,2})\s*hours,\s*(\d{0,2})\s*mins,\s*(\d{0,2})\s*seconds$"
            },
            "system_location": {
                "type": "string",
                "title": "System Location",
                "expected_value": ""
            },
            "mac_address": {
                "type": "regexp",
                "title": "MAC Address",
                "expected_value": r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$"
            },
            "system_contact": {
                "type": "string",
                "title": "System Contact",
                "expected_value": ""
            },
            "ip_address": {
                "type": "string",
                "title": "IP Address",
                "expected_value": os.getenv("SWITCH_IP_ADDRESS")
            },
            "boot_version": {
                "type": "string",
                "title": "Boot Version",
                "expected_value": os.getenv("BOOT_VERSION", "1.00.006")
            },
            "subnet_mask": {
                "type": "string",
                "title": "Subnet Mask",
                "expected_value": os.getenv("SUBNET_MASK", "255.0.0.0")
            },
            "firmware_version": {
                "type": "string",
                "title": "Firmware Version",
                "expected_value": os.getenv("FIRMWARE_VERSION")
            },
            "hardware_version": {
                "type": "string",
                "title": "Hardware Version",
                "expected_value": os.getenv("HARDWARE_VERSION")
            },
            "default_gateway": {
                "type": "string",
                "title": "Default Gateway",
                "expected_value": "0.0.0.0"
            },
            "serial_number": {
                "type": "string",
                "title": "Serial Number",
                "expected_value": os.getenv("SERIAL_NUMBER", "QQDMS12345600")
            },
            "login_timeout": {
                "type": "string",
                "title": " Login Timeout  (minutes)",
                "expected_value": os.getenv("LOGIN_TIMEOUT", "3")
            },
            "stp": {
                "type": "string",
                "title": "STP",
                "expected_value": "Disabled"
            },
            "snmp_status": {
                "type": "string",
                "title": "SNMP Status",
                "expected_value": "Disabled"
            },
            "port_mirroring": {
                "type": "string",
                "title": "Port Mirroring",
                "expected_value": "Disabled"
            },
            "dot1x_status": {
                "type": "string",
                "title": "802.1X Status",
                "expected_value": "Disabled"
            },
            "igmp_snooping": {
                "type": "string",
                "title": "IGMP Snooping",
                "expected_value": "Disabled"
            },
            "safeguard_engine": {
                "type": "string",
                "title": "Safeguard Engine",
                "expected_value": " Enabled"
            },
            "dhcp_client": {
                "type": "string",
                "title": "DHCP Client",
                "expected_value": "Disabled"
            },
            "jumbo_frame": {
                "type": "string",
                "title": "Jumbo Frame",
                "expected_value": "Disabled"
            },
            "power_saving": {
                "type": "string",
                "title": "Power Saving",
                "expected_value": "Disabled"
            }

        },
        "username": "admin", # login username
        "password": "admin", # login password
}
    


@pytest.fixture(scope="session")
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

    driver.set_window_size(config["screen_width"], config["screen_height"])
    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    # printing tear down information to console

    print("\n\n tearing down webdriver")

    driver.quit()


@pytest.fixture(scope="class")
def login_page(driver, config):
    """Login page fixture"""
    print("\n\n initializing login page")

    from .pages.LoginPage import LoginPage

    yield LoginPage(driver, config["base_url"])

    print("\n\n tearing down login page")


@pytest.fixture(scope="class")
def logged_driver(driver, config):
    """
    accept global driver object to log them in,
    then return driver which is logged in.
    :param driver:
    :param config:
    :return:driver
    """
    print("\n\n initializing logged driver")
    from .pages.LoginPage import LoginPage
    login_driver = LoginPage(driver, config["base_url"])
    login_driver.do_login(config["username"], config["password"])
    yield driver
    print("\n\n tearing down logged driver")




@pytest.fixture(scope="class")
def device_information_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing device info page")
    from .pages.DeviceInformationPage import DeviceInformationPage
    yield DeviceInformationPage(logged_driver, config["base_url"])
    print("\n\n tearing down device info page")


@pytest.fixture(scope="class")
def system_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing system settings page")
    from .pages.SystemSettingsPage import SystemSettingsPage
    __system_setting_page = SystemSettingsPage(logged_driver, config["base_url"])
    __system_setting_page.collapse_system_menu_then_click_system_settings()
    yield __system_setting_page
    print("\n\n tearing down system settings page")

# 4
@pytest.fixture(scope="class")
def firmware_information_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing firmware information page")
    from .pages.FirmwareInformationPage import FirmwareInformationPage
    __firmware_information_page = FirmwareInformationPage(logged_driver, config["base_url"])
    yield __firmware_information_page
    print("\n\n tearing down firmware information page")

# 5
@pytest.fixture(scope="class")
def serial_port_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing serial port settings page")
    from .pages.SerialPortSettingsPage import SerialPortSettingsPage
    __page = SerialPortSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down serial port settings page")

# 6
@pytest.fixture(scope="class")
def ip_interface_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ip_interface_page")
    from .pages.IPInterfacePage import IPInterfacePage
    __page = IPInterfacePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ip_interface_page")

# 7
@pytest.fixture(scope="class")
def ipv6_system_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ipv6_system_settings_page")
    from .pages.IPv6SystemSettingsPage import IPv6SystemSettingsPage
    __page = IPv6SystemSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ipv6_system_settings_page")

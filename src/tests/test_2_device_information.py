# tests/test_2_device_information.py
import sys
import os
import allure
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from pages.DeviceInformationPage import DeviceInformationPage

from mixins.TestUtils import ValueCheckMixins


@allure.title("DeviceInformation")
class TestDeviceInformation(ValueCheckMixins):
    def test_check_device_type_title(self, device_information_page, config):
        device_type_title, _ = device_information_page.get_device_type()

        assert device_type_title == config["device_information"]["device_type"]["title"], 'false'

    def test_check_device_type_value(self, device_information_page, config):
        _, device_type = device_information_page.get_device_type()

        assert device_type == config["device_information"]["device_type"]["expected_value"], 'false'

    def test_check_system_time_title(self, device_information_page, config):
        system_time_title, _ = device_information_page.get_system_time()

        assert system_time_title == config["device_information"]["system_time"]["title"], 'false'

    def test_check_system_time_value(self, device_information_page, config):
        _, value = device_information_page.get_system_time()

        value_result = self.check_value(config["device_information"]["system_time"], value)

        assert value_result, "system time value test failed"

    def test_check_system_name(self, device_information_page, config):
        title, value = device_information_page.get_system_name()
        title_result = self.check_title(config["device_information"]["system_name"], title)
        value_result = self.check_value(config["device_information"]["system_name"], value)
        assert title_result, "system name title test failed"
        assert value_result, "system name value test failed"

    def test_check_system_up_time(self, device_information_page, config):
        title, value = device_information_page.get_system_up_time()
        title_result = self.check_title(config["device_information"]["system_up_time"], title)
        value_result = self.check_value(config["device_information"]["system_up_time"], value)
        assert title_result, "system up time title test failed"
        assert value_result, "system up time value test failed"

    def test_check_system_location(self, device_information_page, config):
        title, value = device_information_page.get_system_location()
        title_result = self.check_title(config["device_information"]["system_location"], title)
        value_result = self.check_value(config["device_information"]["system_location"], value)
        assert title_result, "system location title test failed"
        assert value_result, "system location value test failed"

    def test_check_mac_address(self, device_information_page, config):
        title, value = device_information_page.get_mac_address()
        title_result = self.check_title(config["device_information"]["mac_address"], title)
        value_result = self.check_value(config["device_information"]["mac_address"], value)
        assert title_result, "mac address title test failed"
        assert value_result, "mac address value test failed"

    def test_check_system_contact(self, device_information_page, config):
        title, value = device_information_page.get_system_contact()
        title_result = self.check_title(config["device_information"]["system_contact"], title)
        value_result = self.check_value(config["device_information"]["system_contact"], value)
        assert title_result, "system contact title test failed"
        assert value_result, "system contact value test failed"

    def test_check_ip_address(self, device_information_page, config):
        title, value = device_information_page.get_ip_address()
        title_result = self.check_title(config["device_information"]["ip_address"], title)
        value_result = self.check_value(config["device_information"]["ip_address"], value)
        assert title_result, "IP address title test failed"
        assert value_result, "IP address value test failed"

    def test_check_boot_version(self, device_information_page, config):
        title, value = device_information_page.get_boot_version()
        title_result = self.check_title(config["device_information"]["boot_version"], title)
        value_result = self.check_value(config["device_information"]["boot_version"], value)
        assert title_result, "boot version title test failed"
        assert value_result, "boot version value test failed"

    def test_check_subnet_mask(self, device_information_page, config):
        title, value = device_information_page.get_subnet_mask()
        title_result = self.check_title(config["device_information"]["subnet_mask"], title)
        value_result = self.check_value(config["device_information"]["subnet_mask"], value)
        assert title_result, "subnet mask title test failed"
        assert value_result, "subnet mask value test failed"

    def test_check_firmware_version(self, device_information_page, config):
        title, value = device_information_page.get_firmware_version()
        title_result = self.check_title(config["device_information"]["firmware_version"], title)
        value_result = self.check_value(config["device_information"]["firmware_version"], value)
        assert title_result, "firmware version title test failed"
        assert value_result, "firmware version value test failed"

    def test_check_hardware_version(self, device_information_page, config):
        title, value = device_information_page.get_hardware_version()
        title_result = self.check_title(config["device_information"]["hardware_version"], title)
        value_result = self.check_value(config["device_information"]["hardware_version"], value)
        assert title_result, "hardware version title test failed"
        assert value_result, "hardware version value test failed"

    def test_check_default_gateway(self, device_information_page, config):
        title, value = device_information_page.get_default_gateway()
        title_result = self.check_title(config["device_information"]["default_gateway"], title)
        value_result = self.check_value(config["device_information"]["default_gateway"], value)
        assert title_result, "default gateway title test failed"
        assert value_result, "default gateway value test failed"

    def test_check_serial_number(self, device_information_page, config):
        title, value = device_information_page.get_serial_number()
        title_result = self.check_title(config["device_information"]["serial_number"], title)
        value_result = self.check_value(config["device_information"]["serial_number"], value)
        assert title_result, "serial number title test failed"
        assert value_result, "serial number value test failed"

    def test_check_login_timeout(self, device_information_page, config):
        title, value = device_information_page.get_login_timeout()
        title_result = self.check_title(config["device_information"]["login_timeout"], title)
        value_result = self.check_value(config["device_information"]["login_timeout"], value)
        assert title_result, "login timeout title test failed"
        assert value_result, "login timeout value test failed"



# tests/test_6_ip_interface.py

import allure
import pytest


@allure.title("IPInterface")
class TestIPInterfaceUI:
    def test_collapse_system_menu_then_click_serial_port_settings(self, ip_interface_page):
        res = ip_interface_page.init()
        assert res, "error while init ip_interface_page"

    def test_check_header_is_correct(self, ip_interface_page):
        res = ip_interface_page.get_page_header_text()
        expected_val = "IP Interface Settings"

        assert expected_val == res, "header is not correct"

    def test_check_tier2_header_is_correct(self, ip_interface_page):
        res = ip_interface_page.get_tier2_header_text()
        expected_val = "IP Interface Settings"

        assert expected_val == res, "header is not correct"

    def test_check_ip_config_mode_options(self, ip_interface_page):
        option_one = ip_interface_page.get_ip_config_option_one_text()
        option_two = ip_interface_page.get_ip_config_option_two_text()
        expected_val_one = "Static"
        expected_val_two = "DHCP"

        assert expected_val_one == option_one, "ip config option one is not correct"
        assert expected_val_two == option_two, "ip config option two is not correct"

    def check_default_ip_mode_is_static(self, ip_interface_page):
        opt = ip_interface_page.get_checked_ip_mode_option()
        expected_val = "Static"

        assert expected_val == opt, "default ip mode is not static"

    def test_check_interface_name(self, ip_interface_page):
        title, value = ip_interface_page.get_interface_name()
        expected_title = "Interface Name"
        expected_value = ""
        assert expected_title == title
        assert expected_value == value

    def test_check_vlan_name(self, ip_interface_page):
        title, value = ip_interface_page.get_vlan_name()
        expected_title = "VLAN Name"
        expected_value = ""
        assert expected_title == title
        assert expected_value == value

    def test_check_ipv4_address(self, ip_interface_page):
        title, value = ip_interface_page.get_ipv4_address()
        expected_title = "IPv4 Address"
        expected_value = "..."
        assert expected_title == title
        assert expected_value == value

    def test_check_netmask(self, ip_interface_page):
        title, value = ip_interface_page.get_netmask()
        expected_title = "Netmask"
        expected_value = "24 (255.255.255.0)"
        assert expected_title == title
        assert expected_value == value

    def test_check_interface_admin_state(self, ip_interface_page):
        title, value = ip_interface_page.get_interface_admin_state()
        expected_title = "Interface Admin State"
        expected_value = "Enabled"
        assert expected_title == title
        assert expected_value == value

    def test_check_maximum_entries_text(self, ip_interface_page):
        result = ip_interface_page.get_maximum_entries()
        expected_value = "Maximum 4 entries."
        assert expected_value == result

    def test_check_table_title(self, ip_interface_page):
        result = ip_interface_page.get_table_title()
        expected_title = ["Interface Name", "VLAN Name", "IP State", "IPv4 Address", "Netmask", "Admin State", "Link State", "IPv6", "Edit", "Delete"]

        assert expected_title == result


# TODO: IPv6 Interface Settings

# TODO: IP Interface Settings

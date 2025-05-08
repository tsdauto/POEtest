# test_10_dhcp_auto_configuration.py

import allure
import pytest




@allure.title("dhcp_auto_configuration")
class TestDHCPAutoConfiguration:

    def test_check_header(self, dhcp_auto_configuration_page):
        result = dhcp_auto_configuration_page.get_page_header_text()
        expected_val = "DHCP Auto Configuration"

        assert expected_val == result

    def test_check_dhcp_auto_configuration_tier2_header(self, dhcp_auto_configuration_page):
        result = dhcp_auto_configuration_page.get_dhcp_auto_configuration_tier2_header_text()
        expected_val = "DHCP Auto Configuration"

        assert expected_val == result

    def test_check_auto_configuration_title(self, dhcp_auto_configuration_page):
        result = dhcp_auto_configuration_page.get_auto_configuration_title_text()
        expected_val = "Auto Configuration State"

        assert expected_val == result

    def test_check_ip_config_mode_options(self, dhcp_auto_configuration_page):
        option_one = dhcp_auto_configuration_page.get_auto_configuration_State_option_one_text()
        option_two = dhcp_auto_configuration_page.get_auto_configuration_State_option_two_text()
        expected_val_one = "Enabled"
        expected_val_two = "Disabled"

        assert expected_val_one == option_one, "auto_configuration option one is not correct"
        assert expected_val_two == option_two, "auto_configuration option two is not correct"

    def test_default_configuration_state_mode_is_disabled(self, dhcp_auto_configuration_page):
        opt = dhcp_auto_configuration_page.get_checked_config_state_mode_option()
        expected_val = "Disabled"

        assert expected_val == opt, "default configuration state mode is not Disabled"

    def test_check_timeout_title_and_value(self, dhcp_auto_configuration_page):
        title, value = dhcp_auto_configuration_page.get_timeout_title_and_value()
        expected_title = "Timeout (1-65535)"
        expected_val = "50"

        assert expected_title == title
        assert expected_val == value

    def test_check_dhcp_auto_configuration_button(self, dhcp_auto_configuration_page):
        result = dhcp_auto_configuration_page.get_dhcp_auto_configuration_button_value()
        expected_result = "Apply"

        assert expected_result == result

    def test_check_auto_configuration_note(self, dhcp_auto_configuration_page):
        result1, result2, result3 = dhcp_auto_configuration_page.get_auto_configuration_note_text()
        expected_val1 = "The DHCP autoconfiguration function on the switch will load a previously saved configuration file for current use."
        expected_val2 = "Note:"
        expected_val3 = "If the switch is unable to complete the autoconfiguration process, the previously saved local configuration file present in switch memory will be loaded."

        assert expected_val1 == result1
        assert expected_val2 == result2
        assert expected_val3 == result3

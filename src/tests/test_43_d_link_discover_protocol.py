# test_43_dlink_discover_protocol.py

import allure
import pytest


@allure.title("dlink_discover_protocol.ddp_global_settings")
class TestDDPGlobalSettings:

    def test_check_header(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_page_header_text()
        expected_val = "D-Link Discover Protocol"

        assert expected_val == result

    def test_check_ddp_global_settings_title(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_ddp_global_settings_title()
        expected_val = "DDP Global Settings"

        assert expected_val == result

    def test_check_d_link_discover_protocol_state_title(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_protocol_state_title()
        expected_val = "D-Link Discover Protocol State"

        assert expected_val == result

    def test_check_d_link_discover_protocol_state_option_one(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_protocol_state_option_one()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_d_link_discover_protocol_state_option_two(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_protocol_state_option_two()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_d_link_discover_protocol_state_is_disabled(self, dlink_discover_protocol_page):
        opt = dlink_discover_protocol_page.get_checked_d_link_discover_protocol_state_option()
        expected_val = "Disabled"

        assert expected_val == opt, "default d-link discover protocol state is not Disabled"

    def test_check_d_link_discover_report_state_title(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_report_state_title()
        expected_val = "D-Link Discover Report State"

        assert expected_val == result

    def test_check_d_link_discover_report_state_option_one(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_report_state_option_one()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_d_link_discover_report_state_option_two(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_d_link_discover_report_state_option_two()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_d_link_discover_report_state_is_disabled(self, dlink_discover_protocol_page):
        opt = dlink_discover_protocol_page.get_checked_d_link_discover_report_state_option()
        expected_val = "Disabled"

        assert expected_val == opt, "default d-link discover report state is not Disabled"

    def test_check_d_link_discover_protocol_report_timer_title_and_value(self, dlink_discover_protocol_page):
        title, value = dlink_discover_protocol_page.get_d_link_discover_protocol_report_timer_title_and_value()
        expected_title = "D-Link Discover Protocol Report Timer (0-120 Seconds)"
        expected_val = "Never"

        assert expected_title == title
        assert expected_val == value

    def test_check_ddp_global_settings_button_text(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_ddp_global_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("dlink_discover_protocol.DDP Port Settings")
class TestDDPPortSettings:

    def test_check_ddp_port_settings_header(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_ddp_port_settings_header()
        expected_val = "DDP Port Settings"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, dlink_discover_protocol_page):
        title, value = dlink_discover_protocol_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, dlink_discover_protocol_page):
        title, value = dlink_discover_protocol_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, dlink_discover_protocol_page):
        title, value = dlink_discover_protocol_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Enabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_ddp_port_settings_button_text(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_ddp_port_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_table_title(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_table_title()
        expected_val = ["Port", "State"]

        assert expected_val == result

    def test_check_port1_table_value(self, dlink_discover_protocol_page):
        result = dlink_discover_protocol_page.get_port1_table_value()
        expected_val = ["1", "Disabled"]

        assert expected_val == result

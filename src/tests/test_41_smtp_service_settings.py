# test_41_smtp_service_settings.py

import allure
import pytest

from ..utils.all_exist_in_order import all_exist_in_order


@allure.title("smtp_service_settings.smtp_service_settings")
class TestSMTPserviceSettings:

    def test_check_header(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_page_header_text()
        expected_val = "SMTP Server Settings"

        assert expected_val == result

    def test_check_smtp_service_settings_tier2_header(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_smtp_service_settings_tier2_header_text()
        expected_val = "SMTP Service Settings"

        assert expected_val == result

    def test_check_smtp_state_title(self, smtp_service_settings_page):
        title = smtp_service_settings_page.get_smtp_state_title_text()
        expected_title = "SMTP State"

        assert expected_title == title

    def test_check_smtp_state_option_one(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_smtp_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_smtp_state_option_two(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_smtp_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_smtp_state_is_disabled(self, smtp_service_settings_page):
        opt = smtp_service_settings_page.get_checked_smtp_state_option()
        expected_val = "Disabled"

        assert expected_val == opt, "default smtp state is not Disabled"

    def test_check_smtp_server_address_title(self, smtp_service_settings_page):
        title = smtp_service_settings_page.get_smtp_server_address_title_text()
        expected_title = "SMTP Server Address"

        assert expected_title == title

    def test_check_ipv4_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_ipv4_title_and_value()
        expected_title = "IPv4"
        expected_val = "..."

        assert expected_title == title
        assert expected_val == value

    def test_check_ipv6_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_ipv6_title_and_value()
        expected_title = "IPv6"
        expected_val = "::"

        assert expected_title == title
        assert expected_val == value

    def test_check_v4_mode_default_options(self, smtp_service_settings_page):
        assert smtp_service_settings_page.get_checked_v4_mode_option() is False

    def test_check_v6_mode_default_options(self, smtp_service_settings_page):
        assert smtp_service_settings_page.get_checked_v6_mode_option() is True

    def test_check_domain_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_domain_title_and_value()
        expected_title = "Domain"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_domain_mode_default_options(self, smtp_service_settings_page):
        assert smtp_service_settings_page.get_checked_domain_mode_option() is False

    def test_check_self_mail_address_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_self_mail_address_title_and_value()
        expected_title = "Self Mail Address"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_self_mail_address_key_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_self_mail_address_key_title_and_value()
        expected_title = "Self Mail Address key"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_smtp_server_port_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_smtp_server_port_title_and_value()
        expected_title = "SMTP Server Port (1-65535)"
        expected_val = "25"

        assert expected_title == title
        assert expected_val == value

    def test_check_smtp_service_settings_button_text(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_smtp_service_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("smtp_service_settings.mail_receiver_address")
class TestMailReceiverAddress:

    def test_check_mail_receiver_address_header(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_mail_receiver_address_header()
        expected_val = "Mail Receiver Address"

        assert expected_val == result

    def test_check_mail_receiver_address_title_and_value(self, smtp_service_settings_page):
        title, value = smtp_service_settings_page.get_mail_receiver_address_title_and_value()
        expected_title = "Mail Receiver Address"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_mail_receiver_address_button_text(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_mail_receiver_address_button_text()
        expected_val = "Add"

        assert expected_val == result


@allure.title("smtp_service_settings.mail_receiver_address_table")
class TestMailReceiverAddressTable:

    def test_check_mail_receiver_address_table_header(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_mail_receiver_address_table_header()
        expected_val = "Mail Receiver Address Table"

        assert expected_val == result

    def test_check_total_entries_title(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_total_entries_title()
        expected_val = "Maximum Entries : 8,  Total Entries : 0"

        assert expected_val == result

    def test_check_table_title(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_table_title()
        expected_val = ["Index", "Mail Receiver Address", "Delete"]

        assert expected_val == result

    def test_check_table_empty(self, smtp_service_settings_page):
        result = smtp_service_settings_page.get_table_default_is_empty()

        assert result

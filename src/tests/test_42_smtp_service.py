# test_42_smtp_service.py

import allure
import pytest
import asyncio

from ..utils.all_exist_in_order import all_exist_in_order


@allure.title("smtp_service")
class TestSMTPservice:

    def test_check_header(self, smtp_service_page):
        result = smtp_service_page.get_page_header_text()
        expected_val = "SMTP Service"

        assert expected_val == result

    def test_check_smtp_service_settings_tier2_header(self, smtp_service_page):
        result = smtp_service_page.get_smtp_service_settings_tier2_header_text()
        expected_val = "SMTP Mail Service"

        assert expected_val == result

    def test_check_subject_title_and_value(self, smtp_service_page):
        title, value = smtp_service_page.get_subject_title_and_value()
        expected_title = "Subject"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_content_title_and_value(self, smtp_service_page):
        title, value = smtp_service_page.get_content_title_and_value()
        expected_title = "Content"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, smtp_service_page):
        result = smtp_service_page.get_button_text()
        expected_val = "Send"

        assert expected_val == result

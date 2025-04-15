# test_7_ipv6_system_settings.py
import time
import allure
import sys
import os
import pytest
import asyncio

from ..utils.all_exist_in_order import all_exist_in_order


@allure.title("ipv6_system_settings.interface_settings")
class TestIPv6SystemSettings:

    def test_check_header(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_page_header_text()
        expected_val = "IPv6 System Settings"

        assert expected_val == result

    def test_check_v6_settings_tier2_header(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_v6_settings_tier2_header_text()
        expected_val = "IPv6 Interface Settings"

        assert expected_val == result

    def test_check_interface_name_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_interface_name_title_and_value()
        expected_title = "Interface Name"
        expected_val = "System"

        assert expected_title == title
        assert expected_val == value

    def test_check_ipv6_state_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_ipv6_state_title_and_value()
        expected_title = "IPv6 State"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_interface_admin_state_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_interface_admin_state_title_and_value()
        expected_title = "Interface Admin State"
        expected_val = "Enabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_v6_network_address_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_v6_network_address_title_and_value()
        expected_title = "IPv6 Network Address(e.g.: 3710::1/64)"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_dhcp_v6_client_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_dhcp_v6_client_title_and_value()
        expected_title = "DHCPv6 Client"
        expected_val = "Disabled"

        assert expected_title == title
        assert expected_val == value

@allure.title("ipv6_system_settings.ns_retransmit_time_settings")
class TestNSRetransmitTimeSettings:

    def test_check_ns_retransmit_header(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_ns_retransmit_time_header_text()
        expected_val = "NS Retransmit Time Settings"

        assert expected_val == result

    def test_check_ns_retransmit_time_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_ns_retransmit_time_title_and_value()
        expected_title = "NS Retransmit Time (1-3600)"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

class TestAutomaticLinkLocalStateSettings:

    def test_check_automatic_link_local_state_header(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_automatic_link_local_state_header_text()
        expected_val = "Automatic Link Local State Settings"

        assert expected_val == result

    def test_check_automatic_link_local_state_title_and_value(self, ipv6_system_settings_page):
        title, value = ipv6_system_settings_page.get_automatic_link_local_state_title_and_value()
        expected_title = "Automatic Link Local Address"
        expected_val = "Enabled"

        assert expected_title == title
        assert expected_val == value

class TestViewAllIPv6Address:
    def test_check_view_all_ipv6_address_header(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_view_all_ipv6_address_header_text()
        expected_val = "View All IPv6 Address"

        assert expected_val == result

    def test_check_table_title(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_table_title()
        expected_val = ["Address Type", "IPv6 Address", "Delete"]

        assert expected_val == result

    def test_check_table_default_is_empty(self, ipv6_system_settings_page):
        result = ipv6_system_settings_page.get_table_default_is_empty()

        assert result
    
    @pytest.mark.asyncio
    async def test_test(self, serial_port_env):
        from ..command.usecases.Dot1v import run as run_dot1v
        
        async def api_call_task(serial_env):
            """ 模擬持續的 API 調用 """
            if not serial_env.running:  # 如果串口已關閉，退出
                return
            run_dot1v(serial_env)  # 透過 API 發送命令
        

            print("📡 API sent: api_call_end")
            
        # input_task = asyncio.create_task(serial_port_env.user_input_loop())
        api_task = asyncio.create_task(api_call_task(serial_port_env))
        
        # await input_task
        
        assert True


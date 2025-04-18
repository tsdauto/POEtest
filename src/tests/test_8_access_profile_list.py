# test_8_Access_Profile_List.py
import time
import allure
import pytest

from ..utils.all_exist_in_order import all_exist_in_order

@allure.title("access_profile_list")
class TestAccessProfileList:

    """@pytest.mark.asyncio
    def test_reboot_test(self, serial_env):
        from ..command.usecases.ResetThenLogin import run as run_reset_then_login
        from ..command.usecases.ACL import run
        run(serial_env)
        assert True"""

    def test_check_header(self, access_profile_list_page):
        result = access_profile_list_page.get_page_header_text()
        expected_val = "Access Profile List"

        assert expected_val == result

    def test_check_ACL_Profile_List_tier2_header(self, access_profile_list_page):
        result = access_profile_list_page.get_ACL_Profile_List_tier2_header_text()
        expected_val = "Access Profile List"

        assert expected_val == result

    def test_check_ACL_Profile_button1_text(self, access_profile_list_page):
        result = access_profile_list_page.get_ACL_Profile_button1_text()
        expected_val = "Add ACL Profile"

        assert expected_val == result
        
    def test_check_ACL_Profile_button2_text(self, access_profile_list_page):
        result = access_profile_list_page.get_ACL_Profile_button2_text()
        expected_val = "Delete All"

        assert expected_val == result
    
    def test_check_table_title(self, access_profile_list_page):
        result = access_profile_list_page.get_table_title()
        expected_val = ["Profile ID", "Owner Type", "Profile Summary", "Action", "Action", "Action"]

        assert expected_val == result

    def test_check_ACL_Profile_table_total_text(self, access_profile_list_page):
        result = access_profile_list_page.get_ACL_Profile_table_total_text()
        expected_val = "Current/Max. Profile: 0/6, Current/Max. Rule: 0/768"

        assert expected_val == result
        
    @pytest.mark.ui
    def test_check_table_default_is_empty(self, access_profile_list_page):
        result = access_profile_list_page.get_table_default_is_empty()

        assert result
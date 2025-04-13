# tests/test4_firmware_information.py
import time
import allure
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.all_exist_in_order import all_exist_in_order
from mixins.TestUtils import ValueCheckMixins


@allure.title("Firmware Information")
class TestFirmwareInformation():
    def test_collapse_system_menu_then_click_system_settings(self, firmware_information_page):
        res = firmware_information_page.init()
        assert res, "error while init firmware information"

    def test_check_firmware_information_table_title(self, firmware_information_page):
        title_cells = firmware_information_page.get_firmware_information_table_title()
        expected_titles = ["ID", "Version", "Size(B)", "Update Time", "From", "User"]

        assert expected_titles == title_cells

    def test_check_select_prompt_text(self, firmware_information_page):
        select_prompt_text = firmware_information_page.get_selected_input_label_text()
        expected_text = 'Please select the boot up image and config of device.'
        
        assert expected_text == select_prompt_text
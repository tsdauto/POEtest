# tests/test4_firmware_information.py
import time
import allure
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils.all_exist_in_order import all_exist_in_order
from mixins.TestUtils import ValueCheckMixins


@allure.title("Firmware Information")
class TestIPInformation():
    def test_collapse_system_menu_then_click_system_settings(self, firmware_information_page):
        res = firmware_information_page.init()
        assert res, "error while init firmware information"

    def test_check_firmware_information_table_title(self, firmware_information_page):
        title_cells = firmware_information_page.get_firmware_information_table_title()
        expected_titls = ["ID", "Version", "Size(B)", "Update Time", "From", "User"]

        assert expected_titls == title_cells
# pages/vlan802_1qPage.py
from selenium.webdriver.common.by import By
import re

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class Vlan802_1qPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 Vlan802_1qPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        configuration_menu_locator = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(3) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        vlan_802_1q_menu_locator = (By.CSS_SELECTOR, "div:nth-child(3) > li > ul > div:nth-child(2) > a > li > span")

        self.find_element_if_present(configuration_menu_locator).click()
        self.find_element_if_present(vlan_802_1q_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_802_1q_vlan_settings_title(self):
        get_802_1q_vlan_settings_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_802_1q_vlan_settings_title_locator)

    def get_asymmetric_vlan_title(self):
        get_asymmetric_vlan_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(get_asymmetric_vlan_title_locator)

    def get_802_1q_vlan_state_option_one(self):
        get_802_1q_vlan_state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_802_1q_vlan_state_option_one_locator)

    def get_802_1q_vlan_state_option_two(self):
        get_802_1q_vlan_state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_802_1q_vlan_state_option_two_locator)

    def get_checked_802_1q_vlan_state_option(self):
        vlan_802_1q_state_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div")
        target_div = self.find_element_if_present(vlan_802_1q_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_802_1q_vlan_button_text(self):
        get_802_1q_vlan_button_text_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(get_802_1q_vlan_button_text_locator)

    def get_total_entries_title(self):
        get_total_entries_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > div > table > tr > td > span")

        return self.find_element_then_get_text(get_total_entries_title_locator)

    def get_table_title(self):
        table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)

    def get_vid_1_table_value(self):
        table_title_locator = (By.CSS_SELECTOR, ".el-table__body")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)

    def get_vid_1_rename_button_text(self):
        vid_1_rename_button_text_locator = (By.CSS_SELECTOR, "#onEdit0")

        return self.find_input_value(vid_1_rename_button_text_locator)

    def get_vid_1_delete_button_text(self):
        vid_1_delete_button_text_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > div > div > div:nth-child(3) > table > tbody > tr > td:nth-child(8) > div > input")

        return self.find_input_value(vid_1_delete_button_text_locator)

    def get_asymmetric_vlan_page_text(self):
        ASYMMETRIC_VLAN_PAGE_TEXT_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > span.counter")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_TEXT_LOCATOR)
    
    def get_asymmetric_vlan_page_button1_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON1_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > a.firstPage.isdisabled-btn")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_BUTTON1_LOCATOR)
    
    def get_asymmetric_vlan_page_button2_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON2_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > a.prevPage.isdisabled-btn")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_BUTTON2_LOCATOR)
    
    def get_asymmetric_vlan_page_button3_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON3_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > span.pageNum.slected")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_BUTTON3_LOCATOR)
    
    def get_asymmetric_vlan_page_button4_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON4_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > a.nextPage.isdisabled-btn")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_BUTTON4_LOCATOR)
    
    def get_asymmetric_vlan_page_button5_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON5_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > a.lastPage.isdisabled-btn")
        return self.find_element_then_get_text(ASYMMETRIC_VLAN_PAGE_BUTTON5_LOCATOR)

    def get_asymmetric_vlan_page_value(self):
        ASYMMETRIC_VLAN_PAGE_VALUE_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > input.nPageNum")
        return self.find_input_value(ASYMMETRIC_VLAN_PAGE_VALUE_LOCATOR)

    def get_asymmetric_vlan_page_button6_text(self):
        ASYMMETRIC_VLAN_PAGE_BUTTON6_LOCATOR = (By.CSS_SELECTOR, "div.sx-page > input.goButton")
        return self.find_input_value(ASYMMETRIC_VLAN_PAGE_BUTTON6_LOCATOR)

    def get_add_vid_button_text(self):
        add_vid_button_text_locator = (By.CSS_SELECTOR, "#addVid")

        return self.find_input_value(add_vid_button_text_locator)




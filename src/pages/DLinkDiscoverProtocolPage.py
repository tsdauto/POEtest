# pages/DLinkDiscoverProtocolPage.py
from selenium.webdriver.common.by import By
import re

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class DLinkDiscoverProtocolPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 DLinkDiscoverProtocolPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        D_Link_Discover_Protocol_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(28) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(D_Link_Discover_Protocol_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_d_link_discover_protocol_header_text(self):
        get_d_link_discover_protocol_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_d_link_discover_protocol_header_locator)
    
    def get_ddp_global_settings_title(self):
        get_ddp_global_settings_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_ddp_global_settings_title_locator)

    def get_d_link_discover_protocol_state_title(self):
        get_d_link_discover_protocol_state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(get_d_link_discover_protocol_state_title_locator)
    
    def get_d_link_discover_protocol_state_option_one(self):
        get_d_link_discover_protocol_state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_d_link_discover_protocol_state_option_one_locator)
    
    def get_d_link_discover_protocol_state_option_two(self):
        get_d_link_discover_protocol_state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_d_link_discover_protocol_state_option_two_locator)
    
    def get_checked_d_link_discover_protocol_state_option(self):
        d_link_discover_protocol_state_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(1) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(d_link_discover_protocol_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text
    
    def get_d_link_discover_report_state_title(self):
        get_d_link_discover_report_state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")

        return self.find_element_then_get_text(get_d_link_discover_report_state_title_locator)
    
    def get_d_link_discover_report_state_option_one(self):
        get_d_link_discover_report_state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_d_link_discover_report_state_option_one_locator)
    
    def get_d_link_discover_report_state_option_two(self):
        get_d_link_discover_report_state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_d_link_discover_report_state_option_two_locator)
    
    def get_checked_d_link_discover_report_state_option(self):
        d_link_discover_report_state_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(d_link_discover_report_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text
    
    def get_d_link_discover_protocol_report_timer_title_and_value(self):
        d_link_discover_protocol_report_timer_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        d_link_discover_protocol_report_timer_value_locator = (By.CSS_SELECTOR, "#timer")
        title = self.find_element_then_get_text(d_link_discover_protocol_report_timer_title_locator)
        value = self.find_selected_value_within(d_link_discover_protocol_report_timer_value_locator)
        return title, value
    
    def get_ddp_global_settings_button_text(self):
        ddp_global_settings_button_text_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(ddp_global_settings_button_text_locator)
    
    def get_ddp_port_settings_header(self):
        ddp_port_settings_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(ddp_port_settings_header_locator)
    
    def get_from_port_title_and_value(self):
        from_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td")
        from_port_value_locator = (By.CSS_SELECTOR, "#fromPort")
        title = self.find_element_then_get_text(from_port_title_locator)
        value = self.find_selected_value_within(from_port_value_locator)
        return title, value
    
    def get_to_port_title_and_value(self):
        to_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(2)")
        to_port_value_locator = (By.CSS_SELECTOR, "#ToPort")
        title = self.find_element_then_get_text(to_port_title_locator)
        value = self.find_selected_value_within(to_port_value_locator)
        return title, value

    def get_state_title_and_value(self):
        state_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(3)")
        state_value_locator = (By.CSS_SELECTOR, "#State")
        title = self.find_element_then_get_text(state_title_locator)
        value = self.find_selected_value_within(state_value_locator)
        return title, value
    
    def get_ddp_port_settings_button_text(self):
        ddp_port_settings_button_text_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(ddp_port_settings_button_text_locator)
    
    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)

    def get_port1_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, cells_class_name)
    
    
    
    
    


    

        
        
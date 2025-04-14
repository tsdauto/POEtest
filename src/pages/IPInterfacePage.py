# pages/IPInterfacePage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class IPInterfacePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 IPInterfacePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

    def init(self):
        system_menu_locator = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        firmware_information_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(4) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(firmware_information_menu_locator).click()

        return True

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")
        return self.find_element_then_get_text(page_header_locator)

    def get_tier2_header_text(self):
        tier2_page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(tier2_page_header_locator)

    def get_ip_config_option_one_text(self):
        config_one_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr > td > div > span > label")

        return self.find_element_then_get_text(config_one_locator)

    def get_ip_config_option_two_text(self):
        config_two_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr > td > div > span:nth-child(2) > label")
        return self.find_element_then_get_text(config_two_locator)

    def get_checked_ip_mode_option(self):
        ip_config_option_div = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1)")
        target_div = self.find_element_if_present(ip_config_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_interface_name(self):
        title_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        value_locator = (By.CSS_SELECTOR, "#InterfaceName")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)

        return title, value

    def get_vlan_name(self):
        title_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        value_locator = (By.CSS_SELECTOR, "#VLANName")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)

        return title, value

    def get_ipv4_address(self):
        title_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span")
        title = self.find_element_then_get_text(title_locator)
        ip_octets = [
            self.find_input_value(locator)
            for locator in [
                (By.CSS_SELECTOR, "#iPv4Address > span:nth-child(1) > input:nth-child(1)"),
                (By.CSS_SELECTOR, "#iPv4Address > span:nth-child(1) > input:nth-child(3)"),
                (By.CSS_SELECTOR, "#iPv4Address > span:nth-child(1) > input:nth-child(5)"),
                (By.CSS_SELECTOR, "#iPv4Address > span:nth-child(1) > input:nth-child(7)"),
            ]
        ]

        ip_addr = ".".join(ip_octets)
        return title, ip_addr

    def get_netmask(self):
        title_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(5) > td > span")
        value_locator = (By.CSS_SELECTOR, "#Netmask")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)

        return title, value

    def get_interface_admin_state(self):
        title_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(6) > td > span")
        value_locator = (By.CSS_SELECTOR, "#InterfaceAdminState")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)
        return title, value
    
    def get_maximum_entries(self):
        txt_locator = (By.CSS_SELECTOR, "#table2HeaderInfo")
        return self.find_element_then_get_text(txt_locator)
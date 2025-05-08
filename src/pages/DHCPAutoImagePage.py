# pages/DHCPAutoImagePage.py
from selenium.webdriver.common.by import By

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class DHCPAutoImagePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 DHCPAutoImagePage
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
        DHCP_Auto_ImagePage_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(8) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(DHCP_Auto_ImagePage_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_dhcp_auto_image_tier2_header_text(self):
        get_dhcp_auto_image_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_dhcp_auto_image_tier2_header_locator)
    
    def get_auto_image_title_text(self):
        get_auto_image_title_text_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(get_auto_image_title_text_locator)
    
    def get_auto_image_option_one_text(self):
        get_auto_image_option_one_text_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_auto_image_option_one_text_locator)

    def get_auto_image_option_two_text(self):
        get_auto_image_option_two_text_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_auto_image_option_two_text_locator)
        
    def get_checked_auto_image_mode_option(self):
        auto_image_mode_option_div = (By.CSS_SELECTOR, "div.sx-section > fieldset > table > tr:nth-child(1) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(auto_image_mode_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text
        
    def get_timeout_title_and_value(self):
        title_locator = (By.CSS_SELECTOR,
                         "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        value_locator = (By.CSS_SELECTOR, "#sysDhcpAutoConfigTime")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)

        return title, value
    
    def get_dhcp_auto_image_button_text(self):
        dhcp_auto_image_button_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(dhcp_auto_image_button_locator)

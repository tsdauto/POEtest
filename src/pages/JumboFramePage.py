# pages/JumboFramePage.py
from selenium.webdriver.common.by import By
import re

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class JumboFramePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 JumboFramePage
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
        jumbo_frame_menu_locator = (By.CSS_SELECTOR, "div:nth-child(3) > li > ul > div > a > li > span")

        self.find_element_if_present(configuration_menu_locator).click()
        self.find_element_if_present(jumbo_frame_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_jumbo_frame_settings_title(self):
        get_jumbo_frame_settings_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_jumbo_frame_settings_title_locator)

    def get_jumbo_frame_title(self):
        get_jumbo_frame_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(get_jumbo_frame_title_locator)

    def get_jumbo_frame_state_option_one(self):
        get_jumbo_frame_state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_jumbo_frame_state_option_one_locator)

    def get_jumbo_frame_state_option_two(self):
        get_jumbo_frame_state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_jumbo_frame_state_option_two_locator)

    def get_checked_jumbo_frame_state_option(self):
        jumbo_frame_state_option_div = (By.CSS_SELECTOR, "div.sx-section > fieldset > table > tr > td:nth-child(2) > div")
        target_div = self.find_element_if_present(jumbo_frame_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_jumbo_frame_button_text(self):
        get_jumbo_frame_button_text_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(get_jumbo_frame_button_text_locator)


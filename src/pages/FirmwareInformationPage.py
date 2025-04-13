# pages/FirmwareInformationPage.py
import time

from selenium.webdriver.common.by import By
from .BasePage import BasePage

from utils.generate_screenshot_name import generate_screenshot_name


class FirmwareInformationPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 FirmwareInformationPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

    def init(self):
        SYSTEM_MENU_LOCATOR = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        FIRMWARE_INFORMATION_MENU_LOCATOR = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(2) span")

        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(FIRMWARE_INFORMATION_MENU_LOCATOR).click()

    def get_firmware_information_table_title(self):
        FIRMWARE_INFORMATION_TABLE_LOCATOR = (By.CLASS_NAME, "has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(FIRMWARE_INFORMATION_TABLE_LOCATOR, cells_class_name)

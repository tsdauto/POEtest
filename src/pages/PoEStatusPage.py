# pages/PoEStatusPage.py
from selenium.webdriver.common.by import By

from .BasePage import BasePage
from ..conftest import config

from ..utils.generate_screenshot_name import generate_screenshot_name


class PoEStatusPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PoEStatusPage
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

        POE_menu_locator = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(4) > li > div > span:nth-child(4)")
        POE_Status_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(4) > li > ul > div:nth-child(2) > a > li > span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(POE_menu_locator).click()
        self.find_element_if_present(POE_Status_LOCATOR).click()

        return True
    
    def get_poe_status_Used_text(self):
        POE_STATUS_USED_LOCATOR = (By.CSS_SELECTOR, "#Used0")

        value = self.find_element_then_get_text(POE_STATUS_USED_LOCATOR)

        return value
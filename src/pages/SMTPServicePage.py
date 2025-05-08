# pages/SMTPServicePage.py
from selenium.webdriver.common.by import By
from .BasePage import BasePage

from ..utils.generate_screenshot_name import generate_screenshot_name


class SMTPServicePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SMTPServicePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        SMTP_SERVICE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(27) > li > div > span:nth-child(4)")
        SMTP_SERVICE_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(27) > li > ul > div:nth-child(2) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SMTP_SERVICE_MENU_LOCATOR).click()
        self.find_element_if_present(SMTP_SERVICE_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_smtp_service_settings_tier2_header_text(self):
        SMTP_SERVICE_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SMTP_SERVICE_SETTINGS_TIER2_HEADER_LOCATOR)
    
    def get_subject_title_and_value(self):
        SUBJECT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        SUBJECT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#Subject")
        title = self.find_element_then_get_text(SUBJECT_TITLE_LOCATOR)
        value = self.find_input_value(SUBJECT_VALUE_LOCATOR)
        return title, value
    
    def get_content_title_and_value(self):
        CONTENT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        CONTENT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#iPv6PingResult")
        title = self.find_element_then_get_text(CONTENT_TITLE_LOCATOR)
        value = self.find_input_value(CONTENT_VALUE_LOCATOR)
        return title, value
    
    def get_button_text(self):
        BUTTON_TEXT_LOCATOR = (By.CSS_SELECTOR, "#onSend")
        return self.find_input_value(BUTTON_TEXT_LOCATOR)

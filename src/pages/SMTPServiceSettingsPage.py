# pages/SMTPServiceSettingsPage.py
from selenium.webdriver.common.by import By
from .BasePage import BasePage

from ..utils.generate_screenshot_name import generate_screenshot_name


class SMTPServiceSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SMTPServiceSettingsPage
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
        SMTP_SERVER_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(27) > li > ul > div > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SMTP_SERVICE_MENU_LOCATOR).click()
        self.find_element_if_present(SMTP_SERVER_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_smtp_service_settings_tier2_header_text(self):
        SMTP_SERVICE_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SMTP_SERVICE_SETTINGS_TIER2_HEADER_LOCATOR)

    def get_smtp_state_title_text(self):
        SMTP_STATE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        return self.find_element_then_get_text(SMTP_STATE_TITLE_LOCATOR)

    def get_smtp_state_option_one_text(self):
        SMTP_STATE_OPTION_ONE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span > label")
        return self.find_element_then_get_text(SMTP_STATE_OPTION_ONE_LOCATOR)

    def get_smtp_state_option_two_text(self):
        SMTP_STATE_OPTION_TWO_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span:nth-child(2) > label")
        return self.find_element_then_get_text(SMTP_STATE_OPTION_TWO_LOCATOR)

    def get_checked_smtp_state_option(self):
        smtp_state_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(smtp_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_smtp_server_address_title_text(self):
        SMTP_SERVER_ADDRESS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table:nth-child(4) > tr:nth-child(2) > td:nth-child(1) > span")
        return self.find_element_then_get_text(SMTP_SERVER_ADDRESS_TITLE_LOCATOR)

    def get_ipv4_title_and_value(self):
        SMTP_SERVER_ADDRESS_TITLE_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[2]/fieldset/table[2]/tr[2]/td[2]")
        td_element = self.find_element_if_visible(SMTP_SERVER_ADDRESS_TITLE_LOCATOR)
        if td_element:
            title = self.driver.execute_script("""
                var td = arguments[0];
                var text = "";
                for (var i = 0; i < td.childNodes.length; i++) {
                    if (td.childNodes[i].nodeType === Node.TEXT_NODE) {
                        text += td.childNodes[i].textContent;
                    }
                }
                return text.trim();
            """, td_element)
        else:
            title = None
        ipv4_octets = [
            self.find_input_value(locator)
            for locator in [
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(1)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(3)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(5)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(7)"),
            ]
        ]

        ipv4_addr = ".".join(ipv4_octets)
        return title, ipv4_addr

    def get_ipv6_title_and_value(self):
        SMTP_SERVER_ADDRESS_TITLE_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[2]/fieldset/table[2]/tr[3]/td[2]")
        SMTP_SERVER_ADDRESS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#IPv6 > input")
        td_element = self.find_element_if_visible(SMTP_SERVER_ADDRESS_TITLE_LOCATOR)
        if td_element:
            title = self.driver.execute_script("""
                var td = arguments[0];
                var text = "";
                for (var i = 0; i < td.childNodes.length; i++) {
                    if (td.childNodes[i].nodeType === Node.TEXT_NODE) {
                        text += td.childNodes[i].textContent;
                    }
                }
                return text.trim();
            """, td_element)
        else:
            title = None

        ipv6_addr = self.find_input_value(SMTP_SERVER_ADDRESS_VALUE_LOCATOR)
        return title, ipv6_addr
    
    def get_domain_title_and_value(self):
        DOMAIN_TITLE_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[2]/fieldset/table[2]/tr[4]/td[2]")
        DOMAIN_VALUE_LOCATOR = (By.CSS_SELECTOR, "#Domain")
        td_element = self.find_element_if_visible(DOMAIN_TITLE_LOCATOR)
        if td_element:
            title = self.driver.execute_script("""
                var td = arguments[0];
                var text = "";
                for (var i = 0; i < td.childNodes.length; i++) {
                    if (td.childNodes[i].nodeType === Node.TEXT_NODE) {
                        text += td.childNodes[i].textContent;
                    }
                }
                return text.trim();
            """, td_element)
        else:
            title = None

        domain_value = self.find_input_value(DOMAIN_VALUE_LOCATOR)
        return title, domain_value

    def get_checked_v4_mode_option(self):
        v4_mode_locator = (By.CSS_SELECTOR, "#IPv4Radio")
        return self.find_checkbox_checked(v4_mode_locator)

    def get_checked_v6_mode_option(self):
        v6_mode_locator = (By.CSS_SELECTOR, "#IPv6Radio")
        return self.find_checkbox_checked(v6_mode_locator)
    
    def get_checked_domain_mode_option(self):
        domain_mode_locator = (By.CSS_SELECTOR, "#DomainRadio")
        return self.find_checkbox_checked(domain_mode_locator)
    
    def get_self_mail_address_title_and_value(self):
        SELF_MAIL_ADDRESS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table:nth-child(4) > tr:nth-child(5) > td:nth-child(1) > span")
        SELF_MAIL_ADDRESS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SelfMailAddress")
        title = self.find_element_then_get_text(SELF_MAIL_ADDRESS_TITLE_LOCATOR)
        value = self.find_input_value(SELF_MAIL_ADDRESS_VALUE_LOCATOR)
        return title, value

    def get_self_mail_address_key_title_and_value(self):
        SELF_MAIL_ADDRESS_KEY_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table:nth-child(4) > tr:nth-child(6) > td:nth-child(1) > span")
        SELF_MAIL_ADDRESS_KEY_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SelfMailAddresskey")
        title = self.find_element_then_get_text(SELF_MAIL_ADDRESS_KEY_TITLE_LOCATOR)
        value = self.find_input_value(SELF_MAIL_ADDRESS_KEY_VALUE_LOCATOR)
        return title, value

    def get_smtp_server_port_title_and_value(self):
        SMTP_SERVER_PORT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table:nth-child(4) > tr:nth-child(2) > td:nth-child(3) > span")
        SMTP_SERVER_PORT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SMTPServerPort")
        title = self.find_element_then_get_text(SMTP_SERVER_PORT_TITLE_LOCATOR)
        value = self.find_input_value(SMTP_SERVER_PORT_VALUE_LOCATOR)
        return title, value

    def get_smtp_service_settings_button_text(self):
        SMTP_SERVICE_SETTINGS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#onApply")
        return self.find_input_value(SMTP_SERVICE_SETTINGS_BUTTON_LOCATOR)
    
    def get_mail_receiver_address_header(self):
        MAIL_RECEIVER_ADDRESS_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")
        return self.find_element_then_get_text(MAIL_RECEIVER_ADDRESS_HEADER_LOCATOR)

    def get_mail_receiver_address_title_and_value(self):
        MAIL_RECEIVER_ADDRESS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(1) > span")
        MAIL_RECEIVER_ADDRESS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#MailReceiverAddress")
        title = self.find_element_then_get_text(MAIL_RECEIVER_ADDRESS_TITLE_LOCATOR)
        value = self.find_input_value(MAIL_RECEIVER_ADDRESS_VALUE_LOCATOR)
        return title, value

    def get_mail_receiver_address_button_text(self):
        MAIL_RECEIVER_ADDRESS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#onAdd")
        return self.find_input_value(MAIL_RECEIVER_ADDRESS_BUTTON_LOCATOR)

    def get_mail_receiver_address_table_header(self):
        MAIL_RECEIVER_ADDRESS_TABLE_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > legend")
        return self.find_element_then_get_text(MAIL_RECEIVER_ADDRESS_TABLE_HEADER_LOCATOR)

    def get_total_entries_title(self):
        TOTAL_ENTRIES_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(TOTAL_ENTRIES_TITLE_LOCATOR)

    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)















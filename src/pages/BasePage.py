# pages/BasePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class BasePage:
    def __init__(self, driver, base_url):
        """
        初始化 BasePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 30)

    def take_screenshot(self, name):
        """
        截圖，存放於 screenshots 資料夾
        :param name: 截圖檔案名稱
        """
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    def find_element_if_visible(self, locator):
        """
        找到元素並確保其可見
        :param locator: 元素定位器 (By, value)
        :return: 定位到的元素或 None
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def find_element_then_get_text(self, locator):
        """
        找到元素並獲取其文本
        :param locator: 元素定位器 (By, value)
        :return: 元素的文本或 None
        """
        try:
            element = self.find_element_if_visible(locator)
            return element.text if element else None
        except Exception as e:
            print(f"Error getting text from element {locator}: {e}")
            return None

    def click_element(self, locator):
        """
        點擊元素
        :param locator: 元素定位器 (By, value)
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Clicked element {locator}")
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")

    def input_text(self, locator, text):
        """
        在元素中輸入文本
        :param locator: 元素定位器 (By, value)
        :param text: 要輸入的文本
        """
        try:
            element = self.find_element_if_visible(locator)
            if element:
                element.clear()
                element.send_keys(text)
                print(f"Input text '{text}' into element {locator}")
        except Exception as e:
            print(f"Error inputting text into element {locator}: {e}")

    def wait_for_element_to_disappear(self, locator):
        """
        等待元素消失
        :param locator: 元素定位器 (By, value)
        :return: 成功返回 True，否則返回 False
        """
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except Exception as e:
            print(f"Error waiting for element {locator} to disappear: {e}")
            return False

    def navigate_to(self, path=""):
        """
        導航至指定的 URL
        :param path: URL 的相對路徑
        """
        try:
            full_url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
            self.driver.get(full_url)
            print(f"Navigated to {full_url}")
        except Exception as e:
            print(f"Error navigating to {path}: {e}")

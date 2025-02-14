# pages/BasePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

    def find_element_if_present(self, locator):
        """
        找到元素並確保其存在
        :param locator: 元素定位器 (By, value)
        :return: 定位到的元素或 None
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def click_element_by_js(self, locator):
        """
        找到元素並獲取其文本
        :param locator: 元素定位器 (By, value)
        :return: 元素的文本或 None
        """
        try:
            element = self.find_element_if_present(locator)
            self.driver.execute_script("arguments[0].click();", element)

        except Exception as e:
            print(f"Error clicking element with js {locator}: {e}")
            return None

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


    def find_element_by_text(self, parent, text):
        """
        Helper method to find an element containing the specified text within the parent element.
        :param parent: The parent element to search within.
        :param text: The text to search for.
        :return: The found element or None.
        """
        try:
            return parent.find_element(By.XPATH, f".//*[contains(text(), '{text}')]")
        except Exception:
            return None

    def find_element_by_text_within(self, parent_locator, text):
        """
        Find element in specified section.
        :param parent_locator: Locator for the parent element.
        :param text: The text to search for within the parent element.
        :return: The found element or None.
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            return self.find_element_by_text(parent, text)
        except Exception:
            return None

    def text_is_existed_within(self, parent_locator, text):
        """
        Check if text exists in specified section.
        :param parent_locator: Locator for the parent element.
        :param text: The text to search for within the parent element.
        :return: True if the text is found, False otherwise.
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            el = self.find_element_by_text(parent, text)
            return el is not None
        except Exception:
            return False

    def click_element(self, locator):
        """
        點擊元素
        :param locator: 元素定位器 (By, value)
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
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

    def find_input_value(self, locator):
        """
        查找元素并获取 value 值
        :param locator: 元素定位器
        :return: 输入框的值 (str) 或 None
        """
        try:
            element = self.find_element_if_visible(locator)
            if element:
                return element.get_attribute("value")
            # logging.warning(f"Element {locator} not found or not visible.")
        except Exception as e:
            # logging.error(f"Error getting value from element {locator}: {e}", exc_info=True)

            return None

    def find_checked_radio_within(self, parent_element):
        # Retrieve the one and only selected input inside the target div
        inputs = parent_element.find_elements(By.CSS_SELECTOR, "input:checked")
        return inputs[0] if inputs else None

    def find_selected_value_within(self, locator):
        element = self.find_element_if_present(locator)
        select_box = Select(element)
        selected_option = select_box.first_selected_option
        text = selected_option.text
        return text

    def find_cells_value_within(self, locator, cells_cls_name, timeout=10):
        """
        在指定的父元素內查找所有符合 `cells_cls_name` 的子元素，並返回其文本內容。

        :param locator: 父元素的定位器 (By, 值)
        :param cells_cls_name: 目標單元格的 class 名稱
        :param timeout: 等待元素出現的時間（秒）
        :return: list，包含所有符合條件的 cell 文字內容
        """
        try:
            # 等待父元素出現
            parent_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # 查找所有子元素
            cells = parent_element.find_elements(By.CLASS_NAME, cells_cls_name)
            # 過濾出可見的 cell，並提取 text
            return [cell.text for cell in cells if cell.is_displayed()]

        except Exception as e:
            print(f"Error for element {locator} to find cells: {e}")
            return []  # 返回空列表以保持一致性


    def get_selected_input_label_text(self, selected_input):

        label = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{selected_input.get_attribute("id")}"]')
        return label.text.strip() if label else None

    def wait_for_element_to_disappear(self, locator):
        """
        等待元素消失【
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

# pages/BasePage.py
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from dotenv import load_dotenv
load_dotenv("Settings.env")


class BasePage:
    def __init__(self, driver, base_url):
        """
        Initialize BasePage
        :param driver: WebDriver instance
        :param base_url: Base URL
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, os.getenv("WEBDRIVER_TIMEOUT"))

    def take_screenshot(self, name):
        """
        Take a screenshot and save it to the screenshots folder
        :param name: Screenshot file name
        """
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    def find_element_if_present(self, locator):
        """
        Find an element and ensure it exists
        :param locator: Element locator (By, value)
        :return: Located element or None
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def click_element_by_js(self, locator):
        """
        Click an element using JavaScript
        :param locator: Element locator (By, value)
        :return: None
        """
        try:
            element = self.find_element_if_present(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Error clicking element with js {locator}: {e}")
            return None

    def find_element_if_visible(self, locator):
        """
        Find an element and ensure it is visible
        :param locator: Element locator (By, value)
        :return: Located element or None
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def find_element_then_get_text(self, locator):
        """
        Find an element and get its text
        :param locator: Element locator (By, value)
        :return: Element text or None
        """
        try:
            element = self.find_element_if_visible(locator)
            return element.text if element else None
        except Exception as e:
            print(f"Error getting text from element {locator}: {e}")
            return None

    def find_element_by_text(self, parent, text):
        """
        Helper method to find an element containing the specified text within the parent element
        :param parent: The parent element to search within
        :param text: The text to search for
        :return: The found element or None
        """
        try:
            return parent.find_element(By.XPATH, f".//*[contains(text(), '{text}')]")
        except Exception:
            return None

    def find_element_by_text_within(self, parent_locator, text):
        """
        Find element in specified section
        :param parent_locator: Locator for the parent element
        :param text: The text to search for within the parent element
        :return: The found element or None
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            return self.find_element_by_text(parent, text)
        except Exception:
            return None

    def text_is_existed_within(self, parent_locator, text):
        """
        Check if text exists in specified section
        :param parent_locator: Locator for the parent element
        :param text: The text to search for within the parent element
        :return: True if the text is found, False otherwise
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            el = self.find_element_by_text(parent, text)
            return el is not None
        except Exception:
            return False

    def click_element(self, locator):
        """
        Click an element
        :param locator: Element locator (By, value)
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
        Input text into an element
        :param locator: Element locator (By, value)
        :param text: Text to input
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
        Get input element's value
        :param locator: Element locator
        :return: String or None
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
        """
        Retrieve the one and only selected input inside the target div
        """
        inputs = parent_element.find_elements(By.CSS_SELECTOR, "input:checked")
        return inputs[0] if inputs else None

    # select box
    def find_selected_value_within(self, locator):
        """
        Get selected value within specified select box
        :param locator: Element locator
        :return: Selected option text
        """
        element = self.find_element_if_present(locator)
        select_box = Select(element)
        selected_option = select_box.first_selected_option
        text = selected_option.text
        return text

    def find_selected_input_label_text(self, selected_input):
        """
        Get the label text associated with the selected input
        :param selected_input: The selected input element
        :return: Label text or None
        """
        try:
            label = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{selected_input.get_attribute("id")}"]')
            return label.text.strip() if label else None
        except Exception as e:
            print(f"Error getting label text: {e}")
            return None
        
    def find_selected_value(self, locator: tuple[str, str]) -> str:
        """
        根據傳入的 locator 取得 select 元素中被選取的 value。
        
        :param driver: Selenium 的 WebDriver 實例
        :param locator: 例如 ("id", "mySelect") 或 ("xpath", "//select[@name='abc']")
        :return: 被選取的 option 的 value
        """
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        return select.first_selected_option.get_attribute("value")

    # table
    def find_cells_value_within(self, locator, cells_cls_name, timeout=5):
        """
        Find all child elements matching `cells_cls_name` within the specified parent element and return their text content
        :param locator: Parent element locator (By, value)
        :param cells_cls_name: Class name of target cells
        :param timeout: Time to wait for elements to appear (seconds)
        :return: List of text content from matching cells
        """
        try:
            # Wait for the parent element to appear
            parent_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # Find all child elements
            cells = parent_element.find_elements(By.CLASS_NAME, cells_cls_name)
            # Filter visible cells and extract their text
            return [cell.text for cell in cells if cell.is_displayed()]
        except Exception as e:
            print(f"Error for element {locator} to find cells: {e}")
            return []

    

    def wait_for_element_to_disappear(self, locator):
        """
        Wait for an element to disappear
        :param locator: Element locator (By, value)
        :return: True if successful, False otherwise
        """
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except Exception as e:
            print(f"Error waiting for element {locator} to disappear: {e}")
            return False

    # browser manipulation
    def navigate_to(self, path=""):
        """
        Navigate to the specified URL
        :param path: Relative path of the URL
        """
        try:
            full_url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
            self.driver.get(full_url)
            print(f"Navigated to {full_url}")
        except Exception as e:
            print(f"Error navigating to {path}: {e}")

    def refresh(self):
        """
        Refresh the page
        :return: None
        """

        try:
            self.driver.refresh()
        except Exception as e:
            print(f"Error refreshing page: {e}")

# pages/login_page.py
from exceptiongroup import catch
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

import time


# Page Object Model
class LoginPage(BasePage):
    # Page element locators
    USERNAME_INPUT = (By.ID, "Username")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.ID, "Login")
    USERINFO_SPAN = (By.CLASS_NAME, "userInfo")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{base_url}"

    def open(self):
        """Open the login page"""
        try:
            self.driver.get(self.url)
            return self.driver.title
        except Exception as error:
            raise error

    def switch_to_main_frame(self):

        try:
            # wait for element to located
            frame = self.wait.until(
                EC.visibility_of_element_located((By.ID, "iframemain"))
            )

            print("\n\n frame located")

            # switch to frame
            self.driver.switch_to.frame(frame)

            print("\n\n switch to main frame")

            return True

        except Exception as e:

            raise Exception(e)

    def login(self, username, password):
        """Perform login action"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT)
            ).send_keys(username)

            self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            ).send_keys(password)

            self.wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            ).click()

            return True

        except Exception as error:

            raise Exception(error)

    # def is_error_visible(self):
    #     """Check if error message is displayed"""
    #     try:
    #         error = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
    #         return error.is_displayed()
    #     except:
    #         return False:

    def is_login_successful(self):
        """Check if login was successful"""

        # try:
        #     time.sleep(.5)
        #     user_info_el = self.wait.until(EC.visibility_of_element_located(self.USERINFO_SPAN))
        #     print("\n\n userinfo element located", user_info_el.text)
        #     user_info = user_info_el.text.lower()
        #     print("\n\n", user_info)
        #     if "logged in" in user_info:
        #         return True
        #     else:
        #         return False
        try:
            # wait until string "Logged in" show up on page
            retries = 5
            for _ in range(retries):
                user_info_el = self.wait.until(EC.visibility_of_element_located(self.USERINFO_SPAN))
                user_info_text = user_info_el.text.lower()
                if "logged in" in user_info_text:
                    return True
                time.sleep(0.1)
            return False

        except Exception as error:
            raise Exception(error)

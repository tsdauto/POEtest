# pages/LoginPage.py
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    # Page element locators
    USERNAME_INPUT = (By.ID, "Username")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.ID, "Login")
    USERINFO_SPAN = (By.CLASS_NAME, "userInfo")
    MAIN_FRAME_ID = "iframemain"
    LOGIN_STATUS = False

    @classmethod
    def set_login_status(cls, status):
        """設置類屬性 LOGIN_STATUS"""
        cls.LOGIN_STATUS = status

    @classmethod
    def get_login_status(cls):
        """獲取類屬性 LOGIN_STATUS"""
        return cls.LOGIN_STATUS

    def __init__(self, driver, base_url):
        """
        初始化 LoginPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

    def open(self):
        """
        打開登錄頁面
        :return: 當前頁面標題
        """
        self.navigate_to()  # 使用 BasePage 的方法導航到 base_url
        return self.driver.title

    def switch_to_main_frame(self):
        """
        切換到主框架
        :return: 切換成功返回 True
        """
        try:
            frame = self.find_element_if_visible((By.ID, self.MAIN_FRAME_ID))
            self.driver.switch_to.frame(frame)
            print("Switched to main frame")
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to switch to main frame: {e}")

    def login(self, username, password):
        """
        執行登錄操作
        :param username: 用戶名
        :param password: 密碼
        :return: 登錄成功返回 True
        """
        try:
            self.input_text(self.USERNAME_INPUT, username)
            self.input_text(self.PASSWORD_INPUT, password)
            self.click_element(self.LOGIN_BUTTON)
            print("Login button clicked")
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to login: {e}")

    def is_login_successful(self):
        """
        檢查登錄是否成功
        :return: 成功返回 True，否則返回 False
        """
        try:
            user_info_text = self.find_element_then_get_text(self.USERINFO_SPAN)
            if user_info_text and "logged in" in user_info_text.lower():
                LoginPage.set_login_status(True)
                print("\n\n set login status as true", LoginPage.get_login_status())

                print("Login successful")
                return True
            print("Login unsuccessful")
            return False
        except Exception:
            print("Error during login status check")
            return False

    def do_login(self, username, password):
        print("\n\nLOGIN STAT:", LoginPage.get_login_status())
        if not LoginPage.get_login_status():
            self.open()
            self.switch_to_main_frame()
            self.login(username, password)
            self.is_login_successful()
        else:
            self.open()
            self.switch_to_main_frame()

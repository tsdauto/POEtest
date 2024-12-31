import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 初始化 WebDriver
driver = webdriver.Chrome()

try:
    # 打开目标网址
    driver.get("http://10.90.90.90")

    # 等待 iframe 加载并切换
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "iframemain"))
    )
    driver.switch_to.frame(driver.find_element(By.ID, "iframemain"))
    print("Switched to iframe")

    # 定位输入框
    input_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "Username"))
    )
    print("Input element located")

    # 发送文本
    input_element.send_keys("123")
    print("Text input successful")

    # 等待 10 秒
    time.sleep(10)
    print("Waited for 10 seconds")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()

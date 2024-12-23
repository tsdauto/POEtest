# test_web_add.py

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


# fixture environment 
@pytest.fixture
def browser() -> None:
    driver = webdriver.Chrome(
    )  # Make sure ChromeDriver is installed and in PATH
    yield driver
    driver.quit()


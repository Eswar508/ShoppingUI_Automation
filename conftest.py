import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.elements import Element
import time
@pytest.fixture(scope="function")
def driver():
    driver=webdriver.Chrome()
    driver.get("https://sauce-demo.myshopify.com/")
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def element(driver):
    return Element(driver)

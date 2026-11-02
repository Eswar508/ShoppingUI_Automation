import time
import pytest
from utils.wait import wait_until
import utils.helper_fun as fun
import utils.attach_results as attach_results
from selenium.webdriver.common.by import By
from selenium import webdriver
from utils.elements import Element
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
element=Element(driver)
element.driver.get("https://sauce-demo.myshopify.com/")
element.catalog.click()
prod=element.catalog_list[0]
time.sleep(2)
text=prod.find_element(By.TAG_NAME,"h4").text
print(f"Product name: {text}")
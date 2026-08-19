from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def wait(driver,selector,timeout=10):
    try:
        result=WebDriverWait(driver,timeout).until(EC.element_to_be_clickable(selector))
        driver.execute_script("arguments[0].scrollIntoView();", result)
        print(f"wait selector : {result}")
        return result
    except Exception as e:
        print("element not found")
        return False
def wait_until(driver,condition,timeout=10):
    try:
        result=WebDriverWait(driver,timeout).until(condition)
        print(f"wait_until selector : {result}")
        return result
    except Exception as e:
        print("condition or something went wrong")
        return False
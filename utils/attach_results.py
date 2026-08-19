import allure
from  save_data.logging import log
from save_data.save_screenshot import save_screenshot
def attach_error(driver,exception):
    log().error(exception)
    allure.attach(driver.get_screenshot_as_png(),name="error_screenshot",attachment_type=allure.attachment_type.PNG)
    allure.attach(str(exception),name="error_message",attachment_type=allure.attachment_type.TEXT)
    save_screenshot(driver)
def attach_info(message,screen_shot=False,driver=None):
    if screen_shot and driver:
        allure.attach(driver.get_screenshot_as_png(),name="info_screenshot",attachment_type=allure.attachment_type.PNG)
    log().info(message)
    allure.attach(message,name="info_message",attachment_type=allure.attachment_type.TEXT)
def attach_warning(message,screen_shot=False,driver=None):
    if screen_shot and driver:
        allure.attach(driver.get_screenshot_as_png(),name="warning_screenshot",attachment_type=allure.attachment_type.PNG)
    log().warning(message)
    allure.attach(message,name="warning_message",attachment_type=allure.attachment_type.TEXT)
def attach_debug(message,screen_shot=False,driver=None):
    if screen_shot and driver:
        allure.attach(driver.get_screenshot_as_png(),name="debug_screenshot",attachment_type=allure.attachment_type.PNG)
    log().debug(message)
    allure.attach(message,name="debug_message",attachment_type=allure.attachment_type.TEXT)
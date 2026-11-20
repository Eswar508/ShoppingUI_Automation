import allure
from selenium.common.exceptions import WebDriverException

from save_data.logging import log
from save_data.save_screenshot import save_screenshot


def attach_error(driver, error):
    log().error(str(error))

    try:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="failure-screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
        save_screenshot(driver)
    except (OSError, WebDriverException) as screenshot_error:
        log().warning("Could not save failure screenshot: %s", screenshot_error)

    allure.attach(
        str(error),
        name="failure-details",
        attachment_type=allure.attachment_type.TEXT,
    )

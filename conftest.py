import os

import pytest
from selenium import webdriver

from utils.attach_results import attach_error


BASE_URL = "https://sauce-demo.myshopify.com/"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    #if os.getenv("HEADLESS", "true").lower() == "true":
    #    options.add_argument("--headless=new")

    chrome_path = os.getenv("CHROME_BIN")
    if chrome_path:
        options.binary_location = chrome_path

    browser = webdriver.Chrome(options=options)
    try:
        browser.get(os.getenv("BASE_URL", BASE_URL))
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser is not None:
            attach_error(browser, report.longreprtext)

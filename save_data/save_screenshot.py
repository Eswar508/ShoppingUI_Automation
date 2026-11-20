from datetime import datetime
from pathlib import Path


def save_screenshot(driver):
    screenshots_dir = Path("reports/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    driver.save_screenshot(screenshots_dir / f"failed_{timestamp}.png")
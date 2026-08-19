import os,time
def save_screenshot(driver):
    if not os.path.exists("results/screenshots"):
        os.makedirs("results/screenshots")
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"results/screenshots/failed_{timestamp}.png")
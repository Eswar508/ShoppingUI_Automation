from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    prod_container = (By.CSS_SELECTOR, "#page-content > section")
    add_to_cart = (By.CSS_SELECTOR, "#add")
    catalog = (By.CSS_SELECTOR, "#main-menu > li:nth-child(2) > a")
    home = (By.CSS_SELECTOR, "#main-menu > li:nth-child(1) > a")
    mycart_num = (By.CSS_SELECTOR, "#cart-target-desktop")

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, selector, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(selector)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_prod_list(self):
        product_section = self.get_element(self.prod_container)
        return product_section.find_elements(By.XPATH, "./div")

    def get_prod_name(self, prod=None, index=0):
        if prod is None:
            prod = self.get_prod_list()[index]
        return prod.find_element(By.TAG_NAME, "h3").text

    def get_mycart_num(self):
        cart_text = self.get_element(self.mycart_num).text
        return int(cart_text.strip("()"))

    def wait_until(self, condition, timeout=15):
        return WebDriverWait(self.driver, timeout).until(condition)

    def click_prod(self, index, no_of_clicks=1):
        products = self.get_prod_list()
        if index < 0 or index >= len(products):
            raise IndexError(f"Product index {index} is not available.")

        cart_num = self.get_mycart_num()
        product_link = products[index].find_element(By.TAG_NAME, "a")
        product_link.click()

        for _ in range(no_of_clicks):
            self.get_element(self.add_to_cart).click()
            cart_num += 1
            self.wait_until(lambda driver: self.get_mycart_num() == cart_num)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from utils.wait import wait
def by_selector():
    with open("utils/elem_selectors.json") as f:
        data=json.load(f)
    return data
class Element():
    def __init__(self,driver):
        self.driver=driver
        self.selectors=by_selector()
        self.elements=self.selectors.keys()
    @property
    def prod_container(self):
        selector=(By.CSS_SELECTOR, self.selectors["prod_container"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def mycart_button(self):
        selector=(By.CSS_SELECTOR, self.selectors["mycart_button"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def mycart_num(self):
        selector=(By.CSS_SELECTOR, self.selectors["mycart_num"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def mycart_form(self):
        selector=(By.CSS_SELECTOR, self.selectors["catalog form"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def checkout(self):
        selector=(By.CSS_SELECTOR, self.selectors["checkout"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def cart_first_element(self):
        selector=(By.CSS_SELECTOR, self.selectors["cart_first_element"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def cart_prod_price(self):
        selector=(By.CSS_SELECTOR, self.selectors["cart_prod_price"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def cart_prod_total(self):
        selector=(By.CSS_SELECTOR, self.selectors["cart_prod_total"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def cart_prod_name(self):
        selector=(By.CSS_SELECTOR, self.selectors["cart_prod_name"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def remove(self):
        selector=(By.CSS_SELECTOR, self.selectors["remove"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def carts_checkout(self):
        selector=(By.CSS_SELECTOR, self.selectors["carts_checkout"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def catalog_container(self):
        selector=(By.CSS_SELECTOR, self.selectors["catalog container"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def checkouts_prod_container(self):
        selector=(By.CSS_SELECTOR, self.selectors["checkouts prod container"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def checkouts_checkout(self):
        selector=(By.CSS_SELECTOR, self.selectors["checkouts checkout"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def checkouts_total(self):
        selector=(By.CSS_SELECTOR, self.selectors["checkouts total"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def home(self):
        selector=(By.CSS_SELECTOR, self.selectors["home"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def catalog(self):
        selector=(By.CSS_SELECTOR, self.selectors["catalog"])
        ele=wait(self.driver, selector)
        return ele
    @property
    def add_to_cart(self):
        selector=(By.CSS_SELECTOR, self.selectors["add to cart"])
        ele=wait(self.driver, selector)
        return ele
#--------------------------------------------------------------------------------------------------------------------
    @property
    def prod_list(self):
        return self.prod_container.find_elements(By.XPATH,"./div")
    def prod_name(self,prod):
        selector=(By.XPATH, ".//h3")
        ele=wait(prod, selector)
        return ele
    def prod_price(self,prod):
        selector=(By.XPATH, ".//h4")
        ele=wait(prod, selector)
        return ele
    @property
    def catalog_list(self):
        return self.catalog_container.find_elements(By.XPATH,".//a")
    def catalogs_prod_name(self,prod):
        selector=(By.XPATH, ".//h3")
        ele=wait(prod, selector)
        return ele
    def catalogs_prod_price(self,prod):
        selector=(By.XPATH, ".//h4")
        ele=wait(prod, selector)
        return ele
    @property
    def checkouts_prod_list(self):
        return self.checkouts_prod_container.find_elements(By.CLASS_NAME,"row")
    def checkouts_prod_name(self,prod):
        selector=(By.CLASS_NAME, "info")
        ele=wait(prod, selector)
        return ele
    def checkouts_prod_price(self,prod):
        selector=(By.CLASS_NAME, "two columns price desktop")
        ele=wait(prod, selector)
        return ele
    def checkouts_prod_num(self,prod):
        selector=(By.TAG_NAME, "input")
        ele=wait(prod, selector)
        return ele
    def checkouts_prod_total(self,prod):
        selector=(By.CLASS_NAME, "two columns total desktop")
        ele=wait(prod, selector)
        return ele
    
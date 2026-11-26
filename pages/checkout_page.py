from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from time import sleep

class CheckoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    checkouts_prod_list=(By.CSS_SELECTOR,"#cart > form > div:nth-child(1)")
    checkouts_total=(By.CSS_SELECTOR,"#cart > form > div.twelve.columns.alpha.omega.row > div.six.columns.omega.cart.total > h2")
    checkout=(By.CSS_SELECTOR,"#minicart > a.checkout")
    def get_checkout(self):
        return self.get_element(self.checkout)
    def prods_to_checkout(self,index=0,no_of_clicks=1):
        self.click_prod(index=index,no_of_clicks=no_of_clicks)
        ckout=self.get_checkout()
        ckout.click()
    def get_ckout_prod_price(self,prod):
        return float(prod.find_elements(By.TAG_NAME,"div")[2].text[1:])
    def get_ckout_prod_num(self,prod):
        return int(prod.find_element(By.TAG_NAME,"input").get_attribute("value"))
    def get_ckout_prod_total(self,prod):
        return float(prod.find_element(By.TAG_NAME,"span").text[1:])
    def get_checkouts_total(self):
        return float(self.get_element(self.checkouts_total).text[7:])
    def get_ckout_prod_list(self):
        return self.get_element(self.checkouts_prod_list).find_elements(By.CLASS_NAME,"row")
    def update_ckout_prod_num(self,prod,new_quantity):
        #update the quantity of a product with the given new_quantity
        input_field=prod.find_element(By.TAG_NAME,"input")
        input_field.clear()
        input_field.send_keys(str(new_quantity))
        input_field.send_keys("\n")  # Press Enter to update the quantity
        self.wait_until(Ec.staleness_of(prod))
    def get_ckout_prod_name(self,prod):
        return prod.find_element(By.TAG_NAME,"h3").text
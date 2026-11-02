from pages.incrementation_page import AddToCartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.helper_fun import get_cart_total
def test_checkout(element):
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=1)
    element.checkout.click()
    assert element.driver.current_url == "https://sauce-demo.myshopify.com/cart", f"Expected URL to be 'https://sauce-demo.myshopify.com/checkout', but got '{element.driver.current_url}'"
def test_prod_total(element):
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=3)
    element.checkout.click()
    prod=element.checkouts_prod_list[0]
    prod_price=float(prod.find_elements(By.TAG_NAME,"div")[2].text[1:])
    prod_num=int(prod.find_element(By.TAG_NAME,"input").get_attribute("value"))
    prod_total=float(prod.find_element(By.TAG_NAME,"span").text[1:])
    assert prod_total==prod_price*prod_num,f"Expected product total to be {prod_price*prod_num}, but got {prod_total}"
def test_cart_total(element):
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=3)
    element.driver.back()
    AddToCartPage.increment_items_to_cart(element, item_index=1, clicking_no=1)
    element.wait.until(lambda driver: element.add_to_cart.is_enabled() is True)
    element.checkout.click()
    prod_list=element.checkouts_prod_list
    prod_total=get_cart_total(prod_list)
    cart_total=float(element.checkouts_total.text[7:])
    assert cart_total==prod_total,f"Expected cart total to be {prod_total}, but got {cart_total}"
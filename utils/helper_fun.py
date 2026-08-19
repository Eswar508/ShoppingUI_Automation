from utils.wait import wait_until,wait
from selenium.webdriver.common.by import By
import pytest,time
import utils.attach_results as attach_results
def validate_carts_form(element,timeout=3):
    element.driver.execute_script("arguments[0].scrollIntoView();", element.mycart_button)
    element.mycart_button.click()
    result=wait_until(element.driver,lambda driver: element.mycart_form.is_displayed() is True,timeout=timeout)
    return result
def add_to_cart(element,items_index=0,clicking_no=1):
    try:prod=element.prod_list[items_index]
    except:pytest.skip,f"no items exist more than {items_index-1}"
#meta_data={
#    "name":element.prod_name(prod),
#    "price":element.prod_price(prod),
#    "no":clicking_no,
#}
    prod.click()
    for i in range(clicking_no,0,-1):
        element.add_to_cart.click()
        a=time.sleep(3) if i>1 else None
    print("clicked add to cart")
def display_cart_form(element):
    add_to_cart(element)
    element.driver.execute_script("arguments[0].scrollIntoView();",element.mycart_button)
    wait_until(element.driver,lambda driver:element.mycart_num.text[1:-1]!="0")
    if not validate_carts_form(element):
        attach_results.attach_debug("cannot get the cart form via cart button",screen_shot=True,driver=element.driver)
        element.home.click()
        print("last conditional statement")
        if not validate_carts_form(element):
            print("it entered here")
            attach_results.attach_debug("cannot get the cart form even after clicking home button",screen_shot=True,driver=element.driver)
            pytest.skip("Cart form is not displayed after clicking the cart button.")
            return False
    return True
def add_catalog_to_cart(element,items_index=0,clicking_no=1):
    try:
        prod=element.catalog_list[items_index]
        print(f"prod : {prod}")
    except:pytest.skip,f"no items exist more than {items_index-1}"  
    wait(element.driver,prod).click()
    result=wait_until(element.driver,lambda driver:element.add_to_cart.is_displayed() is True)
    for i in range(clicking_no,0,-1):
        element.add_to_cart.click()
        a=time.sleep(3) if i>1 else None
    
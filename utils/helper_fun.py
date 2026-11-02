from utils.wait import wait_until,wait
from selenium.webdriver.common.by import By
import pytest,time
import utils.attach_results as attach_results
def is_carts_form_displayed(element,timeout=3):
    element.driver.execute_script("arguments[0].scrollIntoView();", element.mycart_button)
    element.mycart_button.click()
    result=wait_until(element.driver,lambda driver: element.mycart_form.is_displayed() is True,timeout=timeout)
    return result
def add_to_cart(element,items_index=0,clicking_no=1):
    try:prod=element.prod_list[items_index]
    except:pytest.skip,f"no items exist more than {items_index-1}"
    prod.click()
    for i in range(clicking_no,0,-1):
        element.add_to_cart.click()
        a=time.sleep(3) if i>1 else None
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
def get_cart_total(prod_list):
    total=0
    for prod in prod_list:
        prod_total=float(prod.find_element(By.TAG_NAME,"span").text[1:])
        total+=prod_total
    return total
    
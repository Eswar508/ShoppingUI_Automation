import time
import pytest
from conftest import element
from utils.wait import wait, wait_until
import utils.helper_fun as fun
import utils.attach_results as attach_results
class AddToCartPage:
    @classmethod
    def increment_items_to_cart(cls,element,item_index,clicking_no):
        try:prod=element.prod_list[item_index]
        except:pytest.skip,f"no items exist more than {item_index-1}"
        iN=int(element.mycart_num.text[1:-1]) 
        prod.click()
        for _ in range(clicking_no,0,-1):
            element.add_to_cart.click()
            wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) != iN)
            iN+=1
            
    @classmethod
    def add_catalog_items_to_cart(cls,element,items_index=0,clicking_no=1):
        element.catalog.click()
        try:
            prod=element.catalog_list[items_index]
        except:
            pytest.skip,f"no items exist more than {items_index-1}" 
        element.wait.until(lambda driver:(prod.is_enabled()) is True) 
        prod.click()
        wait_until(element.driver,lambda driver:element.add_to_cart.is_displayed() is True)
        iN=int(element.mycart_num.text[1:-1]) 
        for _ in range(clicking_no,0,-1):
            element.add_to_cart.click()
            wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) != iN)
            iN+=1
            
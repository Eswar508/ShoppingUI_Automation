import time
import pytest
from utils.wait import wait_until
import utils.helper_fun as fun
import utils.attach_results as attach_results
class Exe:
    @classmethod
    def validate_increment(cls,element):
        # Get the initial number of items in the cart
        initial_cart_num = int(element.mycart_num.text[1:-1])  # Assuming the text is in the format "(X)"
        fun.add_to_cart(element)
        wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) != initial_cart_num)
        time.sleep(3)  # Wait for the cart to update
        final_cart_num = int(element.mycart_num.text[1:-1])
        # Assert that the number of items in the cart has increased by 1
        assert final_cart_num == initial_cart_num + 1, f"Expected {initial_cart_num + 1} items in cart, but found {final_cart_num}."
    @classmethod
    def validate_catolog_increment(cls,element):
        element.catalog.click()
        initial_cart_num = int(element.mycart_num.text[1:-1])  # Assuming the text is in the format "(X)"
        fun.add_catalog_to_cart(element, items_index=0)
        wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) != initial_cart_num)
        end=time.perf_counter()
        final_cart_num = int(element.mycart_num.text[1:-1])
        # Assert that the number of items in the cart has increased by 1
        assert final_cart_num == initial_cart_num + 1, f"Expected {initial_cart_num + 1} items in cart, but found {final_cart_num}."
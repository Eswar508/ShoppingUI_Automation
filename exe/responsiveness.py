import time
import pytest
from utils.wait import wait_until
import utils.helper_fun as fun
import utils.attach_results as attach_results
class Exe:
    @classmethod
    def validate_cart_responsivenessI(element):
        start=time.perf_counter()
        initial_cart_num = int(element.mycart_num.text[1:-1])  # Assuming the text is in the format "(X)"
        print("one")
        fun.add_to_cart(element, items_index=0)
        print("two")
        element.driver.execute_script("arguments[0].scrollIntoView();",element.mycart_button)
        result=wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) == initial_cart_num + 1)
        print(f"changes after waiting {result}")
        end=time.perf_counter()
        print(f"Time taken for cart responsiveness test:{end-start} and {end - start:.2f} seconds")
        interval=end-start
        assert interval <= 1
    @classmethod
    def validate_prod_click_responsiveness(element):
        element.prod_list[0].click()
        start=time.perf_counter()
        result=wait_until(element.driver,lambda driver: element.add_to_cart.is_displayed() == True)
        print(result)
        end=time.perf_counter()
        interval=end-start
        print(f"Time taken for product click responsiveness test:{interval} and {interval:.2f} seconds")
        assert interval<=0.5
    @classmethod
    def validate_prod_remove_responsiveness(cls,element):
        if fun.display_cart_form(element):pass
        else: return
        element.remove.click()
        start=time.perf_counter()
        result=wait_until(element.driver,lambda driver:element.cart_first_element.is_displayed() is False)
        print(result)
        end=time.perf_counter()
        interval=end-start
        print(f"Time taken for product removal responsiveness test:{interval} and {interval:.2f} seconds")
        assert interval <= 0.5
        assert False
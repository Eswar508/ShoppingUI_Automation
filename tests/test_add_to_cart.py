import time

from pages.incrementation_page import AddToCartPage

from utils.wait import wait, wait_until
def test_add_product_to_cart(element):
    initial_cart_num=int(element.mycart_num.text[1:-1])  # Assuming the text is in the format "(X)"
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=1)
    final_cart_num = int(element.mycart_num.text[1:-1])
    # Assert that the number of items in the cart has increased by 1
    assert final_cart_num == initial_cart_num + 1, f"Expected {initial_cart_num + 1} items in cart, but found {final_cart_num}."
def test_add_catalog_items_to_cart(element):
    initial_cart_num = int(element.mycart_num.text[1:-1]) 
    AddToCartPage.add_catalog_items_to_cart(element)
    final_cart_num = int(element.mycart_num.text[1:-1])
    # Assert that the number of items in the cart has increased by 1
    assert final_cart_num == initial_cart_num + 1, f"Expected {initial_cart_num + 1} items in cart, but found {final_cart_num}."
def test_add_multiple_items_to_cart(element):
    n=3  # Number of items to add
    initial_cart_num = int(element.mycart_num.text[1:-1]) 
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=n)
    final_cart_num = int(element.mycart_num.text[1:-1])
    # Assert that the number of items in the cart has increased by 3
    assert final_cart_num == initial_cart_num + n, f"Expected {initial_cart_num + n} items in cart, but found {final_cart_num}."
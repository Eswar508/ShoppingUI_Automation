from pages.incrementation_page import AddToCartPage
from pages.cart_form_page import CartFormPage
from utils.helper_fun import is_carts_form_displayed
from utils.wait import wait_until
def test_cart_form(element):
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=1)
    result=is_carts_form_displayed(element)
    assert result is True, "Cart form is not displayed after clicking the cart button."
def test_remove_item_from_cart(element):
    AddToCartPage.increment_items_to_cart(element, item_index=0, clicking_no=1)
    initial_cart_num = int(element.mycart_num.text[1:-1])
    CartFormPage.remove_item(element)
    final_cart_num = int(element.mycart_num.text[1:-1])
    assert final_cart_num != initial_cart_num
from unittest.mock import Mock

import allure

from pages.base_page import BasePage


@allure.feature("Page helpers")
@allure.title("Wait for each product to appear in the cart")
def test_click_product_waits_for_cart_update():
    page = BasePage(driver=Mock())
    product_link = Mock()
    product = Mock()
    product.find_element.return_value = product_link
    add_button = Mock()
    events = []
    cart_numbers = iter([0, 1, 2])

    page.get_prod_list = lambda: [product]
    page.get_mycart_num = lambda: events.append("read cart") or next(cart_numbers)
    page.get_element = lambda selector: add_button
    def wait_for_cart_update(condition):
        events.append("wait for cart update")
        assert condition(None)

    page.wait_until = wait_for_cart_update
    product_link.click.side_effect = lambda: events.append("open product")
    add_button.click.side_effect = lambda: events.append("add product")

    page.click_prod(index=0, no_of_clicks=2)

    assert events == [
        "read cart",
        "open product",
        "add product",
        "wait for cart update",
        "read cart",
        "add product",
        "wait for cart update",
        "read cart",
    ]

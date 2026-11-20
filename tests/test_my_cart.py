import allure

from pages.cart_form_page import CartFormPage


pytestmark = allure.feature("Cart drawer")


@allure.title("Open the cart drawer")
def test_cart_form(driver):
    page = CartFormPage(driver)
    page.click_prod(index=0, no_of_clicks=1)
    page.get_cart_button().click()

    assert page.is_carts_form_displayed() is True


@allure.title("Remove a product from the cart")
def test_remove_item_from_cart(driver):
    page = CartFormPage(driver)
    page.prods_to_cart()
    initial_cart_num = page.get_mycart_num()
    page.remove_item()
    final_cart_num = page.get_mycart_num()

    assert final_cart_num != initial_cart_num


@allure.title("Update a product total after changing its quantity")
def test_cart_prod_total_after_updating_quantity(driver):
    page = CartFormPage(driver)
    page.prods_to_cart(index=0, no_of_clicks=1)
    page.update_cart_quantity(5)
    page.open_cart_form()

    expected_total = page.get_cart_prod_price() * 5
    actual_total = page.get_cart_prod_total()

    assert actual_total == expected_total


@allure.title("Update the cart count after changing quantity")
def test_cart_num_after_updating_quantity(driver):
    page = CartFormPage(driver)
    page.prods_to_cart(index=0, no_of_clicks=1)
    page.update_cart_quantity(2)
    cart_num = page.get_mycart_num()

    assert cart_num == 2


@allure.title("Show the selected product in the cart")
def test_added_prods(driver):
    page = CartFormPage(driver)
    product_name = page.get_prod_name(index=2)
    page.prods_to_cart(index=2, no_of_clicks=1)
    cart_product_name = page.get_cart_prod_name()

    assert product_name in cart_product_name

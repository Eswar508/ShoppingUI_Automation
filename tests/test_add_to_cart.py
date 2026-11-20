import allure

from pages.products_page import AddToCartPage


pytestmark = allure.feature("Adding products to the cart")


@allure.title("Add one product to the cart")
def test_add_product_to_cart(driver):
    page = AddToCartPage(driver)
    initial_cart_num = page.get_mycart_num()
    click_count = 1

    page.click_prod(index=0, no_of_clicks=click_count)
    final_cart_num = page.get_mycart_num()

    assert final_cart_num == initial_cart_num + click_count


@allure.title("Add a catalog product to the cart")
def test_add_catalog_items_to_cart(driver):
    page = AddToCartPage(driver)
    initial_cart_num = page.get_mycart_num()

    page.add_catalog_items_to_cart()
    final_cart_num = page.get_mycart_num()

    assert final_cart_num == initial_cart_num + 1


@allure.title("Add multiple products to the cart")
def test_add_multiple_items_to_cart(driver):
    page = AddToCartPage(driver)
    first_product_count = 3
    second_product_count = 2
    initial_cart_num = page.get_mycart_num()

    page.click_prod(index=0, no_of_clicks=first_product_count)
    page.driver.back()
    page.click_prod(index=1, no_of_clicks=second_product_count)

    expected_cart_num = (
        initial_cart_num + first_product_count + second_product_count
    )
    final_cart_num = page.get_mycart_num()

    assert final_cart_num == expected_cart_num

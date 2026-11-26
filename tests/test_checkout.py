import allure

from pages.checkout_page import CheckoutPage
from selenium.webdriver.support import expected_conditions  as Ec

import time
pytestmark = allure.feature("Cart and checkout")


@allure.title("Open the cart from a product")
def test_checkout(driver):
    page = CheckoutPage(driver)
    page.prods_to_checkout(index=0, no_of_clicks=1)

    expected_url = "https://sauce-demo.myshopify.com/cart"
    assert driver.current_url == expected_url


@allure.title("Show the selected product in the cart")
def test_added_prods(driver):
    page = CheckoutPage(driver)
    product_name = page.get_prod_name(index=2)
    page.prods_to_checkout(index=2, no_of_clicks=1)
    product=page.get_ckout_prod_list()[0]
    cart_product_name = page.get_ckout_prod_name(product)

    assert product_name in cart_product_name


@allure.title("Calculate a product total")
def test_prod_total(driver):
    page = CheckoutPage(driver)
    page.prods_to_checkout(index=0, no_of_clicks=3)
    product=page.get_ckout_prod_list()[0]
    product_price = page.get_ckout_prod_price(product)
    product_quantity = page.get_ckout_prod_num(product)
    product_total = page.get_ckout_prod_total(product)
    expected_total = product_price * product_quantity

    assert product_total == expected_total


@allure.title("Calculate the cart total")
def test_cart_total(driver):
    page = CheckoutPage(driver)
    page.prods_to_checkout(index=0, no_of_clicks=3)
    product=page.get_ckout_prod_list()[0]
    product_total = page.get_ckout_prod_total(product)
    cart_total = float(page.get_element(page.checkouts_total).text[7:])

    assert cart_total == product_total

@allure.title("Update a product total after changing its quantity")
def test_cart_total_after_updating_item(driver):
    page = CheckoutPage(driver)
    page.prods_to_checkout(index=0, no_of_clicks=1)
    new_quantity = 5
    product=page.get_ckout_prod_list()[0]
    page.update_ckout_prod_num(product, new_quantity)
    updated_product = page.get_ckout_prod_list()[0]
    product_price = page.get_ckout_prod_price(updated_product)
    product_total = page.get_ckout_prod_total(updated_product)
    expected_total = product_price * new_quantity
    assert product_total == expected_total


@allure.title("Update the cart total after changing quantity")
def test_cart_prod_total_after_updating_item(driver):
    page = CheckoutPage(driver)
    page.prods_to_checkout(index=0, no_of_clicks=1)
    new_quantity = 5
    product=page.get_ckout_prod_list()[0]
    page.update_ckout_prod_num(product, new_quantity)
    updated_product = page.get_ckout_prod_list()[0]
    product_price = page.get_ckout_prod_price(updated_product)
    cart_total = page.get_checkouts_total()
    expected_total = product_price * new_quantity

    assert cart_total == expected_total

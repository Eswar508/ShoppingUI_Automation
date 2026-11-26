from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

from pages.base_page import BasePage


class CartFormPage(BasePage):
    my_cart_form = (By.CSS_SELECTOR, "#drawer > div > form")
    my_cart_button = (By.CSS_SELECTOR, "#minicart > a.toggle-drawer.cart.desktop")
    cart_prod_price = (
        By.CSS_SELECTOR,
        "#drawer > div > form > div.row.first > div.two.columns.price.desktop",
    )
    cart_prod_total = (
        By.CSS_SELECTOR,
        "#drawer > div > form > div.row.first > div.two.columns.total.desktop",
    )
    cart_prod_name = (
        By.CSS_SELECTOR,
        "#drawer > div > form > div.row.first > div.nine.columns.description > div > h3 > a",
    )
    remove = (
        By.CSS_SELECTOR,
        "#drawer > div > form > div.row.first > div.one.column.remove.desktop > a",
    )

    def cart_prod_input(self):
        cart_form = self.get_element(self.my_cart_form)
        return cart_form.find_element(By.TAG_NAME, "input")

    def get_cart_button(self):
        return self.get_element(self.my_cart_button)

    def get_cart_prod_price(self):
        price = self.get_element(self.cart_prod_price).text
        return float(price[1:])

    def get_cart_prod_total(self):
        total = self.get_element(self.cart_prod_total).text
        return float(total[1:])

    def get_cart_prod_num(self):
        quantity = self.cart_prod_input().get_attribute("value")
        return int(quantity)

    def get_cart_prod_name(self):
        return self.get_element(self.cart_prod_name).text

    def prods_to_cart(self, index=0, no_of_clicks=1):
        self.click_prod(index=index, no_of_clicks=no_of_clicks)
        self.get_element(self.home).click()
        self.open_cart_form()

    def remove_item(self):
        starting_quantity = self.get_mycart_num()
        self.get_element(self.remove).click()
        self.wait_until(lambda driver: self.get_mycart_num() != starting_quantity)

    def is_carts_form_displayed(self):
        form = self.wait_until(
            Ec.visibility_of_element_located(self.my_cart_form),
            timeout=5,
        )
        return form is not None

    def update_cart_quantity(self, quantity):
        quantity_input = self.cart_prod_input()
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))
        quantity_input.send_keys("\n")
        self.wait_until(Ec.staleness_of(quantity_input))

    def open_cart_form(self):
        self.get_cart_button().click()

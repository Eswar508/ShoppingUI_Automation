from pages.base_page import BasePage
class AddToCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    def add_catalog_items_to_cart(self,items_index=0,clicking_no=1):
        self.get_element(self.catalog).click()
        self.click_prod(items_index,clicking_no)
    def get_home_element(self):
            return self.get_element(self.home)
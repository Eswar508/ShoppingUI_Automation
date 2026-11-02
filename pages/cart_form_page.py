from utils.wait import wait_until
class CartFormPage:
    @classmethod
    def remove_item(cls,element):
        In=int(element.mycart_num.text[1:-1])
        element.home.click()
        element.mycart_button.click()
        element.remove.click()
        wait_until(element.driver,lambda driver: int(element.mycart_num.text[1:-1]) != In)
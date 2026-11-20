from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    prod_container=(By.CSS_SELECTOR,"#page-content > section")
    add_to_cart=(By.CSS_SELECTOR,"#add")
    catalog=(By.CSS_SELECTOR,"#main-menu > li:nth-child(2) > a")
    home=(By.CSS_SELECTOR,"#main-menu > li:nth-child(1) > a")
    mycart_num=(By.CSS_SELECTOR,"#cart-target-desktop")
    def get_element(self,selector,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(selector))
            self.driver.execute_script("arguments[0].scrollIntoView();", result)
            return result
        except Exception as e:
            return None  
    def get_prod_list(self):
        pc=self.get_element(self.prod_container)
        prod=pc.find_elements(By.XPATH,"./div")
        return prod
    def get_prod_name(self,prod=None,index=0):
        if prod is  None:
            prod=self.get_prod_list()[index]
        name=prod.find_element(By.TAG_NAME,"h3").text
        return name
    def get_mycart_num(self):
        txt=self.get_element(self.mycart_num).text[1:-1]
        return int(txt)
    def wait_until(self,condition,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(condition)
        except Exception as e:
            print(f"Error occurred while waiting for condition: {e}")
            return None
    def click_prod(self,index,no_of_clicks=1):
        try:
            prods=self.get_element(self.prod_container).find_elements(By.TAG_NAME,"div")
            prod=prods[index]
        except Exception as e:
            print(f"Error occurred while waiting for product container: {e}")
            return None
        self.wait_until(lambda driver:prod.is_enabled() and prod.find_element(By.TAG_NAME,"h3").is_displayed())
        prod.click()
        iN=self.get_mycart_num()
        for _ in range(no_of_clicks,0,-1):
            iN+=1
            add_to_cart=self.get_element(self.add_to_cart)
            add_to_cart.click()
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.wait_until(lambda driver: add_to_cart.is_enabled())

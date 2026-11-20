from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
class RegistrationPage(BasePage):
    first_name=(By.NAME,"customer[first_name]")
    last_name=(By.NAME,"customer[last_name]")
    email=(By.NAME,"customer[email]")
    password=(By.NAME,"customer[password]")
    create_button=(By.CSS_SELECTOR,"#create_customer > div.action_bottom > input[type=submit]")
    error_msg=(By.CSS_SELECTOR,"#create_customer > div.errors > ul")
    def enter_first_name(self,name):
        fn=self.get_element(self.first_name)
        fn.send_keys(name)
        fn.send_keys("\n")
    def enter_last_name(self,name):
        ln=self.get_element(self.last_name)
        ln.send_keys(name)
        ln.send_keys("\n")
    def enter_email(self,email):
        e=self.get_element(self.email)
        e.send_keys(email)
        e.send_keys("\n")
    def enter_password(self,password):
        p=self.get_element(self.password)
        p.send_keys(password)            
        p.send_keys("\n")     
    def get_create_button(self):
        return self.get_element(self.create_button)
    def is_error_message(self,message):
        error=self.get_element(self.error_msg).find_element(By.TAG_NAME,"li")
        return error.text == message
    def is_email_accepted(self):
        e=self.get_element(self.email)
        return self.driver.execute_script( "return arguments[0].checkValidity();", e)
    def is_registered_sucessfully(self):
        logout = self.wait_until(Ec.visibility_of_element_located( (By.LINK_TEXT, "Log Out")))
        my_account = self.wait_until(
            Ec.visibility_of_element_located(
                (By.LINK_TEXT, "My Account")
            )
        )
        return logout.is_displayed() and  my_account.is_displayed()
from exe.incrementation import Exe
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from utils.wait import wait
def test_incrementation_of_cart(element):
    Exe.validate_increment(element)
def test_incremenatation_of_catolog(element):
    Exe.validate_catolog_increment(element)
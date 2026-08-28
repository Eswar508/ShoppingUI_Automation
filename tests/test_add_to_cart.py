from pages.incrementation_page import IncrementPage

from utils.wait import wait
def test_incrementation_of_cart(element):
    IncrementPage.validate_increment(element)
def test_incremenatation_of_catolog(element):
    IncrementPage.validate_catolog_increment(element)
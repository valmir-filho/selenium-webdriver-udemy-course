# Import the pytest library for creating test cases.
import pytest

# Import specific page objects from the "pages" directory.
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Marks the class to use a specific pytest fixture for setup and teardown processes.
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:

    # Test to verify that products can be successfully added to the shopping cart and verified.
    def test_ct01_add_products_to_cart(self):

        # Create an instance of the LoginPage class to handle login operations.
        login_page = LoginPage()

        # Create instances for HomePage and CartPage to perform actions related to shopping.
        home_page = HomePage()
        cart_page = CartPage()

        # Define the names of the products to be added to the cart.
        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bolt T-Shirt"

        # Use the login page to perform the login operation using standard credentials.
        login_page.do_login("standard_user", "secret_sauce")

        # Add the first product to the cart.
        home_page.add_to_cart(product_1)

        # Access the cart to verify the product has been added.
        home_page.access_cart()
        cart_page.check_if_product_to_cart_exist(product_1)

        # Return to the shopping area to add another product.
        cart_page.click_continue_shopping_button()

        # Add the second product to the cart.
        home_page.add_to_cart(product_2)

        # Access the cart again to verify the second product has been added.
        home_page.access_cart()
        cart_page.check_if_product_to_cart_exist(product_2)

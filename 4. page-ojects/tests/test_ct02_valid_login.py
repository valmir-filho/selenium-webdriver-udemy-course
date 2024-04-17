# Import the pytest library for creating test cases.
import pytest

# Import the HomePage class from the "pages" directory to check post-login status.
from pages.home_page import HomePage

# Import the LoginPage class from the "pages" directory to facilitate login.
from pages.login_page import LoginPage


# Marks the class to use a specific pytest fixture for setup and teardown processes.
@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_valid_login(self):

        # Create an instance of the LoginPage class to handle login operations.
        login_page = LoginPage()

        # Create an instance of the HomePage class to handle post-login checks.
        home_page = HomePage()

        # Use the login page to perform the login operation using standard credentials.
        login_page.do_login("standard_user", "secret_sauce")

        # Check if the login was successful by verifying the presence of a specific element on the HomePage.
        home_page.check_if_logged_in_successfully()

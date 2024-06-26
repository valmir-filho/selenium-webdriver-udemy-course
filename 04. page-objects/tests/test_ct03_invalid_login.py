# Import the pytest library for creating test cases.
import pytest

# Import the LoginPage class from the "pages" directory to facilitate login.
from pages.login_page import LoginPage


# Marks the class to use a specific pytest fixture for setup and teardown processes.
@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_valid_login(self):

        expected_error_message = "Epic sadface: Username and password do not match any user in this service"

        # Create an instance of the LoginPage class to handle login operations.
        login_page = LoginPage()

        # Use the login page to perform the login operation using standard credentials.
        login_page.do_login("standard_user", "secret")

        # Check if the appropriate error message is displayed on the login page after the failed login attempt.
        login_page.check_exist_error_message_login()

        # Further validate that the error message text matches the expected message.
        login_page.check_error_text_message(expected_error_message)

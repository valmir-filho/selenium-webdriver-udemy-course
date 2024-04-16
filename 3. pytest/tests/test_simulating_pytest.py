# Import the pytest module to use its features for testing.
import pytest


# Define a custom marker named 'simulating' to categorize certain tests.
@pytest.mark.simulating
class TestSimulating:
    # Define a test method to verify that the number 1 equals itself.
    def test_simulating_1(self):
        assert 1 == 1  # This test will pass as the assertion is true.

    # Apply the "skip" marker to this test method to prevent it from running.
    @pytest.mark.skip
    def test_simulating_2(self):
        assert 1 == 2  # This test would fail because 1 is not equal to 2, but it's skipped.

# Set the expected number for comparison.
expected_number = 2

# Set the number obtained from some process.
obtained_number = 2

# Assert that the expected number matches the obtained number. If not, raise an error with a detailed message.
assert expected_number == obtained_number, f"Expected number: {expected_number}. Obtained number: {obtained_number}."

# Set the expected text for comparison.
expected_text = "Selenium"

# Set the text obtained from some process.
obtained_text = "Webdriver"

# Assert that the expected text matches the obtained text exactly. If not, raise an error with a detailed message.
assert expected_text == obtained_text, f"Expected text: {expected_text}. Obtained text: {obtained_text}."

# Assert that the expected text is a substring of the obtained text. If not, raise an error with a detailed message.
assert expected_text in obtained_text, f"Expected text: {expected_text} in obtained text: {obtained_text}."

# Assert that the expected text is not a substring of the obtained text. If not, raise an error with a detailed message.
assert expected_text not in obtained_text, f"Expected text: {expected_text} not in obtained text: {obtained_text}."

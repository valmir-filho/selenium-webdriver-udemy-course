# Import the time module to use sleep function for pauses.
import time

# Import webdriver to control the browser, By to locate elements, WebDriverWait to manage waits, and expected_conditions
# to use built-in condition methods.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the explicit wait practice page on the website.
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

# Pause the execution for 2 seconds to allow the web page to load.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution to observe the maximized window.
time.sleep(2)

# Create a WebDriverWait instance with a timeout of 30 seconds.
wait = WebDriverWait(driver, 30)

# Click the button to trigger an alert.
driver.find_element(By.ID, "alert").click()

# Wait a short moment to ensure the click has been processed.
time.sleep(2)

# Wait until an alert is present.
wait.until(e_c.alert_is_present())

# Wait a short moment to ensure the alert has been processed.
time.sleep(2)

# Click the button to display text.
driver.find_element(By.ID, "populate-text").click()

# Wait a short moment to ensure the click has been processed.
time.sleep(2)

# Wait until the specific text "Selenium Webdriver" appears on the page.
wait.until(e_c.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdriver"))

# Wait a short moment to ensure the text has been processed.
time.sleep(2)

# Click to display another button.
driver.find_element(By.ID, "display-other-button").click()

# Wait a short moment to ensure the click has been processed.
time.sleep(2)

# Wait until the new button is clickable.
wait.until(e_c.element_to_be_clickable((By.ID, "hidden")))

# Wait a short moment to ensure the button has become clickable.
time.sleep(2)

# Click to enable a button.
driver.find_element(By.ID, "enable-button").click()

# Wait a short moment to ensure the click has been processed.
time.sleep(2)

# Wait until the "disable" button is clickable.
wait.until(e_c.element_to_be_clickable((By.ID, "disable")))

# Wait a short moment to ensure the button has become clickable.
time.sleep(2)

# Click to toggle a checkbox.
driver.find_element(By.ID, "checkbox").click()

# Wait a short moment to ensure the click has been processed.
time.sleep(2)

# Wait until the checkbox is selected.
wait.until(e_c.element_to_be_selected(driver.find_element(By.ID, "ch")))

# Wait a short moment to ensure the checkbox has been selected.
time.sleep(2)

# Close the browser and end the session.
driver.quit()

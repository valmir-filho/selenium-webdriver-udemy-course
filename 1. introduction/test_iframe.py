# Import the time module to use sleep function for pauses.
import time

# Import webdriver from selenium to control the browser, By to locate elements, and Select to interact with dropdown
# elements.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the specified website that contains multiple frames.
driver.get("https://chercher.tech/practice/frames")

# Pause the execution for 2 seconds to allow the web page to load initially.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution briefly to observe the maximized window.
time.sleep(2)

# Locate and switch to the first iframe using its ID.
iframe1 = driver.find_element(By.ID, "frame1")
driver.switch_to.frame(iframe1)

# Inside the first iframe, find the input field by its XPath and enter text into it.
driver.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iframe1")

# Pause execution to observe text entry.
time.sleep(2)

# Locate and switch to the third iframe nested within the first iframe.
iframe3 = driver.find_element(By.ID, "frame3")
driver.switch_to.frame(iframe3)

# Find the checkbox inside the third iframe by its XPath and click it.
checkbox = driver.find_element(By.XPATH, "//*[@type='checkbox']")
checkbox.click()

# Pause execution to observe the checkbox click.
time.sleep(2)

# Switch back to the default content (main page) from the iframes.
driver.switch_to.default_content()

# Locate and switch to the second iframe using its ID.
iframe2 = driver.find_element(By.ID, "frame2")
driver.switch_to.frame(iframe2)

# Inside the second iframe, locate the dropdown menu by its XPath and select an option by value.
dropdown_animals = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")

# Pause execution to observe the dropdown selection.
time.sleep(2)

# Close the browser and end the session.
driver.quit()

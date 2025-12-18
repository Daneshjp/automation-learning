from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open demo page
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2)

# Click "Add Element" button
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_button.click()
time.sleep(2)

# Verify "Delete" button appears
delete_button = driver.find_element(By.CLASS_NAME, "added-manually")
print("Delete button displayed:", delete_button.is_displayed())

# Click Delete button
delete_button.click()
time.sleep(2)

driver.quit()

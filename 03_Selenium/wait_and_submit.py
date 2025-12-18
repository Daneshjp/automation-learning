from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

# Wait for username field
username = wait.until(
    EC.element_to_be_clickable((By.ID, "username"))
)
username.send_keys("tomsmith")

# Wait for password field
password = wait.until(
    EC.element_to_be_clickable((By.ID, "password"))
)
password.send_keys("SuperSecretPassword!")

# Click Login
login_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))
)
login_button.click()

# Wait for success message
message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

print("Message:", message.text)

time.sleep(2)
driver.quit()

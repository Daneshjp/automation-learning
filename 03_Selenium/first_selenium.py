from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Use NCR to avoid consent/redirect issues
driver.get("https://www.google.com/ncr")

wait = WebDriverWait(driver, 10)

# Wait for body and click once
body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
body.click()

# Now safely find the visible search box
search_box = wait.until(
    EC.visibility_of_element_located((By.NAME, "q"))
)

actions = ActionChains(driver)
actions.move_to_element(search_box).click().send_keys(
    "Selenium Python tutorial"
).send_keys(Keys.ENTER).perform()

time.sleep(3)

driver.save_screenshot("03_selenium/google_search.png")
driver.quit()

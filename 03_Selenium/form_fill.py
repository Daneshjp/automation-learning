from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")
time.sleep(2)

input_box = driver.find_element(By.TAG_NAME, "input")
input_box.send_keys("12345")
time.sleep(2)

driver.quit()

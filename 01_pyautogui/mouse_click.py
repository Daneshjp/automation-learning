import pyautogui
import time

print("Starting in 5 seconds...")
time.sleep(5)

# Replace these with your coordinates
x, y = 500, 300

pyautogui.moveTo(x, y, duration=2)
pyautogui.click()

print("Mouse click completed")

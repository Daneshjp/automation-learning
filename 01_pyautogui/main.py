import pyautogui
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

file_path = os.path.join(SCREENSHOT_DIR, "final_test.png")
pyautogui.screenshot(file_path)

print(f"Screenshot saved at: {file_path}")

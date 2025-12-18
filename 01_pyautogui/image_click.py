import pyautogui
import time

pyautogui.FAILSAFE = True

print("Starting in 5 seconds...")
time.sleep(5)

print("Looking for image...")
location = pyautogui.locateOnScreen(
    "01_pyautogui/assets/vscode_icon.png"
)

print("Location result:", location)

if location:
    pyautogui.click(pyautogui.center(location))
    print("Clicked image")
else:
    print("Image NOT found")
